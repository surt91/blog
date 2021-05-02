Title: A Graph a Day
Date: 2017-05-13 17:36
Author: surt91
Category: Code
Tags: Physik, Bild, Python, Code
Slug: randomGraphs
LargeFeaturedImage: img/agraphaday.png
Status: published
Lang: de

Vor einiger Zeit habe ich [@randomGraphs](https://twitter.com/randomGraphs)
geschrieben: Ein Twitterbot, der einen Zufallsgraphen pro Tag tweetet.

Die meisten Graphtypen, die er darstellen kann stammen aus der NetworkX
Bibliothek oder sind reale Netzwerke. Ein paar [Proximity]({filename}/proximity-graphs.md)
[Graphs]({filename}/relative-neighborhood-graph.md) habe ich selbst geschrieben.
Die Darstellung und gegebenenfalls das Layout übernimmt Cytoscape oder
[graph-tool](https://graph-tool.skewed.de/) (dessen Autor diesem Bot folgt).

Bei diesem Projekt habe ich exzessiv Gebrauch von Pythons `Decorator` und
`Introspection` gemacht, sodass man, um einen neuen Graphtyp einzuführen
nur eine Methode schreiben muss, die eine Graph-Datenstruktur zurück gibt.
Einstellungen, welche Darstellungen erlaubt sind, werden per `decorator`
getätigt und alle Methoden werden per Introspection automatisch zum Pool
hinzugefügt, aus dem der Zufallsgenerator zieht.

Eine typische Methode sieht etwa so aus.

```python
@synonym("Barabasi Albert")
@synonym("preferential attachment")
@style(styles_all)
@layout(["kamada-kawai", "force-directed", "sfdp", "fruchterman_reingold", "arf", "radial_tree"])
def generateBarabasiAlbert(self, N=None, m=None, **kwargs):
    if N is None: N = random.randint(4, 400)
    if m is None: m = random.randint(1, 5)

    G = gen.barabasi_albert_graph(N, m)  # gen is networkx Generator
    details = dict(name="Barabási-Albert Graph", N=N, m=m, seed=self.seed,
                   template="{name}, N = {N}, m = {m}")

    return G, details
```

Und liefert für $N=226, m=1$ und das `radial_tree` Layout beispielsweise
diesen Graph. Die Größe der Knoten wird hier von der
[Betweenness Centrality](https://en.wikipedia.org/wiki/Betweenness_centrality)
bestimmt.

![Graph](/img/barabasi.png)

Die `@synonym` Decorators ermöglichen die zweite Funktion des Bots, denn
er tweetet nicht nur einmal am Tag einen zufälligen Graphen, sondern reagiert
auch auf Mentions. Falls in der Mention der Name der Methode oder eines der
per `@synonym` registrierten Worte auftaucht, antwortet er mit einem Bild des
entsprechenden Graphen. Dank `fuzzywuzzy` ist es sogar resistent gegen
Tippfehler.

Twitter unterstützt leider keine Vektorgrafiken und wandelt Bilder gerne in
stark komprimierte `.jpg`, was gerade bei diesen Graphen zu störenden
Artefakten führt. Dagegen hilft es, wenn ich einen Rand aus transparenten
Pixeln dem Bild hinzufüge. Das führt dazu, dass Twitter `.jpg` nicht als
geeignetes Format ansieht und die Bilder im verlustfreien `.png` ausliefert.

```bash
convert -alpha on -channel RGBA -bordercolor "rgba(0,0,0,0)" -border "1x1" input.png output.png
```

![Graph](/img/agraphaday.png)

Der komplette Quellcode ist auf [Github](https://github.com/surt91/AGraphADay).
