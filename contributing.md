# Contributing to Awesome Europe

Thanks for your interest in contributing. This list grows thanks to the community.

## Guidelines

### Adding a project

- Make sure the project is **open source** with a public repository.
- The project must provide **support specifically for Europe** — EU institutions, regulations, standards, or cross-border infrastructure.
- The project must be **actively maintained** (activity in the last 3 years) and not archived.
- Each entry must follow the format: `- [Name](URL) - Brief description starting with a capital letter and ending with a period.`
- Add the entry in **alphabetical order** within the corresponding category.
- Check for **duplicates** and typos.
- Descriptions must be **concise and objective** (one sentence).

### Creating a new category

- Preferably with at least **3 projects** to justify it.
- Add the new category to the **table of contents** in the appropriate order.

### Entry format

```markdown
- [Name](https://github.com/owner/repo) ![Stars](https://img.shields.io/github/stars/owner/repo?style=flat-square&label=⭐) ![Language](https://img.shields.io/github/languages/top/owner/repo?style=flat-square) ![License](https://img.shields.io/github/license/owner/repo?style=flat-square) ![GDPR](https://img.shields.io/badge/GDPR-003399?style=flat-square) ([Demo](https://example.com)) - Description starting with a capital letter and ending with a period.
```

Each entry includes (in this order):
- **Star badge** (required): `![Stars](https://img.shields.io/github/stars/owner/repo?style=flat-square&label=⭐)` — auto-updating.
- **Language badge** (required): `![Language](https://img.shields.io/github/languages/top/owner/repo?style=flat-square)` — auto-updating.
- **License badge** (required): `![License](https://img.shields.io/github/license/owner/repo?style=flat-square)` — auto-updating.
- **EU regulation badges** (required): Blue badges (`#003399`) for each EU regulation/standard. E.g. `![GDPR](https://img.shields.io/badge/GDPR-003399?style=flat-square)`. Common tags: `GDPR`, `eIDAS`, `EN16931`, `PSD2`, `VAT`, `AMLD`, `NIS2`, `DORA`, `CRA`, `AI Act`, `DSA`, `DMA`, `INSPIRE`, `Copernicus`, `FIWARE`, `CERN`, `Peppol`, `SEPA`, `CSIRT`, `EAA`, `ITS`, `Data Spaces`, `Open Data`, `eProcurement`, `CAP`, `EHDS`.
- **Demo link** (optional): `([Demo](url))` — only if a live interactive instance is available (not a marketing page or docs).
- **Description** (required): One sentence, starts with a capital letter, ends with a period. Placed at the end after the ` - ` separator.

Additional rules:
- Description **must not start with the project name** (awesome-lint rejects this).
- Maximum one line per entry.
- Descriptions should be in **English**.
- Run `npx awesome-lint` before submitting your PR to verify there are no errors.

### Pull requests

1. Fork the repository.
2. Create a descriptive branch (`add-project-x` or `new-category-y`).
3. Make changes following the guidelines above.
4. Submit a pull request using the provided template.
5. **Include in the PR description the URL of the EU regulation, institution, or standard** the software supports (e.g., eur-lex.europa.eu, eurostat.ec.europa.eu). This helps verify the project is relevant for Europe.

### Reporting issues

If you find broken links, archived projects, or incorrect information, open an issue describing the problem.

## Code of conduct

Be respectful and constructive. Contributions should be made in good faith and aimed at improving the list for the entire community.
