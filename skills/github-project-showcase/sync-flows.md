# Destination workflows

Use only the sections for destinations the user requested. Confirm exact repository names before running commands.

## Project repository

Read the current README and GitHub About values. Verify links in the README against the repository and live site. If Android release assets are in scope, use the project's release policy and verify package identity, version, signature, and release notes; otherwise do not create a release.

## GitHub profile README

A profile README is stored in a repository whose name matches its owner's GitHub login. Confirm the owner and repository before editing; do not guess based on a local account name.

1. Read `README.md` and record its current SHA.
2. Search for the target repository name. If present, update only the existing line; otherwise add one line in a user-approved category.
3. Update any displayed project count only when the file has such a count and the new count can be verified.
4. Write through the GitHub Contents API using the SHA read in step 1, then read back and compare the changed text.

## Portfolio site

Locate the site's source data from the user or repository documentation. Prefer editing source data over generated pages. Match existing field names and style. Verify the project slug, title, summary, status, repository URL, live URL, release URL, and screenshot path against current facts. Keep existing ordering unless the site defines a clear ordering rule. Run the site's documented checks after edits.

## Commit and deployment

Check `git status`, current branch, remote, and diff before staging. Stage only the files changed for this task. Never use force push. Commit/push/deploy only when the user explicitly asked for it; then verify remote HEAD and deployment status. A successful push alone does not prove that a hosted site has finished deploying.
