Title: Handbrake for Web
Date: 2017-08-08 21:44
Category: Oneliner
Status: published

Konvertiere ein Video neu mit einem Profil das geeignet für Webbrowser und
Smartphones ist.

    #!bash
    HandBrakeCLI -f av_mp4 -O -e x264 --encoder-preset veryslow --encoder-profile main --encoder-level 4.0 -q 22.0 -i input.mp4 -o output.mp4
