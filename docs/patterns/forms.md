# Forms

## Layout
- One topic per screen in onboarding/KYC (a "Step Heading" + 1–4 inputs). Long forms split into steps rather than scroll.
- Body gap `space/24` between the heading and each input. Inputs are full width (Fill).
- Field size **md** (52 field) by default; **lg** (56) for a single hero input (mobile number, amount). Input text is 16px.
- Primary CTA in the footer: `Button Solid · Brand · lg`. Disabled until the form is valid **only** if the PRD asks; otherwise validate on submit.

## Choosing the input
| Data | Component |
|---|---|
| Free text, name, email, PAN | TextField (`Show prefix` for +91 / ₹) |
| 2–3 options (gender, marital status) | Label (`body-sm/Medium`, `text/secondary`) + Segmented Control/Neutral/md, full width |
| 2–5 short options | Radio Group |
| Options that need explanation | Option Card group |
| 5+ options | Dropdown |
| Consent / declaration | Checkbox (never pre-ticked) |
| Code from SMS/email | OTP Input |
| Amount | TextField/Amount (quick-add chips) |
| Long text | TextArea with count |

## Validation
- Show errors after the person leaves the field, or on submit. Never while typing.
- Error = `State=Error` + helper text with ⚠ and what to do ("Enter a 10-digit mobile number").
- Prefilled data (from KYC/DigiLocker): `Style=Filled`, `State=Filled`, with a note in the Step Heading description ("Prefilled from your KYC record. Edit anything that's wrong.").
- Server errors and failures (penny-drop failed): an Alert `Danger` at the top of the Body with the fix as its action.

## States to design (list them in the plan)
Default · Focus (keyboard up) · Filled · Error · Loading on submit (CTA) · Prefilled · Disabled (only when truly unavailable).
