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

TODO: Technik, websockets, vor Veröffentlichung frontend aufhübschen

Und jetzt noch eine viel zu lange Anmerkung, weshalb ich das Projekt von
"RestfulSnake" in "multiJSnake umbenannt habe.

"Restful" wird heutzutage meist synonym mit "JSON API over HTTP" genutzt.
So auch von mir in der Namensgebung von [RestfulSnake]({filename}/restfulsnake.md).
Allerdings ist wohl ein fundamentaler Anspruch, dass außer dem Einstiegspunkt
keine Endpoints bekannt zu sein brauchen, wie ich durch folgendes Zitat des
Vaters von [REST](https://en.wikipedia.org/wiki/Representational_state_transfer)
untermauern möchte:

> A REST API should be entered with no prior knowledge beyond the initial URI [...]
>
> -- <cite>[Roy T. Fielding](https://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven)</cite> (2008)

Stattdessen sollen alle Antworten *Hypermedia* sein, also Links zu verwandten
Endpoints enthalten. So wie man nur die Domain meines Blogs zu kennen braucht
und alle Artikel von dort durch links erreichen kann.

Mein Ansatz hingegen koppelt Client und Server durch feste Endpoints.

Außerdem bin ich für multiJSnake größtenteils von HTTP auf Websockets
als Protokoll umgestiegen -- auch wenn Restful eigentlich nichts mit
dem Protokoll zu tun haben sollte, wird es gefühlt fast ausschließlich
für HTTP verwendet.
