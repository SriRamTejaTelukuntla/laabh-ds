// Fingerprint the DS file so drift against the repo can be found cheaply.
// Run in the DS file (use_figma or figma_execute). Compare the result with
// `python3 scripts/fingerprint.py` (same hashes computed from tokens/ and docs/index.md).
// Returns { file, variables: {collection: {modes, count, groups: {group: [count, hash]}}},
//           text: {role: hash}, effects: {name: hash}, components: [[name, key, variants, propsHash, pageName]] }

const hash = (s) => { let h = 0; for (const ch of s) h = (Math.imul(h, 31) + ch.codePointAt(0)) >>> 0; return h.toString(16); };
const hex = (c) => {
  const h = (x) => Math.round(x * 255).toString(16).padStart(2, '0');
  const a = c.a === undefined ? 1 : c.a;
  return '#' + h(c.r) + h(c.g) + h(c.b) + (a < 1 ? h(a) : '');
};
const vars = await figma.variables.getLocalVariablesAsync();
const byId = new Map(vars.map((v) => [v.id, v]));
const ref = (id) => { const t = byId.get(id); return t ? '{' + t.name.split('/').join('.') + '}' : '{?}'; };
const fmt = (v, raw) => {
  if (raw && raw.type === 'VARIABLE_ALIAS') return ref(raw.id);
  if (v.resolvedType === 'COLOR') return hex(raw);
  if (v.resolvedType === 'FLOAT') {
    const dim = !/weight|opacity/.test(v.name);
    return dim ? Math.round(raw * 100) / 100 + 'px' : String(raw);
  }
  return String(raw);
};

const variables = {};
for (const c of await figma.variables.getLocalVariableCollectionsAsync()) {
  const groups = {};
  for (const id of c.variableIds) {
    const v = byId.get(id);
    const g = v.name.split('/')[0];
    (groups[g] = groups[g] || []).push(v.name + '=' + c.modes.map((m) => fmt(v, v.valuesByMode[m.modeId])).join('|'));
  }
  variables[c.name] = {
    modes: c.modes.map((m) => m.name).join(','),
    count: c.variableIds.length,
    groups: Object.fromEntries(Object.entries(groups).map(([g, l]) => [g, [l.length, hash(l.sort().join('\n'))]])),
  };
}

const unit = (u) => (u.unit === 'PIXELS' ? Math.round(u.value * 100) / 100 + 'px' : u.unit === 'PERCENT' ? Math.round(u.value * 100) / 100 + '%' : 'auto');
const text = {};
for (const s of await figma.getLocalTextStylesAsync()) {
  const b = s.boundVariables || {};
  const r = (k, raw) => (b[k] ? ref(b[k].id) : raw);
  const role = s.name.split('/')[0];
  (text[role] = text[role] || []).push([s.name, r('fontFamily', s.fontName.family), r('fontStyle', s.fontName.style), r('fontSize', s.fontSize + 'px'),
    r('lineHeight', unit(s.lineHeight)), unit(s.letterSpacing), s.textCase].join('|'));
}
for (const k of Object.keys(text)) text[k] = text[k].length + ':' + hash(text[k].sort().join('\n'));

const effects = {};
for (const s of await figma.getLocalEffectStylesAsync()) {
  effects[s.name] = hash(s.effects.map((e) => {
    const b = e.boundVariables || {};
    return [e.type, b.color ? ref(b.color.id) : e.color ? hex(e.color) : '', e.offset ? e.offset.x + ',' + e.offset.y : '', b.radius ? ref(b.radius.id) : e.radius, e.spread || 0].join('|');
  }).join('\n'));
}

await figma.loadAllPagesAsync();
const components = [];
for (const p of figma.root.children) {
  if (/Sandbox|Icons/.test(p.name)) continue;
  for (const n of p.findAllWithCriteria({ types: ['COMPONENT_SET', 'COMPONENT'] })) {
    if (n.type === 'COMPONENT' && n.parent.type === 'COMPONENT_SET') continue;
    let a = n.parent, dark = false; while (a && a.type !== 'PAGE') { if (/Dark/.test(a.name)) dark = true; a = a.parent; }
    if (dark) continue;
    const defs = n.componentPropertyDefinitions || {};
    const sig = Object.entries(defs).map(([k, d]) => k.split('#')[0] + ':' + d.type.toLowerCase() + ':' + (d.variantOptions || []).join(', ')).sort().join(';');
    components.push([n.name, n.key, n.type === 'COMPONENT_SET' ? n.children.length : 1, hash(sig), p.name.replace(/^\s*↳\s*/, ''), n.id]);
  }
}
return { file: figma.root.name, pages: figma.root.children.map((p) => p.name.trim()), variables, text, effects, components };
