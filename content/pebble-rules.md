Title: Pebble Rules
Date: 2017-12-10 15:57
Author: surt91
Category: Code
Tags: Bild, C, Code, GitHub, Tech
Slug: pebble-rules
LargeFeaturedImage: img/pebble-rules.jpg
Status: published
Lang: de

Im letzten Monat habe ich jemanden getroffen, auf dessen [Armbanduhr eine MCMC Simulation von Hamilton-Pfaden](http://clisby.net/projects/pebble_app/)
auf einem quadratischen Gitter liefen. Ich war derartig begeistert, dass ich
beschlossen habe auch etwas auf meiner Pebble simulieren zu lassen. Aufgrund
der geringen Auflösung des Displays ($144 \times 168$) bieten sich "blockige"
Visualisierungen an. Glücklicherweise habe ich schon genügend Spielereien
geschrieben, die sich eignen
[[1]({filename}/labyrinthartiger-zellularer-automat.md),
    [2]({filename}/depth-first-search-und-labyrinthe.md),
    [3]({filename}/rule-90.md),
    [4]({filename}/conways-game-of-life.md)].

Pebble wurde zwar inzwischen von Fitbit aufgekauft, aber das SDK ist noch
verfügbar. Die neueren Exemplare lassen sich per JavaScript programmieren,
meine "Kickstarter Edition" aus der ersten Generation allerdings noch nicht.

Da ich meine Uhr also in C programmieren muss, konnte ich allerdings den
den alten Code aus [Wolfram's Rules]({filename}/rule-90.md) wiederbenutzen.

<video controls loop autoplay poster="/img/pebble-rules.jpg" width="800" height="1000" class="fixed-size-800">
<source src="/vid/pebble-rules.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

Der Code ist auf [GitHub](https://github.com/surt91/pebble-wolfram) verfügbar.
