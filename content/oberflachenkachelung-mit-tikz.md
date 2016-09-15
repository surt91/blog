Title: Oberflächenkachelung mit TikZ
Date: 2013-12-08 12:37
Author: surt91
Category: Code
Tags: LaTeX, TikZ
Slug: oberflachenkachelung-mit-tikz
Status: published

Man arbeitet an einem Seminarvortrag und will ein Modell auf einem
periodischen Gitter erklären. Natürlich kann man sich nicht entscheiden,
wie viele [Elementarzellen](http://de.wikipedia.org/wiki/Elementarzelle)
man darstellen möchte, außerdem ist es einem zuwider mehrere
Elementarzellen per Hand zu schreiben.

Wer kennt das nicht?

Glücklicherweise gibt es eine Lösung. Weil man alle seine Aufzeichnungen
sowieso in LaTeX setzt, benutzt
man [TikZ](http://www.texample.net/tikz/examples/), bastelt eine
Elementarzelle und kachelt sie über die Ebene, bis man das Gefühl hat,
dass es genau passend für die Präsentation ist.  
Als Bonus kann man noch mit den Parametern spielen, um einen möglichst
überzeugenden pseudo 3D Effekt zu erzielen.

Ungefähr so:  
 Und danach kann man es in
ein .svg wandeln und auf seinem Blog zeigen.

![Isingmodell mit Kopplung](img/standaloneIsing.svg){width="100%"}

Und damit wäre wiedereinmal die Vorliebe dieses Blogs für [schwarz-weiße
Bilder]({filename}/conways-game-of-life.md),
die entweder [Linien und Kreise]({filename}/proximity-graphs.md)
oder [zu große]({filename}/seltsamer-attraktor.md)
[Pixel]({filename}/rule-90.md)
enthalten, bestätigt.
