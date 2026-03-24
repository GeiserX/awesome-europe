# AGENTS.md — awesome-europe

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

### Grey area — use judgement

- Projects that started as EU-specific but went global — include if European functionality remains a distinct, prominent feature.
- Software that covers EU + a few non-EU countries — include if the EU/EEA is the primary target.

## Quality standards

**Same quality bar as [awesome-spain](https://github.com/GeiserX/awesome-spain):**

- **No archived repos**: if discovered archived after inclusion, move to `DELETED.md` immediately.
- **No extremely unmaintained repos**: at least one commit in the last 3 years, unless it's a clearly stable/complete project (e.g., a spec validator that hasn't changed because the spec hasn't changed).
- **No broken repos**: if the repo README says "deprecated", "no longer maintained", "use X instead", or similar — do not include. Move to `DELETED.md` if already listed.
- **Minimum stars**: prefer repos with at least a few stars, but exceptional niche tools with 0-1 stars may be included if they fill an important gap.
- **Verify every repo** before adding: check `archived`, `pushed_at`, `stargazers_count` via `gh api repos/owner/name`.

## Entry format

```markdown
- [Name](https://github.com/owner/repo) ![Stars](https://img.shields.io/github/stars/owner/repo?style=flat-square&label=⭐) ![Language](https://img.shields.io/github/languages/top/owner/repo?style=flat-square) ![License](https://img.shields.io/github/license/owner/repo?style=flat-square) ![GDPR](https://img.shields.io/badge/GDPR-003399?style=flat-square) ([Demo](https://example.com)) - Description starting with a capital letter and ending with a period.
```

Each entry includes (in this order):
- **Star badge** (required): `![Stars](https://img.shields.io/github/stars/owner/repo?style=flat-square&label=⭐)` — auto-updating.
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
