// Export all local variables from the DS file as DTCG JSON (legacy dialect: hex strings, px numbers).
// Run inside the DS Figma file with use_figma (official MCP) or figma_execute (figma-console).
// Returns { meta, files } where files maps "tokens/<name>.json" -> token tree.
// The agent writes each file to disk, then runs scripts/format-tokens.py.
// Multi-mode collections: $value = first mode (Light / Mobile); other modes live in $extensions.modes.
// Do not use figma_export_tokens: it read a stale cache (Oct 2026) and dropped and misnamed variables.

const FILE_FOR = {
  'Color Primitives': 'primitives.color',
  'Typography Primitives': 'primitives.typography',
  'Spacing & Radius Primitives': 'primitives.spacing-radius',
  'Color Tokens': 'semantic.color',
  'Typography Tokens': 'semantic.typography',
};

const hex = (c) => {
  const h = (x) => Math.round(x * 255).toString(16).padStart(2, '0');
  const a = c.a === undefined ? 1 : c.a;
  return '#' + h(c.r) + h(c.g) + h(c.b) + (a < 1 ? h(a) : '');
};

const collections = await figma.variables.getLocalVariableCollectionsAsync();
const variables = await figma.variables.getLocalVariablesAsync();
const byId = new Map(variables.map((v) => [v.id, v]));

const typeOf = (v) => {
  if (v.resolvedType === 'COLOR') return 'color';
  if (v.resolvedType === 'STRING') return v.name.includes('family') ? 'fontFamily' : v.name.includes('weight') ? 'fontWeight' : 'string';
  if (v.resolvedType === 'BOOLEAN') return 'boolean';
  if (v.name.includes('weight')) return 'fontWeight';
  if (v.name.includes('opacity')) return 'number';
  return 'dimension';
};

const value = (v, raw) => {
  if (raw && raw.type === 'VARIABLE_ALIAS') {
    const target = byId.get(raw.id);
    return target ? '{' + target.name.split('/').join('.') + '}' : '{UNRESOLVED ' + raw.id + '}';
  }
  if (v.resolvedType === 'COLOR') return hex(raw);
  if (v.resolvedType === 'FLOAT') return typeOf(v) === 'dimension' ? Math.round(raw * 100) / 100 + 'px' : raw;
  return raw;
};

// Put a token at a slash path. A name that is both a token and a group uses "$root" (DTCG 2025).
const put = (tree, path, token) => {
  let node = tree;
  for (const key of path.slice(0, -1)) {
    if (node[key] && node[key].$value !== undefined) node[key] = { $root: node[key] };
    node = node[key] = node[key] || {};
  }
  const last = path[path.length - 1];
  if (node[last] && node[last].$value === undefined) node[last].$root = token;
  else node[last] = token;
};

const files = {};
const meta = { kind: 'variables', fileKey: figma.fileKey, exportedAt: new Date().toISOString(), collections: [] };

for (const c of collections) {
  const name = FILE_FOR[c.name] || 'other.' + c.name.toLowerCase().replace(/[^a-z0-9]+/g, '-');
  const [first, ...rest] = c.modes;
  const tree = { $description: c.name + ' (Figma collection ' + c.id + ', modes: ' + c.modes.map((m) => m.name).join(', ') + ')' };
  let count = 0;
  for (const id of c.variableIds) {
    const v = byId.get(id);
    if (!v) continue;
    const token = { $type: typeOf(v), $value: value(v, v.valuesByMode[first.modeId]) };
    if (rest.length) {
      token.$extensions = { modes: {} };
      for (const m of rest) token.$extensions.modes[m.name] = value(v, v.valuesByMode[m.modeId]);
    }
    if (v.description) token.$description = v.description;
    put(tree, v.name.split('/'), token);
    count++;
  }
  files['tokens/' + name + '.json'] = tree;
  meta.collections.push({ name: c.name, file: 'tokens/' + name + '.json', id: c.id, key: c.key, modes: c.modes.map((m) => m.name + ' ' + m.modeId), count });
}

return { meta, files };
