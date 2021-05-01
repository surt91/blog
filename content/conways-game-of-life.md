Title: Conway's Game of Life
Date: 2011-09-27 13:57
Author: surt91
Category: Code
Tags: GitHub, C, Video
Slug: conways-game-of-life
FeaturedImage: img/conway3.gif
Status: published
Lang: de

Damit man mental nicht ganz einrostet, habe ich gestern Abend
[Conway's Game of Life](http://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens)
in C geschrieben ([GitHub](https://github.com/surt91/conway)). Mit
[cairo](http://cairographics.org/) (deren Logo eine stabile
Konfiguration von Conway's Game of Life ist) werden die einzelnen Runden dann als
`.png` gespeichert. Und wenn ihr selber ein paar Startkonfigurartionen
schreiben wollt, sollte der Quellcode nicht allzu undurchschaubar sein.

Hier ein paar Ergebnisse mit imagemagick animiert:
`convert -delay 20 ./*png ./out2.gif`

![HWSS](/img/conway1.gif){width="600" height="60"}

![Pulsator](/img/conway2.gif){width="300" height="300"}

![Oktagon](/img/conway3.gif){width="285" height="285"}
