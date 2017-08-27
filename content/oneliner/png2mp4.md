Title: png2mp4
Date: 2016-09-17 18:48
Category: Snip
Status: published

Konvertiere einen Ordner mit passend nummerierten `.png`
in ein `x264` Video im `.mp4` Format mit gegebener Framerate.

```bash
ffmpeg -f image2 -pattern_type glob -framerate 60 -i "img*.png" -vcodec libx264 vid.mp4
```
