// Export local text and effect styles from the DS file as DTCG JSON.
// Run like export-variables.js, then: python3 scripts/write-tokens.py <result.json>
// Values bound to variables are written as references ({font.size.body-md}); unbound values are literal.
// Style keys are included so agents can import styles into product files (importStyleByKeyAsync).

const variables = await figma.variables.getLocalVariablesAsync();
const byId = new Map(variables.map((v) => [v.id, v]));
const ref = (alias) => {
  const v = alias && byId.get(alias.id);
  return v ? '{' + v.name.split('/').join('.') + '}' : undefined;
};
const hex = (c) => {
  const h = (x) => Math.round(x * 255).toString(16).padStart(2, '0');
  return '#' + h(c.r) + h(c.g) + h(c.b) + (c.a < 1 ? h(c.a) : '');
};
const px = (n) => Math.round(n * 100) / 100 + 'px';
const unit = (u) => (u.unit === 'PIXELS' ? px(u.value) : u.unit === 'PERCENT' ? Math.round(u.value * 100) / 100 + '%' : 'auto');

const put = (tree, path, token) => {
  let node = tree;
  for (const key of path.slice(0, -1)) node = node[key] = node[key] || {};
  node[path[path.length - 1]] = token;
};

const text = { $description: 'Text styles (role/weight). num-* roles use the numeric family for figures.' };
const textStyles = await figma.getLocalTextStylesAsync();
for (const s of textStyles) {
  const b = s.boundVariables || {};
  put(text, s.name.split('/'), {
    $type: 'typography',
    $value: {
      fontFamily: ref(b.fontFamily) || s.fontName.family,
      fontWeight: ref(b.fontStyle) || ref(b.fontWeight) || s.fontName.style,
      fontSize: ref(b.fontSize) || px(s.fontSize),
      lineHeight: ref(b.lineHeight) || unit(s.lineHeight),
      letterSpacing: ref(b.letterSpacing) || unit(s.letterSpacing),
    },
    $extensions: { figma: { key: s.key, textCase: s.textCase, resolvedSize: s.fontSize, resolvedLineHeight: unit(s.lineHeight) } },
  });
}

const effects = { $description: 'Effect styles. Mode-aware through bound elevation/* color variables: Light uses soft shadows, Dark uses highlights and blur.' };
const effectStyles = await figma.getLocalEffectStylesAsync();
for (const s of effectStyles) {
  const layers = s.effects.map((e) => {
    const b = e.boundVariables || {};
    const layer = { type: e.type.toLowerCase().replace(/_/g, '-') };
    if (e.color) layer.color = ref(b.color) || hex(e.color);
    if (e.offset) {
      layer.offsetX = ref(b.offsetX) || px(e.offset.x);
      layer.offsetY = ref(b.offsetY) || px(e.offset.y);
    }
    if (e.radius !== undefined) layer.blur = ref(b.radius) || px(e.radius);
    if (e.spread !== undefined) layer.spread = ref(b.spread) || px(e.spread);
    if (e.visible === false) layer.visible = false;
    return layer;
  });
  put(effects, s.name.split('/'), { $type: 'shadow', $value: layers, $extensions: { figma: { key: s.key } } });
}

return {
  meta: {
    kind: 'styles',
    fileKey: figma.fileKey,
    exportedAt: new Date().toISOString(),
    collections: [
      { name: 'Text styles', file: 'tokens/styles.text.json', count: textStyles.length },
      { name: 'Effect styles', file: 'tokens/styles.effect.json', count: effectStyles.length },
    ],
  },
  files: { 'tokens/styles.text.json': text, 'tokens/styles.effect.json': effects },
};
