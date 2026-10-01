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
- `Mineo_Raffaele_CV.pdf` - public CV linked from the website

### Internal/profile source material
Editable profile sources and supporting records are kept in `profile_private/`, using the common `Mineo_Raffaele_` prefix:
- `Mineo_Raffaele_CV.tex`
- `Mineo_Raffaele_FotoColorata.webp`
- `Mineo_Raffaele_FotoNeutra.jpg`
- `Mineo_Raffaele_RaccoltaAttivita.txt`
- `Mineo_Raffaele_FirmaEmail.txt`
- `Mineo_Raffaele_ProfiliRicercatore.txt`
- `Mineo_Raffaele_BioBreve.txt`
- `Mineo_Raffaele_BioLunga.txt`
- `Mineo_Raffaele_PublicationsList.docx`
- `Mineo_Raffaele_PublicationsMetadata.xlsx`
- `Mineo_Raffaele_ProfileSync.md`

The CV PDF is rebuilt automatically from `profile_private/Mineo_Raffaele_CV.tex` and written to `Mineo_Raffaele_CV.pdf`.

`profile_private/` is an organizational boundary only. The repository is public, so it must not contain secrets or genuinely private credentials.
