Title: Lissajous Figuren in Gnuplot
Date: 2013-10-09 13:17
Author: surt91
Category: Code
Tags: Gnuplot, Code, Video
Slug: lissajous-figuren-in-gnuplot
Status: published
Lang: de

Da nicht jeder das nötige Kleingeld für ein Oszilloskop und
Funktionsgenerator hat, aber jeder gerne eine
[Lissajous-Figur](http://de.wikipedia.org/wiki/Lissajous-Figur) laufen
haben möchte, liefere ich hier den entsprechenden Gnuplot Code.

```gnuplot
reset
set term gif animate optimize
set output "lissajous.gif"
n=6250

set xr [-1:1]
set yr [-1:1]

set parametric
unset border
unset xtics
unset ytics

fx(t) = sin(t)
fy(t) = sin(2.999*t)

i=0
load "animateLissajou.gp"
set output
```

Die Datei "`animateLissajou.gp`" sieht dann so aus:

```gnuplot
set trange [i:i+2*pi]
plot fx(t),fy(t) lc rgb 'black' notitle

i=i+2*pi*10
if (i < n) reread
```

Stark angelehnt an diesen
[Blogeintrag](http://gnuplot-surprising.blogspot.de/2011/09/creating-gif-animation-using-gnuplot.html).
Das Ergenis sieht dann so aus.

![Lissajous Figur](/img/lissajous.gif)
