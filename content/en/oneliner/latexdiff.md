Title: latexdiff
Date: 2018-01-11 15:28
Author: surt91
Category: Snip
Slug: latexdiff
Status: published
Lang: en

Visualize the differences between two Latex files.

```bash
latexdiff old.tex new.tex > diff.tex
pdflatex diff.tex
```

And if one is using git anyway, there is an even simpler way to compare
a given commit with the current state.

```bash
latexdiff-vc -r 96deadbeef filename.tex --pdf
```
