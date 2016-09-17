Title: svg2png
Date: 2016-09-17 18:46
Category: Oneliner
Status: published

Konvertiere `.svg` in `.png` mit weißem Hintergrund.

    #!bash
    inkscape -z -b \"#fff\" -e img.png -h 1080 img.svg
