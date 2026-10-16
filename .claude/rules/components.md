# Rule: components first

1. Before drawing anything, check `docs/index.md` for a component that does the job.
2. Use an **instance** of the DS component and configure it only through its properties (variants, booleans, text, instance swap).
   - Never detach an instance. If a property is missing, report it as a gap.
   - Text inside instances is set through the component's TEXT properties (`Label`, `Title`, `Value`, ...).
3. Use the **smallest set of components** that expresses the screen. Prefer the variant that exists over overriding styles.
4. Product-specific compositions (e.g. a stock row, a holdings card) are built from DS components inside auto layout.
   When the same composition appears on 2+ screens, propose promoting it to a product component with `/new-component`.
5. Screen-specific sheet content uses the Bottom Sheet `Content` instance-swap slot, not a detached sheet.
6. Status Bar and Home Indicator instances go on every full screen (System Components page), with a `Screen Atmosphere` instance behind them as the first child.
7. Missing component? **Stop.** Tell the person what is missing and offer `/new-component`. Do not improvise a lookalike.
