# Curated Skills

[简体中文](README.md)

Practical AI skills refined through real projects, documented so others can understand and adapt them.

> **Status: private preview.** The first candidate skill is being prepared. Public scope, redistribution terms, and cross-agent installation instructions will be reviewed before any public release.

## What belongs here

This repository is for skills that solve recurring problems and can help developers beyond their original author. Each entry should explain its purpose, required tools, usage, and known limitations. Personal account details, machine-specific paths, internal administration procedures, and private project data do not belong in a public edition.

## First candidate: GitHub project showcase sync

**`github-project-showcase`** helps maintainers keep a completed project's presentation consistent across its GitHub repository, GitHub profile, and portfolio site.

It first verifies repository and link status, checks screenshots for privacy issues and claims against their sources, updates only the presentation targets specified by the user, and then verifies pages, images, and deployment results. A profile README and portfolio site are optional targets; the skill does not assume a particular account, website, or management tool.

Useful for developers, independent makers, and anyone maintaining presentation pages for multiple projects.

### Files

- [Skill instructions](skills/github-project-showcase/SKILL.md)
- [Synchronization workflow](skills/github-project-showcase/sync-flows.md)
- [Screenshot and privacy rules](skills/github-project-showcase/cover-rules.md)
- [Link audit reference](skills/github-project-showcase/link-audit.md)
- [Delivery checklist](skills/github-project-showcase/checklist.md)

### Requirements

- Install and authenticate GitHub CLI `gh` when the task requires it.
- To update a profile README or portfolio site, provide the relevant repository or content source. The skill will not guess its location.
- Confirm that the task includes any remote write, commit, or push before performing it.
- Check the target repository's license, screenshot permissions, and publication scope.

### Installation

This repository is currently a private preview, so public installation instructions are not available yet. Before a public release, tested instructions and a minimal example will be added for clients such as Codex, Claude Code, and OpenCode.

## Selection criteria

A selected skill must be grounded in real use, have clear triggers, actionable steps, and explicit safety boundaries. It should work across projects without depending on the author's private folders or accounts. Third-party content requires license and attribution checks before redistribution.

## License

No license has been selected. This repository is a private preview. Do not copy or redistribute its skills until licensing and redistribution terms are stated.
