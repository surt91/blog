Title: jsnake
Date: 2017-09-02 19:13
Category: Code
Tags: JavaScript, Game, Snake
Slug: jsnake
Status: draft

Bisher habe ich immer nur kurze Fragmente in JavaScript geschrieben, die
meist nur Gimmicks bezweckten oder Bibliotheken aufrufen. JavaScript ist im
Moment möglicherweise die wichtigste Sprache: Schließlich ist sämtlicher
clientseitige Code des Webs JavaScript -- und dank Node wohl auch nennenswerte
Teile des Servercodes. Zumindest macht man nichts falsch, wenn man sich etwas
mit Java vertraut macht.
Deshalb ist das neuste -- und simpelste -- Mitglied meiner Snake Sammlung
[[1]({filename}/snake.md), [2]({filename}/pysnake.md), [3]({filename}/msnake.md), [4]({filename}/rsnake.md)]
in JavaScript gehalten.

Ausprobieren kann man es gleich hier:

<canvas id="jsnake" class="fixed-size-400 center"></canvas>
<script async src="/js/jsnake/jsnake.js"></script>

In der Spielwelt herrschen helikale Randbedingungen, hauptsächlich weil es etwas
anderes ist als gewöhnliche periodische Ränder. Außerdem hat es den Vorteil,
dass man keinen Pause-Modus braucht, weil diese Randbedingungen dafür sorgen,
dass die Schlange sich nicht beißt, wenn man sie einfach geradeaus laufen lässt.

Da es nur ein paar Zeilen sind und sich ein ganzes GitHub Repository nicht lohnt,
habe ich es in einen [Gist](https://gist.github.com/surt91/42eb076974e325433b66a5077d4623eb)
hochgeladen.
