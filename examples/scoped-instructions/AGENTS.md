# Example: scoped instructions for a UI area

This is a teaching example, not a rule for this kit. Copy and adapt it only when your project has a UI directory with distinct conventions.

## UI constraints

- Preserve keyboard operation and visible focus for interactive controls.
- Reuse the project's shared components and design tokens; do not introduce a parallel component system for a one-off screen.
- Keep loading, empty, error, and success states consistent with nearby views.

## Before changing a shared interaction

- Inspect neighboring components and the shared component API.
- Check whether the behavior is covered by an existing interaction or accessibility test.
- If a change affects a shared component, identify the other consumers that may change.

## Review guidance

- Flag removal of keyboard access, focus visibility, or accessible names unless an equivalent is preserved.
- Do not flag visual changes that preserve the interaction contract. Explain the user impact and a safe fix when reporting a finding.

Replace these example rules with verified project conventions. Keep rules that matter to reviews; put design-system details in the UI documentation and deterministic checks in CI.
