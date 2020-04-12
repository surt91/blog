Title: compress-pdf
Date: 2020-04-12 10:26
Category: Snip
Slug: compress-pdf
Status: published
Lang: en

To compress of a `pdf` with many high resolution images
to a sensible filesize (by downscaling and reencoding the images),
one can use ghostscript:

```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dEmbedAllFonts=true -dSubsetFonts=true -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

The available presets are `screen`, `ebook`, `printer`, `prepress` and `default`.
More options can be listed with:

```bash
gs -sDEVICE=pdfwrite -o /dev/null -c "currentpagedevice { exch ==only ( ) print == } forall"
```
