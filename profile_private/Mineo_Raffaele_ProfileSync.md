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
- `main:profile_private/Mineo_Raffaele_EmailSignature.docx` — full signature for new email messages
- `main:profile_private/Mineo_Raffaele_EmailSignature_Short.docx` — short signature for replies/forwards
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

## Chronological ordering and role naming

- Every year-bearing list must use a declared, consistent chronology rather than adding new items at arbitrary positions.
- Academic service (Area / program leadership; editorial; workshops, challenges and special sessions; journal/conference/workshop reviewing; volunteering and mentoring) and memberships/certifications: chronological ascending by start year, with stable order for equal years and undated entries last.
- Professional experience, education, research trajectory and the publications within each research topic: reverse chronological (newest start or publication year first). Keep the complete biographical publication inventory reverse chronological and renumber sequentially.
- Narrative research history can remain chronological from earliest to latest. Selection lists and unordered technical-skills categories do not require artificial year sorting.
- For the same role across different conference editions, preserve exactly the same role wording. Both IEEE ISBI 2026 and IEEE ISBI 2027 must be written `Organizing Committee - IEEE ISBI YYYY, Associate to Technical Program Chairs` in website data, static HTML, CV and CompleteBio. In AcademicActivities use `IEEE International Symposium on Biomedical Imaging (ISBI) YYYY - Organizing Committee, Associate to Technical Program Chairs`.
- Preserve the ISBI 2027 Organizing Committee appointment (Associate to Technical Program Chairs) in the full email signature. The compact display uses `Organizing Committee - IEEE ISBI 2027, Associate to Technical Program Chairs`; the full official name stays in the website/CV/AcademicActivities. Do not add EEAI Session Chair to either signature.
- Any relevant addition must be inserted in chronological position and checked across `profile-data.js`, `index.html`, CV, academic-activities register, CompleteBio, and other affected files; do not simply append it at the end.
- When several roles share a year, keep their relative order consistent between website profile data, the static HTML service section, CV, canonical CompleteBio and AcademicActivities; do not independently reorder equal-year roles in different files.

## Conference-service role synchronization

- When new conference-service or leadership roles are added, synchronize the public `profile-data.js` service list, its static crawlable copy in `index.html`, the CV source, AcademicActivities and CompleteBio, and assess ShortBio/LongBio relevance. Keep annual editions as distinct appointments. Do not alter the email signature unless the user explicitly requests it.

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
- Do not use collapsible, accordion, modal, or otherwise hidden containers for profile content, except for the Publications section progressive-disclosure behavior explicitly defined below. All other substantive website content must be visible on page load.
- Keep the motto as: "My Life is The Research, and I am truly lucky to be able to live it to the fullest" 🙃
- The exact motto, including its final 🙃 emoji, is **mandatory in both email signatures** (full and short) as an expression of the owner’s personality. Its wording, capitalization and emoji must not be altered or removed without a new explicit request. The motto text is 9 pt Segoe UI, subtle italic, #606060; the emoji is 9 pt, upright, with no bold. Keep it on the last line using a soft line break, without adding any extra separator between contact details and motto or a blank paragraph. The only permitted signature prefix is the mandatory first-line `---`.
- The motto text may be italic, but the emoji must remain upright.
- Display the public email as raffaele.mineo[at]phd.unict.it while keeping the real mailto address.

## Portraits

- Website: use the color portrait.
- CV: use the neutral portrait.
- Keep the website image optimized for fast loading without visible softness at the displayed size.
- Keep the CV image at print-suitable resolution for the header photograph.

## Repository layout

All maintained profile material lives on the single `main` branch. Public website files stay at the repository root, while editable/source materials live under `profile_private/`. This directory is organizational only, not a privacy boundary: the repository is public, so do not store passwords, private identifiers or secrets here.


## Generated artifact workflow ownership

- Keep generated-artifact workflows separated by ownership: `.github/workflows/build-assets.yml` builds and commits only `Mineo_Raffaele_CV.pdf`, while `.github/workflows/build-email-signature.yml` builds and commits **both** `profile_private/Mineo_Raffaele_EmailSignature.docx` and `profile_private/Mineo_Raffaele_EmailSignature_Short.docx`. Do not have multiple workflows writing the same binary artifact, to avoid rebase conflicts.

## Scientific standing for signature and profile ordering (mandatory)

- **Source hierarchy for conferences:** prefer the latest official `GII-GRIN-SCIE (GGS)` ranking or its successor `ICORE` (joint CORE/GII/GRIN/SCIE) using the edition most recently published. As of October 2026 this is ICORE 2026 (https://portal.core.edu.au/conf-ranks/), while standalone GGS editions include 2021, 2018, 2017 and 2015 (https://scie.lcc.uma.es/). Check exact venue names and acronyms; do not silently mix up ICASSP, FG, ISBI, IJCNN and MICCAI.
- **Historical fallback:** if the latest edition has no comparable letter rating (including statuses such as `Multiconference`), inspect the previous official edition, then earlier editions, newest first, and record the edition **and** source alongside the retained rating. An older rating is not a current rating. If no ranked result is found in any supported edition, classify that conference as `unranked/unknown` and give it lowest conference-rating priority; do **not** infer a rank from name recognition or other statistics.
- **Score ordering for conferences:** for ICORE use `A* > A > B > C > unranked`. Historical GGS uses `A++ > A+ > A > A- > B > B- > unranked`. Rankings from different schemes/years are **not** automatically interchangeable: preserve their exact native grade and source/year, explicitly note differences in provenance, and use the venue-specific verified history and owner's tie-break preferences when needed.
- **Journal editorial roles (within role group):** take quartiles from the latest complete SCImago/SJR edition (https://www.scimagojr.com/), falling back to previous years only when the journal has no current values. Sort journals by `Q1 > Q2 > Q3 > Q4 > unranked`; for equal quartiles use SJR in the same edition, then journal placement in a relevant subject category. Never confuse `Cognitive Computation` with `Cognitive Computation and Systems`, nor Frontiers in Communication with Frontiers in Medicine. Keep Associate Editor and Guest Editor as *separate* consecutive groups; within Guest Editor list Lead Guest Editors before ordinary Guest Editors, then sort each sublevel by SCImago descending.
- **Signature grouping overrides cross-system prestige:** never compare conference and journal ratings to move an entry across role categories. The email signature must keep contiguous groups in this exact, owner-chosen order: **(1) Organizing Committee; (2) Associate Editor; (3) Guest Editor (Lead Guest Editor before ordinary Guest Editor); (4) Area Chair**. Within every group, sort by importance **descending** using the venue-specific ranking rules below. For Organizing Committee and Area Chair, use GII-GRIN-SCIE / ICORE rating and historical fallbacks; for Associate Editor and Guest Editor use SCImago quartile then SJR. Inside Guest Editor, `Lead Guest Editor > Guest Editor` takes priority, followed by SCImago within each title level. When two entries have identical ratings, use the owner's documented tiebreaker or stable order. No mixing groups, even when one lower group has higher numeric/letter standing.
- **No arbitrary ordering:** within the same rating use verified source year/quality evidence and the owner's documented preference. If still tied, preserve the previous order and mark that the distinction is not ranking-derived. Do not reorder for visual adjacency of IEEE acronyms or by date of appointment.
- Website, CV, AcademicActivities, and CompleteBio **remain chronologically sorted** within their service sections per the chronology rules above. **Only the email signature** uses fixed role-group order first and descending rank within each group. Preserve exact role titles across representations.

**Rank snapshot checked 26 October 2026** (for email-signature ordering):
- MICCAI: `A` in ICORE 2026; https://portal.core.edu.au/conf-ranks/1607/
- IEEE ISBI: `A` only in historical `ERA2010` entry; **not a modern ICORE A**. https://portal.core.edu.au/conf-ranks/694/. Treat as legacy fallback with much lower evidential confidence; recheck GGS history when accessible.
- Springer *Cognitive Computation*: SCImago 2025 `Q1`, SJR `1.197`; https://www.scimagojr.com/ and https://researchcloud.net/journal/1866-9964
- IEEE ICASSP: `Multiconference` in ICORE 2026 (**not** A/B); last graded `B` in CORE 2023; https://portal.core.edu.au/conf-ranks/2042/
- IJCNN: `B` in ICORE 2026; https://portal.core.edu.au/conf-ranks/685/
- IEEE FG: `B` in ICORE 2026; https://portal.core.edu.au/conf-ranks/629/
- *Frontiers in Communication*: SCImago 2025 `Q2`, SJR `0.466`; https://www.scimagojr.com/ and https://www.iit.comillas.edu/publicacion/info_revista/en/1016/Frontiers_in_Communication
- The ICASSP / IJCNN / FG `B` tie is **not resolved by the ranking**: retain the owner's most recent explicit preference `ICASSP > IJCNN > FG` only as a tie-break, until the user changes it.
- Canonical full-signature role order **by contiguous groups**: `Organizing Committee: ISBI 2027` → `Associate Editor: Frontiers in Communication` → `Guest Editor: Lead Guest Editor, Cognitive Computation` → `Area Chair: MICCAI > ICASSP > IJCNN > FG`. These role titles may be condensed to unambiguous conference acronyms, with all four Area Chairs on one line. Keep the Area Chairs without event years and exclude EEAI. Paragraph spacing follows the new full/short typography rules below, not the superseded 6 pt convention.

- **Grouping and ranking are different axes:** fixed group sequence always wins; descending prestige only breaks ties/reorders entries *within* a group. Adding a new role must first assign it to the correct group; update and validate the generator order and its DOCX artifact. There is no global ranking that allows an Area Chair to jump above an Associate Editor in the email signature.

## Email signature maintenance: full and short DOCX (mandatory)

- Maintain **two** canonical generated files from the **same** `Mineo_Raffaele_EmailSignatureGenerator.py`:
  - `Mineo_Raffaele_EmailSignature.docx` — **full** signature for composing a new message, keeping every currently authorized role.
  - `Mineo_Raffaele_EmailSignature_Short.docx` — **short** signature for replies and forwards: opening `---`, name with `Eng. Ph.D.` on the first personal line, Research Fellow/affiliation, essential email/website contacts, and the mandatory personal motto as the last line. **Omit** the separate `Italian National PhD in Artificial Intelligence - Health and Life Sciences` line **from the short signature only**; retain that line unchanged in the full signature and keep `Ph.D.` visible next to the name in both. The short version therefore has five visible lines including the `---` prefix.
- Regenerate **both** on every generator update via `.github/workflows/build-email-signature.yml`, committing both binaries together. Run the non-mutating `Mineo_Raffaele_EmailSignatureValidator.py` after generation; reject workflow results if either signature fails its formatting/content checks.
- **Mandatory three-hyphen opening:** both the full and short DOCX start with a separate **visual line** `---`, made of ordinary ASCII hyphens. It has exactly the same **9 pt Segoe UI, #606060, regular** styling as other non-name text; it is followed by a Word soft line break (`w:br`) and then the name, with no blank paragraph or extra spacing.
- **Typography** for both files: Segoe UI; only `Raffaele Mineo` is bold, **10 pt, #404040**. Honorifics, titles, affiliations, responsibilities, membership, address and every other non-link item are **9 pt, regular, #606060**, except for the **exact personal motto**, which is 9 pt, *italic but not bold*, in #606060; its emoji remains 9 pt and upright. Hyperlinks are **9 pt #365F7D, no underline**, using simple Word external hyperlink relationships to survive Outlook copy/paste.
- **Line layout:** single line spacing (1.0); 0 pt paragraph spacing before/after. Use Word manual line breaks (Shift+Enter / `w:br`) rather than a separate paragraph for every visual line. The full signature can exceptionally separate identity from academic roles using **3–4 pt** after the identity paragraph, without empty paragraphs; the short signature must remain a single paragraph with simple line breaks. Keep no empty lines, borders, logos, visible tables, bright colors, or additional decorations beyond the mandatory `---` prefix and the motto's 🙃 emoji.
- **Full signature role groups:** Organizing Committee → Associate Editor → Guest Editor (Lead before ordinary) → Area Chair → other appointments when the owner authorizes them. Preserve each category as a contiguous block. Within **each** category apply **descending standing** using the official GII-GRIN-SCIE/ICORE ranking with historical fallbacks for conferences and SCImago (Q1..Q4 then SJR) for editorial journal venues. Never globally compare conference and journal rankings to interleave categories. Venue abbreviations may be used to compact the email signature as long as the roles remain unambiguous and full official names are preserved on website/CV/AcademicActivities.
- **Currently approved full roles:** `Organizing Committee - IEEE ISBI 2027, Associate to Technical Program Chairs`; `Associate Editor - Frontiers in Communication`; `Lead Guest Editor - Springer Cognitive Computation`; `Area Chair - MICCAI - IEEE ICASSP - IJCNN - IEEE FG`. Year is omitted for all Area Chair appointments in the **email** signature; their dates are preserved on the public site/CV. **EEAI 2026 Session Chair stays out of both signatures**, although still present in website/CV.
- **Preserve factual data:** academic `Eng. Ph.D.` on the name line in both, the expanded `Italian National PhD in Artificial Intelligence - Health and Life Sciences` **in the full signature only**, IEEE membership (full only), research title, PeRCeiVe.AI Lab, university, DIEEI department (full only), postal address (full only), and institutional contact links. The public profile currently gives `raffaele.mineo@phd.unict.it`; use that verified existing address and `https://ingraffaelemineo.github.io/`. If a contact or title changes, update both signatures and their tests together.
- **Current design:** the first line of **both signatures must be exactly three literal ASCII hyphens (`---`)**, in ordinary Segoe UI **9 pt**, **#606060**, **not bold** and **not italic**. Follow it with a single manual line break (Shift+Enter, not an empty paragraph) and immediately the name/title line. The **original personal motto and 🙃 emoji must also be present in both signatures**. Place them at the end, after contacts, using a soft line break. The motto is the only permitted non-bold italic run; its emoji remains upright. No other decorative separator, logo, icon or graphical element is added.
- When changing the signatures, report explicitly **what was added, removed, and retained**, including any content condensed into acronyms. Review typography, soft breaks, hyperlink relationships, role count, and Outlook paste behavior. A simple Word DOCX cannot guarantee every recipient's Outlook client preserves identical formatting; preserve formatting as far as practical by avoiding Word shapes/tables and nonstandard layout.
- Email-signature changes require explicit owner confirmation before editing the DOCX; the present two-version redesign has been expressly authorized. Later unrequested profile updates must not silently modify either signature.
- The ranking policy in **Scientific standing for signature and profile ordering** remains mandatory within role groups; all other profile/CV chronological ordering rules remain separate.


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

## Website publication presentation

- Keep the Publications section as the final substantive section of the main page, immediately before the footer/contact area, so shorter profile sections are encountered first during ordinary scrolling.
- In the top navigation, keep Publications as the final substantive section link immediately before Contact.
- Group publications by the established research-topic taxonomy. Do not show either an overall publication total (for example `28 items`) or numeric publication-count badges in topic headers. In the interactive browser view, show at most 2 publications per visible topic initially. For `Research Synthesis and Scholarly Outputs`, when exactly 2 matching items exist, show only the first item initially so that a real `Show more` action reveals the second. Hide later items with the explicit `.pub-progressive-hidden` class (`display:none!important`) rather than relying on the native `hidden` attribute. Each topic with additional hidden publications must show a button whose visible label is exactly `Show more`; each click reveals up to 2 additional publications until all matching publications are visible, at which point the button disappears.
- Changing any publication search or filter resets each visible topic to its first 2 matching publications.
- Preserve the complete static publication markup in `index.html` for crawlability and no-JavaScript access even though the enhanced browser interface progressively reveals the list.

## Search-engine discoverability

- Keep the public homepage directly indexable: do not add `noindex`, authentication, crawler blocks or JavaScript-only substantive profile content.
- `index.html` must contain a static, crawlable representation of the substantive profile content already present in `profile-data.js`; JavaScript may enhance and filter that content but must not be the only way a crawler can read it.
- Keep the canonical URL, Open Graph/Twitter metadata and Schema.org JSON-LD aligned with the current profile. The homepage is modeled as a `ProfilePage` whose `mainEntity` is Raffaele Mineo.
- For `ProfilePage.dateModified` in the homepage JSON-LD, always use a complete ISO 8601 date-time with explicit timezone (e.g. `2026-10-06T13:16:21Z`), never a date-only `YYYY-MM-DD` value; base it on the last actual human-edited profile metadata change, not routine rebuilds or purely cosmetic deployments. After changing it, parse the JSON-LD and verify the DateTime.
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
