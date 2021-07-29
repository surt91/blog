Title: RestfulSnake
Date: 2021-07-29 13:48
Author: surt91
Category: Code
Tags: Java, JavaScript, Game, GitHub, Snake
Slug: restfulsnake
Status: published
Lang: de

Vor wenigen Monaten hatte ich eine Handvoll Bewerbungsgespräche und von "Programmieraufgaben",
die durch das Erkennen der Fibonacci-Sequenz gelöst wurden bis zu "Wie viele Grashalme
gibt es in deiner Heimatstadt?" war alles dabei. Unter anderem auch "Wir wissen,
dass du noch nie Java angefasst hast, deshalb sollst du ein Programm in Java schreiben,
über das wir nächste Woche reden können!"

Also bin ich jetzt Java-Experte. Und das bedeutet, dass es Zeit ist für eine weitere
Snake-Version [[1]({filename}/snake.md), [2]({filename}/pysnake.md), [3]({filename}/msnake.md), [4]({filename}/rsnake.md), [5]({filename}/jsnake.md)].

Um besonders professionell zu wirken, habe ich mich für eine *Client-Server-Architektur*
entschieden. Steuerkommandos werden per `http` `post` zum Server geschickt und in der Antwort
steht die neue Position der Schlange.
Das Backend nutzt *Spring Boot* und läuft auf einem Tomcat Server. Das
Frontend besteht hauptsächlich aus dem Visualisierungs-Code von [jsnake]({filename}/jsnake.md),
aber echte Nerds werden es natürlich bevorzugen per *curl* zu spielen.

Normalerweise würde man es natürlich mittels Kubernetes und Docker auf AWS laufen lassen, aber
stattdessen habe ich mich dafür entschieden Heroku zu nutzen, um ein
[kleines Unternehmen](https://en.wikipedia.org/wiki/Salesforce) zu unterstützen.
Auf [restfulsnake.herokuapp.com](https://restfulsnake.herokuapp.com/) kann man also eine Partie
spielen. Und die Quellen liegen wie immer auf [GitHub](https://github.com/surt91/restfulsnake)

Überraschenderweise funktioniert das tatsächlich erstaunlich gut -- solange die Latenz unter ~150 ms bleibt.
Und dieses Design schreit geradezu nach einen Multiplayer-Modus...
