# University of Houston Cullen College of Engineering Thesis Template

This workspace includes a LaTeX class and starter document based specifically on the Cullen College of Engineering thesis and dissertation guide dated October 2022.

Author of this template format: Umar Masood.

Important disclosure: this template is an unofficial implementation of the College of Engineering formatting guide. There may still be errors, omissions, or differences between this LaTeX implementation and the official requirements. Anyone using this template should read and understand the official PDF guide before submission and should verify the final manuscript against that document.

Files:

- `uhthesis.cls`: custom class with College of Engineering margins, spacing, pagination, and front-matter helpers.
- `thesis.tex`: starter manuscript showing how to use the class.
- `references.bib`: starter BibTeX database for thesis references.
- `uh_thesis_guide.pdf`: downloaded source guide.
- `uh_thesis_guide.txt`: extracted text used to capture the formatting rules.

College of Engineering formatting details currently encoded in the class:

- Left margin 1.5 inches; top, right, and bottom margins 1 inch.
- Body text double-spaced.
- Figure and table captions single-spaced.
- Font size kept within the required 10--12 point range by using a 12 point base class.
- Front matter uses Roman numerals.
- Main matter starts at Arabic page 1.
- Page numbers are centered at the bottom of the page.
- Front matter order is set up as title page, optional copyright page, optional dedication, optional acknowledgements, abstract, table of contents, list of tables, and list of figures.
- References are placed before appendices.
- Chapter numbering is Roman numeral based.
- Equation numbering is tied to chapters.
- Abstract text is double-spaced, and the official guide limits the abstract to 350 words.
- The title page is set up to use the graduation semester end date format such as May, August, or December plus the year.

What users should still verify manually against the official PDF:

- Exact title page wording, committee listing, and degree wording.
- Department-specific reference style requirements.
- Final spacing and placement of any unusual elements, large tables, long figure captions, or appendices.
- Any updates issued by the College of Engineering after the October 2022 guide.

Build with BibTeX using:

```powershell
pdflatex thesis.tex
bibtex thesis
pdflatex thesis.tex
pdflatex thesis.tex
```

The starter template uses `\nocite{*}` so the sample entries appear even before you add real citations. Remove that line once you are citing sources normally with `\cite{...}`.

If your department requires a specific bibliography style, change the `\bibliographystyle{...}` line in `thesis.tex`.