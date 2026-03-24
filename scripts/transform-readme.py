#!/usr/bin/env python3
"""Transform awesome-europe README entries with metadata (stars, license, language, EU tags, demos)."""

import json
import re
import sys

# Load metadata
with open("scripts/metadata.json") as f:
    metadata = json.load(f)

# Section → default EU regulation tags
SECTION_TAGS = {
    "GDPR and Data Protection": ["GDPR"],
    "eIDAS and Digital Identity": ["eIDAS"],
    "Digital Regulation": [],  # varies per entry
    "Interoperability and Digital Infrastructure": [],
    "Electronic Invoicing": ["EN16931"],
    "Payments and Banking": ["PSD2"],
    "Central Banking and Monetary Policy": [],
    "VAT, Customs, and Trade": ["VAT"],
    "Anti-Money Laundering and Compliance": ["AMLD"],
    "Public Procurement": ["eProcurement"],
    "Open Data and Statistics": ["Open Data"],
    "Legal and Legislation": [],
    "Healthcare and Pharmaceuticals": [],
    "Agriculture and Food": ["CAP"],
    "Transport and Mobility": ["ITS"],
    "Energy": ["Energy"],
    "Telecommunications": ["EECC"],
    "Environment and Sustainability": [],
    "Geospatial and Earth Observation": [],
    "Cybersecurity and Incident Response": [],
    "Accessibility": ["EAA"],
    "Education and Research": [],
    "Country-Specific Awesome Lists": [],
}

# Keyword → EU tag overrides/additions (applied per-entry based on description)
KEYWORD_TAGS = {
    "GDPR": "GDPR",
    "General Data Protection": "GDPR",
    "eIDAS": "eIDAS",
    "PSD2": "PSD2",
    "AI Act": "AI Act",
    "Artificial Intelligence Act": "AI Act",
    "Digital Services Act": "DSA",
    "DSA": "DSA",
    "Digital Markets Act": "DMA",
    "DMA": "DMA",
    "Data Governance Act": "DGA",
    "DGA": "DGA",
    "NIS2": "NIS2",
    "NIS 2": "NIS2",
    "Network and Information Security": "NIS2",
    "Cyber Resilience Act": "CRA",
    "CRA": "CRA",
    "DORA": "DORA",
    "Digital Operational Resilience": "DORA",
    "EN 16931": "EN16931",
    "EN16931": "EN16931",
    "Factur-X": "EN16931",
    "ZUGFeRD": "EN16931",
    "XRechnung": "EN16931",
    "Peppol": "Peppol",
    "PEPPOL": "Peppol",
    "SEPA": "SEPA",
    "EBICS": "EBICS",
    "INSPIRE": "INSPIRE",
    "Copernicus": "Copernicus",
    "Sentinel": "Copernicus",
    "ECMWF": "ECMWF",
    "Eurostat": "Eurostat",
    "SDMX": "SDMX",
    "NUTS": "NUTS",
    "NGSI": "FIWARE",
    "FIWARE": "FIWARE",
    "Orion": "FIWARE",
    "Smart Data Models": "FIWARE",
    "AMLD": "AMLD",
    "anti-money": "AMLD",
    "Anti-Money": "AMLD",
    "sanctions": "AMLD",
    "VAT": "VAT",
    "customs": "Customs",
    "Customs": "Customs",
    "Intrastat": "Customs",
    "EORI": "Customs",
    "TARIC": "Customs",
    "procurement": "eProcurement",
    "eForms": "eProcurement",
    "TED ": "eProcurement",
    "Tenders Electronic": "eProcurement",
    "eDelivery": "eDelivery",
    "AS4": "eDelivery",
    "SMP ": "eDelivery",
    "CSIRT": "CSIRT",
    "CERT": "CSIRT",
    "incident response": "CSIRT",
    "incident handling": "CSIRT",
    "vulnerability": "CSIRT",
    "MISP": "CSIRT",
    "STIX": "CSIRT",
    "CAP ": "CAP",
    "Common Agricultural": "CAP",
    "IACS": "CAP",
    "Nutri-Score": "FIC",
    "food label": "FIC",
    "EAA": "EAA",
    "Web Accessibility Directive": "EAA",
    "EN 301 549": "EN301549",
    "ACT Rules": "EN301549",
    "accessibility": "EAA",
    "Erasmus": "Erasmus+",
    "ECTS": "ECTS",
    "Horizon": "Horizon",
    "CERN": "CERN",
    "Zenodo": "CERN",
    "OpenAIRE": "OpenAIRE",
    "EOSC": "EOSC",
    "EHDS": "EHDS",
    "HL7": "EHDS",
    "FHIR": "EHDS",
    "e-prescription": "EHDS",
    "EMA ": "EMA",
    "pharmacovigilance": "EMA",
    "IDMP": "EMA",
    "EU Taxonomy": "EU Taxonomy",
    "CSRD": "CSRD",
    "sustainability report": "CSRD",
    "Schengen": "Schengen",
    "Digital Product Passport": "ESPR",
    "DPP": "ESPR",
    "CBAM": "CBAM",
    "Carbon Border": "CBAM",
    "emissions trading": "ETS",
    "ETS": "ETS",
    "DCAT": "DCAT-AP",
    "DCAT-AP": "DCAT-AP",
    "CPSV": "CPSV-AP",
    "CEF": "CEF",
    "EPC": "EPC",
    "ISO 20022": "ISO20022",
    "SWIFT": "ISO20022",
    "OGC": "OGC",
    "WMS": "OGC",
    "WFS": "OGC",
    "noise": "END",
    "Environmental Noise": "END",
    "flood": "Floods Directive",
    "GCVE": "GCVE",
    "ITS-G5": "ITS",
    "ETSI": "ETSI",
    "DATEX": "ITS",
    "NeTEx": "ITS",
    "SIRI ": "ITS",
    "GTFS": "ITS",
    "Transmodel": "ITS",
    "Data Space": "Data Spaces",
    "data space": "Data Spaces",
    "EDC ": "Data Spaces",
    "Eclipse Dataspace": "Data Spaces",
    "Gaia-X": "Gaia-X",
    "Verifiable Credential": "eIDAS",
    "SSI": "eIDAS",
    "digital identity": "eIDAS",
    "X-Road": "X-Road",
    "XAdES": "eIDAS",
    "digital signature": "eIDAS",
    "ASiC": "eIDAS",
    "qualified": "eIDAS",
    "trust service": "eIDAS",
}

# Normalize language names
LANG_MAP = {
    "Jupyter Notebook": "Python",
    "GLSL": None,  # skip
    "Makefile": None,
    "Dockerfile": None,
    "Shell": None,
    "Batchfile": None,
    "Nix": None,
    "CMake": None,
    "Smarty": "PHP",
    "Mustache": "JavaScript",
    "Vue": "JavaScript",
    "Svelte": "JavaScript",
    "CSS": None,
    "SCSS": None,
    "Sass": None,
    "Less": None,
    "Roff": None,
    "PLpgSQL": "SQL",
    "TSQL": "SQL",
    "HCL": "Terraform",
    "Gherkin": None,
    "Groovy": "Java",
    "Scala": "Scala",
    "Clojure": "Clojure",
    "Elixir": "Elixir",
    "Erlang": "Erlang",
    "Haskell": "Haskell",
    "Lua": "Lua",
    "Perl": "Perl",
    "Dart": "Dart",
    "Swift": "Swift",
    "Objective-C": "Objective-C",
    "Assembly": None,
    "Fortran": "Fortran",
    "Mathematica": None,
    "TeX": None,
    "Jinja": "Python",
    "Starlark": None,
}

# License normalization
LICENSE_MAP = {
    "NOASSERTION": None,
    "0BSD": "0BSD",
}

# Demo URLs for known projects (gathered from homepages and research)
DEMO_URLS = {}


def get_eu_tags(section_name, entry_name, description):
    """Determine EU regulation tags for an entry."""
    tags = set()

    # Add section defaults
    if section_name in SECTION_TAGS:
        tags.update(SECTION_TAGS[section_name])

    # Scan description + name for keyword matches
    text = f"{entry_name} {description}"
    for keyword, tag in KEYWORD_TAGS.items():
        if keyword in text:
            tags.add(tag)

    return sorted(tags)


def get_language(owner_repo):
    """Get normalized language for a repo."""
    meta = metadata.get(owner_repo, {})
    lang = meta.get("language", "")
    if not lang:
        return None
    if lang in LANG_MAP:
        return LANG_MAP[lang]
    return lang


def get_license(owner_repo):
    """Get license SPDX ID for a repo."""
    meta = metadata.get(owner_repo, {})
    lic = meta.get("license", "")
    if not lic:
        return None
    if lic in LICENSE_MAP:
        return LICENSE_MAP[lic]
    return lic


def get_demo_url(owner_repo):
    """Get demo URL if available. Only uses curated DEMO_URLS dict."""
    return DEMO_URLS.get(owner_repo)


def transform_entry(line, current_section):
    """Transform a single entry line with metadata."""
    # Match entry pattern: - [Name](url) - Description.
    # Also match already-transformed entries (with ![Stars] etc.)
    m = re.match(r'^- \[([^\]]+)\]\((https://github\.com/([^)]+))\)\s+(?:!\[.*?\]\([^)]+\)\s*)*(?:\(\[Demo\]\([^)]+\)\)\s*)?- (.+)$', line)
    if not m:
        # Try simpler pattern for non-transformed entries
        m = re.match(r'^- \[([^\]]+)\]\((https://github\.com/([^)]+))\) - (.+)$', line)
    if not m:
        return line

    name = m.group(1)
    url = m.group(2)
    owner_repo = m.group(3)
    raw_desc = m.group(4)

    # Strip any existing backtick tags and demo links from description
    description = re.sub(r'\s*\(\[Demo\]\([^)]+\)\)', '', raw_desc)
    description = re.sub(r'\s*`[^`]+`', '', description).strip()

    # Auto-updating shields.io badges
    star_badge = f"![Stars](https://img.shields.io/github/stars/{owner_repo}?style=flat-square&label=⭐)"
    commit_badge = f"![Last Commit](https://img.shields.io/github/last-commit/{owner_repo}?style=flat-square)"
    lang_badge = f"![Language](https://img.shields.io/github/languages/top/{owner_repo}?style=flat-square)"
    license_badge = f"![License](https://img.shields.io/github/license/{owner_repo}?style=flat-square)"

    # EU regulation tags as blue badges
    eu_tags = get_eu_tags(current_section, name, raw_desc)
    eu_badges = " ".join(
        f"![{t}](https://img.shields.io/badge/{t.replace(' ', '%20')}-003399?style=flat-square)"
        for t in eu_tags
    )

    # Demo link
    demo = get_demo_url(owner_repo)
    demo_str = f" ([Demo]({demo}))" if demo else ""

    # Build: Name + auto-badges + EU badges + demo + description
    parts = [f"- [{name}]({url}) {star_badge} {commit_badge} {lang_badge} {license_badge}"]
    if eu_badges:
        parts[0] += f" {eu_badges}"
    if demo_str:
        parts[0] += demo_str
    parts[0] += f" - {description}"

    return parts[0]


def main():
    with open("README.md") as f:
        lines = f.readlines()

    output = []
    current_section = ""

    for line in lines:
        stripped = line.rstrip("\n")

        # Track current section
        section_match = re.match(r'^## (.+)$', stripped)
        if section_match:
            current_section = section_match.group(1)

        # Transform entry lines
        if stripped.startswith("- [") and "github.com/" in stripped and "](#" not in stripped:
            transformed = transform_entry(stripped, current_section)
            output.append(transformed + "\n")
        else:
            output.append(line)

    with open("README.md", "w") as f:
        f.writelines(output)

    print(f"Transformed README.md")


# Known demo URLs
DEMO_URLS.update({
    "intuitem/ciso-assistant-community": "https://demo.ciso-assistant.com",
    "orestbida/cookieconsent": "https://playground.cookieconsent.orestbida.com",
    "EUSurvey/EUSURVEY": "https://ec.europa.eu/eusurvey",
    "electricitymaps/electricitymap-contrib": "https://app.electricitymaps.com",
    "Open-EO/openeo-web-editor": "https://editor.openeo.org",
    "ISAITB/csv-validator": "https://www.itb.ec.europa.eu/csv/upload",
    "ISAITB/json-validator": "https://www.itb.ec.europa.eu/json/upload",
    "ISAITB/shacl-validator": "https://www.itb.ec.europa.eu/shacl/upload",
    "ISAITB/xml-validator": "https://www.itb.ec.europa.eu/xml/upload",
    "OP-TED/ted-open-data": "https://data.ted.europa.eu",
    "ec-europa/europa-component-library": "https://ec.europa.eu/component-library",
    "Nager/Nager.Date": "https://date.nager.at",
    "Lookyloo/lookyloo": "https://www.lookyloo.eu",
    "consul/consul": "https://consuldemocracy.org/en",
    "decidim/decidim": "https://decidim.org",
    "OpenCTI-Platform/opencti": "https://demo.opencti.io",
    "europeana/portal.js": "https://www.europeana.eu",
    "indico/indico": "https://getindico.io",
    "echr-od/ECHR-OD_process": "https://echr-opendata.eu",
    "HowTheyVote/howtheyvote": "https://howtheyvote.eu",
    "HowTheyVote/data": "https://howtheyvote.eu",
    "kiprotect/klaro": "https://klaro.org/demo",
    "altcha-org/altcha": "https://altcha.org/demo",
    "AKVorrat/dearmep": "https://dearmep.eu",
    "AmauriC/tarteaucitron.js": "https://tarteaucitron.io",
    "OpenBankProject/OBP-API": "https://apisandbox.openbankproject.com",
    "geopython/pygeoapi": "https://demo.pygeoapi.io",
    "geopython/GeoHealthCheck": "https://demo.geohealthcheck.org",
    "geonetwork/core-geonetwork": "https://demo.geonetwork-opensource.org",
    "cernopendata/opendata.cern.ch": "https://opendata.cern.ch",
    "cernanalysispreservation/analysispreservation.cern.ch": "https://analysispreservation.cern.ch",
    "HEPData/hepdata": "https://hepdata.net",
    "CERNDocumentServer/cds-videos": "https://videos.cern.ch",
    "EUDAT-B2SHARE/b2share": "https://b2share.eudat.eu",
    "keeps/roda": "https://demo.roda-community.org",
    "deegree/deegree3": "https://demo.deegree.org",
    "compl-ai/compl-ai": "https://compl-ai.org",
    "gcve-eu/gcve.eu": "https://gcve.eu",
    "adorsys/XS2A-Sandbox": "https://demo-dynamicsandbox-xs2a.cloud.adorsys.de",
    "CIRCL/bgp-ranking": "https://bgpranking.circl.lu",
    "getprobo/probo": "https://demo.getprobo.com",
    "CovenantSQL/CookieScanner": "https://gdprexpert.io",
    "FIWARE/catalogue": "https://www.fiware.org/catalogue",
    "gnss-sdr/gnss-sdr": "https://gnss-sdr.org",
    "calliope-project/calliope": "https://www.callio.pe",
    "hove-io/navitia": "https://playground.navitia.io",
    "datasets/eu-emissions-trading-system": "https://datahub.io/core/eu-emissions-trading-system",
    "OpenEnergyPlatform/oeplatform": "https://openenergyplatform.org",
    "HSLdevcom/digitransit-ui": "https://www.reittiopas.fi",
    "FlexMeasures/flexmeasures": "https://flexmeasures.io",
    "brbxai/recommand-peppol": "https://recommand.eu",
    "OpenRailAssociation/osrd": "https://osrd.fr",
    "eclipse-sumo/sumo": "https://eclipse.dev/sumo",
    "juliuste/direkt.bahn.guru": "https://direkt.bahn.guru",
    "MISP/MISP": "https://www.misp-project.org",
    "MISP/misp-galaxy": "https://misp-galaxy.org",
    "elixir-europe/rdmkit": "https://rdmkit.elixir-europe.org",
    "fsfe/reuse-tool": "https://reuse.software",
    "ckan/ckan": "https://demo.ckan.org",
    "aai-institute/practical-ai-act": "https://practical-ai-act.eu",
    "SonnyLabs/EU_AI_ACT_MCP": "https://sonnylabs.ai",
})

if __name__ == "__main__":
    main()
