Title: svg2png
Date: 2016-09-17 18:46
Category: Snip
Slug: svg2png
Status: published
Lang: de

Konvertiere `.svg` in `.png` mit weißem Hintergrund.

```bash
inkscape -z -b \"#fff\" -e img.png -h 1080 img.svg
```

Oder einen ganzen Ordner.

```bash
for i in *.svg
    do inkscape -z -b \"#fff\" -e $(basename -s .svg $i).png -h 1080 $i
done
```
