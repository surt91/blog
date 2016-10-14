Title: Ising Modell zur Bildentrauschung
Date: 2013-12-22 12:37
Author: surt91
Category: Code
Tags: Python, Physik, GitHub, Bild
Slug: ising-modell-zur-bildentrauschung
Status: published

Eines der bekanntesten Modelle der statistischen Physik ist das [Ising-Modell](http://de.wikipedia.org/wiki/Ising-Modell). Es besteht aus
(klassischen) Spins auf einem Gitter im Wärmebad und soll magnetische
Eigenschaften von Festkörpern modellieren. Es zeigt nämlich in 2D und 3D
(und 4D ... ) einen Phasenübergang zweiter Ordnung von "magnetisch" zu
"nicht magnetisch", so wie ferromagnetische Materialien, die oberhalb
der Curie Temperatur nicht mehr ferromagnetisch sind.

In einfachen Worten: Die Spins des Ising-Modells richten sich so aus
wie ihre Nachbarn und die Temperatur bringt sie wieder durcheinander.

Aber es wäre natürlich langweilig das Modell so zu benutzen, wie alle
anderen auch. Deshalb stelle ich hier eine Anwendung aus 
[Pattern Recgonition and Machine Learning](http://scholar.google.de/scholar?q=bishop+pattern+recognition+and+machine+learning&hl=de) 
vor, die nichts mehr mit Magneten zu tun hat: Rauschunterdrückung in Bildern.

Andererseits bin ich Physiker und darf deshalb nichts machen, was direkt
nützlich wäre, also beschränke ich mich auf schwarz-weiße Bilder, die
man direkt auf das "spin up"-"spin down" des Ising-Modells abbilden
kann.

Die Idee ist, das jeder Spin einem Pixel $x_i$ entspricht. Dann koppelt man
die Spins des Ising-Modells $x_i$ an die Pixel $y_i$ des verrauschten Bildes
über einen zusätzlichen Energie-Term 
$$\mathcal{H} = - \beta \sum_{\left< i,j \right>} x_i x_j - \eta \sum_i x_i y_i.$$
Dabei bedeutet $\left< i,j \right>$, dass man über alle Nachbarn von $i$ summiert.

Von diesem Modell kann man dann per [Simulated Annealing]({filename}/simulatedsort.md) 
den Grundzustand suchen oder man macht es sich einfach equilibriert bei $T=0$.

![Ising-Modell]({filename}/img/standaloneIsing.svg){width="100%"}

Das Schema dazu wurde bereits in
[diesem Post]({filename}/oberflachenkachelung-mit-tikz.md)
gezeigt. Graue Knoten entsprechen den Pixeln des verrauschten Bilds $y_i$ und weiße
Knoten den Ising-Spins $x_i$, die am Ende als Pixel des entrauschten Bilds
interpretiert werden.

Genug der Theorie. Es wird Zeit für pixelige Bilder. Leider hatte ich
kein verrauschtes Bild, also habe ich ein beliebiges Bild gemalt und 10%
aller Pixel invertiert.

![Vorher-Nachher Vergleich]({filename}/img/vorhernachher.png)

Links das verrauschte Bild und rechts das entrauschte. Ja, nicht
perfekt. Und in dem zitierten Buch wird auf der gleichen Seite noch eine
sehr viel bessere Methode angesprochen. Aber die hatte nichts mit dem
Ising-Modell zu tun. Und man sieht ja auch eine Verbesserung. Oder?

Nebenbei bemerkt, kann man das Ising-Modell auch als
[zellulären]({filename}/conways-game-of-life.md) [Automaten]({filename}/rule-90.md) mit
zufälligem Element betrachten, denn jeder Spin ist eine Zelle, die nur
lokal von seinen Nachbarn und zufällig durch die Temperatur beeinflusst
wird.

Der Code ist als [Gist auf Github](https://gist.github.com/surt91/7789753).

