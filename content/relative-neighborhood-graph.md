Title: Relative Neighborhood Graph
Date: 2016-10-02 15:34
Author: surt91
Category: Code
Tags: Python, Video, NetworkX
Status: published
Lang: de

<video controls loop autoplay width="100%">
<source src="/vid/rng.mp4" type="video/mp4"></source>
Your browser does not support the video tag.
</video>

Zu jedem Zeitpunkt ist im obigen Video ein Relative Neighborhood Graph (RNG) zu
sehen. Der RNG verbindet Knoten miteinander, die nahe beieinander sind.
Für die Knotenmenge $V$ muss also eine Metrik definiert sein, sodass eine
Distanz $d_{ij}$ zwischen zwei Knoten definiert ist. Dann verbindet der RNG
alle Knoten, die die Bedingung
$$
    d_{ij} \le \max(d_{ik}, d_{kj}) \quad \forall k \in V\setminus\{i, j\}
$$
erfüllen.

Dementsprechend simpel kann man einen RNG erzeugen.

```python
import random

import networkx as nx
import matplotlib.pyplot as plt


def dist(n1, n2):
    """Euclidean distance"""
    return ((n1[0] - n2[0])**2 + (n1[1] - n2[1])**2)**0.5


def rng(G):
    """Insert edges according to the RNG rules into the graph G"""
    for c1 in G.nodes():
        for c2 in G.nodes():
            d = dist(c1, c2)
            for possible_blocker in G.nodes():
                distToC1 = dist(possible_blocker, c1)
                distToC2 = dist(possible_blocker, c2)
                if distToC1 < d and distToC2 < d:
                    # this node is in the lune and blocks
                    break
            else:
                G.add_edge(c1, c2)


if __name__ == "__main__":
    # generate some random coordinates
    coordinates = [(random.random(),random.random()) for _ in range(100)]

    G = nx.Graph()
    for x, y in coordinates:
        G.add_node((x, y), x=x, y=y)

    rng(G)

    # draw the graph G
    pos = {n: (n[0], n[1]) for n in G.nodes()}
    nx.draw_networkx_nodes(G, pos=pos, node_shape="o")
    nx.draw_networkx_edges(G, pos=pos)

    plt.show()
```

Interessanterweise tauchen alle Kanten des RNG auch in der Delaunay Triangulation
der gleichen Knotenmenge auf. Dies kann man nutzen, um RNGs in $\mathcal{O}(N \log N)$
zu konstruieren.

Meiner persönlichen Meinung nach, bildet der RNG mit dem Verhältnis von Knoten
zu Kanten ein ästhetisches Optimum.
