Title: Phase Transitions of Traveling Salesperson Problems solved with Linear Programming and Cutting Planes
Date: 2018-07-31 06:28
Author: surt91
Category: Phys
Tags: Veröffentlichung, Physik
Slug: paper-tsp-pt
Status: published
Lang: de
Doi: 10.1209/0295-5075/113/30004

In diesem Artikel wird ein Ensemble von Problemen des Handlungsreisenden (TSP)
eingeführt, das abhängig von einem Parameter $\sigma$ von einer trivial einfach
zu lösenden Konfiguration, nämlich Städte, die äquidistant auf einem Kreis angeordnet
sind, zum zufälligen euklidischen TSP in der Ebene interpoliert.

![Einfach und schwierig zu lösende TSP Konfigurationen]({filename}/img/tsp_interp.svg)

Danach werden mittels [linearer Programmierung](https://de.wikipedia.org/wiki/Lineare_Optimierung) einige
Phasenübergänge festgestellt, ab welchen Werten von $\sigma$ das Problem
schwierig zu lösen wird. Zu zwei dieser Übergänge werden strukturelle
Eigenschaften der optimalen Lösung gefunden, die sich an dieser Stelle
ebenfalls charakteristisch ändern. Da die optimale Lösung nicht von der
Lösungsmethode abhängt, sind diese Phasenübergänge also nicht nur von Bedeutung
für das spezielle Lineare Programm bzw. den Algorithmus der zu dessen Lösung
genutzt wurde, sondern fundamentale Eigenschaft dieses TSP Ensembles.

Im Detail haben wir die klassische Formulierung von Dantzig genutzt:
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

Hier ist $c_{ij}$ die Distanzmatrix zwischen allen Paaren von Städten aus $V$ und $x_{ij}$
die gesuchte Adjazenzmatrix, also $x_{ij} = 1$, wenn $i$ und $j$ aufeinanderfolgende Stationen
der Tour sind und $x_{ij} = 0$ sonst. Die erste Zeile minimiert also die Strecke der Tour.
Um zu vermeiden, dass wir die triviale Lösung $x_{ij}=0$, also "wenn wir zu Hause
bleiben müssen wir am wenigsten Strecke zurücklegen" finden, zwingt die dritte
Zeile unseren Handlungsreisenden seine Tour so zu planen, dass in Summe zwei
Striche an jede Stadt gezeichnet werden -- genug, um hinein und wieder hinaus
zu reisen. Allerdings, ist unser Handlungsreisender clever und würde versuchen unss
auszutricksen, indem er halbe Striche einzeichnen würde, wie
[in einem anderen Blogeintrag visualisiert]({filename}/tspview.md). Deshalb ist die
Bedingung in der zweiten Zeile nötig, die die Einträge in der Adjazenzmatrix auf
ganze Zahlen beschränkt. Dann bleibt nur noch das Problem, dass mehrere Routen,
die nicht verbunden sind erlaubt wären, sodass wir sie durch die letzte Zeile
verbieten: die *Subtour Elimination Constraints*. Der aufmerksame Leser mag
schon erkannt haben, dass es für jede Untermenge von Städten so eine Constraint
definiert, also exponentiell viele in der Anzahl der Städte. Die Lösung
zu dieses Problem liegt darin, dass nur sehr wenige wirklich gebraucht werden, sodass
man das Problem ohne diese Constraint löst, testet ob eine verletzt ist, was mittels
der Berechnung eines [minimum cut](https://en.wikipedia.org/wiki/Minimum_cut) sehr
schnell geht und dann eine einzelne Constraint, die diese Konfiguration verbietet
hinzufügt. Diese Methode iterativ Constraints hinzuzufügen wird meist als *Cutting Planes*
bezeichnet.

Also haben wir einen schnellen Algorithmus für das Problem des Handlungsreisenden
gefunden? Nein, leider nicht. Es gibt keinen bekannten Algorithmus, der dieses Problem
unter Erfüllung der zweiten Zeilen, also Beschränkung auf ganzzahlige Lösungen lösen kann.
Aber sobald wir diese Bedingung fallen lassen, können wir klassische Verfahren der
linearen Programmierung nutzen, um dieses Problem effizient zu lösen. Dies wird auch
[Relaxation](https://en.wikipedia.org/wiki/Linear_programming_relaxation) genannt. Die Länge der
Strecke ist immer eine untere Schranke für die tatsächliche Lösung. Und wenn unsere
Lösung per Zufall ganzzahlig ist, können wir uns sicher sein, die Optimale Lösung
gefunden zu haben.

Als Ordnungsparameter des Phasenübergangs zwischen leichten und schweren Konfigurationen
dient uns also die Wahrscheinlichkeit, dass
mittels eines Simplex-Solvers eine ganzzahlige, und damit optimale, Lösung
gefunden wird. Ohne die letzte Bedingung, den *Subtour Elimination Constraints*,
fällt der Phasenübergang auf den Punkt, an dem sich die optimale Lösung erstmals
von der Reihenfolge der Städte des ursprünglichen Kreises unterscheidet.
Mit den Subtour Elimination Constraints, fällt der Phasenübergang auf den
Punkt, wo die optimale Tour anfängt von einem Zickzack-Kurs auf große Meander zu
wechseln. Dies wird durch die geometrische Gewundenheit, die *Tortuosität*,
\begin{align*}
    \tau = \frac{n-1}{L} \sum_{i=1}^{n} \left( \frac{L_i}{S_i}-1 \right).
\end{align*}
ermittelt, die an diesem Punkt maximal wird. Hier wird die Tour in $N$
Teilstücke mit gleichem Vorzeichen der Krümmung unterteilt und für jedes
Teilstück das Verhältnis von direkter Ende-zu-Ende-Distanz $S_i$ zu der
Länge entlang der Tour $L-i$ summiert.

Wir haben also kontinuierliche Phasenübergänge in der Schwierigkeit dieses
mittels linearer Programmierung detektiert und sie mit strukturellen Änderungen
des Verhaltens in Verbindung gebracht.
