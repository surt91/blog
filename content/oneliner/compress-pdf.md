Title: compress-pdf
Date: 2020-04-12 10:26
Category: Snip
Slug: compress-pdf
Status: published
Lang: de

Um ein `pdf` mit vielen zu hoch aufgelösten Bildern auf eine angemessene
Dateigröße zu bringen (durch das herunterskalieren und gegebenenfalls
neu-kodieren der Bilder), kann einfach ghostscript genutzt werden:

```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dEmbedAllFonts=true -dSubsetFonts=true -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

Die Qualitätspresets sind `screen`, `ebook`, `printer`, `prepress` und `default`.
Weitere Optionsnamen können durch folgendes Kommando ermittelt werden:

```bash
gs -sDEVICE=pdfwrite -o /dev/null -c "currentpagedevice { exch ==only ( ) print == } forall"
```
