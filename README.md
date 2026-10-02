# Raffaele Mineo Academic Website

Source repository for the academic website of Dr. Eng. Raffaele Mineo, published with GitHub Pages.

## Architecture

The website is a static site served directly from the `main` branch. No application framework or JavaScript build pipeline is required.

The main website content is stored in structured form in `profile-data.js` and rendered by `script.js`. Page structure and styling are defined in `index.html` and `styles.css`.

## Repository structure

### Public website files

- `index.html` - page structure and metadata
- `profile-data.js` - structured academic profile, research topics, publications, service, memberships and collaborations
- `script.js` - client-side rendering, filtering and interface behavior
- `styles.css` - responsive visual styling
- `favicon.svg` - site favicon
- `assets/raffaele-mineo.webp` - portrait used on the website
- `Mineo_Raffaele_CV.pdf` - public academic CV linked from the website

### Profile source material

Supporting source files are stored under `profile_private/`. The directory name separates editable source material from website-facing files; it is not an access-control boundary because the repository is public.

Files use the common `Mineo_Raffaele_` prefix:

- `Mineo_Raffaele_CV.tex` - LaTeX source of the academic CV
- `Mineo_Raffaele_ColorPhoto.webp` - color portrait master
- `Mineo_Raffaele_NeutralPhoto.jpg` - neutral portrait used by the CV
- `Mineo_Raffaele_AcademicActivities.txt` - academic service, reviewing, mentoring, awards and activities
- `Mineo_Raffaele_EmailSignature.docx` - formatted academic email signature
- `Mineo_Raffaele_EmailSignatureGenerator.py` - generator for the email-signature DOCX
- `Mineo_Raffaele_ResearcherProfiles.txt` - researcher identifiers and profile links
- `Mineo_Raffaele_ShortBio.txt` - short biography in Italian and English
- `Mineo_Raffaele_LongBio.txt` - extended biography in Italian and English
- `Mineo_Raffaele_PublicationsList.docx` - maintained publication list
- `Mineo_Raffaele_PublicationsMetadata.xlsx` - publication metadata and research-topic taxonomy
- `Mineo_Raffaele_ProfileSync.md` - synchronization rules for all profile artifacts

## Publication organization

Publications are grouped by primary research topic rather than shown only as a chronological list. The current taxonomy is maintained consistently across the website, CV, DOCX publication list and XLSX metadata file.

New publications should be assigned to an existing topic only when the scientific fit is clear. If no current topic is appropriate, the taxonomy should be extended explicitly rather than using a generic miscellaneous category.

## Generated profile artifacts

The academic CV and formatted email signature are generated automatically by GitHub Actions.

The workflow is triggered when one of the following changes:

- `profile_private/Mineo_Raffaele_CV.tex`
- `profile_private/Mineo_Raffaele_NeutralPhoto.jpg`
- the CV workflow itself

The workflow:

1. installs XeLaTeX and the required TeX packages;
2. compiles `Mineo_Raffaele_CV.tex` twice;
3. writes the generated PDF to `Mineo_Raffaele_CV.pdf` in the repository root;
4. commits the regenerated PDF when its contents change.

## Profile synchronization

`profile_private/Mineo_Raffaele_ProfileSync.md` defines the synchronization policy for profile data.

Changes to publications, roles, affiliations, awards, reviewer activity, research topics or other profile information should be propagated to all affected artifacts. New publications must be independently verified against primary bibliographic sources before they are added. User-supplied citations are treated as leads rather than as the source of truth; the maintained record should use the publisher, proceedings, DOI/Crossref or institutional source for the exact title, author order, year, venue, pages or article number and publication status. When an event year differs from the final publication year, both should be preserved explicitly. Official names of journals, conferences, workshops, grants, committees and formal roles should also be verified against primary or institutional sources before publication.

## Deployment

GitHub Pages publishes the static website from the `main` branch. Changes to website files are therefore deployed without a separate application build step.

## Repository visibility

This repository is public. Files under `profile_private/` are separated for organization and maintenance only and must not contain passwords, credentials, private identifiers or other confidential information.


### Publication file archive

Archival copies of publications are stored in `profile_private/publications/`. Papers, book chapters, proceedings, patents and project reports are retained as PDF files when available; the VolUnD software release is retained as a ZIP archive.

Archive file names use a chronological prefix in the form `YYYY_` or `YYYY-MM_`, followed by a concise venue/publication identifier and title. These files support profile maintenance and are not linked from the public website.
