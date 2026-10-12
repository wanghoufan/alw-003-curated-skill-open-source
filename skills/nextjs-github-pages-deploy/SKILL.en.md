---
name: nextjs-github-pages-deploy
description: Use when deploying a Next.js site to GitHub Pages project sites, migrating a compatible site from Vercel, or maintaining a Vercel and GitHub Pages dual deployment.
metadata:
  version: "1.0.0"
  language: en
  display_name: "Next.js GitHub Pages Deployment"
---

# Next.js GitHub Pages Deployment

Deploy a Next.js site to a GitHub Pages project site, handling project subpaths, static export, and differences between deployment targets.

## Scope

- Deploy a Next.js App Router project to `https://<owner>.github.io/<repo>/`.
- Keep a dynamic Vercel site while publishing a static GitHub Pages edition.
- Diagnose blank Pages sites, routing errors, or missing images and assets.

Plain static HTML does not need this skill. A GitHub user site at `<owner>.github.io` uses the root path and does not need project subpath configuration. Static export cannot support features that require a running server. If the project depends on them, keep a server deployment instead of forcing a migration.

## Workflow

1. Read `package.json`, lockfile, Next.js config, routes, API handlers, image references, Actions workflow, and Git state. Confirm whether the target is a project or user site, the repository name, routes, and current deployments.
2. Identify static-export blockers: request-bound server APIs (`cookies`/`headers`), dynamic APIs, middleware, dynamic route parameters, image optimization, runtime environment variables, server actions, and external data requests.
3. Make the smallest change. For a Vercel + Pages setup, use an explicit build variable to enable `output: "export"`, `basePath`, `trailingSlash`, and any required `images.unoptimized` setting only for the Pages build. Do not change Vercel URLs or behavior accidentally.
4. Share business logic. Put calculations, formatting, and pure rules in modules usable by both browser and server. Clearly disable or replace backend-dependent features in the static edition; never fake a successful result.
5. Fix asset paths. Next.js `<Link>` and `_next` assets use `basePath`; native `<img>`, `<a>`, and site-root paths in data need the project prefix separately. Do not prefix external URLs, `mailto:`, or `data:` URLs.
6. Check dynamic routes can enumerate all paths at build time. Where needed, split a `'use client'` page into a server wrapper and client component so static parameters are exported from a supported location.
7. Configure GitHub Actions to build and publish the export directory. Use `permissions: contents: read` and only the additional permissions required by the official Pages deployment workflow. Verify the Pages source, deployment branch, `_next` assets, `.nojekyll`, cache, and workflow triggers.
8. Validate production build and subpath preview locally: home page, deep routes, refresh, images, fonts, downloads, external links, and browser console. Then verify Actions and the live Pages site. For dual deployment, test Vercel and Pages separately.

## Configuration notes

A project site usually needs `basePath: "/<repo>"`. A dual deployment can distinguish build targets with an explicit environment variable, for example:

```ts
const isPages = process.env.DEPLOY_TARGET === "github-pages";
const basePath = isPages ? process.env.BASE_PATH ?? "" : "";

const nextConfig = {
  ...(isPages ? { output: "export" as const, trailingSlash: true } : {}),
  ...(basePath ? { basePath } : {}),
  images: { unoptimized: isPages },
};
```

Set repository-specific values for the target. Do not copy another project's name. If the installed Next.js version or framework behavior differs from this example, consult the official documentation for that version before changing the configuration.

## Common symptoms

| Symptom | Check first |
|---|---|
| Blank page or refresh returns 404 | Project subpath, exported routes, Pages artifact and basePath |
| Image, font, or download returns 404 | Unprefixed site-root paths; accidental prefixes on external URLs |
| Build succeeds but data is missing | Server APIs, runtime variables, database dependency, and static fallback behavior |
| Vercel URL behavior changed | Whether Pages-only config affected the Vercel build |
| Actions succeeds but the site is stale | Pages source, artifact contents, cache, and deployment target |

## Safety and boundaries

- Inspect working-tree changes first; do not overwrite user files or remove server features or production data without direction.
- Never expose secrets in client code, the repository, or Actions logs. Use platform secrets and distinguish public build variables from server-only secrets.
- Do not change repository visibility, domains, production data, or deployment architecture without explicit authorization.
- Push and deploy only as directed by the user. Verify the actual live page after deployment instead of treating a successful build as proof.
## How to trigger it

```text
Deploy this Next.js project to GitHub Pages.
Keep Vercel and add a GitHub Pages deployment.
The Pages site is blank; check basePath and static asset paths.
```
