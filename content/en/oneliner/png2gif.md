Title: png2gif
Date: 2017-10-31 11:46
Category: Snip
Slug: png2gif
Status: published
Lang: en

Convert a folder of `.png` into an animated `.gif`.

```bash
convert -delay 30 -loop 0 -layers Optimize *.png out.gif
```

Naturally, this works not olny for `.png` and all other options of
Imagemagick can be used as well.

```bash
convert -resize 256x256\> -delay 30 -loop 0 -layers Optimize *.svg out.gif
```
