# Repository agent instructions

This repository is the persistent source of truth for the academic profile of Dr. Eng. Raffaele Mineo.

## Required startup

Before any modification:

1. Work on `main` only.
2. Read `README.md`.
3. Read `profile_private/Mineo_Raffaele_ProfileSync.md` in full.
4. Inspect the current files affected by the requested change; never reconstruct repository state from memory.
5. Apply the user's newest explicit instruction when it conflicts with older repository guidance, then update the synchronization instructions if the new rule is durable.

The detailed rules in `profile_private/Mineo_Raffaele_ProfileSync.md` are mandatory.

## Core invariants

- Keep website, CV, publication masters, bios, academic activities and other affected profile artifacts synchronized.
- Independently verify official names and bibliographic facts using primary or institutional sources before publishing changes.
- For every new publication, verify its metadata, assign exactly one established research topic when the fit is clear, update all publication representations, and archive the full-text PDF when available.
- If the user did not supply a publication PDF, proactively seek a legitimate copy from an official/reliable source. If none can be obtained, explicitly ask the user to provide it.
- Do not create a new research topic unless no existing topic fits; ask Raffaele before adding one.
- Never restore MAPT / "Memory-Augmented Prompt Tuning for Self-Supervised Continual Learning in Medical Imaging"; the user confirmed it does not exist.
- Publication artifacts belong in `profile_private/publications/` and are tracked by `profile_private/Mineo_Raffaele_PublicationFiles.md`.
- `profile_private/Mineo_Raffaele_PublicationsIntegrity.py` and the `Validate publication masters` GitHub Action enforce the publication-master invariants; do not bypass them.
- All substantive website content must be visible on page load; do not introduce collapsible profile sections.
- Avoid template-like/LLM-like copy and the centered-dot separator.
- Email-signature changes require explicit user confirmation before editing the signature DOCX.
- Maintain **two** Outlook-compatible email signature DOCX artifacts (full for new messages; short for replies/forwards) from the same generator. They use Segoe UI; only the 10 pt name is bold, remaining text 9 pt regular, and links are #365F7D without underline. Preserve direct copy/paste behavior using simple Word soft line breaks, no graphics or decorative separators except the explicitly required first-line `---` prefix, and validate both. Full signature role order is fixed by category: `Organizing Committee` > `Associate Editor` > `Guest Editor` (Lead ahead of regular) > `Area Chair`; sort by descending ranking only *within* each category. See `profile_private/Mineo_Raffaele_ProfileSync.md` for full formatting, omission, and conference GII-GRIN-SCIE/ICORE and journal SCImago rules.
- Only the full email signature includes the separate `Italian National PhD in Artificial Intelligence - Health and Life Sciences` line. The short signature **omits** that line, while preserving `Eng. Ph.D.` next to the name, the Research Fellow affiliation, both contact hyperlinks, and the motto with 🙃.
- Both email signatures must start with **exactly `---` on its own visual line**, formatted in regular Segoe UI 9 pt #606060, followed by one simple Word soft line break before the name. No extra blank paragraph, 10 pt name style or bold on the hyphens; no additional separator elsewhere.
- The exact personal motto `"My Life is The Research, and I am truly lucky to be able to live it to the fullest" 🙃` must appear in **both** the full and short email signatures, after contacts. Keep the motto in discreet 9 pt italic Segoe UI with an upright emoji. This is a specific, owner-confirmed exception to otherwise regular signature text; do not remove it under general minimalism/compactness rules.
- `profile_private/` is organizational, not private; never put secrets in this public repository.

## Completion checks

After a substantive change, verify the relevant generated artifacts/workflows and confirm that no stale contradictory copy remains elsewhere in the repository.
