Title: Phase Transitions of Traveling Salesperson Problems solved with Linear Programming and Cutting Planes
Date: 2018-07-31 06:28
Author: surt91
Category: Phys
Tags: Veröffentlichung, Physik
Slug: paper-tsp-pt
Status: published
Lang: de
Doi: 10.1209/0295-5075/113/30004

In diesem Artikel wird ein Ensemble des Problems des Handlungsreisenden (TSP)
eingeführt, das abhängig von einem Parameter $\sigma$ von einer trivial einfach
zu lösenden Konfiguration, Städten, die equidistant auf einem Kreis angeordnet
sind zum zufälligen euklidischen TSP in der Ebene
interpoliert. Danach werden mittels linearer Programmierung  einige
Phasenübergänge festgestellt, ab welchen Werten von $\sigma$ das Problem
schwierig zu lösen wird. Zu zwei dieser Übergänge werden strukturelle
Eigenschaften der optimalen Lösung gefunden, die sich an dieser Stelle
ebenfalls charakteristisch ändern. Da die optimale Lösung nicht von der
Lösungsmethode abhängt, sind diese Phasenübergänge also nicht nur von Bedeutung
für das spezielle Lineare Programm bzw. den Algorithmus der zu dessen Lösung
genutzt wurde, sondern fundamentale Eigenschaft dieses TSP Ensembles.

Im Detail wurde die klassische Formulierung von Dantzig genutzt:
\begin{align*}
    \label{eq:objective}
    &\text{minimize}     &  \sum_i \sum_{j<i} c_{ij} x_{ij}\\
    \label{eq:int}
    &\text{subject to}   &  x_{ij}                                &\in \{0,1\}\\ %\mathbb{Z}\\
    \label{eq:inout}
    &                    &  \sum_{j} x_{ij}                       &= 2&            & \forall i \in V \\
    \label{eq:sec}
    &                    &  \sum_{i \in S, j \notin S} x_{ij}     &\ge 2&          & \forall S \varsubsetneq V, S \ne \varnothing
\end{align*}
Als Ordnungsparameter des Phasenübergangs dient die Wahrscheinlichkeit, dass
mittels eines Simplex-Solvers eine ganzzahlige, und damit optimale, Lösung
gefunden wird. Ohne die letzte Bedingung, den "Subtour Elimination Constraints",
fällt der Phasenübergang auf den Punkt, an dem sich die optimale Lösung erstmals
von der Reihenfolge der Städte des ursprünglichen Kreises unterscheidet.
Mit den "Subtour Elimination Constraints", fällt der Phasenübergang auf den
Punkt, wo die optimale Tour anfängt von einem Zickzack-Kurs auf große Meander zu
wechseln. Dies wird durch die geometrische "Gewundenheit", die Tortuosität,
\begin{align*}
    \tau = \frac{n-1}{L} \sum_{i=1}^{n} \brac{\frac{L_i}{S_i}-1}.
\end{align*}
ermittelt, die an diesem Punkt maximal wird. Hier wird die Tour in $N$
Teilstücke mit gleichem Vorzeichen der Krümmung unterteilt und für jedes
Teilstück das Verhältnis von direkter Ende-zu-Ende-Distanz $S_i$ zu der
Länge entlang der Tour $L-i$ summiert wird.
