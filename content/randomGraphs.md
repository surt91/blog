Title: A Graph a Day
Date: 2017-05-13 17:36
Author: surt91
Category: Code
Tags: Physik, Bild, Python, Code
Slug: randomGraphs
LargeFeaturedImage: img/agraphaday.png
Status: published

Vor einiger Zeit habe ich @randomGraphs geschrieben, ein Twitterbot,
der Zufallsgraphen tweetet -- einen pro Tag.

<blockquote class="twitter-tweet" data-lang="de"><p lang="en" dir="ltr">Relaxed Caveman Graph (36 nodes) <a href="https://t.co/L4vNBbvSQ5">pic.twitter.com/L4vNBbvSQ5</a></p>&mdash; A Graph A Day (@randomGraphs) <a href="https://twitter.com/randomGraphs/status/848499540361703428">2. April 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Die meisten Graphtypen, die er darstellen kann stammen aus der NetworkX
Bibliothek und die Darstellung übernimmt Cytoscape oder
[graph-tool](https://graph-tool.skewed.de/) (dessen Autor diesem Bot folgt).

Bei diesem Projekt habe ich exzessiv Gebrauch von Pythons `Decorator` und
`Introspection` gemacht, sodass man, um einen neuen Typ Graph einzuführen
nur eine Methode schreiben muss, die eine Graph Datenstruktur zurück gibt,
Einstellungen, welche Darstellungen erlaubt sind, werden per `decorator`
getätigt und alle Methoden werden automatisch zum Pool hinzugefügt aus dem,
der Zufallsgenerator zieht.

Eine typische Methode sieht also so aus.

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

Die `@synonym` Decorators ermöglichen die zweite Funktion des Bots, denn
er tweetet nicht nur einmal am Tag einen zufälligen Graphen, sondern reagiert
auch auf Mentions. Falls in der Mention der Name der Mehtode oder eines der
per `@synonym` registrierten Worte auftaucht, antwortet er mit einem Bild des
entsprechenden Graphen. Dank des `fuzzywuzzy` Pakets ist es sogar resistent
gegen Tippfehler.

![Graph]({filename}/img/agraphaday.svg)

Da Twitter leider keine Vektorgrafiken unterstützt und alles, was keine
transparenten Pixel enthält in stark komprimierte `.jpg` wandelt, was gerade
bei diesen Graphen zu störenden Artefakten führt, füge ich einen Rand aus
transparenten Pixeln hinzu. Somit ergeben sich ansehnliche `.png`.

Der komplette Quellcode ist auf [Github](https://github.com/surt91/AGraphADay).
