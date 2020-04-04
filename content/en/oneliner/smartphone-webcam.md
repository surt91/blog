Title: smartphone webcam
Date: 2020-04-04 10:59
Author: surt91
Category: Snip
Slug: smartphone-webcam
Status: published
Lang: en

To use the camera of a smartphone for a video conference on a computer, first
an app is needed, which provides the image of the camera as a `http` stream,
for example [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en).

For Linux we can use `v4l2loopback` and `ffmpeg` to use the stream as a virtual
webcam (here for the case that the smartphone has the IP `192.168.1.127`):

```bash
sudo modprobe v4l2loopback
ffmpeg -i http://192.168.1.127:8080/video -map 0:v -vcodec rawvideo -vf format=yuv420p -fflags nobuffer -flags low_delay -fflags discardcorrupt -f v4l2 /dev/video2
```

Additionally, one can use any filter `ffmpeg` offers, for example a `colorkey`
or `chromakey`, to use any image `background.jpg` as a virtual background.
Here for the case that a white sheet is used as a "green screen":

```bash
ffmpeg -i images/background.jpg -i http://192.168.1.127:8080/video -vcodec rawvideo -fflags nobuffer -flags low_delay -fflags discardcorrupt -filter_complex "[1:v]colorkey=0xbbbbbb:0.3:0.2[foregroud];[0:v][foregroud]overlay[composite];[composite]format=yuv420p[out]" -map "[out]:v" -f v4l2 /dev/video2
```

Similarly, one can use the microphone of the smartphone as audio input for the
computer. Here using `pulseaudio` and `gstreamer`:

```bash
pactl load-module module-null-sink sink_name="ipwebcam"
pactl set-default-source "ipwebcam.monitor"
gst-launch-1.0 souphttpsrc location="http://192.168.1.127:8080/audio.wav" is-live=true ! audio/x-raw,format=S16LE,layout=interleaved,rate=44100,channels=1 ! queue ! pulsesink device="ipwebcam"
```
