Title: png2mp4
Date: 2016-09-17 18:48
Category: Snip
Slug: png2mp4
Status: published
Lang: en

Convert a folder with enumerated `.png` files into a `x264` Video
i a `.mp4` container with a given frame rate.

```bash
ffmpeg -f image2 -pattern_type glob -framerate 60 -i "img*.png" -vcodec libx264 vid.mp4
```
