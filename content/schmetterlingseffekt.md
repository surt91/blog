Title: Schmetterlingseffekt
Date: 2012-05-15 23:04
Author: surt91
Category: Code
Tags: Physik, C, Bild, Python, GitHub, Chaos
Slug: schmetterlingseffekt
Status: published
Lang: de

Differentialgleichungen numerisch zu lösen macht mehr Spaß, als man
erwarten würde, wenn man es hört. Und sobald man den ersten
[Runge-Kutta](http://de.wikipedia.org/wiki/Klassisches_Runge-Kutta-Verfahren)-Algorithmus
in einer kommerziellen Interpretersprache geschrieben hat, bemerkt man,
dass dieses Skript doch recht lange braucht.

Für dieses Problem gibt es zwei Lösungen: Entweder wird man zum Guru und
wendet irgendeine okkulte Matlab-Magie an, um das Programm schneller
laufen zu lassen, oder man schreibt das Programm in einer schönen
Sprache neu. In C zum Beispiel.

![Lorenzattraktor]({filename}/img/lorenzattraktor.png)

Ich habe mich für den einfachen Weg
entschieden und wenig überraschend eine Tempoverbesserung von Faktor
$\sim 140$ festgestellt. Jedenfalls für diesen
[Lorenzattraktor](http://de.wikipedia.org/wiki/Lorenzattraktor).
\begin{align}
    \dot{X} &= a(Y - X) \\
    \dot{Y} &= X(b - Z) - Y \\
    \dot{Z} &= XY - cZ \\
\end{align}
Geplottet habe ich die Werte dann mit [Python und matplotlib](http://matplotlib.sourceforge.net/examples/mplot3d/lines3d_demo.html).

Warum ich den Titel
"[Schmetterlingseffekt](http://de.wikipedia.org/wiki/Schmetterlingseffekt#Wissenschaftlicher_Hintergrund)"
gewählt habe? Naja, das Bild hier sieht ein wenig nach einem
Schmetterling aus. Und tatsächlich wurde der Schmetterlingseffekt nach diesem
Differentialgleichungssystem benannt -- und nicht nach der Geschichte aus
*Jurassic Park*.

> Er bewegt in Peking die Flügel, und
> im Central Park gibt's Regen statt Sonne.
>
> -- <cite>Dr. Ian Malcolm</cite> (1993)

Wie genau der [Lorenzattraktor mit Chaos zusammenhängt, habe ich in diesem
Post dargestellt]({filename}/seltsamer-attraktor.md).

Der Quellcode ist als [Gist auf GitHub](https://gist.github.com/surt91/54cdc0bcd86bae19c22b4856889ea519).
