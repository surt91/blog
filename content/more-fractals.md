Title: Noch mehr Fraktale
Date: 2021-06-07 20:45
Author: surt91
Category: Code
Tags: Physik, Bild, Rust, Formel
Slug: more-fractals
LargeFeaturedImage: img/ising1200.webp
Status: published
Lang: de

Seit meinem [ersten Eintrag]({filename}/randomFractals.md) über meinen
Fraktal-tweetenden Bot [@AFractalADay](https://twitter.com/AFractalADay),
habe ich selbigen noch um ein paar Fraktale erweitert, die ich hier kurz
festhalten möchte. Der ganze Code ist [auf Github](https://github.com/surt91/AFractalADay).

### Chaotic Maps

Eine *Quadratic Map* is eine Rekursionsgleichung mit einem quadratischen
Term, also beispielsweise
$$x_{i+1} = a_0 x^2 + a_1 x + a_2.$$
Das berühmteste Mitglied dieser Familie ist die [*Logistic-Map*](https://de.wikipedia.org/wiki/Logistische_Gleichung)
mit $a_0=1, a_1=r, a_2=0$, die chaotisches Verhalten für $3.56995 < r < 4$ zeigt.
Aber leider ist sie nur eindimensional und ihr Attraktor deshalb nicht besonders hübsch.

Um visuell ansprechende Fraktale daraus zu erzeugen, brauchen wir also ein System aus
zwei Rekursionsgleichungen, die wir als $x$- und $y$-Koordinaten betrachten können:

\begin{align*}
x_{i+1} &= a_{0} + a_{1} x + a_{2} x^2 + a_{3} x y + a_{4} y + a_{5} y^2\\
y_{i+1} &= a_{6} + a_{7} x + a_{8} x^2 + a_{9} x y + a_{10} y + a_{11} y^2.
\end{align*}

Jetzt haben wir 12 freie Parameter, die einen riesigen Parameterraum aufspannen,
in dem [etwa 1.6%](http://sprott.physics.wisc.edu/pubs/paper203.htm) aller Möglichkeiten
chaotisches Verhalten mit einem seltsamen Attraktor zeigen.

[![Quadratic Map](/img/quadraticMap1200.webp)](/img/quadraticMap.png)

### Chaotische Differentialgleichungssysteme

Ein echter Klassiker ist das Differentialgleichungssystem, das die Chaostheorie
begründet hat und nach dem der *Schmetterlingseffekt* benannt
ist [[1]({filename}/schmetterlingseffekt.md), [2]({filename}/seltsamer-attraktor.md)].
Für bestimmte Paramtersätze verlaufen die Bahnkurven entlang eines *seltsamen Attraktors*,
dessen fraktale Dimension $\approx 2.06$ ist. Da der vollständige Attraktor somit in
einer zweidimensionalen Projektion [etwas langweilig](/img/lorenz_full_attractor.png) aussieht,
habe ich hier nur eine Trajektorie über kurze Zeit dargestellt.

[![Lorenz-Attraktor](/img/lorenzattraktor2_1200.webp)](/img/lorenzattraktor2.png)

Und es gibt [eine ganze Menge](https://en.wikipedia.org/wiki/List_of_chaotic_maps)
weitere Differntialgleichungssysteme (und *chaotic maps*), die chaotische
Attraktoren aufweisen. Deshalb zeige ich hier noch einen Rössler-Attraktor, der
eine vereinfachte Version des Lorenz-Systems ist:

\begin{align*}
\frac{\mathrm{d}x}{\mathrm{d}t} &= -(y+z)\\
\frac{\mathrm{d}y}{\mathrm{d}t} &= x + ay\\
\frac{\mathrm{d}z}{\mathrm{d}t} &= b + xz - cz
\end{align*}

Und hier haben wir das Glück, dass auch seine Projektion sehr ansehnlich ist.

[![Rössler-Attraktor](/img/rossler1200.webp)](/img/rossler.png)

Ich persönlich frage mich, nun wie der Attraktor für das [Doppelpendel]({filename}/doppelpendel.md)
aussieht. Es ist anscheinend kein Fraktal, aber es sieht dennoch ganz interessant aus:

[![Doppelpendel](/img/doublePendulumLong1200.webp)](/img/doublePendulumLong.png)

### Ising model

Das Ising Modell für Ferromagnetismus wird auch als Drosophila
der statistischen Physik bezeichnet: Es ist ein einfaches
Modell, dass einen Phasenübergang aufweist -- Eisen verliert
seine magnetischen Eigenschaften oberhalb der Curie-Temperatur.

Es besteht aus magnetischen Momenten, *Spins*, die gerne in die
gleiche Richtung zeigen wie ihre Nachbarn, aber durch hohe Temperatur
gestört werden. Oder etwas formaler: Die innere Energie $U$ wird durch
den Hamiltonian $\mathcal{H} = - \sum_{<ij>} s_i s_j$ bestimmt, wobei
$s_i = \pm 1$, je nachdem ob der Spin *up* oder *down* ist und die
Summe über benachbarte Spins läuft. Das System
wird immer einen Zustand anstreben, der die freie Energie $F=U-TS$
minimiert. Das kann entweder passieren, indem $U$ möglichst klein
ist oder die Entropie $S$ möglichst hoch. Bei großen Werten der
Temperatur $T$ bekommt der Entropie-Term ein höheres Gewicht, sodass
Zustände mit hoher Entropie, also zufälligen Spinausrichtungen,
bevorzugt sind, bei niedrigen Temperaturen werden Konfigurationen
mit niedriger innerer Energie bevorzugt, also solche in denen alle Spins
in die selbe Richtung zeigen. Die Temperatur, bei der sich beide
Terme die Waage halten, nennt man kritische Temperatur. Hier bilden
sich Regionen von Spins, die in die gleiche Richtung zeigen, auf allen
Größenskalen. Die fraktale Dimension dieser Regionen ist
[187/96](https://doi.org/10.1103/PhysRevLett.62.1067),
was solche kritische Konfigurationen interessant anzusehen macht.
Ich empfehle auf das folgende Bild zu klicken und etwas hineinzuzoomen.

[![Kritisches Ising System](/img/ising1200.webp)](/img/ising.png)
