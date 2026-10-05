# Profile synchronization rules

This directory stores working profile material and source files separately from the website-facing files.

## Mandatory bootstrap for a new chat or agent

Before modifying this repository, treat the repository itself as the persistent source of context. Do not rely on memory from a previous conversation.

1. Work only on the `main` branch.
2. Read `AGENTS.md`, `README.md` and this file before making changes.
3. Inspect the current versions of `profile-data.js`, `Mineo_Raffaele_CV.tex`, `Mineo_Raffaele_PublicationsMetadata.xlsx`, `Mineo_Raffaele_PublicationsList.docx`, and the relevant support files before editing them.
4. Never assume a title, role, publication, award, venue name, date or status from a user message is already in its official form; verify it as specified below.
5. Preserve all synchronization, naming, visual-style and confirmation rules documented here.
6. If repository state and a user instruction conflict, the newest explicit user instruction wins; then update this file when the instruction establishes a durable rule.

## Files that must stay synchronized

Whenever a professional or scientific profile item changes, review and update all relevant files:

- `main:profile-data.js`
- `main:profile_private/Mineo_Raffaele_CV.tex`
- `main:Mineo_Raffaele_CV.pdf` through the GitHub Actions build
- `main:profile_private/Mineo_Raffaele_AcademicActivities.txt`
- `main:profile_private/Mineo_Raffaele_EmailSignature.docx`
- `main:profile_private/Mineo_Raffaele_ResearcherProfiles.txt`
- `main:profile_private/Mineo_Raffaele_ShortBio.txt`
- `main:profile_private/Mineo_Raffaele_LongBio.txt`
- `main:profile_private/Mineo_Raffaele_CompleteBio.txt`
- `main:profile_private/Mineo_Raffaele_PublicationsList.docx`
- `main:profile_private/Mineo_Raffaele_PublicationsMetadata.xlsx`
- `main:profile_private/Mineo_Raffaele_ColorPhoto.webp`
- `main:profile_private/Mineo_Raffaele_NeutralPhoto.jpg`
- `main:profile_private/publications/` - PDF/ZIP publication archive
- `main:profile_private/Mineo_Raffaele_PublicationFiles.md` - canonical publication-to-file manifest

## Complete Bio maintenance

- `Mineo_Raffaele_CompleteBio.txt` is the exhaustive maintained biographical profile. Unlike ShortBio and LongBio, it must be reviewed and updated whenever any current role, education item, research line, collaboration, patent, publication/output, academic-service role, reviewing venue, award, teaching role, membership, qualification, language, technical competency or researcher-profile link changes. It must preserve the complete current lists rather than selectively summarizing them.

## Verification rules

1. Independently verify every new or corrected publication before adding it. User-provided citation text, links or metadata are leads, not the bibliographic source of truth. Check the official publisher, proceedings, DOI/Crossref, conference or institutional record for the exact title, full author order, publication year, venue or book/proceedings title, pages or article number, DOI/ISBN when available, output type and publication status.
2. When an event year differs from the final publication year, preserve both explicitly rather than conflating them. The bibliographic year must follow the final published record.
3. Verify the official wording of journals, conferences, workshops, committees, grants, awards, volunteering programs and formal roles using primary or institutional sources before publishing a change.
4. Do not turn an informal description into an official title without verification.
5. Remove failed, withdrawn, obsolete or explicitly excluded activities from all public profile surfaces.
6. Keep publication titles exactly aligned with the publisher/proceedings record whenever possible.
7. Keep the CV "Last updated" date current after substantive changes.
8. For every new, corrected or removed publication, update the website publication data, the CV publication section, the publication DOCX and XLSX, and any affected bios in the same synchronization pass.
9. Treat `Mineo_Raffaele_PublicationsMetadata.xlsx` and `Mineo_Raffaele_PublicationsList.docx` as the canonical publication support files in `profile_private`.
10. Every publication must have exactly one primary research topic, using the stable taxonomy below:
   - Cardiovascular AI and Computational Physiology
   - Multimodal Sensing and Inclusive Healthcare
   - Neurocognitive and Brain Signal AI
   - Adaptive, Efficient and Edge AI
   - Scientific and Industrial Intelligent Systems
   - Research Synthesis and Scholarly Outputs
11. When a new publication is added, assign it to an existing topic only if the scientific fit is clear. If none of the existing topics is appropriate, ask Raffaele before creating a new research topic. Never create or use a generic "Other" or "Miscellaneous" topic without explicit approval.
12. Keep the same topic assignment synchronized across `main:profile-data.js`, the CV publication section, `Mineo_Raffaele_PublicationsMetadata.xlsx` and `Mineo_Raffaele_PublicationsList.docx`.

## Publication synchronization workflow

Whenever a publication or scholarly output is added, corrected or removed:

1. Verify the official title, author order, venue, year, DOI/URL and publication status against the publisher, proceedings, DOI record or another primary source.
2. Update `main:profile-data.js` and assign exactly one research-topic key from the public publication taxonomy.
3. Update `main:profile_private/Mineo_Raffaele_CV.tex`; the PDF is then rebuilt by GitHub Actions.
4. Update `main:profile_private/Mineo_Raffaele_PublicationsList.docx`.
5. Update `main:profile_private/Mineo_Raffaele_PublicationsMetadata.xlsx`.
   Preserve the existing publication-metadata worksheet styling: data rows use a fixed 15 pt height and alternating green row fills, continuing the established parity pattern. New publication rows must match the surrounding font, alignment, wrapping and table formatting; never allow a newly appended row to auto-expand because of long BibTeX or abstract content.
6. Reconcile `main:profile_private/publications/` against the canonical publication masters and `Mineo_Raffaele_PublicationFiles.md`.
   - When the user asks to add a publication and does not provide the full-text file, proactively look for a legitimate downloadable copy from the publisher, official proceedings, an institutional/author repository, Zenodo or another reliable public source.
   - Store the verified PDF in the archive; use ZIP for VolUnD.
   - If no legitimate/reliable downloadable copy can be found, tell Raffaele explicitly which file is missing and ask him to provide it. Never silently omit the artifact and never use dubious download sources.
   - If the user supplies the file, prefer that supplied copy after confirming it corresponds to the verified publication record.
7. Keep joint-first authorship and other authorship notes consistent across every representation.
8. Update ShortBio/LongBio only when the new output materially changes the research profile or selected achievements.
9. Do not expose drafts, pending manuscripts or speculative future outputs unless explicitly requested.

The DOCX and XLSX are persistent publication masters and must never be treated as disposable uploads.

## Style rules

- Use direct factual prose.
- Avoid template-like or promotional language.
- Do not use the centered-dot separator.
- Use normal hyphens or ordinary punctuation where a separator is needed.
- Use "Dr. Eng. Raffaele Mineo" in personal presentation contexts, but use "Raffaele Mineo" in publication author lists and bibliographic records.
- Do not use collapsible, accordion, modal, or otherwise hidden containers for profile content. All substantive website content must be visible on page load.
- Keep the motto as: "My Life is The Research, and I am truly lucky to be able to live it to the fullest" 🙃
- The motto text may be italic, but the emoji must remain upright.
- Display the public email as raffaele.mineo[at]phd.unict.it while keeping the real mailto address.

## Portraits

- Website: use the color portrait.
- CV: use the neutral portrait.
- Keep the website image optimized for fast loading without visible softness at the displayed size.
- Keep the CV image at print-suitable resolution for the header photograph.

## Repository layout

All maintained profile material lives on the single `main` branch. Public website files stay at the repository root, while editable/source materials live under `profile_private/`. This directory is organizational only, not a privacy boundary: the repository is public, so do not store passwords, private identifiers or secrets here.


## Email signature maintenance

- `Mineo_Raffaele_EmailSignature.docx` is the canonical formatted email signature.
- `Mineo_Raffaele_EmailSignatureGenerator.py` is the reproducible source used to regenerate the DOCX.
- Review the signature whenever there is a potentially important change to current affiliation, academic title, editorial leadership, area-chair roles, website/contact information, or another role that may materially improve the signature.
- Email signature changes require explicit confirmation from Raffaele before modifying the DOCX, even when the underlying profile information has already been verified and synchronized elsewhere.
- Minor reviewer assignments, one-off volunteering activities, individual publications, and similar additions should not be inserted into the email signature unless explicitly requested.
- Email signature separator: use one paragraph containing exactly three ASCII hyphens (`---`), with 6 pt paragraph spacing before and 6 pt after. Use paragraph spacing rather than blank paragraphs, and keep it as text rather than a graphical rule or border.
- Preserve the remaining formatting, line structure, hyperlink, motto italics, and upright emoji.


## Publication metadata spreadsheet formatting

- `Mineo_Raffaele_PublicationsMetadata.xlsx` must keep its publication records inside the structured Excel Table named `Tabella1`.
- `Tabella1` must cover all eleven publication columns from A through K, including `Research Topic` and `Topic Key`, and must expand when a new publication is added.
- Preserve the existing Excel table style `TableStyleMedium14` with banded rows enabled. Do not simulate the alternating colors by manually coloring isolated rows.
- Keep publication data rows at a fixed height of 15 points, with wrapping and column widths consistent with the existing table.
- A new publication must be appended as a row of `Tabella1`, never written immediately below or outside the structured table.
- After every XLSX edit, visually verify the header and at least the surrounding rows of any inserted record to confirm row height and banded-row alternation.


## Publication file archive

- Archival copies of publication files are stored under `profile_private/publications/`.
- Use PDF for papers, chapters, proceedings, patents and reports when a PDF copy is available. Keep VolUnD as a ZIP archive.
- File names must begin with `YYYY_` or `YYYY-MM_`, followed by a concise publication/venue identifier and title, using underscores instead of spaces where practical.
- The date prefix describes the archived document/file chronology when that is materially different from the final bibliographic year; bibliographic metadata in the website, CV, DOCX and XLSX must still follow the verified final publication record.
- When a publication is added, removed or corrected, review the corresponding PDF/ZIP archive entry in the same synchronization pass.
- The archive is repository support material and is not linked from the public website unless explicitly requested.
- The publication archive must be checked against the canonical publication masters after every add/remove operation; a publication deleted from the canonical record (for example a non-existent entry) must also be removed from archive expectations.


## Publication source files

- Store the available publication/output source files under `profile_private/publications/`.
- Use the filename pattern `YYYY_Name.ext` or `YYYY-MM_Name.ext`; use zero-padded months.
- Keep filenames ASCII-safe: use ordinary hyphens instead of typographic hyphens and avoid encoded Unicode markers in filenames.
- Store publications as PDF whenever a PDF is available. Keep VolUnD as a ZIP archive.
- Patent/source-output files supplied together with the publication archive may be stored in the same directory, but they remain typed as patents/technical outputs in the metadata rather than publications.
- Whenever a publication is added, corrected or removed, review the publication-files directory in the same synchronization pass. Remove files for records explicitly removed from the profile and add the corresponding file when available.
- The publication-files directory, website record, CV, DOCX list and XLSX metadata must refer to the same canonical set. Do not invent a publication merely because a similarly named file exists.


## Explicit exclusions and corrections

- Do not add or restore a publication titled "Memory-Augmented Prompt Tuning for Self-Supervised Continual Learning in Medical Imaging" or an output referred to as "MAPT". Raffaele explicitly confirmed that this publication does not exist.
- An excluded or non-existent record must be absent from the website, CV, DOCX publication list, XLSX metadata, publication-file manifest and PDF/ZIP archive expectations.


## Repository self-sufficiency

The repository must contain enough instructions and maintained source material for a new ChatGPT conversation or another agent to continue profile maintenance without access to earlier chats.

- `AGENTS.md` is the entry-point instruction file.
- This file is the detailed operational specification.
- `README.md` explains repository architecture for human readers.
- `profile-data.js` is the public website data source.
- `Mineo_Raffaele_PublicationsMetadata.xlsx` and `Mineo_Raffaele_PublicationsList.docx` are the persistent publication masters.
- `Mineo_Raffaele_PublicationFiles.md` maps every canonical output to its archived PDF/ZIP.
- Durable user preferences or workflow rules must be written here when introduced, rather than being left only in chat history.


## Publication archive naming invariant

The preferred archive filename pattern is `YYYY_Venue_Short_Title.ext` or `YYYY-MM_Venue_Short_Title.ext` when the month is known and useful. Use zero-padded months and ASCII-safe ordinary hyphens. The filename date may reflect the event/document chronology used by the supplied archive even when the verified final bibliographic year differs; the bibliographic year in the maintained metadata must remain the verified publication year.


## Website translation

- Keep website translation optional and isolated in `translate.js`. The canonical/source language remains English; the Google Website Translator may translate the rendered page on demand, but its external availability must never be required for navigation, profile rendering, SEO metadata, or core site operation. Preserve a graceful fallback if Google's widget cannot load.

## Search-engine discoverability

- Keep the public homepage directly indexable: do not add `noindex`, authentication, crawler blocks or JavaScript-only substantive profile content.
- `index.html` must contain a static, crawlable representation of the substantive profile content already present in `profile-data.js`; JavaScript may enhance and filter that content but must not be the only way a crawler can read it.
- Keep the canonical URL, Open Graph/Twitter metadata and Schema.org JSON-LD aligned with the current profile. The homepage is modeled as a `ProfilePage` whose `mainEntity` is Raffaele Mineo.
- Keep `robots.txt` permissive and point it to `sitemap.xml`.
- Keep `sitemap.xml` limited to canonical URLs on this host and update `lastmod` after substantive website or CV changes.
- Preserve the IndexNow key file and `.github/workflows/indexnow.yml`; the key is a public ownership-verification token, not a credential or secret.
- Do not add unverifiable search-engine verification tokens. Google Search Console, Bing Webmaster Tools or other ownership tokens may be added only when Raffaele supplies or authorizes the actual verification value.
- Avoid keyword stuffing, hidden SEO text, doorway pages, duplicate profile pages and fabricated structured-data claims.


## Current role and section routing

- Current public role wording: `Research Fellow in Artificial Intelligence`. Keep the website profile data, Schema.org person data, CV and biographies aligned with this wording unless Raffaele explicitly changes it.
- Keep the main website sections exposed in the top navigation.
- Human-readable section routes are navigation aliases for the single-page site: `/about`, `/research`, `/selected-work`, `/patents`, `/publications`, `/service`, `/recognition`, `/experience`, `/education`, `/network`, `/background` and `/contact`.
- Menu navigation must update the browser URL to the corresponding section route and smoothly scroll to that section. Direct visits to those route paths must be recovered by `404.html` and forwarded to the matching homepage section.
- Section-route aliases are usability routes, not separate canonical documents. Keep the homepage as the canonical indexable profile page and do not add the aliases to `sitemap.xml`.
- Preserve `googlef3c96fd9bbcbecc2.html` in the repository root as the Google Search Console HTML-file ownership verification artifact; do not rename, edit or remove it while the Search Console property is in use.
- Keep the top navigation, active underline and browser pathname synchronized while the user scrolls: the currently viewed section must receive `aria-current="page"`, and the browser path must be updated with `history.replaceState` so passive scrolling does not create extra browser-history entries.
- Menu clicks and route navigation are owned by the standalone `navigation.js`, independently of profile rendering. They must use a custom frame-by-frame eased scroll with visible acceleration at the start and deceleration at the end, explicit sticky-header offset, manual history scroll restoration, and cancellation on deliberate user scrolling.
