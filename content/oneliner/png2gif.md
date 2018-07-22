Title: png2gif
Date: 2017-10-31 11:46
Category: Snip
Slug: png2gif
Status: published
Lang: de

Konvertiere einen Ordner voller `.png` in ein animiertes `.gif`

```bash
convert -delay 30 -loop 0 -layers Optimize *.png out.gif
```

Natürlich klappt das nicht nur für `.png` und alle anderen Optionen von
Imagemagick lassen sich kombinieren.

```bash
convert -resize 256x256\> -delay 30 -loop 0 -layers Optimize *.svg out.gif
```
