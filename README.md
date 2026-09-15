# Raffaele Mineo — Academic website

This is a **plain static GitHub Pages site**. There is **no Node.js, npm, Jekyll or local build step for the website**.

## Main files

- `profile-data.js` — structured content: publications, service, memberships, experience, education, patents, etc.
- `index.html` — page wording and section order.
- `styles.css` — colors and visual design.
- `script.js` — rendering and publication-filter behavior.
- `assets/raffaele-mineo.jpg` — profile photograph, also used by the CV source.
- `cv/Raffaele_Mineo_Academic_CV.pdf` — public CV linked from the website.
- `cv/Raffaele_Mineo_Academic_CV.tex` — LaTeX source of the academic CV.

The website deliberately links to the **PDF only**; the `.tex` is kept in the repository as editable source.

## Updating the website

For ordinary content updates, edit `profile-data.js` directly from GitHub.com and commit the change. GitHub Pages serves the updated static site automatically.

When `cv/Raffaele_Mineo_Academic_CV.tex` or the profile photograph changes, the GitHub Actions workflow in `.github/workflows/build-assets.yml` recompiles the PDF automatically with XeLaTeX and commits the regenerated PDF.

## Visual identity

The palette is intentionally restrained and derived from the portrait:
- Deep navy `#0B1F33` — authority and technical confidence.
- Warm amber `#C98C43` — selective accent derived from the portrait background.
- Warm off-white `#F7F4EE` — softer academic/editorial background.
- Graphite / blue-grey — body text and supporting information.

The site is responsive, accessible, search-engine friendly and uses no framework.
