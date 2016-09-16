Title: Depth First Search und Labyrinthe
Date: 2013-12-15 12:30
Author: surt91
Category: code
Tags: Python, Video, NetworkX, GitHub
Slug: depth-first-search-und-labyrinthe
Status: published

Wenn man alle Knoten eines Graphen besuchen möchte, sind eine Breitensuche oder 
eine Tiefensuche die offensichtlichen Algorithmen dafür.

1.  Man starte an einem Knoten.
2.  Man schiebe die noch nicht besuchten Nachbarn auf einen Stack (für
    die Tiefensuche) oder eine Queue (für die Breitensuche).
3.  Man entnehme einen Knoten vom Stack/Queue und fahre bei 2. fort, bis
    der Stack/Queue leer ist.

Der beste Anwendungsfall für die Tiefensuche, wenn man ein bisschen Zufall in 
den Algorithmus mischt, ein Labyrinth zu bauen und davon ein Video zu erstellen!

<video controls="controls" height="450" type="video/webm" width="800">
<source src="vid/DFSLabyrinth.mp4"></source>
</video>

Bei dieser Gelegenheit muss `NetworkX` erwähnt werden. Ein Python
Modul, das sehr schöne Klassen für Graphen bereitstellt und perfekt geeignet
ist, um schnell Prototypen von Graphalgorithmen zu testen.

Der Code ist als [Gist auf GitHub](https://gist.github.com/surt91/7790052) verfügbar.
