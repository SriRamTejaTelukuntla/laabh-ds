// Read what /design-review needs from screens that a screenshot can't show reliably. Read-only: it never changes the file.
// Run in the DS or product file (figma_execute / use_figma). Set TARGET to node IDs (a page, section or screen frame).
// Returns { exportedAt, file, target, screens, more } where each screen is:
//   { id, name, section, mode, size, texts, components, annotations, anIds, flags }
//   texts       visible text in reading order (top to bottom, then left to right): "<characters> [<text style>]"
//   components  DS instances that aren't nested in another instance: "<component> (<variant props>) {<text props>}"
//   annotations Figma annotations on the screen and its layers: "<layer>: <label>"; anIds = the AN-xx IDs they start with
//   flags       things easy to miss in a screenshot: hyphen used as a minus, K/M/B abbreviations, placeholder-looking text
// `more` names screens past MAX_SCREENS (run again with those IDs). Save with scripts/figma-result.py <exportedAt> <out.json>.
const TARGET = ['101:129022'];
const MAX_SCREENS = 40;
const MAX_TEXTS = 150;

const isScreen = (n) => n.type === 'FRAME' && n.width >= 320 && n.width <= 440 && n.height >= 560;
const screens = [];
async function collect(node, path) {
  for (const c of node.children || []) {
    if (c.type === 'SECTION') await collect(c, path.concat(c.name));
    else if (isScreen(c)) screens.push({ node: c, path });
  }
}
for (const id of TARGET) {
  const n = await figma.getNodeByIdAsync(id);
  if (!n) continue;
  let page = n; while (page.type !== 'PAGE') page = page.parent;
  await page.loadAsync();
  if (n.type === 'PAGE' || n.type === 'SECTION') await collect(n, n.type === 'SECTION' ? [n.name] : []);
  else if (n.type === 'FRAME') screens.push({ node: n, path: n.parent.type === 'SECTION' ? [n.parent.name] : [] });
}

const collCache = new Map();
async function modeOf(n) {
  for (const [cid, mid] of Object.entries(n.resolvedVariableModes || {})) {
    if (!collCache.has(cid)) collCache.set(cid, await figma.variables.getVariableCollectionByIdAsync(cid));
    const c = collCache.get(cid);
    if (c && c.name === 'Color Tokens') { const m = c.modes.find((x) => x.modeId === mid); return m ? m.name : '?'; }
  }
  return null;
}
const styleCache = new Map();
async function styleName(id) {
  if (!id || id === figma.mixed) return id === figma.mixed ? 'mixed' : 'UNSTYLED';
  if (!styleCache.has(id)) { const s = await figma.getStyleByIdAsync(id); styleCache.set(id, s ? s.name : '?'); }
  return styleCache.get(id);
}
const visible = (n, root) => { for (let p = n; p && p !== root.parent; p = p.parent) if (p.visible === false) return false; return true; };
const insideInstance = (n, root) => { for (let p = n.parent; p && p !== root; p = p.parent) if (p.type === 'INSTANCE') return true; return false; };

const out = [];
for (const s of screens.slice(0, MAX_SCREENS)) {
  const root = s.node;
  const texts = [], flags = [], components = [], annotations = [];
  const nodes = [root, ...root.findAll(() => true)].filter((n) => visible(n, root));
  const textNodes = nodes.filter((n) => n.type === 'TEXT' && n.characters.trim())
    .map((n) => ({ n, b: n.absoluteBoundingBox || { x: 0, y: 0 } }))
    .sort((a, b) => (Math.abs(a.b.y - b.b.y) < 4 ? a.b.x - b.b.x : a.b.y - b.b.y));
  for (const { n } of textNodes.slice(0, MAX_TEXTS)) {
    const t = n.characters.replace(/\s+/g, ' ').trim();
    texts.push(t.slice(0, 120) + ' [' + (await styleName(n.textStyleId)) + ']');
    if (/(^|[\s(₹])-\s?₹?\d/.test(t)) flags.push('hyphen as minus: "' + t.slice(0, 60) + '" (use the true minus −, TR-NUM-07)');
    if (/\d\s?[KMB]\b/.test(t)) flags.push('K/M/B abbreviation: "' + t.slice(0, 60) + '" (L/Cr only, TR-NUM-04)');
    if (/lorem|ipsum|placeholder|xxxx|\bTBD\b/i.test(t)) flags.push('placeholder text: "' + t.slice(0, 60) + '"');
  }
  if (textNodes.length > MAX_TEXTS) texts.push('… ' + (textNodes.length - MAX_TEXTS) + ' more texts');
  for (const n of nodes) {
    if (n.type === 'INSTANCE' && !insideInstance(n, root)) {
      const m = await n.getMainComponentAsync();
      const set = m && m.parent && m.parent.type === 'COMPONENT_SET' ? m.parent.name : m ? m.name : '?';
      const props = Object.entries(n.componentProperties || {});
      const v = props.filter(([, p]) => p.type === 'VARIANT').map(([k, p]) => k + '=' + p.value).join(', ');
      const tx = props.filter(([, p]) => p.type === 'TEXT').map(([k, p]) => k.split('#')[0] + '="' + String(p.value).slice(0, 40) + '"').join(', ');
      const off = props.filter(([, p]) => p.type === 'BOOLEAN' && p.value === false).map(([k]) => k.split('#')[0]).join(', ');
      components.push(set + (v ? ' (' + v + ')' : '') + (tx ? ' {' + tx + '}' : '') + (off ? ' [off: ' + off + ']' : ''));
    }
    for (const a of n.annotations || []) {
      const label = (a.label || a.labelMarkdown || '').replace(/\s+/g, ' ').trim();
      if (label) annotations.push(n.name + ': ' + label.slice(0, 160));
    }
  }
  const anIds = [...new Set(annotations.map((a) => (a.match(/\bAN-\d{2}\b/g) || [])).flat())].sort();
  out.push({ id: root.id, name: root.name, section: s.path.join(' / '), mode: await modeOf(root),
    size: Math.round(root.width) + '×' + Math.round(root.height), texts, components, annotations, anIds, flags: [...new Set(flags)] });
}

return { exportedAt: new Date().toISOString(), file: figma.root.name, target: TARGET, screens: out,
  more: screens.slice(MAX_SCREENS).map((s) => s.node.id) };
