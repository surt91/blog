Title: Labyrinthartiger Zellulärer Automat
Date: 2016-10-14 21:38
Author: surt91
Category: Code
Tags: Python, Video, GitHub
Status: published
Lang: de

Der wohl berühmteste zelluläre Automat ist vermutlich [Conway's Game of Life]({filename}/conways-game-of-life.md).
Er und nahe Verwandte sind geradezu lächerlich gut untersucht. [Das LifeWiki](http://www.conwaylife.com/)
gibt einen ganz guten Überblick.
Die Regeln sind einfach: Jede Zelle hat 8 Nachbarn, wenn genau 3 Nachbarn leben,
erwacht sie auch zum Leben, bei weniger als 2 oder mehr als 3 stirbt sie (23/3).
Wenn man die Regeln des Automaten ändert, kann man mit 12345/3 [labyrinth]({filename}/depth-first-search-und-labyrinthe.md)artige
Strukturen erzeugen.

<video controls width="100%" poster="/img/cellular_maze.png">
<source src="/vid/cellular_maze.mp4" type="video/mp4"></source>
Your browser does not support the video tag.
</video>

Der Code ist als [Gist auf GitHub](https://gist.github.com/surt91/610615d7204a8994ed1145be710df130) verfügbar.
