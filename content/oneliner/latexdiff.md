Title: latexdiff
Date: 2018-01-11 15:28
Author: surt91
Category: Snip
Slug: latexdiff
Status: published
Lang: de

Um die Unterschiede zwischen zwei Latex Dateien zu ermitteln, die beispielsweise
aus Git kommen.

```bash
latexdiff old.tex new.tex > diff.tex
pdflatex diff.tex
```
