# Keep the kit useful over time

Instructions and prompts tend to grow after a confusing task. Without cleanup, they become contradictory, too broad, or stale. Maintain them like code: change them when the workflow changes, and remove rules that no longer help.

## When to update

- A repeated review comment reveals an important invariant.
- A project command, architecture boundary, or supported interface changes.
- An agent repeatedly misses a check or follows a misleading example.
- A rule creates false alarms or conflicts with a more specific instruction.

## Lightweight review

Every few months, or during a project workflow review:

1. Check setup and verification commands against the current project configuration.
2. Follow links and remove outdated examples.
3. Read root and nested `AGENTS.md` files together for conflicts or duplicated rules.
4. Remove rules that are obvious, unenforced, or no longer useful.
5. Try one representative task and one safe counterexample for any new review rule.

Keep the review proportional. A small repository may only need a quick README and command check; a larger team can assign ownership and automate link or structure checks.
