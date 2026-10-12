# Link audit

Check links before placing them in a public-facing README or portfolio.

## Repository facts

Use authenticated GitHub metadata for a named repository:

```bash
gh api repos/OWNER/REPOSITORY --jq '[.full_name,.visibility,.fork,.default_branch,.pushed_at,.homepage]|@tsv'
```

Confirm that the repository name is current, whether it is a fork, and whether it is public. A private repository must not be linked from a public listing.

## Releases and websites

- Check that a release tag exists and includes the expected assets before linking to it.
- `/releases/latest` may not resolve to a prerelease; use the specific tag page when needed.
- Open the live project site and confirm it belongs to this project. Deployment configuration alone is not evidence of a live site.
- A network timeout or proxy error is not the same as HTTP 404. Retry through another permitted method before declaring a link dead.
- Prefer repository-hosted images over third-party image hosts when feasible.

## Report evidence

For each link, report the exact URL and what was verified: HTTP status, page title, release tag, or asset name. Mark any checks that could not be completed.
