# Curated Skills

[简体中文](README.md) · English

#### Practical AI workflows, refined through real projects and documented for others to use.

This is more than a folder of prompts. Every selected skill should solve a clear problem, come from real project use, provide actionable steps, and state its safety boundaries. The repository is private while its contents are being reviewed. Licensing and public release scope have not been decided.

Skills use the `SKILL.md` format and can be read by tools that support Agent Skills. Installation depends on the agent and whether it has access to this private repository.

---

## 📋 Contents

| Name | In one sentence | Guide |
|---|---|---|
| [github-project-showcase](skills/github-project-showcase/SKILL.md) (GitHub Project Showcase Sync) | Keep a project's GitHub repository, profile entry, and portfolio listing accurate, verified, and privacy-safe. | [Instructions](skills/github-project-showcase/SKILL.md) |

---

## 📦 Install and use

This repository is currently **Private**. An agent can read a skill here only if its user has repository access and the agent can reach GitHub.

In an agent that can read GitHub-hosted skills, you can ask:

```text
Please read and install this skill:
https://github.com/wanghoufan/alw-003-curated-skill-open-source/tree/main/skills/github-project-showcase
```

Alternatively, clone the repository and install the entire `skills/github-project-showcase/` directory using your agent's instructions. Keep its reference files alongside `SKILL.md`.

If the agent cannot access the private repository, configure read access first. Do not paste the whole repository or an access token into a conversation. Client-specific commands will be added after they are tested against the public release.

---

## ✨ Skills

### 🧭 github-project-showcase

> When a project is ready, its repository, profile, and portfolio descriptions should be in sync too.

This skill helps prepare **one named project** for presentation. It checks the real project and current GitHub state, verifies that claims have evidence, tests links, and reviews screenshots for privacy. It then changes only the destinations requested by the user and reads back or opens the result for verification.

#### What it can do

- Improve a project repository's README, About description, and relevant links.
- Add or update a project entry in a GitHub profile README.
- Update a project description, links, or screenshots on a portfolio site.
- Verify GitHub Pages, Vercel, release, and image links.
- Review screenshots and copy for personal data, device identifiers, credentials, and third-party asset rights.

A profile README and portfolio site are **optional**. The skill changes only destinations named by the user; it does not guess account details, website repositories, or content file locations. It does not audit an entire account or manage projects.

#### When to use it

```text
This project is wrapping up. Sync its repository description and portfolio entry.
Check whether this GitHub repository's README, links, and screenshots are ready to show.
Add this project to my GitHub profile README, checking for duplicates first.
```

#### Requirements and boundaries

- Use an authenticated GitHub CLI `gh` when GitHub checks are needed. The user must provide or identify the profile or portfolio destination.
- Never list a private project on a public page or present a fork, template, or third-party project as original work.
- Perform remote edits, commits, pushes, releases, or deployments only when explicitly requested.
- If no genuine and safe product screenshot is available, omit it; do not substitute a logo, concept image, or decoration.

#### Files

- [SKILL.md](skills/github-project-showcase/SKILL.md): workflow and behavior boundaries
- [sync-flows.md](skills/github-project-showcase/sync-flows.md): destination-specific steps
- [cover-rules.md](skills/github-project-showcase/cover-rules.md): screenshot selection and privacy review
- [link-audit.md](skills/github-project-showcase/link-audit.md): repository, website, and release link checks
- [checklist.md](skills/github-project-showcase/checklist.md): delivery checklist

---

## 🌱 Selection principles

We prioritize skills that solve recurring problems, have been used in real projects, and do not depend on their author's private environment. Each entry should state its purpose, prerequisites, limitations, and source. Third-party content requires license and attribution checks. Personal account details, local paths, internal administration procedures, and private project data do not belong in a public edition.

## About and license

This is a personally maintained collection in private review. No license has been selected. Do not copy or redistribute its skills until licensing and redistribution terms are stated.
