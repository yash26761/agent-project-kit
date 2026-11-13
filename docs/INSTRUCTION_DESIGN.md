# Design useful agent instructions

Agent instructions are part of the repository interface. They should help someone find the right facts and checks without repeating the whole handbook in every task.

## Put information where it belongs

| Put it here | When it belongs there | Examples |
| --- | --- | --- |
| Root `AGENTS.md` | It applies to most changes and should be seen early | Core boundaries, verification expectations, pointers to project docs |
| Nested `AGENTS.md` | It applies only to a directory or subsystem | API compatibility rules, UI accessibility conventions, migration rollout steps |
| Project documentation | It is detailed reference material people need to consult selectively | Architecture map, local setup, deployment runbook, domain model |
| CI or tooling | The rule is deterministic and should block invalid changes | Formatting, type checks, schema validation, dependency policy |
| Task prompt | It is specific to this change and not durable repo knowledge | Acceptance criteria, desired behavior, temporary constraints |

## Write rules that change outcomes

Good instructions describe a durable invariant, explain why it matters when that context is non-obvious, and give a safe path forward. For example:

```md
### Public API compatibility

Keep existing response fields and meanings compatible with supported clients.
If a change must break compatibility, propose a versioned migration path and call
out affected consumers before editing the contract.
```

Prefer rules a reviewer has had to explain more than once. Avoid generic slogans, speculative constraints, and directions already enforced by a clear CI error.

## Scope rules narrowly

Keep cross-project rules in the root file. Put service-specific context in that service's directory-level `AGENTS.md`. A rule should not apply to unrelated files merely because the instructions are easier to write at the root.

For important review guidance, include a safe alternative and a counterexample where useful. This helps distinguish a real violation from a valid change and reduces noisy findings.

## Keep the root file a map

Start with a concise root file. Link to deeper docs rather than copying long setup guides, architectural explanations, or policies into it. The agent should be able to discover the relevant source of truth when a task needs it.

## Avoid instruction drift

- Use commands copied from project documentation or verified configuration; do not guess.
- Include an owner or source of truth for rules that can change.
- Remove instructions when the codebase or process no longer supports them.
- Ask whether a rule should be automated when it is objective and repeatedly checked.

See [maintenance](MAINTENANCE.md) for a lightweight way to keep guidance current.
