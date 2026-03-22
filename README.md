<div align="center">
  <img src="media/banner.svg" alt="Awesome Europe">
  <br><br>
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat.svg" alt="Awesome"></a>
  <br><br>
  <p>A curated list of open source software that provides support specifically for Europe — its institutions, regulations, standards, and cross-border infrastructure.</p>
</div>

## Contents

<!--lint disable awesome-list-item-->

- [GDPR and Data Protection](#gdpr-and-data-protection)
- [eIDAS and Digital Identity](#eidas-and-digital-identity)
- [Digital Regulation](#digital-regulation)
- [Interoperability and Digital Infrastructure](#interoperability-and-digital-infrastructure)
- [Electronic Invoicing](#electronic-invoicing)
- [Payments and Banking](#payments-and-banking)
- [Central Banking and Monetary Policy](#central-banking-and-monetary-policy)
- [VAT, Customs, and Trade](#vat-customs-and-trade)
- [Anti-Money Laundering and Compliance](#anti-money-laundering-and-compliance)
- [Finance and Capital Markets](#finance-and-capital-markets)
- [Open Data and Statistics](#open-data-and-statistics)
- [Legal and Legislation](#legal-and-legislation)
- [Intellectual Property](#intellectual-property)
- [Democracy and Governance](#democracy-and-governance)
- [Public Procurement](#public-procurement)
- [Energy and Electricity](#energy-and-electricity)
- [Sustainability and ESG](#sustainability-and-esg)
- [Transport and Mobility](#transport-and-mobility)
- [Space and Aviation](#space-and-aviation)
- [Geospatial and Earth Observation](#geospatial-and-earth-observation)
- [Health and Pharmaceuticals](#health-and-pharmaceuticals)
- [Cybersecurity](#cybersecurity)
- [Accessibility](#accessibility)
- [Education and Research](#education-and-research)
- [European Utilities](#european-utilities)
- [Country-Specific Awesome Lists](#country-specific-awesome-lists)

<!--lint enable awesome-list-item-->

## GDPR and Data Protection

EU General Data Protection Regulation (2016/679) and related data protection frameworks.

- [Cookie Consent](https://github.com/orestbida/cookieconsent) - Simple cross-browser cookie-consent plugin written in vanilla JavaScript for GDPR and ePrivacy compliance.
- [Consent-O-Matic](https://github.com/cavi-au/Consent-O-Matic) - Browser extension that automatically fills out cookie popups based on your preferences.
- [Klaro](https://github.com/kiprotect/klaro) - Privacy-friendly and compliant consent manager for websites.
- [GDPR Transparency and Consent Framework](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework) - Technical specifications for IAB Europe Transparency and Consent Framework for GDPR compliance in digital advertising.
- [GDPR Checklist](https://github.com/privacyradius/gdpr-checklist) - Checklist for GDPR compliance.
- [CISO Assistant](https://github.com/intuitem/ciso-assistant-community) - GRC platform supporting 100+ frameworks including GDPR, NIS2, DORA, and ISO 27001 with automatic control mapping.
- [Probo](https://github.com/getprobo/probo) - Open source compliance solutions for SOC2, GDPR, and ISO 27001.
- [Databunker](https://github.com/paranoidguy/databunker) - Secure vault for customer PII records providing a GDPR compliance API.
- [tarteaucitron.js](https://github.com/AmauriC/tarteaucitron.js) - Compliant and accessible cookie consent banner with built-in support for hundreds of services.
- [Fides](https://github.com/ethyca/fides) - Privacy engineering and compliance framework for GDPR data mapping, consent, and subject request automation.
- [gdpr_rails](https://github.com/prey/gdpr_rails) - Rails engine for GDPR compliance including data portability, consent management, and right to erasure.

## eIDAS and Digital Identity

Electronic Identification, Authentication and Trust Services regulation for cross-border digital identity, including the EU Digital Identity Wallet.

- [EUDI Architecture and Reference Framework](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) - Architecture and reference framework for the European Digital Identity Wallet.
- [EUDI Wallet Android](https://github.com/eu-digital-identity-wallet/eudi-app-android-wallet-ui) - EUDI Wallet prototype for Android.
- [EUDI Wallet iOS](https://github.com/eu-digital-identity-wallet/eudi-app-ios-wallet-ui) - EUDI Wallet prototype for iOS.
- [EUDI Verifier Endpoint](https://github.com/eu-digital-identity-wallet/eudi-srv-verifier-endpoint) - Web application that acts as a Verifier trusted endpoint for the EUDI Wallet.
- [walt.id Identity](https://github.com/walt-id/waltid-identity) - All-in-one open source identity and wallet toolkit with eIDAS 2.0 support.
- [Procivis One Core](https://github.com/procivis/one-core) - Issue, hold and verify digital identities and credentials with eIDAS 2.0 compliancy.
- [Procivis One Wallet](https://github.com/procivis/one-wallet) - Digital wallet with eIDAS 2.0 compliancy, ISO 18013-5 mdocs, and SD-JWT VC support.
- [eIDAS Middleware](https://github.com/Governikus/eidas-middleware) - Implementation of the European eIDAS middleware provided under the EUPL 1.2 by Governikus.
- [eIDAS Keycloak Extension](https://github.com/grnet/eidas-keycloak-extension) - Keycloak Identity Provider extension supporting the eIDAS SAML v2.0 dialect.
- [Apple eIDAS](https://github.com/apple/eidas) - Tools for reading and creating eIDAS certificate signing requests.
- [pyMDOC-CBOR](https://github.com/IdentityPython/pyMDOC-CBOR) - MDOC CBOR static Verifier and Issuer for EUDI Wallet PID and mDL use cases.
- [tl-create](https://github.com/PeculiarVentures/tl-create) - Cross-platform CLI tool to create X.509 trust lists from various trust stores including eIDAS.
- [SSI Agent](https://github.com/impierce/ssi-agent) - eIDAS 2.0-compliant Self Sovereign Identity Agent that connects European Identity Wallets to IT systems.
- [Open Banking eIDAS Broker](https://github.com/enablebanking/open_banking_eidas_broker) - Microservice using eIDAS certificates for signing PSD2 API requests and accessing banks over mTLS.
- [js-undersign](https://github.com/moll/js-undersign) - JavaScript library for creating eIDAS compatible XAdES signatures with support for OCSP and timestamps.
- [EUDI Wallet Core Android](https://github.com/eu-digital-identity-wallet/eudi-lib-android-wallet-core) - Core libraries for the EUDI Wallet reference implementation on Android.
- [EUDI OpenID4VCI Kotlin](https://github.com/eu-digital-identity-wallet/eudi-lib-jvm-openid4vci-kt) - Kotlin implementation of the OpenID for Verifiable Credential Issuance protocol for the EUDI Wallet.
- [EUDI SD-JWT Kotlin](https://github.com/eu-digital-identity-wallet/eudi-lib-jvm-sdjwt-kt) - Kotlin library for issuing and verifying SD-JWT credentials in the EUDI Wallet ecosystem.
- [EUDI PID Issuer](https://github.com/eu-digital-identity-wallet/eudi-srv-pid-issuer) - Microservice for issuing Person Identification Data and mDL according to OpenID4VCI.
- [EUDI Web Verifier](https://github.com/eu-digital-identity-wallet/eudi-web-verifier) - Web-based verifier application for the European Digital Identity Wallet.
- [OID4VCI](https://github.com/sphereon-opensource/OID4VCI) - TypeScript modules for OpenID for Verifiable Credential Issuance used in EUDI Wallet implementations.

## Digital Regulation

EU AI Act, Digital Services Act (DSA), Digital Markets Act (DMA), and related digital regulation compliance tools.

- [EuConform](https://github.com/Hiepler/EuConform) - EU AI Act compliance tool for risk classification and bias testing.
- [DSA Transparency Database](https://github.com/digital-services-act/transparency-database) - Official Digital Services Act Transparency Database for content moderation reporting.

## Interoperability and Digital Infrastructure

CEF building blocks (eDelivery, eSignature, eTranslation), X-Road, EBSI, and EU cross-border digital infrastructure.

- [DSS](https://github.com/esig/dss) - EU Digital Signature Service for creation, extension and validation of advanced electronic signatures (CAdES, XAdES, PAdES, ASiC).
- [X-Road](https://github.com/nordic-institute/X-Road) - Data exchange layer software used by EU member states for secure cross-border data exchange.
- [Eclipse Dataspace Connector](https://github.com/eclipse-edc/Connector) - EDC core services including data plane and control plane for EU data spaces.
- [FIWARE Catalogue](https://github.com/FIWARE/catalogue) - Curated framework of open source platform components for EU smart applications using NGSI-LD.
- [Europa Component Library](https://github.com/ec-europa/europa-component-library) - Component library used by the European Commission websites.
- [sovity EDC CE](https://github.com/sovity/edc-ce) - Community Edition of the Eclipse Dataspace Connector by sovity.
- [Orion-LD](https://github.com/FIWARE/context.Orion-LD) - Context Broker and CEF building block for context data management supporting NGSI-LD and NGSI-v2.
- [FIWARE NGSI-LD Tutorials](https://github.com/FIWARE/tutorials.NGSI-LD) - Step-by-step tutorials for FIWARE NGSI-LD smart applications.
- [pkilint](https://github.com/digicert/pkilint) - Framework for verifying PKI structures including EU trust service certificates.
- [Smart Data Models](https://github.com/smart-data-models/data-models) - Harmonized data models for EU-funded smart applications based on NGSI-LD.
- [Europeana Portal](https://github.com/europeana/portal.js) - Europeana.eu website providing access to European cultural heritage collections.
- [Europeana Core Library](https://github.com/europeana/corelib) - Core library containing EDM (Europeana Data Model) used by Europeana applications.
- [LinkedPipes ETL](https://github.com/linkedpipes/etl) - RDF-based lightweight ETL tool developed under EU research funding.
- [Stellio Context Broker](https://github.com/stellio-hub/stellio-context-broker) - NGSI-LD compatible context broker for EU smart applications.
- [Scorpio Broker](https://github.com/ScorpioBroker/ScorpioBroker) - NGSI-LD compliant context broker developed by NEC for EU data spaces.
- [hale»studio](https://github.com/halestudio/hale) - Spatial data harmonisation tool for INSPIRE-compliant data transformation.
- [Interoperability Test Bed](https://github.com/ISAITB/gitb) - Conformance testing solution supported by the European Commission for EU IT systems interoperability.
- [publiccode.yml](https://github.com/publiccodeyml/publiccode.yml) - Metadata standard for describing public software adopted across EU administrations.
- [Eclipse EDC IdentityHub](https://github.com/eclipse-edc/IdentityHub) - Identity management component for the Eclipse Dataspace Connector ecosystem.
- [Minimum Viable Dataspace](https://github.com/eclipse-edc/MinimumViableDataspace) - Documentation and scripts for deploying a minimum viable EU dataspace with Eclipse EDC.
- [SEMIC Core Vocabularies](https://github.com/SEMICeu/Core-Person-Vocabulary) - Core Person Vocabulary for cross-border data exchange in the EU, maintained by SEMIC.

## Electronic Invoicing

Peppol, EN 16931, and the EU e-invoicing directive (2014/55/EU) for cross-border electronic invoicing.

- [Mustang](https://github.com/ZUGFeRD/mustangproject) - Java e-invoicing library, validator, and tool for Factur-X, ZUGFeRD, and XRechnung.
- [ZUGFeRD C#](https://github.com/stephanstapel/ZUGFeRD-csharp) - C# library for creating and reading ZUGFeRD and Factur-X e-invoices.
- [ZUGFeRD/XRechnung Library](https://github.com/horstoeko/zugferd) - PHP library for ZUGFeRD, XRechnung, and Factur-X e-invoicing formats.
- [Factur-X](https://github.com/akretion/factur-x) - Python library for Factur-X, the e-invoicing standard for France and Germany based on EN 16931.
- [eInvoicing-EN16931](https://github.com/ConnectingEurope/eInvoicing-EN16931) - Official validation artefacts for the European eInvoicing standard EN 16931.
- [drafthorse](https://github.com/pretix/python-drafthorse) - Pure Python ZUGFeRD and Factur-X implementation for creating EN 16931 e-invoices.
- [e-invoice-eu](https://github.com/gflohr/e-invoice-eu) - Generate EN 16931 compliant e-invoices from spreadsheet data or JSON.
- [phase4](https://github.com/phax/phase4) - AS4 client and server with built-in support for Peppol and CEF eDelivery.
- [phoss SMP](https://github.com/phax/phoss-smp) - Peppol and OASIS BDXR SMP Server, CEF eDelivery compliant.
- [einvoicing (PHP)](https://github.com/josemmo/einvoicing) - PHP library for reading and creating European-compliant electronic invoices (EN 16931).
- [OpenXRechnungToolbox](https://github.com/jcthiele/OpenXRechnungToolbox) - GUI for visualization and validation of XRechnung and other EN 16931-compliant e-invoices.
- [Oxalis](https://github.com/OxalisCommunity/oxalis) - PEPPOL Access Point open source implementation.
- [Oxalis-NG](https://github.com/OxalisCommunity/oxalis-ng) - Open source implementation of OpenPeppol AS4 profile (next generation).
- [Peppol BIS Invoice 3](https://github.com/OpenPEPPOL/peppol-bis-invoice-3) - Official Peppol BIS 3.0 billing specifications.
- [UBL Invoice](https://github.com/num-num/ubl-invoice) - PHP library to read and create valid UBL and Peppol BIS files.
- [phive](https://github.com/phax/phive) - Generic business document validation engine for EU e-invoicing standards.
- [phive-rules](https://github.com/phax/phive-rules) - Preconfigured validation rules for Peppol, XRechnung, and other EU e-invoicing formats.
- [Peppol Commons](https://github.com/phax/peppol-commons) - Java library with shared Peppol components including identifier handling and SMP/SML clients.
- [phoss Directory](https://github.com/phax/phoss-directory) - Official Peppol Directory software.
- [Recommand Peppol](https://github.com/brbxai/recommand-peppol) - Open source Peppol API.
- [einvoicing (JS)](https://github.com/esvit/einvoicing) - JavaScript library for creating and parsing electronic invoices compliant with the eInvoicing Directive and EN 16931.
- [e-invoicing (PHP)](https://github.com/easybill/e-invoicing) - PHP library to generate and read EN 16931 structured XML with UBL and CII syntaxes.

## Payments and Banking

SEPA, PSD2, Open Banking, EBICS, and the Single Euro Payments Area infrastructure.

- [OBP-API](https://github.com/OpenBankProject/OBP-API) - Open source RESTful API platform for banks supporting PSD2, Open Banking, and XS2A.
- [Open Banking Gateway](https://github.com/adorsys/open-banking-gateway) - RESTful API, tools, adapters, and connectors for transparent access to open banking APIs (PSD2).
- [XS2A](https://github.com/adorsys/xs2a) - Open source NextGenPSD2 XS2A implementation for PSD2 compliance.
- [php-sepa-xml](https://github.com/php-sepa-xml/php-sepa-xml) - PHP library for generating SEPA XML files for credit transfer and direct debit.
- [Nordigen Python](https://github.com/nordigen/nordigen-python) - Python library for the Nordigen open banking API.
- [Sephpa](https://github.com/AbcAeffchen/Sephpa) - PHP class to create SEPA XML files for credit transfer and direct debit.
- [SepaUtilities](https://github.com/AbcAeffchen/SepaUtilities) - PHP methods for validating and sanitizing inputs used in SEPA files.
- [python-sepaxml](https://github.com/raphaelm/python-sepaxml) - Python library to generate SEPA XML files for direct debit and credit transfer.
- [sepa_king](https://github.com/salesking/sepa_king) - Ruby gem for creating SEPA XML files for credit transfer and direct debit.
- [epics](https://github.com/railslove/epics) - EBICS client for Ruby supporting secure European banking communication.
- [node-ebics-client](https://github.com/node-ebics/node-ebics-client) - Node.js EBICS client compliant with ISO 20022 for European electronic banking.
- [ebics-client-php](https://github.com/ebics-api/ebics-client-php) - PHP EBICS library supporting versions 2.4, 2.5, and 3.0 for European banking communication.
- [libfintx](https://github.com/libfintx/libfintx) - .NET banking client library for HBCI 2.2, FinTS 3.0, and EBICS H004/H005.

## Central Banking and Monetary Policy

ECB APIs, TARGET2/T2S/TIPS, Euribor/ESTR, euro exchange rates, and Eurosystem tools.

- [Frankfurter](https://github.com/lineofflight/frankfurter) - Currency data API built on top of ECB exchange rates.
- [Swap](https://github.com/florianv/swap) - Currency exchange rates library supporting ECB and other European central bank providers.
- [eu_central_bank](https://github.com/RubyMoney/eu_central_bank) - Ruby gem that calculates exchange rates using published rates from the European Central Bank.
- [CurrencyConverter](https://github.com/alexprengere/currencyconverter) - Python currency converter using historical exchange rate data from the European Central Bank.

## VAT, Customs, and Trade

EU VAT system (VIES, OSS/IOSS), TARIC customs tariffs, CN codes, EORI, and Intrastat.

- [valvat](https://github.com/yolk/valvat) - Ruby library for validating European VAT numbers with VIES lookup.
- [ibericode VAT](https://github.com/ibericode/vat) - PHP library for dealing with European VAT including rates and VIES validation.
- [node-sales-tax](https://github.com/valeriansaliou/node-sales-tax) - International sales tax calculator for Node.js with EU VAT support including VIES validation.
- [VIES](https://github.com/DragonBe/vies) - PHP component for the European Commission VAT Information Exchange System (VIES).
- [vat](https://github.com/dannyvankooten/vat) - Go package for EU VAT number validation and rates retrieval.
- [VAT Calculator](https://github.com/driesvints/vat-calculator) - PHP package to handle EU MOSS tax and VAT regulations including rate lookup and VIES validation.
- [vat-rates](https://github.com/ibericode/vat-rates) - Community-maintained JSON dataset of VAT rates for all EU member states.

## Anti-Money Laundering and Compliance

EU Anti-Money Laundering Directives (AMLD), sanctions screening, KYC/KYB, beneficial ownership, and LEI tools.

- [Aleph](https://github.com/alephdata/aleph) - Search and browse documents and data to find people and companies, used for investigative journalism and EU compliance.
- [OpenSanctions](https://github.com/opensanctions/opensanctions) - Open database of international sanctions data, persons of interest and politically exposed persons, including EU sanctions lists.
- [Follow the Money](https://github.com/alephdata/followthemoney) - Data model and processing tools for investigative entity data used in EU AML compliance.
- [Yente](https://github.com/opensanctions/yente) - Entity matching and search API for OpenSanctions data, supporting EU sanctions screening and KYC workflows.
- [Beneficial Ownership Data Standard](https://github.com/openownership/data-standard) - Open standard for publishing beneficial ownership data, aligned with EU AMLD transparency requirements.

## Finance and Capital Markets

EBA, ESMA regulations, MiFID II, MiCA, DORA, EMIR, XBRL/iXBRL reporting, and European financial market infrastructure.

- [Arelle](https://github.com/Arelle/Arelle) - Open source XBRL platform for European financial reporting including EBA and ESMA taxonomies.
- [Arelle iXBRL Viewer](https://github.com/Arelle/ixbrl-viewer) - Interactive viewer for Inline XBRL reports used in EU financial filings under ESEF regulation.
- [py-xbrl](https://github.com/manusimidt/py-xbrl) - Python parser for XBRL and iXBRL files used in EU ESEF financial reporting.
- [ixbrl-parse](https://github.com/kanedata/ixbrl-parse) - Python library for extracting structured data from iXBRL files used in EU regulatory filings.
- [esma_data_py](https://github.com/European-Securities-Markets-Authority/esma_data_py) - Official ESMA Python package for searching and downloading data from the ESMA register.

## Open Data and Statistics

Eurostat, EU Open Data Portal, SDMX, NUTS regions, and pan-European statistical infrastructure.

- [eurostat (R)](https://github.com/rOpenGov/eurostat) - R tools for Eurostat open data access and analysis.
- [Nuts2json](https://github.com/eurostat/Nuts2json) - Eurostat NUTS regions dataset as JSON for web mapping.
- [SDMX-ML](https://github.com/sdmx-twg/sdmx-ml) - Format specification for statistical data exchange used by Eurostat and ECB.
- [Open Data Handbook](https://github.com/okfn/opendatahandbook) - Guide to legal, social and technical aspects of open data, widely used in EU open data initiatives.
- [Metis Framework](https://github.com/europeana/metis-framework) - Data publication framework for ingesting and processing European cultural heritage metadata.
- [CKAN](https://github.com/ckan/ckan) - Open source data management system powering many European government open data portals.
- [DCAT-AP](https://github.com/SEMICeu/DCAT-AP) - Application profile of DCAT for describing public sector datasets in European data portals.
- [udata](https://github.com/opendatateam/udata) - Customizable social platform for open data publication, powering data.gouv.fr and other EU portals.
- [gridviz](https://github.com/eurostat/gridviz) - JavaScript library for visualising European gridded statistical data.
- [eurostat-map.js](https://github.com/eurostat/eurostat-map.js) - JavaScript library for creating thematic web maps of European NUTS regions based on D3.
- [pandaSDMX](https://github.com/dr-leo/pandaSDMX) - Python interface to SDMX for accessing data from ECB, Eurostat, and other European statistical providers.

## Legal and Legislation

EUR-Lex, ECLI, CELEX, ELI, Akoma Ntoso, and tools for accessing and processing European legislation.

- [eForms SDK](https://github.com/OP-TED/eForms-SDK) - eForms notification standard for public procurement procedures in the EU, published by the EU Publications Office.
- [eForms Notice Viewer](https://github.com/OP-TED/eforms-notice-viewer) - Sample application that can visualise an eForms notice using the eForms SDK.
- [eurlex](https://github.com/step21/eurlex) - Python package for querying the EU Cellar repository and downloading EUR-Lex legislative data.
- [eurlex (R)](https://github.com/michalovadek/eurlex) - R package for retrieving data on European Union laws and policies from EUR-Lex and CELLAR.

## Intellectual Property

European Patent Office (EPO), EUIPO, Unitary Patent, and EU trademark tools.

- [python-epo-ops-client](https://github.com/ip-tools/python-epo-ops-client) - Python client for the European Patent Office Open Patent Services API.
- [PatZilla](https://github.com/ip-tools/patzilla) - Modular patent information research platform with access to EPO data sources.

## Democracy and Governance

European Parliament, EU elections, Transparency Register, European Citizens' Initiative, and EU legislative tracking.

- [HowTheyVote](https://github.com/HowTheyVote/howtheyvote) - Tracks how Members of the European Parliament vote in plenary sessions.
- [Parltrack](https://github.com/parltrack/parltrack) - Parliamentary tracker application for monitoring the European Parliament.
- [EveryPolitician Data](https://github.com/everypolitician/everypolitician-data) - Data for national legislatures worldwide including all EU member states.
- [FragDenStaat](https://github.com/okfde/fragdenstaat_de) - Freedom of information portal for government transparency requests.
- [EUSurvey](https://github.com/EUSurvey/EUSURVEY) - Official European Commission open source survey tool used across EU institutions.
- [Dear MEP](https://github.com/AKVorrat/dearmep) - Tool empowering citizens to contact Members of the European Parliament about legislative debates.

## Public Procurement

TED (Tenders Electronic Daily), eForms, ESPD, CPV codes, and EU public procurement infrastructure.

- [OCDS Standard](https://github.com/open-contracting/standard) - Open Contracting Data Standard used in EU public procurement transparency.
- [ESPD-EDM](https://github.com/OP-TED/ESPD-EDM) - European Single Procurement Document Exchange Data Model for integration with national ESPD service providers.
- [eProcurement Ontology](https://github.com/OP-TED/ePO) - Formal semantic foundation for linked open data in the domain of EU public procurement.
- [TED Open Data](https://github.com/OP-TED/ted-open-data) - SPARQL query editor for the Tenders Electronic Daily Open Data Service.
- [eForms Notice Editor](https://github.com/OP-TED/eforms-notice-editor) - Sample application demonstrating how to create eForms notices using the SDK.
- [model2owl](https://github.com/OP-TED/model2owl) - Tool to transform UML models into OWL ontologies and SHACL shapes for EU procurement data.
- [ted-rdf-mapping](https://github.com/OP-TED/ted-rdf-mapping) - Transformation rules for the TED Semantic Web Services RDF conversion.

## Energy and Electricity

ENTSO-E Transparency Platform, ACER, REMIT, and the European energy market.

- [PyPSA](https://github.com/PyPSA/PyPSA) - Python framework for simulating and optimising power systems, widely used in European energy research.
- [PyPSA-Eur](https://github.com/PyPSA/pypsa-eur) - Open optimisation model of the European energy system covering electricity, heating, and transport sectors.
- [Nord Pool](https://github.com/custom-components/nordpool) - Home Assistant integration for fetching day-ahead energy prices from the Nord Pool European energy exchange.
- [entsoe-py](https://github.com/EnergieID/entsoe-py) - Python client for the ENTSO-E API (European Network of Transmission System Operators for Electricity).
- [ENTSO-E Home Assistant](https://github.com/JaccoR/hass-entso-e) - Home Assistant integration for fetching day-ahead energy prices from the ENTSO-E Transparency Platform.
- [atlite](https://github.com/PyPSA/atlite) - Python package for calculating renewable power potentials and time series for the European energy system.
- [powerplantmatching](https://github.com/PyPSA/powerplantmatching) - Tools to combine multiple European power plant databases.
- [technology-data](https://github.com/PyPSA/technology-data) - Compiled assumptions on European energy system technologies including costs and efficiencies.
- [PowSyBl](https://github.com/powsybl/powsybl-core) - Java framework for power system analysis used by European transmission system operators.
- [Open Smart Grid Platform](https://github.com/OSGP/open-smart-grid-platform) - Open source platform for smart grid management in European energy networks.
- [Electricity Maps](https://github.com/electricitymaps/electricitymap-contrib) - Open source data parsers powering real-time electricity generation and carbon intensity maps across Europe.
- [Dispa-SET](https://github.com/energy-modelling-toolkit/Dispa-SET) - Unit commitment and optimal dispatch model for the European power system, developed at the JRC.
- [Open Energy Ontology](https://github.com/OpenEnergyPlatform/ontology) - Ontology for energy system modelling and analysis in the European research context.
- [Calliope](https://github.com/calliope-project/calliope) - Multi-scale energy systems modelling framework used in European energy research.
- [FlexMeasures](https://github.com/FlexMeasures/flexmeasures) - Intelligent energy management system supporting real-time flexibility applications in European energy markets.

## Sustainability and ESG

EU Taxonomy, CSRD, SFDR, CBAM, Digital Product Passport, EU Deforestation Regulation, and sustainable finance.

- [Eclipse Tractus-X](https://github.com/eclipse-tractusx/tractus-x-release) - EU-funded Catena-X automotive data ecosystem for supply chain transparency and sustainability.
- [Tractus-X Traceability](https://github.com/eclipse-tractusx/traceability-foss) - Supply chain traceability application for the Catena-X EU Digital Product Passport ecosystem.
- [Tractus-X BPDM](https://github.com/eclipse-tractusx/bpdm) - Business Partner Data Management for the Catena-X EU automotive data ecosystem.
- [Battery Pass Data Model](https://github.com/batterypass/BatteryPassDataModel) - Data model for the EU Battery Passport under the Digital Product Passport framework.
- [EU Emissions Trading System Data](https://github.com/datasets/eu-emissions-trading-system) - Open dataset of the EU Emissions Trading System.
- [OS-Climate ITR](https://github.com/os-climate/ITR) - Python implementation of the Implied Temperature Rise methodology for EU sustainable finance.

## Transport and Mobility

European railway interoperability (ERA, ETCS), cross-border transport, eCall, EETS, and EU mobility frameworks.

- [traffic](https://github.com/xoolive/traffic) - Python toolbox for processing and analysing air traffic data from Eurocontrol and OpenSky.
- [OpenSky API](https://github.com/openskynetwork/opensky-api) - Python and Java bindings for the OpenSky Network REST API for European air traffic data.
- [hafas-client](https://github.com/derhuerst/hafas-client) - JavaScript client for HAFAS public transport APIs used across European transit systems.
- [Pumperly](https://github.com/GeiserX/pumperly) - Open source fuel and EV route planner with real-time prices across European countries.
- [OSRD](https://github.com/OpenRailAssociation/osrd) - Open source web application for railway infrastructure design, capacity analysis, and timetabling across European networks.
- [Eclipse SUMO](https://github.com/eclipse-sumo/sumo) - Open source, highly portable microscopic traffic simulation package used in EU transport research.
- [UIC Barcode](https://github.com/UnionInternationalCheminsdeFer/UIC-barcode) - Implementation of the FCB barcode standard (IRS 90918-9) for European railway ticketing.
- [Digitransit UI](https://github.com/HSLdevcom/digitransit-ui) - Open source multi-modal journey planner UI used in European public transport.
- [NeTEx](https://github.com/NeTEx-CEN/NeTEx) - CEN technical standard for exchanging public transport schedules and related data across Europe.
- [Transitous](https://github.com/public-transport/transitous) - Free and open public transport routing engine for pan-European journey planning.
- [MOTIS](https://github.com/motis-project/motis) - Multimodal travel information system providing routing, geocoding, and map tiles across European transit networks.

## Space and Aviation

ESA, Eurocontrol, Galileo, EGNOS, and European space and aviation infrastructure.

- [GNSS-SDR](https://github.com/gnss-sdr/gnss-sdr) - Open source software-defined GNSS receiver with Galileo signal support.
- [Orekit](https://github.com/CS-SI/Orekit) - Java library for space dynamics and orbital mechanics developed with ESA support.
- [galmon](https://github.com/berthubert/galmon) - Open source monitoring system for the Galileo satellite navigation constellation.

## Geospatial and Earth Observation

INSPIRE directive, Copernicus programme, Sentinel data, and European geospatial infrastructure.

- [eo-learn](https://github.com/sentinel-hub/eo-learn) - Earth observation processing framework for machine learning using Copernicus Sentinel data.
- [sentinel2-cloud-detector](https://github.com/sentinel-hub/sentinel2-cloud-detector) - Cloud detector for Copernicus Sentinel-2 satellite images in Python.
- [sentinelhub-py](https://github.com/sentinel-hub/sentinelhub-py) - Python library to download and process satellite imagery using Sentinel Hub services.
- [eodag](https://github.com/CS-SI/eodag) - Python framework for searching and downloading Earth observation data from Copernicus and other providers.
- [pygeoapi](https://github.com/geopython/pygeoapi) - Python server implementation of the OGC API suite of standards used in INSPIRE infrastructure.
- [OWSLib](https://github.com/geopython/OWSLib) - Python package for client programming with OGC web services used in European geospatial infrastructure.
- [CDS API](https://github.com/ecmwf/cdsapi) - Python API to access the Copernicus Climate Data Store.
- [cfgrib](https://github.com/ecmwf/cfgrib) - Python interface to map GRIB files to NetCDF, widely used with Copernicus weather data.
- [eccodes](https://github.com/ecmwf/eccodes) - ECMWF library for GRIB and BUFR decoding and encoding used in European weather and climate services.
- [CliMetLab](https://github.com/ecmwf/climetlab) - Python package for easy access to Copernicus weather and climate data.
- [Atlas](https://github.com/ecmwf/atlas) - ECMWF library for numerical weather prediction and climate modelling.
- [OpenSarToolkit](https://github.com/ESA-PhiLab/OpenSarToolkit) - ESA toolkit for inventory, download and pre-processing of Sentinel-1 SAR data.
- [LISFLOOD](https://github.com/ec-jrc/lisflood-code) - JRC spatially distributed water resources model used for European flood forecasting.
- [c2cgeoportal](https://github.com/camptocamp/c2cgeoportal) - Geoportal application framework used in European INSPIRE-compliant geospatial portals.
- [ldproxy](https://github.com/interactive-instruments/ldproxy) - Server for sharing geospatial data via modern OGC API web services, used in INSPIRE infrastructure.
- [GeoNetwork](https://github.com/geonetwork/core-geonetwork) - Metadata catalog application for managing spatially referenced resources, widely used in EU INSPIRE nodes.
- [deegree](https://github.com/deegree/deegree3) - Java framework for OGC web service implementations used in European geospatial data infrastructure.
- [openEO Python Client](https://github.com/Open-EO/openeo-python-client) - Python client for the openEO API, providing access to Copernicus and other European Earth observation data.
- [earthkit](https://github.com/ecmwf/earthkit) - ECMWF Python tools for working with European weather and climate data.
- [INSPIRE Validator](https://github.com/INSPIRE-MIF/helpdesk-validator) - Community discussion and issue tracker for the INSPIRE data and service validation tools.
- [actinia](https://github.com/mundialis/actinia_core) - Open source REST API for scalable geospatial data processing used in European environmental monitoring.

## Health and Pharmaceuticals

European Health Data Space (EHDS), EMA, EudraVigilance, EHIC, EU MDR/IVDR, and cross-border healthcare.

- [HL7 EU Laboratory](https://github.com/hl7-eu/laboratory) - HL7 Europe Laboratory Report FHIR Implementation Guide.
- [HL7 EU Base](https://github.com/hl7-eu/base) - Base profiles and common artefacts for HL7 FHIR in Europe.
- [EGA Download Client](https://github.com/EGA-archive/ega-download-client) - Python client for the European Genome-phenome Archive.
- [Blaze](https://github.com/samply/blaze) - FHIR server with built-in CQL evaluation engine used in European health data spaces.
- [openEHR Archie](https://github.com/openEHR/archie) - Java library implementing openEHR specifications used across European eHealth systems.
- [HL7 EU Imaging](https://github.com/hl7-eu/imaging) - HL7 Europe FHIR Implementation Guide for imaging study reports.
- [HL7 Gravitate Health](https://github.com/hl7-eu/gravitate-health) - EU-funded FHIR Implementation Guide for patient-centric health information.
- [EUDAMED API](https://github.com/openregulatory/eudamed-api) - Unofficial API reference for EUDAMED, the EU medical device database under MDR/IVDR.

## Cybersecurity

NIS2 directive, ENISA, EU Cybersecurity Act, Cyber Resilience Act, and European cyber frameworks.

- [MISP](https://github.com/MISP/MISP) - Open source threat intelligence and sharing platform used by EU-CERTs and endorsed by ENISA.
- [DRAKVUF Sandbox](https://github.com/CERT-Polska/drakvuf-sandbox) - Automated hypervisor-level malware analysis system developed by CERT Polska.
- [OpenCTI](https://github.com/OpenCTI-Platform/opencti) - Open cyber threat intelligence platform used by European CERTs and security agencies.
- [Artemis](https://github.com/CERT-Polska/Artemis) - Modular vulnerability scanner with automatic report generation developed by CERT Polska.
- [AIL Framework](https://github.com/ail-project/ail-framework) - Analysis of Information Leaks framework developed by CIRCL Luxembourg for threat intelligence.
- [Lookyloo](https://github.com/Lookyloo/lookyloo) - Web interface for capturing and analysing website page request trees, developed by CIRCL.
- [Karton](https://github.com/CERT-Polska/karton) - Distributed malware processing framework developed by CERT Polska.
- [IntelMQ](https://github.com/certtools/intelmq) - Security feed processing framework for CERTs, developed by Austrian CERT for European cybersecurity operations.
- [ALTCHA](https://github.com/altcha-org/altcha) - GDPR and EAA compliant, self-hosted CAPTCHA alternative with proof-of-work mechanism.

## Accessibility

European Accessibility Act (EAA), EN 301 549, EU Web Accessibility Directive, and accessibility conformance testing.

- [ACT Rules](https://github.com/act-rules/act-rules.github.io) - Community-maintained accessibility conformance testing rules used to harmonize EU EN 301 549 compliance evaluation.
- [BIK Web Test](https://github.com/BIK-BITV/BIK-Web-Test) - Test procedures for evaluating web accessibility against WCAG 2.1 and EN 301 549 criteria.

## Education and Research

ECTS, Erasmus+, Horizon Europe, CORDIS, OpenAIRE, EOSC, CERN, and European research infrastructure.

- [CERN Open Data Portal](https://github.com/cernopendata/opendata.cern.ch) - Source code for the CERN Open Data portal providing access to particle physics research data.
- [OpenAPC](https://github.com/OpenAPC/openapc-de) - Collect and disseminate information on fee-based Open Access publishing in European research.
- [ELIXIR RDMkit](https://github.com/elixir-europe/rdmkit) - ELIXIR European Research Data Management Toolkit.
- [CSV Validator](https://github.com/digital-preservation/csv-validator) - CSV Validation Tool and API used in European digital preservation projects.
- [Zenodo](https://github.com/zenodo/zenodo) - CERN-hosted open research repository for EU-funded research outputs.
- [InvenioRDM](https://github.com/inveniosoftware/invenio) - CERN-developed digital library framework powering Zenodo and European institutional repositories.
- [ROOT](https://github.com/root-project/root) - CERN framework for data processing, statistical analysis and visualization in particle physics.
- [Geant4](https://github.com/geant4/geant4) - CERN toolkit for simulating the passage of particles through matter.
- [B2SHARE](https://github.com/EUDAT-B2SHARE/b2share) - EUDAT collaborative data infrastructure service for storing and sharing European research data.
- [DSpace](https://github.com/DSpace/DSpace) - Digital asset management system powering institutional repositories across European universities.

## European Utilities

Pan-European utility libraries: IBAN validation, NUTS regions, European phone numbers, postal codes, holidays, and locale tools.

- [Nager.Date](https://github.com/Nager/Nager.Date) - .NET library and REST API for public holidays across 100+ countries including all EU member states.
- [workalendar](https://github.com/workalendar/workalendar) - Python library for holidays and working days computation across European countries.
- [iban4j](https://github.com/arturmkrtchyan/iban4j) - Java library for IBAN and BIC generation and validation.
- [ibantools](https://github.com/Simplify/ibantools) - TypeScript/JavaScript library for IBAN, BBAN, and BIC validation, creation, and extraction.
- [php-iban](https://github.com/globalcitizen/php-iban) - PHP library to generate, parse, validate, error-correct and present IBAN bank account numbers.
- [iban-validation](https://github.com/jschaedl/iban-validation) - PHP library for validating International Bank Account Numbers (IBANs) used in SEPA.
- [IbanNet](https://github.com/skwasjer/IbanNet) - C# .NET IBAN validator, parser, builder, and generator.
- [python-stdnum](https://github.com/arthurdejong/python-stdnum) - Python library to validate tax numbers, VAT IDs, IBANs and other standard numbers used across Europe.
- [schwifty](https://github.com/mdomke/schwifty) - Python library for IBAN and BIC parsing, validation and generation.
- [date-holidays](https://github.com/commenthol/date-holidays) - JavaScript library providing public holiday data for countries worldwide including all EU member states.
- [stdnum-js](https://github.com/koblas/stdnum-js) - JavaScript library to validate European tax numbers, VAT IDs, and other standard identifiers.

## Country-Specific Awesome Lists

Awesome lists focused on individual European countries.

- [awesome-portugal-data](https://github.com/rgllm/awesome-portugal-data) - Open data repositories in Portugal.
- [awesome-italian-public-datasets](https://github.com/italia/awesome-italian-public-datasets) - Open datasets from Italian public administration.
- [awesome-spain](https://github.com/GeiserX/awesome-spain) - Open source software for Spain.
- [awesome-germany](https://github.com/bundestag/awesome-germany) - Fiscally financed German public projects relevant to citizens.

## Contributing

Contributions are welcome. Read the [contributing guidelines](contributing.md) before submitting a pull request.

**Note:** This list focuses on open source software that provides **support specifically for Europe** — its institutions, regulations, standards, and cross-border infrastructure. The scope covers the **EU-27 and EEA** (Norway, Iceland, Liechtenstein). Software specific to a single country belongs in country-specific awesome lists. Software that is global and merely happens to work in Europe is also out of scope.

**Disclaimer:** No projects related to pornography, NSFW content, gambling, religion, partisan politics, or any other controversial topic are accepted. This list aims to be a neutral and useful technical resource for the developer community.
