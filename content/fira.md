Title: Fira Code
Date: 2021-06-21 19:45
Category: Meta
Tags: Typographie, Code, Bild
Status: draft
Slug: fira
Lang: de

Fira ist eine [humanist](https://en.wikipedia.org/wiki/Sans-serif#Classification) Sans-Serif Schriftart,
die für FirefoxOS entwickelt wurde und wird zur Zeit für die Sans-Serif Typen, wie die Überschriften,
in diesem Blog genutzt. Aber eigentlich geht es mir hier um die Monospace Variante, die
später mit Ligaturen (und mehr) zu [Fira Code](https://github.com/tonsky/FiraCode) erweitert wurde.
Ich sehe bereits wie im Geist des Lesers die Frage
"Ligaturen in einer Monospace Type?!" auftaucht. Beziehungsweise "Was sind Ligaturen?" falls der Leser
kein Hobby-Typographie-Nerd ist.

![fi](/img/fi.png){: .icon}
Ligaturen sind Kontraktionen von mehreren Glyphen in eine Glyphe. Die typischen Ligaturen sind fi oder fl
(allerdings nicht in der Schriftart, in der diese Zeilen geschrieben sind, weshalb ich hier ein Bild
der fi Ligatur in [Computer Modern](https://de.wikipedia.org/wiki/Computer_Modern) zeige).
Ein paar Ligaturen haben sich mittlerweile zu eigenen Symbolen entwickelt, wie das Kaufmannsund &, das ursprünglich
eine Ligatur von *et* war (Latein für *und*). Aber dieses Konzept beißt sich anscheinend mit einer
Monotype Schrift, in der jeder Buchstabe die gleiche Breite hat. Der Clou an der Sache ist, dass
Fira Code Ligaturen für übliche Ausdrücke für mathematische Symbole in Programmiersprachen
wie >=, != und -> hat, die wie folgt dargestellt werden: `>=, !=, ->`.

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

[![A+A a+a, die Plus-Zeichen haben unterschiedliche vertikale Positionen](/img/fira_arith.png)](/img/fira_arith.png)

Ich persönlich weiß solche Details sehr wertzuschätzen. Es ist ein Beispiel dafür,
dass alle Aspekte unserer modernen Gesellschaft, so wenige Gedanken wir uns auch darum machen und
für wie trivial wir sie halten, zahllose Stunden Design und Entwicklung gekostet haben und ständig
verbessert werden. Typographie -- und um das klarzustellen, ich bin beileibe kein Experte -- fasziniert
mich. Schriften sind exakt, mit klar definierter Funktion, aber obwohl wir sie seit Jahrtausenden
benutzen, ist ihre Entwicklung noch lange nicht abgeschlossen. Mit jedem neuen Medium gibt es neue
Anforderungen. Marken haben steten Bedarf an individuellen Schrifttypen als Teil ihres Brandings.
Und für jede neue Anwendung gibt es andere Optimierungskriterien.

Und jedes Mal wenn in meinem Code `=` und `>` wieder zu `=>` verschmelzen, freue ich mich
wieder über die Magie und Ästhetik.
