# Rule: working safely in Figma

- **Know which file you're in.** Product screens go in the feature's own Figma file (`Laabh — <Feature>`, linked in `prds/<feature>/plan.md`). Never put two features in one file.
- **Library up to date.** Before building or reviewing in a feature file, ask whether it shows "Library updates available" (scripts can't see this) and have it accepted first. The DS file is read-only unless the task is `/new-component` or a DS owner asks.
- **Look before you write.** Screenshot or inspect the target page first, then place new work in clear space inside a named Section. Never overlap existing work.
- **Ask first** before deleting, moving, renaming or restructuring anything you did not create in this session, and before creating pages.
- **Clean up after failures.** If a step fails halfway, remove the partial frames you created before retrying.
- **Small steps.** One section or screen per `use_figma` call; screenshot after each step.
- Re-find nodes each session by name or key. Node IDs you remember from another session may be stale.
- Never publish the library, change variable values or edit component masters as a side effect of building screens.
