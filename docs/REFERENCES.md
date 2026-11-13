# References

The kit favors concise, scoped, repository-local guidance. These official OpenAI references informed that approach:

- [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/) — keep `AGENTS.md` as a map to deeper repository knowledge; avoid monolithic instruction files; make important invariants legible and enforce mechanical rules with tools.
- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) — keep instruction descriptions focused and use progressive disclosure so unrelated guidance does not consume context.
- [Custom Code Review rules for Codex](https://developers.openai.com/blog/custom-code-review-rules-for-codex) — scope review rules to the relevant code, encode consequential non-obvious invariants, state a safe path, and keep mechanical checks in CI.

Codex behavior and best practices evolve. Recheck official documentation when updating product-specific guidance; do not treat this kit as a complete or permanent Codex specification.

For multi-agent file discovery and adapters, see the product documentation collected in [`integrations/README.md`](../integrations/README.md). These integrations concern repository instructions only; provider credentials and model selection stay in each product.
