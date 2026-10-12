---
name: vercel-deploy-triage
description: Use when a Vercel deployment is blocked or skipped, a deployment reports success but the live site is stale, or Git integration rejects a commit author.
metadata:
  version: "1.0.0"
  language: en
  display_name: "Vercel Deployment Triage"
---

# Vercel Deployment Triage

Find where deployment is stuck, then choose the smallest effective fix. Similar status labels can have different causes; do not repeat deployments blindly.

## When to use

- A deployment shows `BLOCKED`, `UNKNOWN`, `SKIPPED`, or no build was created.
- A command reports success but the live site still shows an older version.
- Git integration says it cannot associate the commit author with a GitHub or Git provider account.

## Diagnostic workflow

1. Collect the project, team, Git repository, branch, commit SHA, deployment ID, status, full error, creation time, and production domain. Prefer read-only checks through Vercel CLI, deployment details/API, and Git state.
2. Identify the trigger: Git integration, CLI, external API, or manual action. Compare the expected production branch and commit SHA with the recorded deployment. Do not mistake a preview deployment for production.
3. Read the full error and linked official guidance. Distinguish author/collaboration permissions, build failures, project linkage, quotas, queues, cache, domains, and platform incidents. Do not infer the cause from `UNKNOWN` alone.
4. If the error says the author cannot be associated, verify that the commit author email belongs to a connected Git account. Check integration permissions, team membership, and project linkage. Do not make the repository public to bypass an access check.
5. If the build succeeded but the site is stale, verify the commit behind the production deployment, domain alias, cache, and project. Before redeploying, confirm that build steps have no harmful side effects if repeated.
6. Propose the smallest reversible fix first. Explain the impact and wait for authorization before changing Git identity, team permissions, billing, project linkage, repository visibility, or production domains.
7. After the fix, verify using a new deployment record and the live site: status is Ready, the production domain points to the intended deployment, and page content or a version marker matches the expected commit. Keep the error and verification evidence.

## Read-only checks

```bash
vercel project ls
vercel ls
vercel inspect <deployment-url>
git status --short
git log -1 --format='%H%n%an <%ae>'
git remote -v
```

CLI options can change by version. Check `vercel --help` or current official CLI documentation before relying on syntax. Never put a token in shell history, command output, or reports.

## Principles

- Keep initial diagnosis read-only; propose a change only after confirming the cause.
- Do not treat making a repository public, upgrading a paid plan, rewriting Git history, or changing team permissions as default fixes.
- Before deploying from a temporary directory without Git metadata, clearing cache, or rerunning builds, confirm that required files will remain and side effects are safe.
- Do not bypass platform restrictions by removing overlays, altering server responses, or faking deployment state.
- When uncertain, preserve the error and evidence, state what still needs checking, and do not claim the issue is fixed.

## Completion criteria

Report the cause (or unconfirmed hypothesis), evidence, changes made, deployment ID/commit, live verification result, and remaining risks. A successful build alone does not prove the production site was updated.
