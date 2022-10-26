Title: Fira Code
Date: 2021-06-21 19:45
Category: Meta
Tags: Typographie, Code, Bild
Status: published
Slug: fira
Lang: de

Fira ist eine [humanist](https://en.wikipedia.org/wiki/Sans-serif#Classification) Sans-Serif Schriftart,
die für FirefoxOS entwickelt wurde, und wird zur Zeit für die Sans-Serif Typen, wie die Überschriften,
in diesem Blog genutzt. Aber eigentlich geht es mir hier um Fira Mono die
[dicktengleiche](https://de.wikipedia.org/wiki/Nichtproportionale_Schriftart) Variante, die
später mit Ligaturen (und mehr) zu [Fira Code](https://github.com/tonsky/FiraCode) erweitert wurde.
Ich sehe wie in genau diesem Moment im Geist des Lesers die Frage
"Ligaturen in einer dicktengleichen Schrift?!" auftaucht. Beziehungsweise "Ist da ein Tippfehler in *dickengleich*?" oder
"Was sind Ligaturen?" falls der Leser kein Hobby-Typographie-Nerd ist.

Für letztere klären wir erstmal kurz die beiden Fragen:

Die *Dickte* bezeichnet die Breite der Metall-Lettern im klassischen Buchdruck; wenn sie für alle Glyphen
gleich ist, stehen die Buchstaben immer in perfekt ausgerichteten Spalten untereinander, was von vielen
für das Schreiben von Code bevorzugt wird. Die meisten Schreibmaschinen haben ebenfalls solche Schrifttypen
verwendet.

![fi](/img/fi.png){: .icon .invertable}
*Ligaturen* sind Kontraktionen von mehreren Glyphen in eine Glyphe. Die typischen Ligaturen sind fi oder fl
(allerdings nicht in der Schriftart, in der diese Zeilen geschrieben sind, weshalb ich hier ein Bild
der fi Ligatur in [Computer Modern](https://de.wikipedia.org/wiki/Computer_Modern) zeige).
Ein paar Ligaturen haben sich mittlerweile zu eigenen Symbolen entwickelt, wie das Kaufmannsund &, das ursprünglich
eine Ligatur von *et* war (Latein für *und*). Aber dieses Konzept beißt sich anscheinend mit einer
dicktengleichen Schrift, in der jeder Buchstabe die gleiche Breite haben soll. Der Clou an der Sache ist, dass
Fira Code Ligaturen für übliche Ausdrücke für mathematische Symbole in Programmiersprachen
wie >=, != und -> hat, die wie folgt dargestellt werden: `>=, !=, ->`. Nur zu, kopiert diese Symbole
in einen Editor eurer Wahl, um zu sehen, wie sie sich wieder in ihre Bestandteile zerlegen

Nur eine Spielerei? Möglicherweise. Aber ich bin begeistert davon, und verwende Fira Code in
allen Editoren, die Ligaturen unterstützen. Der Fairness halber sollte gesagt werden, dass Fira Code nicht
als erstes Projekt diese Idee hatte. [Hasklig](https://github.com/i-tu/Hasklig) beispielsweise hatte
ihr erstes Release 2 Jahre vor der Veröffentlichung von Fira Code im Jahr 2014. Und mittlerweile sind
Code-Ligaturen so ziemlich im Mainstream angekommen, seitdem
[JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) im letzten Jahr von
dem gleichnamigen IDE-Entwickler veröffentlicht wurde.

Zum Schluss möchte ich noch auf eine Kleinigkeit aufmerksam machen, die wohl nur die wenigsten Nutzer
von Fira Code bewusst bemerken würden, die aber zweifellos demonstriert wie durchdacht diese Schrift ist.
Denn Fira Code passt die Position von arithmetischen Symbolen an die benachbarten Glyphen an: ein `+`
zwischen zwei Großbuchstaben ist höher als eines zwischen zwei Kleinbuchstaben.

[![A+A a+a, die Plus-Zeichen haben unterschiedliche vertikale Positionen](/img/fira_arith.png)](/img/fira_arith.png){: .invertable}

Ich persönlich weiß solche Details sehr wertzuschätzen. Es ist ein Beispiel dafür,
dass alle Aspekte unserer modernen Gesellschaft, so wenige Gedanken wir uns auch darum machen und
für wie trivial wir sie halten, zahllose Stunden Design und Entwicklung gekostet haben und ständig
verbessert werden. Typographie -- und um das klarzustellen, ich bin beileibe kein Experte -- fasziniert
mich. Schriften sind exakt, mit klar definierter Funktion, aber obwohl wir sie seit Jahrtausenden
benutzen, ist ihre Entwicklung noch lange nicht abgeschlossen. Mit jedem neuen Medium gibt es neue
Anforderungen. Marken haben steten Bedarf an individuellen Schrifttypen als Teil ihres Brandings.
Für jede neue Anwendung gibt es andere Optimierungskriterien.

Und jedes Mal wenn in meinem Code `=` und `>` wieder zu `=>` verschmelzen, freue ich mich
erneut über die Magie.
