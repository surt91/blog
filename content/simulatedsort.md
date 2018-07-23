Title: SimulatedSort
Date: 2014-06-14 15:20
Author: surt91
Category: Code
Tags: Python, Physik, GitHub
Slug: simulatedsort
Status: published
Lang: de

[Simulated Annealing](http://de.wikipedia.org/wiki/Simulated_annealing)
ist eine Optimierungsmethode, die von natürlichen
Kristallisationsprozessen inspiriert ist. Man startet in der Schmelze
bei hohen Temperaturen und lässt es dann abkühlen, sodass die Atome sich
in einem Zustand minimaler Energie anordnen, dem Kristallgitter. Wenn
man also für ein Optimierungsproblem die zu optimierende Größe als
Energie ansieht, und man eine Lösung durch eine kleine Änderung in eine
andere Lösung verwandeln kann, kann man mit dieser Methode eine Näherung
für das Optimum finden.

Wenn wir also eine Sequenz $S$ von $N$ Zahlen sortieren wollen, können wir die
Summe der Differenzen zwischen benachbarten Zahlen als Energie
betrachten, denn die ist minimal in einer sortierten Liste.
\begin{equation}
    \mathcal{H} = \sum_{i=1}^{N-1} \left| S_i - S_{i+1} \right|
\end{equation}
Um eine Lösung in eine andere zu verwandeln, reicht es zwei Elemente der Sequenz
zu tauschen.

Der Kern von Simulated Annealing ist der Metropolis Algorithmus.

1. Starte bei einer hohen Temperatur $T$.
2. Berechne Energie $\mathcal{H}(S)$ der aktuellen Konfiguration $S$ nach $(1)$.
3. Erzeuge eine neue Konfiguration $R$ durch eine kleine Änderunge von $S$.
4. Akzeptiere $R$ mit der Wahscheinlichkeit
   $$p_\mathrm{acc} = \min\left[1 ,\exp(-(\mathcal{H}(R) - \mathcal{H}(S))/T) \right],$$
   sodass eine "sortiertere" Sequenz immer akzeptiert wird und eine "unsortiertere"
   vor allem bei hohen Temperaturen. Wenn $R$ akzeptiert wird, gilt $S:=R$,
   ansonsten wir die alte Konfiguration $S$ weiter benutzt.
5. Reduziere die Temperatur (beispielsweise durch Multiplikation mit einer Zahl
   etwas kleiner als 1) und breche ab, wenn die Zieltemperatur erreicht ist.
   Ansonsten beginne wieder bei 2.

Genug der Theorie: In einem [Gist auf GitHub](https://gist.github.com/surt91/e399500e780e184d9ac7)
präsentiere ich ein schnell terminierendes
Sortierprogramm, das zwar nicht immer eine sortierte Liste findet, aber
zumindest eine Näherung! Es ist also
[Bogosort](http://de.wikipedia.org/wiki/Bogosort) in mehr als nur einer
Hinsicht überlegen!

Wer braucht da noch $\mathcal{O}(N \log(N))$ Sortier-Algorithmen?!
