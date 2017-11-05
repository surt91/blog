Title: A Fractal A Day
Date: 2017-12-13 17:36
Author: surt91
Category: Code
Tags: Physik, Bild, Rust, Code
Slug: randomFractals
LargeFeaturedImage: img/afractaladay.png
Status: draft

Vor einiger Zeit habe ich ein [Programm](https://github.com/surt91/AFractalADay)
geschrieben, das verschiedene Typen von Fraktalen generiert. Da viele Methoden
Fraktale zu generieren relativ einfach zu parallelisieren sind und großen
Bedarf an Rechenkraft haben, habe ich mich entschieden es in Rust zu
implementieren.

Da Fraktale nett anzuschauen sind, ist dieser Beitrag voller hochaufgelöster
Bilder. Und es gibt [@AFractalADay](https://twitter.com/AFractalADay) auf
Twitter, der täglich ein zufälliges Fraktal tweetet.


### Escape Time

Eine Klasse von Fraktalen bildet sich durch das Konvergenzverhalten des
wiederholten Anwendens einer Funktion. Was genau dieser Satz bedeutet, lässt
sich am besten an Beispielen erklären.


#### Mandelbrot-Menge

Das vermutlich bekannteste Fraktal ist das Apfelmännchen, das die
Mandelbrotmenge visualisiert. Das ist die Menge der Punkte $c = x + iy$, die
nicht konvergieren, wenn die Funktion $f_c(z) = z^2 + c$ wiederholt angewendet
wird, also wenn die Folge $f_c(0), f_c(f_c(0)), f_c(f_c(f_c(0))), ...$
gegen einen endlichen Wert strebt.

Wenn man jeden Punkt $c$ auf der komplexen Ebene entsprechend des Konvergenzverhaltens
bezüglich dieser Folge einfärbt -- schwarz wenn es konvergiert, blau für langsame
Divergez, rot für schnelle Divergenz -- erhält man ein solches Bild:

![Zoom auf das Apfelmännchen]({filename}/img/mandelbrot.png)

Dies ist ein Zoom auf den Rand des Apfelmännchens. Tatsächlich ist die
Mandelbrotmenge kein Fraktal im eigentlich Sinne, da seine fraktale Dimension
2 ist -- der schwarze Bereich füllt eine Fläche.

Ohne auf Details einzugehen, ist es einfach möglich dieses Fraktal zu rastern
und dabei jeden Pixel parallel zu berechnen. Um tiefer hineinzuzoomen reicht
allerdings die 64-Bit-Float-Präzision, die mein Programm nutzt nicht mehr aus.


#### Julia-Mengen

Nahe verwandt sind die Julia-Mengen. Hier färbt man allerdings jeden Punkt $z$
entsprechend ein und gibt $c$ als Parameter vor.

![Ein Julia-Fraktal]({filename}/img/julia.png)

Tatsächlich ist jede beliebige Funktion $f$ erlaubt und nicht nur die
quadratische. Mit unkonventioneller Zuordnung von Farben zu Divergenzzeiten
ergibt sich mit $f(z) = (-2.6-i) \cosh(z)$ dieses Bild:

![Ein weiteres Julia-Fraktal]({filename}/img/julia2.png)


#### Newton-Fraktal

Das [Newton-Verfahren zur Findung von Nullstellen](https://de.wikipedia.org/wiki/Newton-Verfahren)
startet an einem beliebigen Punkt auf einer Kurve, und berechnet die Nullstelle
der Tangente an diesem Punkt. Mit der Tangente dieses Punktes wird genauso
verfahren. Dabei sollten sich die so erhaltenen Punkte immer dichter einer.
Nullstelle nähern. Bei einer Komplexen Funktion können wir dies für jeden
Startpunkt iterieren. Jeder Punkt wird gegen eine Nullstelle konvergieren, der
wir eine Farbe zuordnen und den Punkt mit dieser Farbe einfärben. Wenn wir die
Sättigung davon abhängig machen, wie schnell die Konvergenz ist, sieht das
Ergebnis für $f(x) = z^4 + 5^{z+i} + 15$ so aus.

![Newton Fraktal für f(x) = z^4 + 5^{z+i} + 15]({filename}/img/newton.png)


### Chaos Game

Eine große Klasse von Fraktalen lässt sich mit dem Chaos Game erzeugen. Man
benutzt dazu mindestens zwei Abbildungen $f_1(z)$ und $f_2(z)$, die jeweils einen
Punkt $z$ auf einen anderen Punkt abbilden. Man wählt einen Punkt zum Starten,
bildet ihn mit einer zufälligen der beiden Abbildungen ab, zeichnet den
resultierenden Punkt ein und wiederholt dies sehr oft.

Dieser Algorithmus ist inherent sequenziell, allerdings kann man parallel an
vielen verschiedenen Punkten starten und die Ergebnisse dieser unabhängigen
Markovketten in einem Bild zusammenführen.

#### Sierpinski Dreieck und Bernsley Farn

Mit dieser Methode kann man alte Bekannte wie das [Sierpinski-Dreieck]({filename}/rule-90.md)
erzeugen.

![Sierpinski-Dreieck]({filename}/img/sierpinski.png)

Dazu benötigt man die drei affinen Transformationen
$$\begin{align}
f_1(\vec z) &=\begin{pmatrix}
            -1/4         & \sqrt 3 / 4 \\
            -\sqrt 3 / 4 & -1/4
        \end{pmatrix}
        \cdot
        \begin{pmatrix}
            z_x \\
            z_y
        \end{pmatrix}
        +
        \begin{pmatrix}
                -1/4\\
                \sqrt 3 / 4
        \end{pmatrix}\\
f_2(\vec z) &=\begin{pmatrix}
            1/2 & 0 \\
            0   & 1/2
        \end{pmatrix}
        \cdot
        \begin{pmatrix}
            z_x \\
            z_y
        \end{pmatrix}
        +
        \begin{pmatrix}
                1/4\\
                \sqrt 3 / 4
        \end{pmatrix}\\
f_3(\vec z) &=\begin{pmatrix}
            -1/4 & -\sqrt 3 / 4 \\
            \sqrt 3 / 4   & 1/4
        \end{pmatrix}
        \cdot
        \begin{pmatrix}
            z_x \\
            z_y
        \end{pmatrix}
        +
        \begin{pmatrix}
                1\\
                0
        \end{pmatrix}
\end{align}$$

Diesen vier affinen Transformationen
$$\begin{align}
f_1(z) &=\begin{pmatrix}
                0.16\\
                0
        \end{pmatrix}\\
f_2(z) &=\begin{pmatrix}
            0.85 & 0.04 \\
            0    & -0.04
        \end{pmatrix}
        \cdot
        \begin{pmatrix}
            z_x \\
            z_y
        \end{pmatrix}
        +
        \begin{pmatrix}
                0.85\\
                1.6
        \end{pmatrix}\\
f_3(z) &=\begin{pmatrix}
            0.2 & -0.26 \\
            0   & 0.23
        \end{pmatrix}
        \cdot
        \begin{pmatrix}
            z_x \\
            z_y
        \end{pmatrix}
        +
        \begin{pmatrix}
                0.22\\
                1.6
        \end{pmatrix}\\
f_4(z) &=\begin{pmatrix}
            -0.15 & 0.28 \\
            0     & 0.26
        \end{pmatrix}
        \cdot
        \begin{pmatrix}
            z_x \\
            z_y
        \end{pmatrix}
        +
        \begin{pmatrix}
                0.24\\
                0.44
        \end{pmatrix}\\
\end{align}$$

erzeugen diesen Farn.

![Bernsley-Farn]({filename}/img/fern.png)


#### Fractal Flame

[Fractal Flame](http://flam3.com/flame_draves.pdf) ist der Name einer Klasse
von Zufallsfraktalen, die nach dem gleichen Muster wie oben aus einer Reihe
affiner Transformationen $A_i$ bestehen. Zusätzlich können die affinen
Transformationen mit einer nichtlinearen *Variantion* $V_j$ erweitert werden,
sodass $f_i(\vec z) = V_j(A_i(\vec z))$ (oder Linearkombinationen dieser Variantionen).
Zur Visualisierung werden die Punkte nicht direkt gezeichnet, sondern in ein
Histogramm eingetragen, aus dem die Farbintensitäten typischerweise
logarithmisch berechnet werden.

![Fractal Flame, 'Horseshoe' Variation]({filename}/img/horseshoe.png)


#### Möbius Flame

Diese Fraktale sind nahezu identisch zu den Fractal Flames, nur dass anstatt von
affinen Transformationen Möbius Transformationen auf der komplexen Ebene genutzt
werden.

$$f_i(z) = \frac{a_i*z + b_i}{c_i*z + d_i}$$

![Möbius Flame]({filename}/img/mobius.png)


#### Wie findet man "gute" Parameter?

Offenbar hat dieser Typ von Fraktal sehr viele freie Parameter, die angepasst
werden müssen für hübsche Resultate. Tatsächlich gibt es mit [electric sheep](https://electricsheep.org/)
(ich hoffe stark, dass es eine Blade Runner Referenz ist) ein Crowdsourcing-Projekt,
das mithilfe von evolutionären Algorithmen und dem Feedback von Menschen
besonders ansehnlich Fraktale erzeugt.

Für mein Programm habe ich eine simplere Methode genutzt. Damit man ein Fraktal
gut sehen kann, sollte seine fraktale Dimension größer als 1 sein. Abschätzbar
ist es relativ einfach über die [Korrelations-Dimension](https://en.wikipedia.org/wiki/Correlation_dimension).
Dazu misst man die paarweisen Abstände von Punkten und misst den Exponenten ihrer
kumulativen Verteilungsfunktion.


### Weitere Fraktale

Es gibt natürlich viel mehr Typen von Fraktalen. Von einigen habe ich noch
Bilder angefertigt, die ich hier auch gerne zeigen möchte.


#### Diffusionsbegrenztes Wachstum

Diffusionsbegrenztes Wachstum bildet das Wachstum von Kristallen in stark
verdünnten Lösungen ab. Man startet mit einem Seed und lässt dann einzelne
Teilchen diffundieren, bis sie auf dem Nachbarfeld eines Seeds landen, wo sie
dann bleiben und Teil des Seeds werden. Dieser Prozess bildet verästelte
Strukturen aus.

![Diffusionsbegrenztes Wachstum]({filename}/img/dla_core.png).


#### Random Walks

Einige Arten von Random Walks haben eine fraktale Dimension zwischen 1 und 2,
was sie zu ansehnlichen Fraktalen machen sollte. Der Smart Kinetic Self
Avoiding Walk, der in meinem [rsnake]({filename}/rsnake.md) die Strategie des
Autopiloten ist, hat eine fraktale Dimension von $\frac{7}{4}. 100000 Schritte
sehen so aus:

![Smart Kinetic Self Avoiding Walk, 100000 Schritte]({filename}/img/sksaw.png).
