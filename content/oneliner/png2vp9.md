Title: png2vp9
Date: 2017-08-26 11:05
Category: Snip
Slug: png2vp9
Status: published
Lang: de

Konvertiere einen Ordner voller `.png` in ein zur Web-Wiedergabe geeignetes
`VP9`, das von allen [wichtigen Browsern unterstützt](http://caniuse.com/webm/embed)
wird.

```bash
ffmpeg -f image2 -pattern_type glob -i "img*.png" -c:v libvpx-vp9 -pass 1  \
    -b:v 1000K -threads 1 -speed 4 -tile-columns 0 -frame-parallel 0 \
    -auto-alt-ref 1 -lag-in-frames 25 -g 9999 -aq-mode 0 -an -f null -


ffmpeg -f image2 -pattern_type glob -i "img*.png" -c:v libvpx-vp9 -pass 2 \
    -b:v 1000K -threads 1 -speed 0 -tile-columns 0 -frame-parallel 0 \
    -auto-alt-ref 1 -lag-in-frames 25 -g 9999 -aq-mode 0 -c:a libopus -b:a 64k \
    -f webm video.webm
```

Für maximale Kompatibilität kann als Fallback noch ein `MP4` erstellt werden.

```bash
ffmpeg -an -f image2 -pattern_type glob -i "img*.png" -vcodec libx264 \
    -pix_fmt yuv420p -profile:v baseline -level 3 video.mp4
```

Einbettung erfolgt mit:

```html
<video>
  <source src="path/to/video.webm" type="video/webm; codecs=vp9,vorbis">
  <source src="path/to/video.mp4" type="video/mp4">
</video>
```
