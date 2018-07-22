Title: Rule 90
Date: 2013-12-01 15:11
Author: surt91
Category: Code
Tags: C, Bild, GitHub
Slug: rule-90
FeaturedImage: img/wolfram090.png
Status: published
Lang: de

Vor kurzem habe ich angefangen "[Think Complexity](http://www.greenteapress.com/complexity/index.html)" zu
lesen -- ein leicht verständliches, interessantes Buch, in dem unter
anderem [Zelluläre Automaten](http://de.wikipedia.org/wiki/Zellul%C3%A4rer_Automat)
angesprochen werden. Und zwar die [von Stephen Wolfram](http://www.stephenwolfram.com/publications/academic/?cat=cellular-automata)
-- ja der Stephen Wolfram, der
[Mathematica](http://www.wolfram.com/mathematica/) und
[Wolfram|Alpha](http://www.wolframalpha.com/) entwickelt hat (vermutlich
jedoch nicht allein).  
Zelluläre Automaten eignen sich natürlich sehr gut, pixelige Bilder zu
erstellen, wie der
[Conways-Game-of-Life-Post]({filename}/conways-game-of-life.md)
beweist. Daher, lasse ich erstmal ein Bild sprechen.  

![Wolframs Rule 90]({filename}/img/wolfram090.png)

Die Idee ist, dass man mit einem eindimensionalen Zustand startet, und
einen neuen Zustand daraus mit lokalen Regeln, die je einen rechten und
linken Nachbarn berücksichtigen, erzeugt. Stellt man diese Zustände
untereinander da, entstehen Strukturen, wie die, die an ein
[Sierpinski-Dreieck](http://de.wikipedia.org/wiki/Sierpinski-Dreieck)
erinnert.  
Die [Erklärung](http://www.wolframalpha.com/input/?i=rule+90), wie genau
diese Regeln lauten, und wie sie definiert sind, überlasse ich
passenderweise Wolfram|Alpha.

Und damit ich auch etwas sage, das tiefsinnig erscheint: Die Dreieckige
Form entspricht übrigens
dem [Vorwärtslichtkegel](http://de.wikipedia.org/wiki/Lichtkegel) des
Startwertes in der ersten Zeile. Die $y$-Achse entspricht hier schließlich
einer Zeit und die "Lichtgeschwindigkeit", mit der Beeinflussungen
propagieren können, ist 1 Pixel pro Iteration.

Den Quellcode gibt es natürlich bei
[GitHub](https://github.com/surt91/-bungen-in-C/blob/master/numeric/cellular_automata.c).
Wenn auch nur in einem "kleine Fingerübungen in C"-Repo.

Für Liebhaber, hier noch eins im original 1982 Retro-Look.

![Wolframs Rule 150]({filename}/img/wolfram150.png)

Passend zur Jahreszeit, wie ich finde.
