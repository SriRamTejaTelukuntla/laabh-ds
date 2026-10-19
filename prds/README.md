# prds/

One folder per feature: `prds/<feature-name>/`

| File | Who writes it | What it is |
|---|---|---|
| `prd.md` | PM / designer | The PRD (paste from Google Docs, PDF or Notion; any format is fine) |
| `plan.md` | Claude (`/prd-to-screens`) | Review context, flows, screen list with IDs, components, states, rules that apply, open questions, Decisions & waivers, Figma links, status |
| `review.md` | Claude (`/design-review`) | UX + accessibility review reports, newest on top, with the verdict |
| `notes.md` | Anyone | Feedback and discussion from reviews (decisions that stick go in `plan.md` or `docs/ux/decisions.md`) |

`plan.md` is how work survives switching laptops or people: Claude updates it after every approved step.
