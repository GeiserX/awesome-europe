# Maintenance guide

> **This file is maintained exclusively by @GeiserX.** PRs modifying it will not be accepted.

Guidelines for maintainers of this list. This guide is shared across the awesome lists ecosystem (awesome-spain + regional lists + awesome-europe). Following it ensures all repositories maintain the same quality, format, and inclusion criteria, so the collection works as a coherent whole.

## Inclusion philosophy

The fundamental criterion is: **we accept software that specifically supports Europe, not software simply made by someone from Europe.**

A repository is included because it interacts with institutions, services, infrastructure, regulations, or data specific to Europe. It is not enough for the author to be European or reside here. A generic JS framework created by a European developer does not belong in this list. A client for an EU institution API or an integration with European public services does.

- **Yes:** Client for EU open data portals, GDPR compliance tools, integration with European public transport APIs, EU VAT validation.
- **No:** Generic libraries created by European teams, generic software whose author simply lives in Europe.

See `AGENTS.md` (if present) for detailed criteria, edge cases, and prohibited topics.

## Reviewing PRs

1. Check the **minimum to get in**: 5 stars and 3 months of history, and not a dump. If it falls short, close it without further review (see `CLAUDE.md`). Software from official bodies is exempt.
2. Verify the project **specifically supports Europe** (not simply that the author is European).
3. Check the PR includes the **URL of the European service or institution** the project supports.
4. Check format: simple entry, alphabetical order, description starting with uppercase and ending with a period.
5. **CI must be green** before merging: awesome-lint-extra (format and order) + `links-changed` (lychee over the links the PR adds or changes).
6. Badges are auto-generated. Contributors only submit:
   ```markdown
   - [Name](https://github.com/owner/repo) - Brief description starting with uppercase and ending with period.
   ```
7. After merging, run the badge pipeline (if available) and push:
   ```bash
   bash scripts/gather-metadata.sh
   python3 scripts/transform-readme.py
   ```

## Adding entries as maintainer

1. Add the simple entry in the correct section, in alphabetical order.
2. Run the badge pipeline (if the repo has the scripts):
   ```bash
   bash scripts/gather-metadata.sh
   python3 scripts/transform-readme.py
   ```
3. Commit and push. Verify CI is green.
4. If the project owner hasn't been notified, open a courtesy issue on their repo:
   - Title: `Listed in awesome-europe`
   - Body: brief message explaining the inclusion and offering to remove if preferred.
   - **One issue per owner** — never open multiple issues for repos from the same user/org.

## Removing entries and DELETED.md

Each repository has (or should have) a `DELETED.md` file. It is a fundamental part of maintenance: it records all projects that were once listed and later removed, along with the reason. Its purpose is:

- **Prevent re-additions:** if someone proposes a previously removed project, the reason for removal can be checked.
- **Preserve history:** it documents past decisions for future maintainers.
- **Record reasoning:** each entry carries enough context to understand the removal.

Entries are never simply deleted from the README. They are moved to `DELETED.md` in the corresponding section:

| Reason | Section in DELETED.md |
|--------|-----------------------|
| Repo archived/read-only | Archived |
| Repo deleted (a renamed repo stays: update its link) | Missing or renamed repos |
| Author confirmed abandonment and it no longer works | Abandoned |
| Does not meet inclusion criteria | Removed for not being Europe-specific |
| Superseded by another project | Replaced (link successor) |
| Broken, old and unverifiable without a reputation, or serving a retired system | Removed in review (say why and how it was checked) |

If the repo doesn't have a `DELETED.md` yet, create it with the sections above the first time a project is removed.

## Periodic maintenance

- **Weekly:** a check shared by every list goes through all the README links each Monday from Spain (many official sites do not answer GitHub's runners) and keeps one open "Dead links" issue with the ones that still fail on a second pass five minutes later. Fix those links. A dead link alone does not show that the project is broken. If a link cannot be fixed, review its entry against "Staying in" in `CLAUDE.md`. If it must go, it joins a removal proposal, which Sergio approves before it moves to `DELETED.md`. The issue closes itself on the next clean run.
- **Quarterly:** Review the entries with more than 3 years without commits on the default branch against "Staying in" in `CLAUDE.md`: archived, broken or retired-system entries go, and so do entries superseded by a maintained entry; the rest stay if they have a reputation, or if they have none but are shown to work (by running them, by checking them against the service they consume, or by checking their data against the official source). Get the proposed removals approved before touching `DELETED.md`. Refresh badges (`gather-metadata.sh` + `transform-readme.py`). Check for recently archived repos:
  ```bash
  grep -oE 'https://github\.com/[^/)]+/[^/)]+' README.md | sort -u | while read url; do
    repo="${url#https://github.com/}"
    archived=$(gh api "repos/$repo" --jq '.archived') || { echo "ERROR: could not query $repo" >&2; continue; }
    [ "$archived" = "true" ] && echo "ARCHIVED: $repo"
  done
  ```
  Add the archived repos to the same proposal; they move to `DELETED.md` once it is approved. A newer entry found broken, serving a retired system or superseded by a maintained entry joins a proposal as soon as it is found: the 3-year filter only sets when age gets reviewed.

## Tools

- **awesome-lint-extra** — Custom linter. Validates format, alphabetical order, badges, and descriptions. Runs as GitHub Action (`GeiserX/awesome-lint-extra@main`) and standalone (`python3 lint.py`). Configuration in `.awesomerc.json`.
- **transform-readme.py** — Generates shields.io badges and institution/service tags from `scripts/metadata.json`.
- **gather-metadata.sh** — Fetches metadata (stars, language, license, branch) from the GitHub API for each listed repo.
- **lychee** — Link checker. `links-changed.yml` checks only the README lines a PR adds or changes, through the `links-changed` action in awesome-lint-extra, and it does block the merge: 403 and 429 pass (bot blocks), any other error or timeout fails if it repeats on a second pass a minute later. The weekly check of the whole README runs outside this repo, never fails on a dead link, and opens or updates the "Dead links" issue. Hosts that always block the checker go in `.lycheeignore`.

## Format rules

- Description must **not start with the project name**.
- One line per entry, no line breaks.
- Descriptions in **English**.
- **Alphabetical order** within each section/subsection (case-insensitive).
- New categories: preferably with at least 3 projects.

## Prohibited content

Projects related to: pornography, NSFW, gambling, lotteries, religion, partisan politics.

## Outreach

- Open notification issues on listed projects' repos (one per owner).
- Post in relevant European developer communities after reaching critical mass.
