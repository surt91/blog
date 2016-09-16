Title: SimulatedSort
Date: 2014-06-14 15:20
Author: surt91
Category: Code
Tags: Python, Physik, GitHub
Slug: simulatedsort
Status: published

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
$$\mathcal{H} = \sum_{i=1}^{N-1} S_i - S_{i+1}$$
Um eine Lösung in eine andere zu verwandeln, reicht eine Permutation.

Genug der Theorie: In einem [Gist auf GitHub](https://gist.github.com/surt91/e399500e780e184d9ac7)
präsentiere ich ein schnell terminierendes
Sortierprogramm, das zwar nicht immer eine sortierte Liste findet, aber
zumindest eine Näherung! Es ist also
[Bogosort](http://de.wikipedia.org/wiki/Bogosort) in mehr als nur einer
Hinsicht überlegen! 

Wer braucht da noch $\mathcal{O}(n \log(n))$ Sortier-Algorithmen?!
