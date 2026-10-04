# CLAUDE.md — awesome-europe

## Purpose

A curated list of open source software that provides **support specifically for Europe** — its institutions, regulations, standards, and cross-border infrastructure. All content in English. The focus is pan-European: software must target a significant portion of European countries, not just one or two.

## Scope

- **EU-27 member states** and **EEA countries** (Norway, Iceland, Liechtenstein) are in scope.
- **Switzerland and UK** — include only if the software explicitly targets them alongside EU/EEA countries for EU regulation compliance.
- **EU candidate countries** (Ukraine, Serbia, Montenegro, etc.) are **not** in scope.

## Inclusion criteria

### Include

- Software that interacts with **EU/EEA institutions** (European Commission, ECB, Eurostat, EBA, ESMA, ENISA, ERA, EFSA, EEA, Europol, Eurojust, ESA, Eurocontrol, EUIPO, EPO, EMA, etc.).
- Implementations of **EU regulations and directives**:
  - Data protection: GDPR, ePrivacy
  - Digital identity: eIDAS, EU Digital Identity Wallet
  - Digital regulation: DSA, DMA, EU Data Act, Data Governance Act, EU AI Act
  - Financial: PSD2, MiFID II, MiCA, DORA, EMIR, AMLD, SEPA
  - Cybersecurity: NIS2, Cyber Resilience Act, EU Cybersecurity Act
  - Sustainability: EU Taxonomy, CSRD, SFDR, CBAM, EU Deforestation Regulation
  - Product safety: CE marking, MDR, IVDR, REACH, CLP, RoHS, WEEE
  - Accessibility: European Accessibility Act, EN 301 549
  - Transport: ETCS, eCall, EETS, U-space
  - Energy: EU ETS, REMIT
  - Procurement: eForms, ESPD, TED
  - Labor: Posted Workers Directive, Pay Transparency Directive
  - Migration: Schengen, ETIAS, EU Blue Card
- Tools for **EU-wide standards** (SEPA, Peppol, EN 16931, INSPIRE, CE marking, EBICS, etc.).
- Software for **pan-European data systems** (Eurostat, EU Open Data Portal, Copernicus, Galileo, ENTSO-E Transparency Platform, EUR-Lex, ECLI, EudraVigilance, RASFF, TED, VIES, TARIC, etc.).
- Cross-border **digital infrastructure** (CEF building blocks, X-Road, EBSI, eDelivery, eSignature, eTranslation, FIWARE, Once Only Technical System, etc.).
- **EU VAT, customs, and trade** tools (VIES, OSS/IOSS, TARIC, CN codes, EORI, Intrastat, EU customs systems).
- **Pan-European energy** systems (ENTSO-E, ACER, EU ETS, REMIT).
- **European financial infrastructure** (ECB APIs, TARGET2, T2S, TIPS, Euribor, ESTR, XBRL EU reporting, LEI).
- **EU procurement** (TED, eForms, ESPD, CPV codes, eSender).
- **EU democracy and governance** (European Parliament data, EU Transparency Register, European Citizens' Initiative, legislative tracking).
- **EU intellectual property** (EUIPO, EPO, Unitary Patent, EU trademark tools).
- **EU space and aviation** (ESA, Eurocontrol, SESAR, Galileo, EGNOS).
- **EU health and pharma** (EMA, EHDS, EudraVigilance, IDMP, EHIC, EU MDR/IVDR, EUDAMED).
- **EU sustainability and ESG** (EU Taxonomy, CSRD, SFDR, CBAM, Digital Product Passport, EU Green Bond Standard).
- **EU AML and compliance** (AMLD, EU sanctions screening, beneficial ownership, KYC/KYB EU, LEI, Travel Rule).
- **EU migration** (Schengen visa tools, ETIAS, EU Blue Card, residence permits).
- **EU labor and employment** (EURES, Europass, posted workers, pay transparency, European Qualifications Framework).
- **EU education and research** (ECTS, Erasmus+, Horizon Europe, CORDIS, OpenAIRE, EOSC, CERN tools).
- **Pan-European utility libraries** (IBAN validation, NUTS regions, European phone/address formats, EU postal codes, European holidays, euro currency tools).
- Software that explicitly targets **multiple European countries** as its primary scope.

### Do not include

- Software specific to a **single country** — that belongs in country-specific awesome lists (awesome-spain, awesome-germany, etc.).
- Software that targets only **2-3 countries** or a small regional cluster, unless implementing an EU-wide standard.
- **Global software** that happens to work in Europe among many other regions (e.g., generic payment processors, global tax tools, worldwide IBAN validators that aren't EU-focused).
- Software by European developers that has **no Europe-specific functionality** (generic JS frameworks, visualization libraries, etc.).
- **NATO or military** software.
- Software only tangentially related to Europe (e.g., a global mapping tool that includes European map tiles).
- **Archived or read-only** repositories — these go to `DELETED.md`.
- Repos where the **author explicitly states the project is broken, unmaintained, or deprecated** — treat as abandoned.
- Repos with **no meaningful README** or that are clearly test/experiment repos.
- **Open-core funnels**: repos whose open-source part exists as the free tier or marketing surface of a paid product or hosted service selling the same capability. Signals: a pricing page for a hosted version of what the repo does, development happening in a private repo with the public one as a synced snapshot, launch-day self-submission across multiple lists. The license being permissive and the code being substantial does not cure this — the list recommends community open source, not commercial funnels. Company-backed libraries remain fine when the vendor's business is elsewhere and the library is a complete give-away (e.g. pretix's drafthorse): the test is whether the vendor sells a paid version of the very thing the repo does. Precedent: Attestwire EN 16931, delisted Aug 2026 (see `DELETED.md`).

### Grey area — use judgement

- Projects that started as EU-specific but went global — include if European functionality remains a distinct, prominent feature.
- Software that covers EU + a few non-EU countries — include if the EU/EEA is the primary target.
- **Global tools with EU coverage**: if a tool supports multiple EU data sources/institutions BUT also has significant non-EU coverage (e.g., half its providers are non-European), it's a global tool — reject. The test: if the tool were stripped of all non-EU functionality, would it still be a coherent, substantial project? If yes and the EU part is dominant, include. If the EU providers are just a subset of a worldwide collection, reject.

## Quality standards

**Same quality bar as [awesome-spain](https://github.com/GeiserX/awesome-spain):**

- **No archived repos**: if discovered archived after inclusion, move to `DELETED.md` immediately.
- **No extremely unmaintained repos**: at least one commit in the last 3 years, unless it's a clearly stable/complete project (e.g., a spec validator that hasn't changed because the spec hasn't changed).
- **No broken repos**: if the repo README says "deprecated", "no longer maintained", "use X instead", or similar — do not include. Move to `DELETED.md` if already listed.
- **Minimum stars**: prefer repos with at least a few stars, but exceptional niche tools with 0-1 stars may be included if they fill an important gap.
- **Verify every repo** before adding: check `archived`, `pushed_at`, `stargazers_count` via `gh api repos/owner/name`.

## Entry format

```markdown
- [Name](https://github.com/owner/repo) ![Stars](https://img.shields.io/github/stars/owner/repo?style=flat-square&label=⭐) ![Last Commit](https://img.shields.io/github/last-commit/owner/repo?style=flat-square) ![Language](https://img.shields.io/github/languages/top/owner/repo?style=flat-square) ![License](https://img.shields.io/github/license/owner/repo?style=flat-square) ![GDPR](https://img.shields.io/badge/GDPR-003399?style=flat-square) ([Demo](https://example.com)) - Description starting with a capital letter and ending with a period.
```

Each entry includes (in this order):
- **Star badge** (required): `![Stars](https://img.shields.io/github/stars/owner/repo?style=flat-square&label=⭐)` — auto-updating.
- **Last Commit badge** (required): `![Last Commit](https://img.shields.io/github/last-commit/owner/repo?style=flat-square)` — auto-updating.
- **Language badge** (required): `![Language](https://img.shields.io/github/languages/top/owner/repo?style=flat-square)` — auto-updating.
- **License badge** (required): `![License](https://img.shields.io/github/license/owner/repo?style=flat-square)` — auto-updating.
- **EU regulation badges** (required): blue badges (`#003399`) manually assigned. E.g. `![GDPR](https://img.shields.io/badge/GDPR-003399?style=flat-square)`. Common: `GDPR`, `eIDAS`, `EN16931`, `PSD2`, `VAT`, `AMLD`, `NIS2`, `DORA`, `CRA`, `AI Act`, `DSA`, `DMA`, `INSPIRE`, `Copernicus`, `FIWARE`, `CERN`, `Peppol`, `SEPA`, `CSIRT`, `EAA`, `ITS`, `Data Spaces`, `Open Data`, `eProcurement`, `CAP`, `EHDS`.
- **Demo link** (optional): `([Demo](url))` — only live interactive instances, not marketing pages or docs.
- **Description** (required): one sentence at the end, starts with capital letter, ends with period. Must not start with the project name.

- Maximum one line per entry.
- Entries in **alphabetical order** (by display name, case-insensitive) within each section and subsection.
- Validate with [awesome-lint-extra](https://github.com/GeiserX/awesome-lint-extra): `python3 /path/to/lint.py` or via CI.
- The `scripts/transform-readme.py` script can auto-enrich entries using GitHub API metadata stored in `scripts/metadata.json`. Run `scripts/gather-metadata.sh` first to refresh metadata.

## Verification before adding

Before including a repository, check:

- **Exists and is public**: the GitHub link works and the repo is not private.
- **Not archived or read-only**: if archived, it goes to `DELETED.md` ("Archived" section).
- **Not deprecated**: check if the README says "deprecated", "unmaintained", "broken", "use X instead".
- **Reasonable activity**: at least one commit in the last 3 years, unless it's a stable/complete project.
- **Not a duplicate**: cross-check with `README.md` and `DELETED.md`.
- **Minimum quality**: has documentation (README) and is not an empty or test repository.

## Pull requests and contributions

- PRs should use the template in `.github/PULL_REQUEST_TEMPLATE.md`.
- **Required**: include in the PR the **URL of the EU regulation, institution, or standard** the software supports (e.g., eur-lex.europa.eu, eurostat.ec.europa.eu).
- Issue templates available for suggesting projects (`suggest-project.md`) and requesting removal (`remove-project.md`).

## Structure

- Sections with `##`, subsections with `###`.
- Table of contents at the top between `<!--lint disable/enable awesome-list-item-->` comments.
- At the end: Contributing section, Note, and Disclaimer (as bold paragraphs, not ## headings).

## Prohibited topics

No projects related to: pornography, NSFW content, gambling, religion, partisan politics.

## Outreach

- Notify repo owners by opening an issue titled "Listed on awesome-europe" with a brief English message offering to remove if preferred. Only 1 issue per organization/user — do not spam repos from the same owner.
- Post to European dev communities (Reddit r/europe, r/programming, Hacker News) after reaching critical mass.
- Submit PR to [sindresorhus/awesome](https://github.com/sindresorhus/awesome) after 30 days from repo creation.

---

*Generated by [LynxPrompt](https://lynxprompt.com) CLI*

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:6cd5cc61 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->

## Where the tracker syncs

This repo is public, so its tracker syncs only to the private remote named by `sync.remote` in `.beads/config.yaml`. The block above says sync uses "your git remote". Here that never means this GitHub repo. Don't add it as a Dolt remote and don't push `refs/dolt/*` to it.
