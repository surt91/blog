Title: seltsamer Attraktor
Date: 2012-10-11 00:24
Author: surt91
Category: Code
Tags: C, Video, Physik
Slug: seltsamer-attraktor
Status: published

Ich hab ja schon mal kurz eine [Trajektorie zum
Schmetterlingseffekt]({filename}/schmetterlingseffekt.md)
gezeigt.

Ich habe da mal was gebastelt: Die Projektion in die y-z-Ebene, wie 13
Teilchen den Attraktor durchlaufen.

<video controls="controls" height="624" width="624">
<source src="https://dl.dropbox.com/u/963344/blog/lorenz13yz.m4v" />
<source src="https://dl.dropbox.com/u/963344/blog/lorenz13yz.mp4" type="video/mp4" />
<source src="https://dl.dropbox.com/u/963344/blog/lorenz13yz.webm" type="video/webm" />
</video>

(mit C gerechnet mit Cairo gezeichnet und mit ffmpeg bewegt)

Sie starten alle fast auf dem selben Punkt, aber nehmen sehr
verschiedene Wege. Dennoch sieht es irgendwie  geordnet aus.
[Seltsam.](http://de.wikipedia.org/wiki/Chaosforschung#Der_seltsame_Attraktor)  
Hier sieht es so aus, als ob sich die Trajektorien schneiden, was
natürlich nicht der Fall ist. Aber abgesehen davon, dass eine 2D
Projektion einfacher durchzuführen ist, haben diese Quadrate in meinen
Augen etwas Ästhetisches, was in drei Dimensionen verloren ginge.  
Es ist minimalistisch und elegant.

Sobald ich das in 3D in Cairo umgesetzt habe, ändere ich meine Meinung
vielleicht ;)
