Title: Depth First Search und Labyrinthe
Date: 2013-12-15 12:30
Author: surt91
Category: Code
Tags: Python, Video, GitHub
Slug: depth-first-search-und-labyrinthe
LargeFeaturedImage: img/maze.png
Status: published
Lang: de

Ein Algorithmus, von dem jeder schoneinmal gehört haben sollte, ist die
Tiefensuche (Depth First Search). Wenn man Zusammenhangskomponenten in einem
Graphen finden will oder nach einem bestimmten Knoten in einem Graphen sucht,
ist die Tiefensuche meist der einfachste und oft ein geeigneter Algorithmus
mit einer Zeitkomplexität $\mathcal{O}(N+M)$, die linear in der Anzahl der
Knoten und der Kanten ist. Da man gefühlt alle Graphalgorithmen am besten
rekursiv beschreiben kann, folgt hier eine (nichtrigorose) Beschreibung.

1.  Man startet die Tiefensuche an einem beliebigen Knoten.
2.  Bei jedem noch nicht besuchten Nachbarn startet man wieder eine Tiefensuche.

Aber was macht man im Alltag mit einer Tiefensuche?
Meine Antwort darauf ist: Labyrinthe bauen.

<video controls width="100%" poster="/img/maze.png">
<source src="/vid/maze.mp4" type="video/mp4"></source>
Your browser does not support the video tag.
</video>

Bei dieser Gelegenheit muss `NetworkX` erwähnt werden. Ein Python
Modul, das sehr schöne Klassen für Graphen bereitstellt und perfekt geeignet
ist, um schnell Prototypen von Graphalgorithmen zu testen.

Der Code ist als [Gist auf GitHub](https://gist.github.com/surt91/7790052) verfügbar.
