# Publishing to GitHub

This folder is a local Git repository. The checklist below prepares its public GitHub home; it does not publish anything automatically.

## Suggested repository details

- **Name:** `agent-project-kit`
- **Description:** A practical, language-agnostic instruction kit for AI coding agents.
- **Topics:** `agents-md`, `ai-coding`, `developer-tools`, `coding-agents`, `repository-template`, `codex`, `claude-code`, `gemini-cli`, `github-copilot`
- **Website:** leave blank unless you have a project page.

Check that the name is available and adjust the description or topics to match the final content.

## Publish the local repository

1. Create a new empty public repository on GitHub. Do not add a README, license, or `.gitignore` there; those files are already in this repository.
2. From this folder, create the initial commit, rename the branch to `main`, add the GitHub repository as `origin`, then push:

   ```sh
   git add .
   git commit -m "Initial release of Agent Project Kit"
   git branch -M main
   git remote add origin https://github.com/OWNER/agent-project-kit.git
   git push -u origin main
   ```

   Replace `OWNER` with your GitHub username or organization. If an `origin` remote already exists, update it to the new repository instead of adding it again.

3. In repository **Settings → General**, enable **Template repository** if you want users to create projects from this kit.
4. In **Settings → Security**, enable private vulnerability reporting if you want to receive reports through GitHub. The guidance in `SECURITY.md` points users there.
5. Add a short release note or announcement only after confirming the repository contents and license are what you intend to publish.

## Before the first push

- Review the commit contents and confirm no secrets or personal data are present.
- Confirm the MIT license and copyright attribution fit your intentions.
- Check the repository name is available and the branch is `main`.
- Preview the README on GitHub after pushing; the repository's homepage is its main onboarding page.
