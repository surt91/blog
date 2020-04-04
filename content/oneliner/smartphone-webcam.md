Title: smartphone webcam
Date: 2020-04-04 10:59
Author: surt91
Category: Snip
Slug: smartphone-webcam
Status: published
Lang: de

Um die Kamera eines Smartphones als Webcam für eine Videokonferenz auf dem Computer zu nutzen,
braucht man zuerst eine App, die das Bild der Kamera als `http`-Stream bereit
stellt, bspw. [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=de).

Für Linux existieren die Projekte `v4l2loopback` und `ffmpeg` mit deren Hilfe
der Stream als Webcam input genutzt werden kann (hier für den Fall, dass das
Smartphone die IP `192.168.1.127` hat):

```bash
sudo modprobe v4l2loopback
ffmpeg -i http://192.168.1.127:8080/video -map 0:v -vcodec rawvideo -vf format=yuv420p -fflags nobuffer -flags low_delay -fflags discardcorrupt -f v4l2 /dev/video2
```

Natürlich kann man beliebige Filter von `ffmpeg` anwenden, zum Beispiel einen
`colorkey` oder `chromakey`, um ein beliebiges Bild `background.jpg` als
virtuellen Hintergrund zu nutzen. Hier für den Fall, dass ein weißes Bettlaken
als "green screen" genutzt wird:

```bash
ffmpeg -i images/background.jpg -i http://192.168.1.127:8080/video -vcodec rawvideo -fflags nobuffer -flags low_delay -fflags discardcorrupt -filter_complex "[1:v]colorkey=0xbbbbbb:0.3:0.2[foregroud];[0:v][foregroud]overlay[composite];[composite]format=yuv420p[out]" -map "[out]:v" -f v4l2 /dev/video2
```

Ähnlich kann auch das Smartphone-Mikrophon als Mikrophon für den Computer genutzt
werden. Hier mithilfe von `pulseaudio` und `gstreamer`:

```bash
pactl load-module module-null-sink sink_name="ipwebcam"
pactl set-default-source "ipwebcam.monitor"
gst-launch-1.0 souphttpsrc location="http://192.168.1.127:8080/audio.wav" is-live=true ! audio/x-raw,format=S16LE,layout=interleaved,rate=44100,channels=1 ! queue ! pulsesink device="ipwebcam"
```
