# Raffaele Mineo academic website

Personal academic website for Dr. Eng. Raffaele Mineo.

## Repository layout

The repository uses a single working branch: `main`.

### Website-facing files
- `index.html` - page structure
- `profile-data.js` - website content
- `styles.css` - styles
- `script.js` - rendering and publication filters
- `assets/raffaele-mineo.webp` - website portrait
- `cv/Raffaele_Mineo_Academic_CV.pdf` - public CV linked from the website

### Internal/profile source material
All editable profile sources and supporting records are kept under `profile_private/`:
- `profile_private/cv/Raffaele_Mineo_Academic_CV.tex` - LaTeX CV source
- `profile_private/photos/` - profile-photo masters
- `profile_private/RaccoltaAttivita.txt`
- `profile_private/FirmaEmail.txt`
- `profile_private/ProfiliRicercatore.txt`
- `profile_private/BioBreve.txt`
- `profile_private/BioLunga.txt`
- `profile_private/Mineo_R_publicationsList.docx`
- `profile_private/Mineo_R_publicationsMetadata.xlsx`
- `profile_private/PROFILE_SYNC.md` - synchronization rules

The CV PDF is rebuilt automatically from the LaTeX source and written to `cv/Raffaele_Mineo_Academic_CV.pdf`.

`profile_private/` is an organizational boundary only. The repository is public, so it must not contain secrets or genuinely private credentials.
