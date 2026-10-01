# Profile synchronization rules

This directory stores working profile material and source files separately from the website-facing files.

## Files that must stay synchronized

Whenever a professional or scientific profile item changes, review and update all relevant files:

- `main:profile-data.js`
- `main:profile_private/cv/Raffaele_Mineo_Academic_CV.tex`
- `main:cv/Raffaele_Mineo_Academic_CV.pdf` through the GitHub Actions build
- `main:profile_private/RaccoltaAttivita.txt`
- `main:profile_private/FirmaEmail.txt`
- `main:profile_private/ProfiliRicercatore.txt`
- `main:profile_private/BioBreve.txt`
- `main:profile_private/BioLunga.txt`
- `main:profile_private/Mineo_R_publicationsList.docx`
- `main:profile_private/Mineo_R_publicationsMetadata.xlsx`
- `main:profile_private/photos/FotoTessera2024_colorato_HQ.webp`
- `main:profile_private/photos/FotoTessera2024_neutro_HQ.jpg`

## Verification rules

1. Verify the official wording of journals, conferences, workshops, committees, grants, awards, volunteering programs and formal roles using primary or institutional sources before publishing a change.
2. Do not turn an informal description into an official title without verification.
3. Remove failed, withdrawn, obsolete or explicitly excluded activities from all public profile surfaces.
4. Keep publication titles exactly aligned with the publisher/proceedings record whenever possible.
5. Keep the CV "Last updated" date current after substantive changes.
6. For every new, corrected or removed publication, update the website publication data, the CV publication section, the publication DOCX and XLSX, and any affected bios in the same synchronization pass.
7. Treat `Mineo_R_publicationsMetadata.xlsx` and `Mineo_R_publicationsList.docx` as the canonical publication support files in `profile_private`.
8. Every publication must have exactly one primary research topic, using the stable taxonomy below:
   - Cardiovascular AI and Computational Physiology
   - Multimodal Sensing and Inclusive Healthcare
   - Neurocognitive and Brain Signal AI
   - Adaptive, Efficient and Edge AI
   - Scientific and Industrial Intelligent Systems
   - Research Synthesis and Scholarly Outputs
9. When a new publication is added, assign it to an existing topic only if the scientific fit is clear. If none of the existing topics is appropriate, ask Raffaele before creating a new research topic. Never create or use a generic "Other" or "Miscellaneous" topic without explicit approval.
10. Keep the same topic assignment synchronized across `main:profile-data.js`, the CV publication section, `Mineo_R_publicationsMetadata.xlsx` and `Mineo_R_publicationsList.docx`.

## Publication synchronization workflow

Whenever a publication or scholarly output is added, corrected or removed:

1. Verify the official title, author order, venue, year, DOI/URL and publication status against the publisher, proceedings, DOI record or another primary source.
2. Update `main:profile-data.js` and assign exactly one research-topic key from the public publication taxonomy.
3. Update `main:profile_private/cv/Raffaele_Mineo_Academic_CV.tex`; the PDF is then rebuilt by GitHub Actions.
4. Update `main:profile_private/Mineo_R_publicationsList.docx`.
5. Update `main:profile_private/Mineo_R_publicationsMetadata.xlsx`.
6. Keep joint-first authorship and other authorship notes consistent across every representation.
7. Update BioBreve/BioLunga only when the new output materially changes the research profile or selected achievements.
8. Do not expose drafts, pending manuscripts or speculative future outputs unless explicitly requested.

The DOCX and XLSX are persistent publication masters and must never be treated as disposable uploads.

## Style rules

- Use direct factual prose.
- Avoid template-like or promotional language.
- Do not use the centered-dot separator.
- Use normal hyphens or ordinary punctuation where a separator is needed.
- Use "Dr. Eng. Raffaele Mineo" in personal presentation contexts, but use "Raffaele Mineo" in publication author lists and bibliographic records.
- Keep all expandable website information panels open by default.
- Keep the motto as: "My Life is The Research, and I am truly lucky to be able to live it to the fullest" 🙃
- The motto text may be italic, but the emoji must remain upright.
- Display the public email as raffaele.mineo[at]phd.unict.it while keeping the real mailto address.

## Portraits

- Website: use the color portrait.
- CV: use the neutral portrait.
- Keep the website image optimized for fast loading without visible softness at the displayed size.
- Keep the CV image at print-suitable resolution for the header photograph.

## Repository layout

All maintained profile material lives on the single `main` branch. Public website files stay at the repository root, while editable/source materials live under `profile_private/`. This directory is organizational only, not a privacy boundaryy: the repository is public, so do not store passwords, private identifiers or secrets here.
