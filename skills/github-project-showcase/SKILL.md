---
name: github-project-showcase
description: Use when a developer wants to prepare or update the public presentation of one completed software project across its GitHub repository, profile README, or portfolio site. Verify project facts, links, screenshots, privacy, and consistency before changing only the targets the user names.
compatibility: Requires Git and GitHub CLI (gh) for repository checks; optional portfolio-site tooling depends on the target project.
---

# GitHub Project Showcase

Keep the presentation of one named project accurate across the locations the user requests. Work from the project's current files and live GitHub state. Do not invent features, links, deployment status, screenshots, or release assets.

## When to use

- The user asks to prepare a project for public presentation.
- A project has changed and its repository README, profile listing, or portfolio entry needs to be synchronized.
- A project link, screenshot, summary, or release link needs verification.

Do not use this skill for a full account-wide portfolio audit, project management, or writing only one README. Keep the task limited to the one project named by the user.

## Rules

1. **Verify before presenting.** Check the repository, fork status, default branch, latest changes, releases, and online destination as relevant. A local deployment configuration is not proof that a site is live.
2. **Use source-backed wording.** Every feature, number, and product claim must be supported by the current README, source, docs, release notes, or information the user supplied. If unsupported, omit it or label it unverified.
3. **Treat destinations as opt-in.** Update only the GitHub repository, profile README, and/or portfolio site named in the task. Do not infer the profile repository or portfolio source; ask for its location if needed.
4. **Protect private work.** Never add a private repository or private project details to public-facing material. Do not change repository visibility.
5. **Respect ownership and licenses.** Do not present a fork, upstream project, or third-party template as the user's original work. Check permissions for images, fonts, audio, and other assets.
6. **Protect privacy.** Inspect screenshots and copied text for names, faces, contact details, locations, account identifiers, device IDs, customer data, financial or health data, credentials, and local paths. Replace or omit affected material.
7. **Avoid duplicate entries.** Search the selected destination for the repository name or project slug before adding anything. Update an existing entry in place.
8. **Keep changes narrow.** Do not edit unrelated repositories, account-wide lists, or unrelated portfolio entries. Do not delete useful material just to simplify the page.
9. **Confirm before remote writes.** A remote edit, commit, push, release, or deployment must be within the user's explicit request. Never force-push or stage all files blindly.

## Workflow

### 1. Identify and inspect the project

Confirm the exact local directory or `OWNER/REPOSITORY`. Inspect its README, package/build configuration, screenshots, release notes, license, and current Git status. Check the remote, current branch, and recent commits. Do not expose secrets found during inspection.

Build a short fact sheet: project name, purpose, audience, verified capabilities, current online links, release/download links, screenshots available, and known limitations. Separate verified facts from unknowns.

### 2. Check each requested destination

Only inspect destinations the user requested:

- **Project repository:** current README and About fields; relevant release and deployment links.
- **GitHub profile README:** identify the account from the user's instruction or authenticated context, then read the current file and look for this repository before editing.
- **Portfolio site:** locate the content source from the user or the named site's repository instructions. Do not edit generated output if a source file exists.

Before writing, summarize the exact files or fields that will change. For a remote destination, state the current and proposed values. Keep categories and ordering consistent with neighboring entries; ask the user when the category is not clear.

### 3. Prepare accurate presentation material

- Use a concise, source-backed summary focused on the value to a visitor.
- Prefer a working GitHub Pages URL when verified; otherwise use a verified Vercel URL, then another verified project site. Do not include a dead or unconfirmed link.
- Use a specific release tag URL if `/releases/latest` is unavailable or points to a prerelease.
- For GUI and web products, use authentic screenshots of the current product. Follow `cover-rules.md`; if no safe, genuine screenshot is available, leave the image out and report the gap.
- Keep the repository README, profile entry, and portfolio entry consistent without duplicating implementation details.

### 4. Edit only selected destinations

Update only the requested destination files or fields. Preserve useful existing content and surrounding style. For a GitHub profile README, use the GitHub Contents API with the current file SHA to avoid overwriting concurrent edits, then read the file back. For a portfolio site, edit its source data, update related tests if that project requires them, and use its documented build/deploy process only when requested.

Before commit, inspect the exact staged diff and ensure it contains no unrelated changes, credentials, private paths, or personal data. Commit and push only when the user explicitly requested those actions.

### 5. Verify and report

Read back every changed remote field or file. Check each updated URL and relevant image. If deployed, verify the deployed page after the deployment finishes; bypass cache when necessary. Report what changed, verification evidence, and anything still unverified. Do not claim a deployment or public release succeeded unless it was directly confirmed.

## Output

Provide a short report with:

- Project and destinations checked.
- Files or fields changed.
- Link, image, and deployment checks performed.
- Commit/push/deployment status, only when applicable.
- Remaining gaps or decisions.
