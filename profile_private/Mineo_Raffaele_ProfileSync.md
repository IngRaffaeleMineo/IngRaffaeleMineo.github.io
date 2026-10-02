# Profile synchronization rules

This directory stores working profile material and source files separately from the website-facing files.

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
- `main:profile_private/Mineo_Raffaele_PublicationsList.docx`
- `main:profile_private/Mineo_Raffaele_PublicationsMetadata.xlsx`
- `main:profile_private/Mineo_Raffaele_ColorPhoto.webp`
- `main:profile_private/Mineo_Raffaele_NeutralPhoto.jpg`

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
6. Keep joint-first authorship and other authorship notes consistent across every representation.
7. Update ShortBio/LongBio only when the new output materially changes the research profile or selected achievements.
8. Do not expose drafts, pending manuscripts or speculative future outputs unless explicitly requested.

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
