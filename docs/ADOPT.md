# Add the kit to an existing project in five minutes

You do not need to adopt every file. Start with repository instructions and a prompt you can use today.

## Minute 1: keep a safe copy

Start a branch or make sure your current work is saved. This makes the first edit easy to review and undo.

## Minute 2: merge the root instructions

Open the kit's [`AGENTS.md`](../AGENTS.md) and your project's existing `AGENTS.md`.

- If your project has no `AGENTS.md`, copy the kit's file to the repository root.
- If one already exists, merge only useful guidance. Keep real project commands, architectural constraints, and existing team agreements.
- Do not replace verified project guidance with generic examples.

Add concrete details under a short project section:

```md
## Project-specific notes

- Setup: [real setup command or link to setup guide]
- Checks: [real test, lint, or build commands]
- Architecture: [important boundary or entry point]
```

Replace every bracketed note with facts from your repository, or remove the line. Do not leave guessed commands in place.

## Minute 3: add scoped guidance only where needed

Keep the root file useful across the repository. Add a directory-level `AGENTS.md` only when that area has distinct conventions or constraints. See the [scoped instructions example](../examples/scoped-instructions/AGENTS.md).

## Minute 4: choose a prompt

Pick a prompt from the [prompt library](../prompts/README.md), fill in the goal and acceptance criteria, and start with a small task. The recipes are plain text: copy one into your coding agent and adapt it to your context.

If your team uses several coding agents, follow the [AI tool setup guide](../integrations/README.md) and add only the small adapters those tools need.

## Minute 5: tune from real use

Review the resulting diff and the exact checks that ran. If the same project fact was missing, add that fact to the appropriate `AGENTS.md`. If the prompt was unclear, improve the task description. Avoid adding broad rules to solve a one-time misunderstanding.

## Optional files

- Merge `.gitignore` entries with your current file; do not replace project-specific ignore rules.
- Copy issue and pull request templates if your team uses GitHub.
- Use `CONTRIBUTING.md`, `SUPPORT.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` when they fit your project's community needs.
- Review the license before copying it. Licensing is a project decision.
