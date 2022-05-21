Title: Perfect Snake
Date: 2022-05-21 11:03
Author: surt91
Category: Code
Tags: Java, JavaScript, Python, Neural Networks, Game, GitHub, Snake
Slug: perfect-snake
Status: published
Lang: de

Ich habe auf diesem Blog schon über eine Reihe von Snake Clonen [[1]({filename}/snake.md), [2]({filename}/msnake.md), [3]({filename}/jsnake.md), [4]({filename}/restfulsnake.md), [5]({filename}/multijsnake.md)] geschrieben, die zum Teil auch Autopilot-Strategien hatten [[6]({filename}/pysnake.md), [7]({filename}/rsnake.md)].
Die Autopiloten waren zwar meist interessant anzusehen -- vor allem bei hohen Geschwindigkeiten -- aber bei weitem nicht perfekt.

Auch wenn der Titel etwas zu viel verspricht, schafft es dieser Autopilot (zumindest manchmal) perfekte Spiele zu spielen.

![Eine perfekte Partie Snake](/img/perfectsnake.gif)

Und falls dieses gif nicht überzeugt, kann man den Autopiloten online
-- dank TensorFlow.js -- direkt im Browser ausprobieren auf [snake.schawe.me](https://snake.schawe.me/).

Aber was steckt dahinter?

## Neuronale Netze

Wenn man nicht clever genug ist, eine direkte Lösung für ein Problem zu finden, kann man
versuchen ein Neuronales Netz auf die Lösung des Problems trainieren. Vor einigen Jahren
hat ein [Artikel](https://arxiv.org/abs/1312.5602), in dem ein neuronales Netz trainiert
wurde alte Atari-Spiele zu spielen, für mediale Aufmerksamkeit gesorgt. Und die gleiche
Idee des Reinforcement Learning werde ich hier (nicht als erster) auf Snake anwenden.

Die grundlegende Idee von Reinforcement Learning ist relativ einsichtig: Wir belohnen
das Modell für gute Entscheidungen, sodass es lernt mehr gute Entscheidungen zu treffen.
In unserem Fall ist das zu maximierende Kriterium die Länge der Schlange.

Glücklicherweise können wir auf die Literatur zurückgreifen, wie wir diese grundsätzliche
Idee umsetzen können. Das Modell, für das ich mich entschieden habe ist ein Actor-Critic
Ansatz. Dabei nutze ich ein neuronales Netz, das als Input den aktuellen Zustand des
Spielfeldes bekommt -- wie genau dieser Zustand aussieht, diskutieren wir weiter unten.
Dann geht es durch ein paar Schichten und endet in zwei "Köpfen". Einer ist der Actor,
mit drei OutputNeuronen, die für "nach links", "nach rechts" und "geradeaus weiter" stehen,
und der andere ist der Critic, der ein Output-Neuron hat, das abschätzt wie lang die
Schlange, ausgehend von der aktuellen Situation, noch werden kann.

Das Training läuft dann so ab, dass der Critic darauf trainiert wird möglichst gute
Schätzungen abzugeben und der Actors mit trainiert wird zu möglichst hohen Schätzungen
des Critic zu führen. Der gemeinsame Teil des neuronalen Netzes sollte im Idealfall also
ein "Verständnis" für das Spiel entwickeln. Genial!

## Technische Nebensächlichkeiten

Meine Implementierung benutzt die Python Bibliotheken Keras und Tensorflow zum Training
und [multiJSnake]({filename}/multijsnake.md) als *Environment*. Wir steuern also einen
Java-Prozess, um unser neuronales Netz in Python zu trainieren.
Diese Entscheidung ist etwas unorthodox, aber bot Potential für einen Blogpost auf dem
[Blog meines Arbeitgebers](https://blog.codecentric.de/2021/11/java-klassen-python/).

Wir können das Environment getrost als Black-Box betrachten, die dafür sorgt, dass die Regeln
von Snake befolgt werden.

## Lokale Informationen

Eine der wichtigsten Entscheidungen ist nun wie der Input in das Modell aussieht.
Die einfachste Variante, die sich auch gut zum Testen eignet, ist die lokale
Information rund um den Kopf der Schlange: Drei Neuronen, die jeweils 1 oder 0 sind,
wenn das Feld links, rechts und geradeaus vom Kopf belegt sind (und acht weitere für
etwas mehr Weitsicht auf die Diagonalen und übernächste Felder vorne, rechts links und
diesmal auch zurück). Damit die Schlange
auch das Futter finden kann, fügen wir noch 4 weitere Neuronen hinzu, die per 1 oder 0
anzeigen, ob das Futter nördlich, östlich, südlich oder westlich vom Kopf der Schlange
ist.

Dieser Input mit ein paar vollvernetzten Schichten im Netz reichen aus, damit
die Schlange nach ein paar hundert Trainingsspielen zielstrebig auf das Futter
steuert und sich selbst ausweicht. Allerdings reicht es noch nicht um zu verhindern,
dass sie sich selbst in Schlaufen fängt. Da war der Autopilot von
[rsnake]({filename}/rsnake.md) besser.

![Layout des Neural Networks (Visualisierung: netron)](/img/nn_local.svg)

## Globale Informationen

Um der Schlange eine Chance zu geben zu erkennen, dass sie sich gerade selbst fängt,
sollte man ihr erlauben das ganze Spielfeld zu sehen -- schließlich sehen menschliche
Spieler auch das ganze Spielfeld. Bei einem $10 \times 10$ Spielfeld haben wir also
schon mindestens 100 Input-Neuronen, sodass vollvernetzte Schichten zu sehr großen
Modellen führen würden. Stattdessen bietet es sich bei solchen zweidimensionalen
Daten an [*convolutional* neuronale Netze](https://en.wikipedia.org/wiki/Convolutional_neural_network)
zu nutzen. Um es unserer Schlange etwas einfacher zu machen, werden wir unser Spielfeld
in drei Kanäle aufteilen:

* der Kopf: nur an der Position des Kopfes ist eine 1, der Rest ist 0
* der Körper: die Positionen an denen sich der Körper befindet zeigen wie viele Zeitschritte der Körper noch an dieser Position sein wird
* das Futter: nur an der Position des Futters ist eine 1, der Rest ist 0

Also zeigen wir der Schlange das Feld praktisch mit drei Farbkanälen.

Und damit die Schlange nicht auch noch lernen muss was rechts und links bedeutet,
geben wir dem Actor 4 Outputs, die für Norden, Osten, Süden und Westen stehen.

![Layout des Convolutional Neural Networks (Visualisierung: netron)](/img/nn_global.svg)

Die Details welche Parameter ich für das Modell gewählt habe, kann auf
[github.com/surt91/multiJSnake](https://github.com/surt91/multiJSnake)
nachgeschlagen werden. Aber es funktioniert nach einigen zehntausend
Trainingsspielen gut genung, um regelmäßig perfekte Spiele auf einem
$10 \times 10$ Spielfeld zu erreichen. Aber da ich es nur auf  $10 \times 10$
Feldern trainiert habe, versagt es leider auf jeder anderen Größe.
