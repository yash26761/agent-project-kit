# A practical AI-assisted development workflow

This guide is a lightweight routine for working with a coding agent in an unfamiliar or changing codebase. Adapt it to your team's review and release process.

## 1. Give the task enough shape

Include the outcome you want, the context the agent needs, and any constraints. For example:

> Add a way to export the current report as CSV. Keep the existing screen behavior, follow the project's export patterns, and include a check for empty reports. First inspect the relevant code and tell me your plan.

For a tiny, clear task, ask directly for the change. For work that touches several areas, ask for a short plan first and resolve important unknowns before implementation.

## 2. Match the process to the risk

- **Small and reversible:** make the change, run a focused check, inspect the diff.
- **Cross-cutting or uncertain:** inspect first, outline the approach and affected interfaces, then implement in reviewable steps.
- **High impact** (data migrations, auth, public contracts, security controls, production operations): identify failure modes and rollback or compatibility needs early; run the relevant checks and get the appropriate human review before release.

Do not force a planning ceremony onto a one-line fix. Do not treat a passing test suite as authorization to deploy, delete data, or make an external change.

## 3. Make one reviewable change at a time

- Ask the agent to inspect the relevant implementation and nearby examples.
- Keep the requested outcome narrow enough that you can understand the resulting diff.
- Let the agent explain assumptions when project behavior is unclear.
- Split independent features into separate tasks when that makes review easier.

## 4. Verify the result

Ask for checks that fit the project. Common examples include a focused test, the full test suite, formatting, linting, type checks, or a manual reproduction. A check that does not exist in the project should not be invented as though it does.

Useful follow-up:

> Run the checks relevant to this change. Tell me exactly which commands ran and whether they passed. If you could not run one, explain why.

## 5. Review before merging

Read the diff yourself. Look for behavior changes, missed edge cases, accidental generated files, and documentation that no longer matches the code. You can ask an agent to review the diff separately; treat that review as another set of eyes, not a substitute for project review.

## 6. Improve the repository guidance

When an agent repeatedly needs the same project context, add a short, durable note to `AGENTS.md` or a more specific directory-level file. Keep it concrete: real commands, important boundaries, and examples beat broad slogans. Remove obsolete guidance when the project changes.

## Prompt shape

For a clear task, use this pattern:

```text
Goal: [observable outcome]
Context: [relevant area or existing behavior]
Constraints: [compatibility, scope, or design limits]
Acceptance: [how we will know it works]
```

Not every task needs every field. See the [prompt library](../prompts/README.md) for examples.
