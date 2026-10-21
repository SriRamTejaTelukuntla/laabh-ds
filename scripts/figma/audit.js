// Audit screens against the repo's rules. Read-only: it never changes the file.
// Run in the DS or product file (figma_execute / use_figma). Set TARGET to node IDs (a page, section or screen frame).
// Big targets: the deep checks stop near BUDGET_MS and the result's `next` is the screen index to continue from.
// Run again with FROM = next until `next` is null, save each result, then pass them all to scripts/audit-report.py.
// Returns { exportedAt, file, isDsFile, target, from, next, screens, findings, contrast, foreignVariables, styles, exempt, notMeasured }.
// The result is often too big to show inline: the tool output is saved to a file, and scripts/figma-result.py finds it by exportedAt.
// screens: [id, name, w, h, section, mode, layerCount (audited ones only)]. contrast: [fg, bg, mode, kind, minRatio, count, needed, exampleNode].
// Each finding: { check, sev, screen, node, name, detail, scope, count, nodes } where scope 'ds' = inside a DS component (fix in the
// library; grouped across screens, `screens` lists them). Repeats of the same problem on one screen are grouped (`nodes`, `count`).
const TARGET = ['101:129022'];
const FROM = 0;
const BUDGET_MS = 20000;

// Components a person taps (hit target checks). Instances nested in one of these count as part of it.
const TAPPABLE = ['Button', 'Icon Button', 'Compact Button', 'Checkbox', 'Radio', 'Switch', 'Switch Row', 'Segment', 'Tab Item',
  'Dropdown', 'Dropdown Item', 'TextField', 'TextField/Search', 'TextField/Amount', 'TextArea', 'Option Card', 'OTP Input', 'File Upload'];
const CONTAINER_TAPS = ['Option Card', 'Switch Row', 'Dropdown Item', 'Dropdown', 'TextField', 'TextField/Search', 'TextField/Amount', 'TextArea', 'OTP Input', 'File Upload'];
// Controls whose border identifies them (non-text contrast, 3:1).
const CONTROLS = ['TextField', 'TextField/Search', 'TextField/Amount', 'TextArea', 'Dropdown', 'OTP Cell', 'Checkbox', 'Radio', 'Switch', 'File Upload'];
// DS component names: a plain frame with one of these names is a lookalike. Keep in step with docs/index.md.
const DS_NAMES = ['Alert', 'App Header', 'Avatar', 'Badge', 'Bottom Sheet', 'Sheet Scrim', 'Button', 'Icon Button', 'Compact Button',
  'Checkbox', 'Checkbox Group', 'Dropdown', 'Dropdown Item', 'Dropdown Menu', 'File Upload', 'Icon', 'Icon Tile', 'List Row', 'Option Card', 'OTP Input', 'OTP Cell', 'Radio', 'Radio Group',
  'Screen Atmosphere', 'Segment', 'Segmented Control', 'Step', 'Step Indicator', 'Switch', 'Switch Row', 'Status Bar', 'Home Indicator',
  'Summary Card', 'Summary Row', 'Tab Item', 'Tab Bar', 'TextArea', 'TextField', 'Timeline', 'Timeline Item', 'Tooltip', 'Top Bar'];
// Known exemptions (docs/components/*.md "Figma doc drift").
const EXEMPT = [{ component: 'Status Bar', layer: 'Time', checks: ['text-style', 'raw-fill'], why: 'iOS system font by design (system-components.md)' }];
const DS_COLOR_KEY = 'f10929d83247605f5e490e15a6d3ed57e1ce70ce'; // Color Tokens collection key (tokens/_meta.variables.json)

const t0 = Date.now();
const findings = [];
const add = (f) => findings.push(f);
const r2 = (x) => Math.round(x * 100) / 100;
const hex = (c) => '#' + [c.r, c.g, c.b].map((x) => Math.round(x * 255).toString(16).padStart(2, '0')).join('') +
  (c.a !== undefined && c.a < 1 ? Math.round(c.a * 255).toString(16).padStart(2, '0') : '');

// ---------- caches ----------
const varMeta = new Map();   // id -> { name, coll, collKey, remote }
const collMeta = new Map();
const uses = { variables: {}, styles: {} };
async function coll(id) {
  if (!collMeta.has(id)) {
    const c = await figma.variables.getVariableCollectionByIdAsync(id);
    collMeta.set(id, c ? { name: c.name, key: c.key, remote: c.remote, modes: c.modes } : null);
  }
  return collMeta.get(id);
}
async function vmeta(id, nodeId) {
  if (!varMeta.has(id)) {
    const v = await figma.variables.getVariableByIdAsync(id);
    const c = v ? await coll(v.variableCollectionId) : null;
    varMeta.set(id, v ? { v, name: v.name, coll: c ? c.name : '?', collKey: c ? c.key : '?', remote: v.remote } : null);
  }
  const m = varMeta.get(id);
  const u = (uses.variables[id] = uses.variables[id] || [m ? m.name : '?', m ? m.coll : '?', m ? m.collKey : '?', 0, []]);
  u[3]++;
  if (u[4].length < 3 && nodeId) u[4].push(nodeId);
  return m;
}
const styleMeta = new Map();
async function smeta(id, nodeId, kind) {
  if (!styleMeta.has(id)) {
    const s = await figma.getStyleByIdAsync(id);
    styleMeta.set(id, s ? { name: s.name, key: s.key, remote: s.remote } : null);
  }
  const m = styleMeta.get(id);
  const u = (uses.styles[id] = uses.styles[id] || [m ? m.name : '?', m ? m.key : '?', m ? m.remote : null, kind, 0, []]);
  u[4]++;
  if (u[5].length < 3 && nodeId) u[5].push(nodeId);
  return m;
}
const mainCache = new Map();
async function mainOf(inst) {
  if (!mainCache.has(inst.id)) {
    const m = await inst.getMainComponentAsync();
    let page = m; while (page && page.type !== 'PAGE' && page.type !== 'DOCUMENT') page = page.parent;
    const set = m && m.parent && m.parent.type === 'COMPONENT_SET' ? m.parent.name : m && m.name;
    mainCache.set(inst.id, m ? { name: set, remote: m.remote, page: page ? page.name : '?', key: m.key } : null);
  }
  return mainCache.get(inst.id);
}

// ---------- colour ----------
async function paintColors(paint, node) {
  // -> [{ c: {r,g,b,a}, token }] for SOLID (one) or GRADIENT (one per stop); null for IMAGE/VIDEO/unknown
  const op = paint.opacity === undefined ? 1 : paint.opacity;
  const resolve = async (raw, alias) => {
    let c = raw, token = null, a = (raw.a === undefined ? 1 : raw.a) * op;
    if (alias) {
      const m = await vmeta(alias.id, null);
      if (m && m.v) {
        const r = m.v.resolveForConsumer(node);
        if (r && r.value && typeof r.value === 'object') c = r.value;
        token = m.name;
        // Figma mirrors a bound SOLID colour's alpha into paint.opacity, so use the variable's alpha alone (else it counts twice)
        a = (c.a === undefined ? 1 : c.a) * (paint.type === 'SOLID' ? 1 : op);
      }
    }
    return { c: { r: c.r, g: c.g, b: c.b, a }, token };
  };
  if (paint.type === 'SOLID') return [await resolve(paint.color, paint.boundVariables && paint.boundVariables.color)];
  if (paint.type && paint.type.startsWith('GRADIENT')) {
    const out = [];
    for (const s of paint.gradientStops) out.push(await resolve(s.color, s.boundVariables && s.boundVariables.color));
    return out;
  }
  return null;
}
const over = (fg, bg) => ({ r: fg.r * fg.a + bg.r * (1 - fg.a), g: fg.g * fg.a + bg.g * (1 - fg.a), b: fg.b * fg.a + bg.b * (1 - fg.a), a: 1 });
const lum = (c) => { const f = (x) => (x <= 0.04045 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4)); return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
const avg = (cs) => {
  const a = cs.reduce((s, x) => s + x.c.a, 0) / cs.length || 0;
  const w = cs.reduce((s, x) => s + x.c.a, 0) || 1;
  const m = (k) => cs.reduce((s, x) => s + x.c[k] * x.c.a, 0) / w;
  return { r: m('r'), g: m('g'), b: m('b'), a };
};

// ---------- raw-value checks ----------
const visiblePaints = (p) => (Array.isArray(p) ? p.filter((x) => x.visible !== false) : []);
const sw = (n) => (typeof n.strokeWeight === 'number' ? n.strokeWeight : Math.max(n.strokeTopWeight || 0, n.strokeRightWeight || 0, n.strokeBottomWeight || 0, n.strokeLeftWeight || 0));
const hasStroke = (n) => 'strokes' in n && sw(n) > 0 && visiblePaints(n.strokes).length > 0;
const RAW_FIELDS = { fills: ['fills', 'boundVariables'], strokes: ['strokes', 'boundVariables'], effects: ['effects', 'effectStyleId'],
  text: ['textStyleId', 'fontSize', 'fontName', 'lineHeight', 'letterSpacing'],
  radius: ['cornerRadius', 'topLeftRadius', 'topRightRadius', 'bottomLeftRadius', 'bottomRightRadius', 'boundVariables'],
  space: ['paddingLeft', 'paddingRight', 'paddingTop', 'paddingBottom', 'itemSpacing', 'counterAxisSpacing', 'boundVariables'] };
const wants = (fields, kind) => !fields || RAW_FIELDS[kind].some((f) => fields.includes(f));

async function checkRaw(n, fields, ctx) {
  const base = { screen: ctx.screen.id, node: n.id, name: n.name, scope: 'screen', inInstance: ctx.instName || null };
  const exempt = ctx.exempt;
  for (const kind of ['fills', 'strokes']) {
    if (!(kind in n) || !wants(fields, kind) || n[kind] === figma.mixed) continue;
    if (kind === 'strokes' && !(sw(n) > 0)) continue;
    if (n.isMask) continue;
    for (const p of visiblePaints(n[kind])) {
      if (p.type === 'IMAGE' || p.type === 'VIDEO' || p.type === 'PATTERN') continue;
      const stops = p.type === 'SOLID' ? [{ color: p.color, bv: p.boundVariables && p.boundVariables.color }]
        : (p.gradientStops || []).map((s) => ({ color: s.color, bv: s.boundVariables && s.boundVariables.color }));
      const raw = stops.filter((s) => !s.bv);
      if (raw.length) {
        if (exempt && exempt.checks.includes('raw-fill')) { ctx.exemptHit(exempt); continue; }
        add({ ...base, check: 'raw-color', sev: 'S3', detail: (kind === 'fills' ? 'fill' : 'stroke') + ' ' + (p.type === 'SOLID' ? '' : p.type.toLowerCase().replace('_', ' ') + ' stop ') + raw.map((s) => hex({ ...s.color, a: (s.color.a === undefined ? 1 : s.color.a) * (p.opacity === undefined ? 1 : p.opacity) })).join(', ') + ' is not a token' });
      }
      for (const s of stops.filter((x) => x.bv)) {
        const m = await vmeta(s.bv.id, n.id);
        if (!m) add({ ...base, check: 'missing-variable', sev: 'S2', detail: kind + ' bound to a variable that no longer exists' });
        else if (m.coll === 'Color Primitives') add({ ...base, check: 'primitive-color', sev: 'S3', detail: kind + ' bound to primitive `' + m.name + '`; use a Color Tokens role' });
        else if (m.coll !== 'Color Tokens') add({ ...base, check: 'primitive-color', sev: 'S3', detail: kind + ' bound to `' + m.name + '` from collection "' + m.coll + '"' });
      }
    }
  }
  if ('effects' in n && wants(fields, 'effects')) {
    const fx = n.effects.filter((e) => e.visible !== false);
    if (fx.length && !n.effectStyleId) add({ ...base, check: 'raw-effect', sev: 'S3', detail: fx.map((e) => e.type.toLowerCase().replace('_', ' ')).join(', ') + ' without an elevation/* style' });
    if (n.effectStyleId) { const m = await smeta(n.effectStyleId, n.id, 'effect'); if (m && !/^elevation\//.test(m.name)) add({ ...base, check: 'raw-effect', sev: 'S3', detail: 'effect style `' + m.name + '` is not elevation/*' }); }
  }
  if (n.type === 'TEXT' && wants(fields, 'text')) {
    const ids = n.textStyleId === figma.mixed ? [...new Set(n.getStyledTextSegments(['textStyleId']).map((s) => s.textStyleId))] : [n.textStyleId];
    if (ids.includes('')) {
      if (exempt && exempt.checks.includes('text-style')) ctx.exemptHit(exempt);
      else add({ ...base, check: 'unstyled-text', sev: 'S3', detail: (ids.length > 1 ? 'part of the text' : 'text') + ' has no text style (' + (n.fontSize === figma.mixed ? 'mixed' : n.fontSize) + 'px "' + n.characters.slice(0, 40).replace(/\n/g, ' ') + '")' });
    }
    for (const id of ids.filter(Boolean)) {
      const m = await smeta(id, n.id, 'text');
      if (m && /^mono\//.test(m.name) && !ctx.isDsDoc) add({ ...base, check: 'doc-style', sev: 'S3', detail: '`' + m.name + '` is for DS docs only' });
    }
  }
  if ('cornerRadius' in n && wants(fields, 'radius') && (visiblePaints(n.fills).length || visiblePaints(n.strokes).length || n.clipsContent)) {
    const corners = ['topLeftRadius', 'topRightRadius', 'bottomLeftRadius', 'bottomRightRadius'];
    const bv = n.boundVariables || {};
    const rad = (k) => (typeof n[k] === 'number' ? n[k] : typeof n.cornerRadius === 'number' ? n.cornerRadius : 0);
    const raw = corners.filter((k) => rad(k) > 0 && !bv[k]);
    if (raw.length) add({ ...base, check: 'raw-radius', sev: 'S3', detail: 'radius ' + [...new Set(raw.map(rad))].join('/') + ' is not a radius/* token' });
    for (const k of corners.filter((k) => bv[k])) {
      const m = await vmeta(bv[k].id, n.id);
      if (m && !/^radius\//.test(m.name)) { add({ ...base, check: 'raw-radius', sev: 'S3', detail: 'radius bound to `' + m.name + '`, not radius/*' }); break; }
    }
  }
  if (n.layoutMode && n.layoutMode !== 'NONE' && wants(fields, 'space')) {
    const bv = n.boundVariables || {};
    const keys = ['paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft'];
    const visKids = (n.children || []).filter((c) => c.visible !== false && c.layoutPositioning !== 'ABSOLUTE').length;
    if (visKids > 1 && n.primaryAxisAlignItems !== 'SPACE_BETWEEN') keys.push('itemSpacing');
    if (n.layoutWrap === 'WRAP' && visKids > 1) keys.push('counterAxisSpacing');
    const raw = keys.filter((k) => typeof n[k] === 'number' && n[k] > 0 && !bv[k]);
    if (raw.length) add({ ...base, check: 'raw-space', sev: 'S3', detail: raw.map((k) => k.replace('padding', 'pad ').replace('itemSpacing', 'gap').replace('counterAxisSpacing', 'row gap').toLowerCase() + ' ' + r2(n[k])).join(', ') + ' not bound to space/*' });
    for (const k of keys.filter((k) => bv[k])) {
      const m = await vmeta(bv[k].id, n.id);
      if (m && !/^space\//.test(m.name)) { add({ ...base, check: 'raw-space', sev: 'S3', detail: k + ' bound to `' + m.name + '`, not space/*' }); break; }
    }
  }
}

// ---------- screens ----------
const isScreen = (n) => n.type === 'FRAME' && n.width >= 320 && n.width <= 440 && n.height >= 560;
const NAME_RE = /^([A-Z]\d{2}[a-z]?)\s+(.+?)\s+—\s+(Light|Dark)$/;
const screens = [];
const sectionsWithScreens = new Map();

async function collect(node, path) {
  for (const c of node.children || []) {
    if (c.type === 'SECTION') { await collect(c, path.concat(c.name)); continue; }
    const where = path.length ? path[path.length - 1] : '(page)';
    if (isScreen(c)) {
      screens.push({ node: c, path });
      if (path.length) sectionsWithScreens.set(node.id, node.name);
    } else if (c.type === 'COMPONENT' || c.type === 'COMPONENT_SET' || c.type === 'TEXT' || c.type === 'STICKY' || c.type === 'CONNECTOR') {
      continue; // local components and canvas labels are allowed on a page
    } else if (c.visible !== false && (c.type === 'INSTANCE' || ('findOne' in c && c.findOne((x) => x.type === 'INSTANCE')))) {
      add({ check: 'stray-node', sev: 'S4', screen: null, node: c.id, name: c.name, scope: 'screen',
        detail: c.type.toLowerCase() + ' ' + Math.round(c.width) + '×' + Math.round(c.height) + ' sits loose in "' + where + '", outside any screen' });
    }
  }
}

for (const id of TARGET) {
  const n = await figma.getNodeByIdAsync(id);
  if (!n) { add({ check: 'not-found', sev: 'S4', screen: null, node: id, name: '', detail: 'target not found', scope: 'screen' }); continue; }
  let page = n; while (page.type !== 'PAGE') page = page.parent;
  await page.loadAsync();
  if (n.type === 'PAGE' || n.type === 'SECTION') await collect(n, n.type === 'SECTION' ? [n.name] : []);
  else if (n.type === 'FRAME') screens.push({ node: n, path: n.parent.type === 'SECTION' ? [n.parent.name] : [] });
}

const localColls = await figma.variables.getLocalVariableCollectionsAsync();
const isDsFile = localColls.some((c) => c.key === DS_COLOR_KEY);
async function modeOf(n) {
  const rv = n.resolvedVariableModes || {};
  let best = null;
  for (const [cid, mid] of Object.entries(rv)) {
    const c = await coll(cid);
    if (!c || c.name !== 'Color Tokens') continue;
    const m = c.modes.find((x) => x.modeId === mid);
    if (!best || c.key === DS_COLOR_KEY) best = m ? m.name : '?';
  }
  return best;
}

// ---------- page-level checks (every run) ----------
const screenList = [];
for (const s of screens) {
  const n = s.node, b = n.absoluteBoundingBox;
  const m = n.name.match(NAME_RE);
  screenList.push({ id: n.id, name: n.name, w: Math.round(n.width), h: Math.round(n.height), x: Math.round(b.x), y: Math.round(b.y),
    section: s.path.join(' / '), nameMode: m ? m[3] : null, mode: await modeOf(n) });
}
for (const [sid, sname] of sectionsWithScreens)
  if (!/^\d+[a-z]?\s+·\s+\S/.test(sname)) add({ check: 'section-name', sev: 'S4', screen: null, node: sid, name: sname, scope: 'screen', detail: 'section holding screens should be named "<n> · <Step name>"' });
const byName = new Map();
for (const s of screenList) {
  if (!NAME_RE.test(s.name)) add({ check: 'screen-name', sev: 'S4', screen: s.id, node: s.id, name: s.name, scope: 'screen', detail: 'name should be "<ID> <Screen name> — Light|Dark"' });
  if (s.nameMode && s.mode && s.nameMode !== s.mode) add({ check: 'wrong-mode', sev: 'S2', screen: s.id, node: s.id, name: s.name, scope: 'screen', detail: 'named ' + s.nameMode + ' but renders in ' + s.mode + ' mode' });
  if (!byName.has(s.name)) byName.set(s.name, []);
  byName.get(s.name).push(s);
}
for (const [name, list] of byName) if (list.length > 1 && NAME_RE.test(name))
  add({ check: 'duplicate-name', sev: 'S3', screen: null, node: list.map((x) => x.id).join(', '), name, scope: 'screen', detail: list.length + ' screens share this name (' + list.map((x) => x.section || '(page)').join(' | ') + ')' });
const base = (s) => s.name.replace(/\s+—\s+(Light|Dark)$/, '');
const lights = screenList.filter((s) => s.nameMode === 'Light'), darks = screenList.filter((s) => s.nameMode === 'Dark');
for (const l of lights) {
  const d = darks.filter((x) => base(x) === base(l));
  if (!d.length) add({ check: 'missing-dark', sev: 'S2', screen: l.id, node: l.id, name: l.name, scope: 'screen', detail: 'no "' + base(l) + ' — Dark" in the audited area' });
  else if (!d.some((x) => x.x > l.x || /Dark/.test(x.section))) add({ check: 'dark-placement', sev: 'S4', screen: d[0].id, node: d[0].id, name: d[0].name, scope: 'screen', detail: 'Dark copy is not to the right of its Light frame' });
}
for (const d of darks) if (!lights.some((l) => base(l) === base(d)))
  add({ check: 'missing-light', sev: 'S3', screen: d.id, node: d.id, name: d.name, scope: 'screen', detail: 'no "' + base(d) + ' — Light" in the audited area' });

// ---------- deep checks per screen (budgeted) ----------
const contrastPairs = new Map();
const notMeasured = [];
const exemptCount = {};
const layerCount = new Map();
let next = null;

const contains = (b, x, y) => b && x >= b.x && x <= b.x + b.width && y >= b.y && y <= b.y + b.height;
const clipTo = (b, clip) => {
  if (!b) return null;
  if (!clip) return b;
  const x = Math.max(b.x, clip.x), y = Math.max(b.y, clip.y);
  const w = Math.min(b.x + b.width, clip.x + clip.width) - x, h = Math.min(b.y + b.height, clip.y + clip.height) - y;
  return w > 0 && h > 0 ? { x, y, width: w, height: h } : null;
};

async function auditScreen(screen) {
  const layers = [];   // painted fills in paint order
  const texts = [];
  const uiParts = [];
  const taps = [];
  const seen = new Set();   // main component names on this screen
  let order = 0;
  const ends = new Map();
  const ctxBase = { screen, exemptHit: (e) => { exemptCount[e.component + ' ' + e.layer] = (exemptCount[e.component + ' ' + e.layer] || 0) + 1; } };

  async function walk(n, st) {
    if (n.visible === false || n.opacity === 0) return;
    const box = clipTo(n.absoluteBoundingBox, st.clip);
    if (!box) return;
    const opacity = st.opacity * (n.opacity === undefined ? 1 : n.opacity);
    let s = { ...st, opacity };
    let fields = null; // null = check everything
    if (n.type === 'INSTANCE') {
      const main = await mainOf(n);
      const nm = main ? main.name : null;
      if (nm) seen.add(nm);
      if (!main) add({ check: 'missing-main', sev: 'S3', screen: screen.id, node: n.id, name: n.name, scope: 'screen', detail: 'instance whose main component is missing (deleted or not published)' });
      else if (/Sandbox/i.test(main.page)) add({ check: 'sandbox-component', sev: 'S3', screen: screen.id, node: n.id, name: n.name, scope: 'screen', detail: 'instance of "' + nm + '" from the Sandbox page' });
      else if (!isDsFile && !main.remote && !st.inst) add({ check: 'local-component', sev: 'S4', screen: screen.id, node: n.id, name: n.name, scope: 'screen', detail: '"' + nm + '" is a local component, not from the DS library' });
      const props = n.componentProperties || {};
      const pv = (k) => (props[k] ? props[k].value : null);
      const disabled = pv('State') === 'Disabled' || st.disabled;
      const inst = st.inst || { id: n.id, name: nm, overrides: new Map() };
      if (!st.inst) for (const o of n.overrides || []) inst.overrides.set(o.id, o.overriddenFields);
      s = { ...s, inst, instName: nm, disabled, focus: pv('State') === 'Focus' || st.focus, control: CONTROLS.includes(nm) ? nm : st.control,
        exempt: EXEMPT.find((e) => e.component === nm) || st.exempt, atmosphere: st.atmosphere || nm === 'Screen Atmosphere',
        icon: st.icon || /^icon\//.test(nm || ''), scrim: st.scrim || nm === 'Sheet Scrim' };
      if (TAPPABLE.includes(nm) && !st.tapContainer) taps.push({ n, name: nm, props, inInst: st.inst ? st.inst.name : null, disabled, wrapper: st.parentWrapper });
      if (CONTAINER_TAPS.includes(nm) || (TAPPABLE.includes(nm))) s.tapContainer = st.tapContainer || nm;
      // icons that may carry meaning: standalone, in icon-only buttons, or a control's state glyph (not icons beside a text label)
      const iconHome = st.tapContainer && /Icon Button|Compact Button/.test(st.tapContainer) ? st.tapContainer : st.control || null;
      if (nm && /^icon\//.test(nm) && !st.icon && !st.atmosphere && (!st.tapContainer || iconHome))
        uiParts.push({ n, kind: 'icon', order, inInst: iconHome || (st.inst ? st.inst.name : null), disabled, opacity });
      fields = inst.overrides.get(n.id) || [];
    } else if (st.inst) {
      fields = st.inst.overrides.get(n.id) || [];
    }
    if (!st.inst && n.type !== 'INSTANCE' && (n.type === 'FRAME' || n.type === 'GROUP') && n !== screen) {
      const di = n.detachedInfo;
      if (di) add({ check: 'detached', sev: 'S3', screen: screen.id, node: n.id, name: n.name, scope: 'screen', detail: 'detached from a ' + di.type + ' component (' + (di.componentKey || di.componentId) + ')', key: di.componentKey || null, componentId: di.componentId || null });
      else if (DS_NAMES.some((x) => x.toLowerCase() === n.name.trim().toLowerCase())) add({ check: 'lookalike', sev: 'S3', screen: screen.id, node: n.id, name: n.name, scope: 'screen', detail: 'a plain ' + n.type.toLowerCase() + ' named like the DS component "' + n.name + '"' });
    }
    // raw values: everything outside instances; inside instances only what the screen overrides
    const layerName = s.exempt && n.name === s.exempt.layer ? s.exempt : null;
    if (fields === null || fields.length) await checkRaw(n, fields, { ...ctxBase, instName: s.instName, exempt: layerName, isDsDoc: false });

    // collect paint layers / texts for contrast
    const myOrder = order++;
    if (n.type === 'TEXT') {
      texts.push({ n, order: myOrder, opacity, disabled: s.disabled, box, inInst: s.instName, atmosphere: s.atmosphere,
        inst: s.inst ? s.inst.id : null, overridden: !!fields && fields.some((f) => /fills|textStyleId|boundVariables/.test(f)) });
    } else if ('fills' in n && n.fills !== figma.mixed && !n.isMask) {
      const ps = visiblePaints(n.fills);
      if (ps.length) {
        let kind = 'solid', cols = [], tokens = [];
        for (const p of ps) {
          const pc = await paintColors(p, n);
          if (!pc) { kind = 'image'; continue; }
          if (pc.length > 1) kind = kind === 'image' ? 'image' : 'gradient';
          cols.push(pc.length > 1 ? { c: avg(pc), token: pc.map((x) => x.token || hex(x.c)).join('→') } : pc[0]);
        }
        for (const c of cols) c.c = { ...c.c, a: c.c.a * opacity };
        tokens = cols.map((c) => c.token || hex(c.c));
        if (cols.some((c) => c.c.a > 0.001) || kind === 'image')
          layers.push({ id: n.id, order: myOrder, box, cols, kind, tokens, atmosphere: s.atmosphere, scrim: s.scrim, inst: s.inst ? s.inst.id : null });
      }
    }
    if (s.control && !s.disabled && !s.icon && hasStroke(n) && n.type !== 'TEXT')
      uiParts.push({ n, kind: 'border', order: myOrder, inInst: s.control, disabled: s.disabled, opacity });
    else if (s.focus && !s.icon && hasStroke(n))
      uiParts.push({ n, kind: 'focus', order: myOrder, inInst: s.instName, disabled: false, opacity });

    if ('children' in n) {
      const clip = n.clipsContent ? box : st.clip;
      const kids = n.children.filter((c) => c.visible !== false);
      const wrapper = n.type !== 'INSTANCE' && kids.length === 1 ? { w: n.width, h: n.height, id: n.id } : null;
      for (const c of n.children) await walk(c, { ...s, clip, parentWrapper: wrapper });
    }
    ends.set(n.id, order); // descendants are orders myOrder+1 .. end-1
  }

  await walk(screen, { opacity: 1, clip: screen.absoluteBoundingBox, inst: null, disabled: false });
  layerCount.set(screen.id, order);

  // structure
  const mode = await modeOf(screen);
  const first = screen.children[0];
  const firstMain = first && first.type === 'INSTANCE' ? await mainOf(first) : null;
  const phone = isScreen(screen); // a frame targeted directly (e.g. a component's Focus states) skips the screen-chrome checks
  if (phone && (!firstMain || firstMain.name !== 'Screen Atmosphere'))
    add({ check: 'structure', sev: 'S3', screen: screen.id, node: screen.id, name: screen.name, scope: 'screen', detail: seen.has('Screen Atmosphere') ? 'Screen Atmosphere is not the first (bottom) layer' : 'no Screen Atmosphere instance' });
  if (phone && !seen.has('Status Bar')) add({ check: 'structure', sev: 'S3', screen: screen.id, node: screen.id, name: screen.name, scope: 'screen', detail: 'no Status Bar instance' });
  if (phone && !seen.has('Home Indicator')) add({ check: 'structure', sev: 'S3', screen: screen.id, node: screen.id, name: screen.name, scope: 'screen', detail: 'no Home Indicator instance' });
  if (phone && (Math.round(screen.width) !== 390 || screen.height < 844))
    add({ check: 'canvas', sev: 'S4', screen: screen.id, node: screen.id, name: screen.name, scope: 'screen', detail: 'frame ' + Math.round(screen.width) + '×' + Math.round(screen.height) + ' (canvas is 390×844; height may grow)' });
  const pageFill = visiblePaints(screen.fills)[0];
  if (pageFill && pageFill.boundVariables && pageFill.boundVariables.color) {
    const m = await vmeta(pageFill.boundVariables.color.id, screen.id);
    if (m && m.name !== 'surface/page') add({ check: 'frame-fill', sev: 'S4', screen: screen.id, node: screen.id, name: screen.name, scope: 'screen', detail: 'frame fill is `' + m.name + '`; screens use surface/page' });
  }

  // background behind a point, composited bottom-up; returns { c, tokens, kind } or null if covered
  const bgAt = (x, y, beforeOrder, selfOrder, selfEnd) => {
    const stack = layers.filter((l) => l.order < beforeOrder && !l.atmosphere && contains(l.box, x, y) && !(l.order >= selfOrder && l.order < selfEnd));
    const above = layers.find((l) => l.order >= selfEnd && !l.atmosphere && contains(l.box, x, y) && (l.scrim || l.cols.some((c) => c.c.a >= 0.2)));
    let c = { r: 1, g: 1, b: 1, a: 1 }, kind = 'solid', tokens = [];
    for (const l of stack) {
      if (l.kind === 'image') { kind = 'image'; tokens = ['image']; continue; }
      if (l.cols.some((p) => p.c.a >= 0.99) && l.kind === 'solid') { kind = 'solid'; tokens = []; }
      if (l.kind === 'gradient' && kind !== 'image') kind = 'gradient';
      for (const p of l.cols) c = over(p.c, c);
      tokens = tokens.concat(l.tokens);
    }
    return { c, tokens: tokens.slice(-2).reverse(), kind: stack.length ? kind : 'none', covered: !!above, topInst: stack.length ? stack[stack.length - 1].inst : null };
  };
  const pair = (fg, bg, m, k, r, need, id) => {
    const key = [fg, bg, m, k].join('|');
    const p = contrastPairs.get(key) || { fg, bg, mode: m, kind: k, min: 99, count: 0, need, example: id };
    p.count++; if (r < p.min) { p.min = r; p.example = id; }
    contrastPairs.set(key, p);
  };

  for (const t of texts) {
    if (t.atmosphere || !t.box || !t.n.characters.trim()) continue;
    if (t.disabled) { exemptCount['disabled text'] = (exemptCount['disabled text'] || 0) + 1; continue; }
    const cx = t.box.x + t.box.width / 2, cy = t.box.y + t.box.height / 2;
    const bg = bgAt(cx, cy, t.order, t.order, t.order + 1);
    if (bg.covered) { exemptCount['text covered by an overlay'] = (exemptCount['text covered by an overlay'] || 0) + 1; continue; }
    if (bg.kind === 'image' || bg.kind === 'none') { notMeasured.push({ screen: screen.id, node: t.n.id, name: t.n.name, why: bg.kind === 'image' ? 'text over an image' : 'no background found behind it' }); continue; }
    const segs = t.n.getStyledTextSegments(['fills', 'fontSize', 'fontWeight']);
    for (const sg of segs) {
      if (!sg.characters.trim()) continue;
      const large = sg.fontSize >= 24 || (sg.fontSize >= 19 && sg.fontWeight >= 700);
      const need = large ? 3 : 4.5;
      for (const p of visiblePaints(sg.fills)) {
        const pc = await paintColors(p, t.n);
        if (!pc) continue;
        // a huge, faint glyph (watermark) is decoration, which WCAG 1.4.3 exempts
        if (sg.fontSize >= 48 && pc.every((x) => x.c.a * t.opacity <= 0.2)) { exemptCount['decorative text (≥48px, ≤20% opacity)'] = (exemptCount['decorative text (≥48px, ≤20% opacity)'] || 0) + 1; continue; }
        let worst = 99, tok = null;
        for (const x of pc) {
          if (x.token === 'text/disabled') { worst = 99; tok = 'text/disabled'; break; }
          const fg = over({ ...x.c, a: x.c.a * t.opacity }, bg.c);
          const r = ratio(fg, bg.c);
          if (r < worst) { worst = r; tok = pc.map((y) => y.token || hex(y.c)).join('→'); }
        }
        if (tok === 'text/disabled') { exemptCount['text/disabled token'] = (exemptCount['text/disabled token'] || 0) + 1; continue; }
        const bgName = bg.tokens.join(' over ') || 'white';
        pair(tok, bgName, mode, large ? 'large text' : 'text', worst, need, t.n.id);
        // text and the surface right behind it both come from one DS instance, untouched by the screen: the component's own pairing
        const own = t.inst && bg.topInst === t.inst && !t.overridden;
        if (worst < need) add({ check: 'contrast', sev: 'S2', screen: screen.id, node: t.n.id, name: t.n.name, scope: own ? 'ds' : 'screen', component: own ? t.inInst : null, inInstance: t.inInst || null,
          text: sg.characters.slice(0, 40).replace(/\n/g, ' '), detail: r2(worst) + ':1 (needs ' + need + ':1' + (large ? ', large text' : '') + ') · `' + tok + '` on ' + bgName + ' · ' + mode + (bg.kind === 'gradient' ? ' · gradient bg, approximate' : '') });
      }
    }
  }
  for (const u of uiParts) {
    if (u.disabled || u.n.visible === false) continue;
    const b = u.n.absoluteBoundingBox; if (!b) continue;
    let paint = null, target = u.n;
    if (u.kind === 'icon') {
      target = u.n.findOne((v) => v.visible !== false && (hasStroke(v) || (v.type !== 'FRAME' && visiblePaints(v.fills).length)));
      if (!target) continue;
      paint = hasStroke(target) ? visiblePaints(target.strokes)[0] : visiblePaints(target.fills)[0];
    } else paint = visiblePaints(u.n.strokes)[0];
    const pc = paint && (await paintColors(paint, target));
    if (!pc) continue;
    // UI parts are judged against what is outside them, so the part's own fill and children don't count
    const bg = bgAt(b.x + b.width / 2, b.y + b.height / 2, u.order, u.order, ends.get(u.n.id) || u.order + 1);
    if (bg.covered || bg.kind === 'image' || bg.kind === 'none') continue;
    let worst = 99, tok = pc.map((y) => y.token || hex(y.c)).join('→');
    for (const x of pc) worst = Math.min(worst, ratio(over({ ...x.c, a: x.c.a * u.opacity }, bg.c), bg.c));
    // a control whose own fill already stands out 3:1 from its surroundings doesn't need its border to
    const own = u.kind === 'border' && layers.find((l) => l.id === u.n.id);
    if (own && own.kind === 'solid') {
      let fc = bg.c; for (const p of own.cols) fc = over(p.c, fc);
      if (ratio(fc, bg.c) >= 3) worst = Math.max(worst, ratio(fc, bg.c));
    }
    const bgName = bg.tokens.join(' over ') || 'white';
    const kind = u.kind === 'icon' ? 'icon' : u.kind === 'focus' ? 'focus ring' : 'border';
    pair(tok, bgName, mode, kind, worst, 3, u.n.id);
    if (worst < 3) add({ check: 'contrast-ui', sev: 'S2', screen: screen.id, node: u.n.id, name: u.n.name, scope: u.inInst ? 'ds' : 'screen', component: u.inInst || null,
      detail: kind + ' ' + r2(worst) + ':1 (needs 3:1) · `' + tok + '` on ' + bgName + ' · ' + mode + (u.kind === 'icon' ? ' · only if the icon carries meaning' : '') });
  }

  // hit targets
  for (const t of taps) {
    const b = t.n.absoluteBoundingBox; if (!b) continue;
    let w = b.width, h = b.height;
    if (t.wrapper && t.wrapper.w >= w && t.wrapper.h >= h) { w = t.wrapper.w; h = t.wrapper.h; }
    const style = t.props.Style ? t.props.Style.value : null;
    const primary = t.name === 'Button' && style === 'Solid';
    const short = Math.min(w, h);
    const scope = t.inInst ? 'ds' : 'screen';
    const what = t.name + (style ? ' ' + style : '') + (t.inInst ? ' inside ' + t.inInst : '');
    // name the short side only, so the same chip row groups into one finding
    const size = w < 44 && h < 44 ? Math.round(w) + '×' + Math.round(h) : h < w ? Math.round(h) + ' pt tall' : Math.round(w) + ' pt wide';
    if (short < 24) add({ check: 'hit-target', sev: 'S2', screen: screen.id, node: t.n.id, name: t.n.name, scope, component: t.inInst, detail: what + ' is ' + size + ': under 24 (WCAG 2.5.8) unless spaced or an equivalent control exists' });
    else if (short < 44) add({ check: 'hit-target', sev: primary ? 'S2' : 'S3', screen: screen.id, node: t.n.id, name: t.n.name, scope, component: t.inInst, detail: what + ' is ' + size + ': under 44 pt (house rule)' + (primary ? ', primary action' : '') });
    else if (primary && short < 48 && !(t.n.annotations || []).some((a) => /48/.test(a.label || a.labelMarkdown || '')))
      add({ check: 'hit-target-android', sev: 'S3', screen: screen.id, node: t.n.id, name: t.n.name, scope, component: t.inInst, detail: 'primary Button ' + Math.round(w) + '×' + Math.round(h) + ': annotate a 48×48 dp Android hit area (D-04)' });
  }
}

let i = FROM;
for (; i < screens.length; i++) {
  if (Date.now() - t0 > BUDGET_MS) { next = i; break; }
  await auditScreen(screens[i].node);
}

// name the components that frames were detached from (DS file only: product files can't look up library keys)
const detachedKeys = new Set(findings.filter((f) => f.check === 'detached' && f.key).map((f) => f.key));
if (isDsFile && detachedKeys.size) {
  const names = new Map();
  await figma.loadAllPagesAsync();
  for (const p of figma.root.children) {
    if (/Icons|Sandbox/.test(p.name)) continue;
    for (const c of p.findAllWithCriteria({ types: ['COMPONENT'] })) if (detachedKeys.has(c.key)) names.set(c.key, c.parent.type === 'COMPONENT_SET' ? c.parent.name + ' (' + c.name + ')' : c.name);
  }
  for (const f of findings) if (f.check === 'detached' && names.has(f.key)) f.detail = 'detached from the DS component "' + names.get(f.key) + '"';
}
for (const f of findings) if (f.check === 'detached' && f.componentId) {
  const c = await figma.getNodeByIdAsync(f.componentId);
  if (c) f.detail = 'detached from the local component "' + (c.parent && c.parent.type === 'COMPONENT_SET' ? c.parent.name : c.name) + '"';
}

// group repeats: same problem on one screen -> one finding; same problem inside a DS component -> one finding across screens
const groups = new Map();
for (const f of findings) {
  const key = f.scope === 'ds' ? ['ds', f.check, f.component, f.detail].join('|') : [f.screen, f.check, f.detail, f.inInstance || ''].join('|');
  const g = groups.get(key);
  if (!g) { groups.set(key, { ...f, count: 1, nodes: [f.node], screens: f.scope === 'ds' ? [f.screen] : undefined }); continue; }
  g.count++;
  if (g.nodes.length < 6) g.nodes.push(f.node);
  if (g.screens && !g.screens.includes(f.screen) && g.screens.length < 6) g.screens.push(f.screen);
}
const grouped = [...groups.values()].map((g) => { delete g.componentId; return g; });

const contrast = [...contrastPairs.values()].map((p) => [p.fg, p.bg, p.mode, p.kind, r2(p.min), p.count, p.need, p.example]);
const DS_COLLECTIONS = ['6a54a2191a1381de06926ce7fbf437348551bf05', DS_COLOR_KEY, '00fe2be19c8c4ab791bce372d11b4ef4b13d1e87', '30e508c183603bcfc4b39e178c4e98a5466fce30', '5102cecaeeef8b6305278786c4ecbf7f26aea9ce'];
const foreignVars = Object.values(uses.variables).filter((u) => !DS_COLLECTIONS.includes(u[2]));
return { exportedAt: new Date().toISOString(), file: figma.root.name, isDsFile, target: TARGET, from: FROM, next, audited: [FROM, i],
  ms: Date.now() - t0, screens: screenList.map((s) => [s.id, s.name, s.w, s.h, s.section, s.mode, layerCount.get(s.id) || null]),
  findings: grouped, contrast, foreignVariables: foreignVars, styles: Object.values(uses.styles), exempt: exemptCount, notMeasured };
