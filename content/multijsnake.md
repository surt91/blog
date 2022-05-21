Title: multiJSnake
Date: 2021-09-26 9:27
Author: surt91
Category: Code
Tags: Java, JavaScript, Game, GitHub, Snake
Slug: multijsnake
Status: draft
Lang: de

Vor Kurzem habe ich ein Server-Client Snake in meine Liste von simplen
Snake-Clonen [[1]({filename}/snake.md), [2]({filename}/pysnake.md), [3]({filename}/msnake.md), [4]({filename}/rsnake.md), [5]({filename}/jsnake.md), [6]({filename}/restfulsnake.md)]
eingereiht. Wie ich in meinem Artikel ["RestfulSnake"]({filename}/restfulsnake.md)
bereits angedeutet hatte, habe ich es um eine Multiplayer Komponente erweitert.

Das grundlegende Design ist, dass der Server in festen Intervallen den nächsten Zeitschritt berechnet,
den Spielzustand an alle Spieler schickt und auf Steuerkommandos von den Spielern lauscht. Dass der
Server die gesamte Spiellogik verwaltet ist einerseits möglich, weil Snake einen relativ kleinen Zustand
hat und nicht extrem empfindlich auf Latenzen reagiert. Außerdem können Spieler nicht (so einfach) schummeln,
wenn der Spiel-Zustand auf dem Server berechnet wird.

Hier sehen wir auch schon das erste Problem für die alte Kommunikation per http: Da der Server nicht von sich aus
Nachrichten an die Clients schicken kann, müssten die Clients pollen, was zu einem ganzen Haufen an Problemen
führen kann (Poll kurz vor dem Tick zum nächsten Zeitschritt, Last, uneinheitliche Antwortzeiten und Races bei
schlechtem Netzwerk, ...)
Genau für diesen Zweck sind aber [Websocket](https://de.wikipedia.org/wiki/WebSocket)-Verbindungen wie geschaffen!
Da SpringBoot vernünftige Mechanismen mitbringt, um Websockets zu handhaben ist die Umstellung sogar
[vergleichsweise schmerzfrei](https://github.com/surt91/multiJSnake/commit/927f3bc02c9a3e024048b7d7111969c3cc304aff).

Das größte Problem ist nun, dass die meisten Leute "Rest" als synonym für "json über http" verstehen. Also
muss ein neuer Name her -- leider war "multisnake" auf Heroku schon belegt, sodass ich mit "multiJSnake"
subtil darauf hinweise, dass Java und JavaScript das fundament bilden.

Ausprobiert werden kann es auf [multijsnake.herokuapp.com](https://multijsnake.herokuapp.com/) und weitere
Spieler können durch einen Einladungslink in die eigene Session eingeladen werden. Die Quellen sind natürlich
auf Github: [github.com/surt91/multiJSnake](https://github.com/surt91/multiJSnake/tree/v0.2.0).

![multiJSnake](/img/multisnake.gif)
