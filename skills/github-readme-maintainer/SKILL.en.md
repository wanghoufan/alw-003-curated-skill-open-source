---
name: github-readme-maintainer
description: Use when writing, reviewing, or updating a software project's GitHub README, repository About metadata, product screenshots, or GitHub Release notes. Verify claims against the repository and keep requested languages aligned.
metadata:
  version: "1.0.0"
  language: en
  display_name: "GitHub Project Documentation"
---

# GitHub Project Documentation

Help a first-time repository visitor understand the project, see the real product, follow its setup instructions, and learn what changed in each release.

## When to use

- Create, rewrite, or maintain `README.md` and its requested language versions.
- Update GitHub About fields: Description, Website, and Topics.
- Prepare genuine screenshots for a product with a user interface.
- Publish or maintain GitHub Releases, especially Android APKs and bilingual notes.

## Workflow

1. **Confirm scope and current state.** Read repository files, branch and working-tree changes, recent commits, version configuration, and build/release workflows. Confirm which documents or release items are in scope.
2. **Build a fact base.** Derive the product name, purpose, features, platforms, setup, limitations, and release changes from code, configuration, observed behavior, or verifiable user-provided facts. Mark unknowns instead of guessing.
3. **Plan for readers.** Start the README with what the product is, what problem it solves, and how to get started. Move details into `docs/` only when useful; do not create empty or redundant documents.
4. **Prepare screenshots.** A GUI or web product README must show genuine product screens near the top. For a mobile app, place one real screenshot for each major bottom navigation tab in a horizontal row, preserving aspect ratio; a typical displayed width is about 140–220 px. Do not stretch images across the page. For a website, use the home page and, if needed, one or two key views; usually keep the total to 1–3 images. A data-free demo view is acceptable if it matches the current implementation. If no genuine interface image is available, mark it as a release blocker. Never substitute a logo, concept image, or invented UI. CLI tools, libraries, and APIs without a UI do not need screenshots.
5. **Keep language versions aligned.** If the project uses Chinese and English READMEs, update both. Features, versions, commands, limitations, links, and screenshot order must agree. Write natural English without adding unsupported claims.
6. **Check links and privacy.** Test repository, website, documentation, download, and image links. For GitHub About Website, prefer a GitHub Pages site that is actually published and reachable, then Vercel, then another genuine live site. Configuration alone does not prove a site is live. Remove secrets, tokens, personal data, and unlicensed assets from documents, screenshots, and changes.
7. **Read back and deliver.** Check Markdown rendering, relative links, language consistency, spelling, copyable commands, and change scope. Report what is complete and what remains unverified.

## README rules

- Use the formal project name supported by the repository, followed by a plain-language value statement.
- For a product with a UI, show genuine screenshots soon after the title and summary; do not bury the product under badges, directory trees, or technology lists.
- Include setup, configuration, startup, and minimum usage steps relevant to the project. Commands must come from the real project.
- Explain what users can do before describing implementation details. Put deep technical material in later sections or separate documents.
- Document environment-variable names, purpose, and safe example formats only; never include real values.
- Base GitHub About fields on repository evidence. Do not invent features or live websites.

## Android APK and GitHub Releases

When the task includes a formal Android APK release or keeping an installable copy for migration to another computer:

1. Confirm the repository and app versions, build source, and target architecture. Build or obtain the matching **installable, correctly signed** APK. Never present a debug build as a production release.
2. Attach the latest APK requested by the user to a GitHub Release whether the repository is public or private. Users with repository access can then download it. Visibility affects access, not the need to retain the package.
3. Write release notes in Chinese and English. Summarize user-visible additions, improvements, fixes, and relevant compatibility requirements. Include only changes supported by code, commits, or verification. Omit empty categories.
4. Match the release title and tag to the actual version. Check that the attachment filename and package version agree. Before upload, verify file size, signing, SHA-256, and that the correct APK was selected.
5. After publishing, open the Release page and check its title, bilingual notes, and APK attachment. Confirm the asset is downloadable or inspect its API metadata; optionally download and compare SHA-256.

Suggested bilingual release-note structure:

```markdown
## 简体中文
### 本次更新
- 新增：……
- 优化：……
- 修复：……
### 安装与兼容
- Android：……
- 安装包：`<filename>.apk`（SHA-256：`<hash>`）

## English
### What’s new
- Added: …
- Improved: …
- Fixed: …
### Install and compatibility
- Android: …
- Package: `<filename>.apk` (SHA-256: `<hash>`)
```

Do not invent entries to fill a template. A release note is not a copy of the full technical documentation.

## Git and publishing boundaries

- Review existing working-tree changes first and do not overwrite the user's work.
- Commit, push, create a Release, or deploy only when the user explicitly requests that action.
- When the user has authorized publishing, finish local documentation and artifact checks, then commit and push. Finally open the latest GitHub page in the system default browser and verify the live result.
- Changes to repository visibility, replacing existing release assets, or overwriting an existing Release require explicit authorization.

## Example requests

```text
Update the Chinese and English READMEs from the current code, with genuine product screenshots near the top.
Prepare a GitHub Release for this Android version, attach the signed APK, and write bilingual notes.
Check whether the GitHub About Website should point to GitHub Pages.
```
