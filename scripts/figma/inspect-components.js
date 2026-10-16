// Inspect DS components and render the AUTO block of docs/components/<name>.md from the real bindings.
// Run in the DS file (use_figma or figma_execute). Set GROUPS to { "<doc-file-name>": [node IDs] }
// (IDs from docs/index.md; one group per docs/components/<name>.md). Returns { <name>: { md, docText, raw } } where:
//   md      = markdown to paste between <!-- AUTO:START --> and <!-- AUTO:END -->
//   docText = the text written on the component page's Reference/Patterns frames (to compare, not to trust)
//   raw     = count of unbound fills/strokes and unstyled text across all variants (should be 0)
const GROUPS = { alert: ['55:92'] };

const vars = await figma.variables.getLocalVariablesAsync();
const vName = new Map(vars.map((v) => [v.id, v.name]));
const tStyle = new Map((await figma.getLocalTextStylesAsync()).map((s) => [s.id, s.name]));
const eStyle = new Map((await figma.getLocalEffectStylesAsync()).map((s) => [s.id, s.name]));

const bound = (n, k) => {
  const b = n.boundVariables && n.boundVariables[k];
  if (!b) return null;
  return Array.isArray(b) ? b.map((a) => vName.get(a.id) || '?').join(', ') : vName.get(b.id) || '?';
};
const num = (n, k, tokKey) => bound(n, tokKey || k) || (typeof n[k] === 'number' ? String(Math.round(n[k] * 100) / 100) : null);
const hasPaint = (p) => Array.isArray(p) && p.some((x) => x.visible !== false && x.type !== 'IMAGE');

function facts(n) {
  const f = [];
  if (n.layoutMode && n.layoutMode !== 'NONE') {
    const pad = ['paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft'].map((k) => num(n, k) || '0');
    if (pad.some((p) => p !== '0')) f.push('pad ' + (new Set(pad).size === 1 ? pad[0] : pad.join(' ')));
    if (n.itemSpacing) f.push('gap ' + num(n, 'itemSpacing'));
  }
  const r = bound(n, 'topLeftRadius') || (typeof n.cornerRadius === 'number' && n.cornerRadius ? String(n.cornerRadius) : null);
  if (r) f.push('radius ' + r);
  if (n.type === 'TEXT') f.push('text ' + (n.textStyleId === figma.mixed
    ? [...new Set(n.getStyledTextSegments(['textStyleId']).map((g) => tStyle.get(g.textStyleId) || 'UNSTYLED'))].join(' + ')
    : tStyle.get(n.textStyleId) || 'UNSTYLED'));
  if ('fills' in n && hasPaint(n.fills)) f.push('fill ' + (bound(n, 'fills') || 'RAW'));
  if ('strokes' in n && hasPaint(n.strokes)) f.push('stroke ' + (bound(n, 'strokes') || 'RAW') + ' ' + n.strokeWeight + 'px');
  if (n.effectStyleId) f.push('effect ' + eStyle.get(n.effectStyleId));
  return f.join(' · ');
}

async function anatomy(root, depth = 0, lines = []) {
  for (const c of root.children || []) {
    if (lines.length > 24 || c.visible === false) continue;
    let label = c.name;
    if (c.type === 'INSTANCE') {
      const main = await c.getMainComponentAsync();
      const set = main && main.parent && main.parent.type === 'COMPONENT_SET' ? main.parent.name : main && main.name;
      label += ' → `' + set + '`';
    }
    lines.push('  '.repeat(depth) + '- ' + label + (facts(c) ? ' — ' + facts(c) : ''));
    if (c.type !== 'INSTANCE' && depth < 2) await anatomy(c, depth + 1, lines);
  }
  return lines;
}

async function inspect(IDS) {
const out = [];
let raw = 0;
const docPages = new Set();
for (const id of IDS) {
  const node = await figma.getNodeByIdAsync(id);
  if (!node) { out.push('> Node ' + id + ' not found'); continue; }
  let page = node; while (page.type !== 'PAGE') page = page.parent;
  docPages.add(page);
  const isSet = node.type === 'COMPONENT_SET';
  const variants = isSet ? node.children : [node];
  const def = isSet ? node.defaultVariant : node;

  out.push('### ' + node.name, '');
  out.push('| | |', '|---|---|');
  out.push('| Node ID | `' + node.id + '` (page `' + page.id + '`) |');
  out.push('| Key | `' + node.key + '` |');
  out.push('| Variants | ' + variants.length + ' · default: `' + def.name + '` |');
  out.push('| Default size | ' + Math.round(def.width) + '×' + Math.round(def.height) + ' |', '');

  const defs = node.componentPropertyDefinitions || {};
  if (Object.keys(defs).length) {
    out.push('| Property | Type | Values / default |', '|---|---|---|');
    for (const [k, d] of Object.entries(defs)) {
      const vals = d.type === 'VARIANT' ? d.variantOptions.join(', ') + ' (default ' + d.defaultValue + ')' : String(d.defaultValue).slice(0, 40);
      out.push('| ' + k.split('#')[0] + ' | ' + d.type.toLowerCase() + ' | ' + vals + ' |');
    }
    out.push('');
  }

  const sizeKey = Object.keys(defs).find((k) => k.split('#')[0] === 'Size' && defs[k].type === 'VARIANT');
  if (isSet && sizeKey) {
    out.push('| Size | H | Specs (default variant at that size) |', '|---|---|---|');
    const base = Object.fromEntries(Object.entries(def.variantProperties || {}));
    for (const s of defs[sizeKey].variantOptions) {
      const v = variants.find((x) => Object.entries({ ...base, Size: s }).every(([k, val]) => x.variantProperties[k] === val)) ||
        variants.find((x) => x.variantProperties.Size === s);
      if (v) out.push('| ' + s + ' | ' + Math.round(v.height) + ' | ' + facts(v) + ' |');
    }
    out.push('');
  }

  out.push('**Anatomy (default variant):** ' + (facts(def) || '—'), '');
  out.push(...(await anatomy(def)), '');

  const colors = new Set(), texts = new Set(), effects = new Set();
  for (const v of variants) {
    for (const n of [v, ...v.findAll(() => true)]) {
      if (n.type === 'TEXT') {
        const ids = n.textStyleId === figma.mixed ? n.getStyledTextSegments(['textStyleId']).map((g) => g.textStyleId) : [n.textStyleId];
        for (const id of ids) { const s = tStyle.get(id); s ? texts.add(s) : raw++; }
      }
      for (const k of ['fills', 'strokes']) {
        if (!(k in n) || !hasPaint(n[k])) continue;
        const b = bound(n, k); b ? b.split(', ').forEach((t) => colors.add(t)) : n.type !== 'INSTANCE' && raw++;
      }
      if (n.effectStyleId) effects.add(eStyle.get(n.effectStyleId));
    }
  }
  const list = (s) => [...s].sort().map((x) => '`' + x + '`').join(' ');
  out.push('**Colour tokens across all variants:** ' + (list(colors) || '—'));
  out.push('**Text styles:** ' + (list(texts) || '—') + ' · **Effects:** ' + (list(effects) || '—'), '');
}

const docText = [];
for (const page of docPages) {
  for (const f of page.children) {
    if (!/— (Reference|Patterns)$/.test(f.name)) continue;
    const t = f.findAllWithCriteria({ types: ['TEXT'] })
      .filter((x) => { let p = x.parent; while (p && p !== f) { if (p.type === 'INSTANCE') return false; p = p.parent; } return true; })
      .map((x) => x.characters.replace(/\s+/g, ' ').trim()).filter((s) => s.length > 2);
    docText.push(f.name + ': ' + t.join(' | ').slice(0, 2500));
  }
}

return { md: out.join('\n'), docText, raw };
}

const result = {};
for (const [name, ids] of Object.entries(GROUPS)) result[name] = await inspect(ids);
return result;
