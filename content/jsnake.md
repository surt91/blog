Title: jsnake
Date: 2017-09-24 15:50
Category: Code
Tags: JavaScript, Game, Snake
Slug: jsnake
Status: draft

Bisher habe ich immer nur kurze Fragmente in JavaScript geschrieben, die
meist nur Gimmicks bezweckten oder Bibliotheken aufrufen. JavaScript ist im
Moment möglicherweise die wichtigste Sprache: Schließlich ist sämtlicher
clientseitiger Code des Webs JavaScript -- und dank Node wohl auch nennenswerte
Teile des Servercodes. Zumindest macht man nichts falsch, wenn man sich etwas
mit JavaScript vertraut macht.
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

Ich habe versucht möglichst moderne Features zu nutzen. Tatsächlich scheint mir
diese Sprache einige interessante Sprachelemente erhalten zu haben, wie *arrow
functions* `x => x*x` für lambdas oder den *spread operator* `...` den ich am
ehesten mit Pythons *splat* `*` vergleichen möchte.
Insgesamt werden dadurch solche Monster wie das folgende kartesische Produkt
möglich:

```JavaScript
var SIZE = 3;
[].concat(
    ...[...Array(SIZE).keys()].map(
        x => [...Array(SIZE).keys()].map(
            y => [x, y]
        )
    )
);
```

Anscheinend gibt es mit der nächsten geplanten Version (ES6) noch mehr nette
Sprachelemente. Unter anderem [Module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import).
Ich bin geradezu sprachlos, dass man bisher keine Sprachunterstützung für
die Verteilung des Quellcodes über mehrere Dateien hatte. Anscheinend bin ich
noch zu sehr von den Konzepten der "C-artigen" Sprachen beeinflusst.

Da `jsnake` nur ein paar Zeilen in einer Datei sind und sich ein ganzes GitHub
Repository deshalb nicht lohnt, habe ich es in einen [Gist](https://gist.github.com/surt91/42eb076974e325433b66a5077d4623eb)
hochgeladen.
