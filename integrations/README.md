# Connect your coding agent

This repository shares **project instructions** with coding agents. It does not connect an account, choose a model, set up billing, provide API keys, or configure access to external services. Use each product's own model and account settings for those.

## Usually: open the repository

The kit includes `AGENTS.md` as the canonical, vendor-neutral instruction file. These agents can read it directly or through a small adapter:

| Tool | How this repo connects the instructions | What to do |
| --- | --- | --- |
| OpenAI Codex | Reads root `AGENTS.md` | Open the repository in Codex |
| Cursor | Supports root `AGENTS.md` | Open the repository in Cursor |
| Cline | Detects root `AGENTS.md` | Open the repository in Cline |
| Windsurf | Supports directory-scoped `AGENTS.md` | Open the repository in Windsurf |
| GitHub Copilot | Reads `AGENTS.md` in supported agent surfaces; Copilot CLI can import it from repo instructions | Open the repository with Copilot. Surface support varies; check the adapter `.github/copilot-instructions.md` is loaded in your client |
| Claude Code | `CLAUDE.md` imports `AGENTS.md` | Open the repository with Claude Code |
| Gemini CLI | `GEMINI.md` imports `AGENTS.md` | Open the repository with Gemini CLI |
| Aider | `.aider.conf.yml` loads `AGENTS.md` as read-only context | Run Aider from the repository root |
| Continue | Project rule asks the agent to read canonical `AGENTS.md` | Open the repository with Continue; see `.continue/rules/00-project.md` |

The native adapters are deliberately tiny. Keep shared project guidance in `AGENTS.md` and put only tool-specific behavior in the adapter. This prevents conflicting copies from drifting apart.

## Add the kit to an existing repository

From a clone of this kit, run:

```sh
python scripts/connect.py --target /path/to/your/project --tools all
```

Use specific tool names instead of `all` to add fewer adapters, for example `--tools codex claude copilot`. Run with `--dry-run` first to preview. The script only adds missing files; it never overwrites existing guidance or tool configuration. Review and merge skipped files yourself.

Then verify the files:

```sh
python /path/to/agent-project-kit/scripts/doctor.py --target /path/to/your/project
```

Open the target repository in each tool and ask it to summarize the project instructions it loaded. The checker verifies files and import pointers; it cannot prove that a specific app version loaded them. Keep model/provider setup in the tool's own settings. Never commit API keys or tokens.

## Other tools and model providers

Many coding agents accept Markdown project instructions, even when they use a different filename. If a tool does not discover `AGENTS.md` or one of the included adapters, add its supported project-rules file with a short instruction to read the root `AGENTS.md`, or paste the relevant project guidance into its project settings. Check that product's current documentation because file names and import behavior can change.

This is a compatibility layer, not a promise that every AI tool loads every repository file. Instruction files guide a model; they do not enforce permissions or replace tests, code review, or CI.

### Using a web chat or an unlisted tool

If the AI cannot open your local repository, attach `AGENTS.md` and the relevant project docs to the conversation, then use a recipe from `prompts/`. If a coding tool is not listed, configure its project-instructions setting to read `AGENTS.md` or add a short native adapter that points to it. Reuse the same source; do not maintain a second full rulebook.

The kit does not provide model access. Choose a provider and configure credentials in the product you use. A tool can only use models and services that its own integration supports.

## Official setup references

- [Claude Code memory and imports](https://docs.anthropic.com/en/docs/claude-code/memory)
- [GitHub Copilot custom instructions](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions)
- [Cursor rules](https://docs.cursor.com/context/rules-for-ai)
- [Gemini CLI context files](https://geminicli.com/docs/cli/gemini-md/)
- [Cline rules](https://docs.cline.bot/customization/cline-rules)
- [Windsurf `AGENTS.md` support](https://docs.windsurf.com/windsurf/cascade/agents-md)
- [Continue project rules](https://docs.continue.dev/customize/rules)
- [Aider conventions](https://aider.chat/docs/usage/conventions.html) and [Aider config](https://aider.chat/docs/config/aider_conf.html)
