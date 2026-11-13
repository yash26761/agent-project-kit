# Agent Project Kit

**A practical, language-agnostic starter for giving AI coding tools clear, reusable project instructions.**

Keep project guidance in one place, connect supported coding agents with small adapters, and give developers repeatable workflows for planning, changing, and reviewing code.

[Get started](#get-started) · [Supported tools](#supported-tools) · [How it works](#how-it-works) · [Guides](#guides)

## Why use this?

AI coding tools often need the same context for every task: how to run the project, what must not change, which checks matter, and how a good contribution should look. When this guidance lives only in chat history or is copied into several tool-specific files, it gets repeated, missed, or out of date.

Agent Project Kit gives a repository one shared `AGENTS.md`, practical task prompts, and small adapters for popular coding tools. The included connector can add missing files without overwriting your existing instructions. The read-only doctor checks whether the shared file and adapters are present and wired together.

It is a starter kit, not an AI model, framework, security boundary, or guarantee that generated code is correct. Your team still reviews changes and runs its own checks.

## Who it is for

- Developers adopting AI coding tools for the first time.
- Teams that want project guidance reviewed and versioned with their code.
- Repositories used with more than one coding agent.
- Maintainers who want reusable prompts and a simple onboarding workflow.

The kit is language- and framework-agnostic. Customize the commands and rules to match your repository.

## What you get

- A root `AGENTS.md` with clear, practical project guidance.
- Small adapters that point supported tools back to the shared instructions.
- A safe connector with preview mode; it keeps existing files instead of replacing them.
- A read-only doctor that checks instruction files and references.
- Task prompts for orientation, planning, implementation, debugging, and review.
- Guides for adoption, AI-assisted workflows, instruction design, and maintenance.
- Contribution, security, support, issue, and pull request guidance for a public repository.

## Get started

### Add the kit to an existing project

1. Download or clone this repository.
2. Preview the files that would be added:

   ```sh
   python scripts/connect.py --target /path/to/your/project --tools all --dry-run
   ```

3. If the preview looks right, add the missing files:

   ```sh
   python scripts/connect.py --target /path/to/your/project --tools all
   ```

4. Check the setup:

   ```sh
   python scripts/doctor.py --target /path/to/your/project
   ```

The scripts require Python 3.9 or newer and use only the Python standard library. The connector does not overwrite existing files. If your project already has an `AGENTS.md` or tool configuration, keep it and merge guidance manually where appropriate.

To add only selected adapters, replace `all` with tool names, for example:

```sh
python scripts/connect.py --target /path/to/your/project --tools codex claude copilot
```

### Use it as a new repository template

On GitHub, select **Use this template** to create a repository from this kit. Then update the new repository's `README.md`, `AGENTS.md`, and `.gitignore` with your project details. If you downloaded the files instead, copy them into a new folder and initialize Git there.

For the detailed walkthrough, see the [five-minute adoption guide](docs/ADOPT.md).

## Supported tools

The kit includes direct `AGENTS.md` guidance and adapters for these tools:

| Tool | Setup included |
| --- | --- |
| OpenAI Codex | Reads root `AGENTS.md` |
| Cursor | Root `AGENTS.md` support |
| Cline | Root `AGENTS.md` support |
| Windsurf | Directory-scoped `AGENTS.md` support |
| Claude Code | `CLAUDE.md` imports `AGENTS.md` |
| Gemini CLI | `GEMINI.md` imports `AGENTS.md` |
| GitHub Copilot | `.github/copilot-instructions.md` adapter |
| Aider | `.aider.conf.yml` loads `AGENTS.md` as read-only context |
| Continue | Project rule points to `AGENTS.md` |

Product behavior and supported instruction surfaces can change. Some tools support instructions differently across their editor, CLI, or agent modes. See [AI tool setup](integrations/README.md) for details and official product references. The doctor checks local files; it cannot confirm that a particular app version loaded them.

Other tools may work if they can read Markdown project instructions. Check their documentation and configure them to use `AGENTS.md` or add a small adapter. This kit does not connect accounts, choose models, provide API keys, or configure provider access.

## How it works

1. **Write shared guidance once.** Put durable repository facts, commands, constraints, and review expectations in `AGENTS.md`.
2. **Point tools to it.** Keep native adapter files small so tool-specific setup does not become a second source of truth.
3. **Give the agent a focused task.** State the goal, relevant context, acceptance criteria, and checks to run.
4. **Review the work.** Inspect the diff and run the repository's normal checks before merging.

The connector only adds missing files. Use `--dry-run` to preview. The doctor is read-only and reports whether files and references are present; it does not launch or authenticate any AI product. For larger instruction conversion or linting needs, compare this lightweight kit with [agnix](https://github.com/agent-sh/agnix) or [rulesync](https://github.com/dyoshikawa/rulesync).

## A good first task

After adding the kit, ask your coding agent:

> Read `AGENTS.md` and inspect this repository. Identify the project-specific details that are missing from the instructions. Suggest exact additions, but do not edit files yet.

This helps you tailor the starter guidance before asking the agent to make code changes.

## Guides

- [Five-minute adoption](docs/ADOPT.md) — add the kit to an existing project.
- [AI-assisted workflow](docs/AI_WORKFLOW.md) — plan, implement, verify, and review changes.
- [Instruction design](docs/INSTRUCTION_DESIGN.md) — keep guidance useful and maintainable.
- [Maintenance](docs/MAINTENANCE.md) — review instructions as a project changes.
- [AI tool setup](integrations/README.md) — understand adapters and product-specific behavior.
- [Prompt library](prompts/README.md) — copyable prompts for common development tasks.
- [Scoped instruction example](examples/scoped-instructions/AGENTS.md) — see folder-level guidance in practice.
- [Contributing](CONTRIBUTING.md) — propose changes to the kit.
- [Publishing checklist](PUBLISHING.md) — prepare a public GitHub repository.

## Verify the kit

Run the built-in checks with Python:

```sh
python -m unittest discover -s tests -v
```

These checks cover the connector's preview and file-preservation behavior, selected tool setup, and the doctor's reports.

## Contributing

Contributions are welcome. Keep additions broadly useful across languages and tools, explain the problem they solve, and avoid unnecessary setup or dependencies. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

This project is released under the [MIT License](LICENSE).
