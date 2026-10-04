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
- `profile_private/` is organizational, not private; never put secrets in this public repository.

## Completion checks

After a substantive change, verify the relevant generated artifacts/workflows and confirm that no stale contradictory copy remains elsewhere in the repository.
