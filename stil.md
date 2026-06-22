# Stil-Guide für blog.schawe.me

Dieses Dokument beschreibt den Sprachstil, die Themenwahl, die Struktur und die
technischen Konventionen der Blogeinträge auf [blog.schawe.me](https://blog.schawe.me)
(Sitename: *möchtegerngeek*). Ziel ist es, dass anhand dieser Anleitung ein
Gastbeitrag verfasst werden kann, der nahtlos in das bestehende Konzept passt.

Das Motto des Blogs fasst die Themenwahl zusammen:

> Dinge, die ich für hübsch, praktisch oder interessant halte.

---

## 1. Das Wesen des Blogs in einem Satz

Ein technisch versierter, neugieriger Autor stellt seine eigenen kleinen
Programmier-, Physik- und Mathe-Spielereien vor – mit Begeisterung für Eleganz und
Schönheit, trockenem Humor und immer einem Link zum Quellcode am Ende.

---

## 2. Sprachstil und Tonfall

**Sprache:** Primär Deutsch. Einige Beiträge haben zusätzlich eine englische
Fassung (siehe Abschnitt 7). Englische Fachbegriffe werden selbstverständlich
eingestreut (*Reinforcement Learning*, *Actor-Critic*, *Prompts*) und meist
*kursiv* gesetzt, wenn sie eingeführt werden.

**Perspektive:** Erste Person Singular („ich habe … geschrieben“, „ich habe mich
für den einfachen Weg entschieden“). Beim Durchgehen einer Herleitung oder eines
Algorithmus wechselt der Text ins erklärende „wir“ („Unser Ziel ist es …“, „dazu
erweitern wir Patience Sort“, „wir schreiben jedes Element auf eine Karte“).

**Grundton:** Locker, gesprächig, selbstironisch und mit trockenem Humor. Der
Autor nimmt sich selbst nicht zu ernst, ist aber fachlich präzise. Beispiele:

- Selbstironie über den eigenen Code:
  > „… ist meiner dennoch sehenswert, da er SHA-256 in 256 Zeilen darstellt.“
  > „Auch wenn der Titel etwas zu viel verspricht, schafft es dieser Autopilot
  > (zumindest manchmal) perfekte Spiele zu spielen.“
- Augenzwinkernde Übertreibung:
  > „Aus diesem Grund sollte ein Doppelpendel auf keinem Schreibtisch fehlen und
  > bietet sich als grandiose Geschenkidee für Physiker an.“
- Begeisterung wird offen gezeigt, oft als kurzer Ausruf am Absatzende:
  > „Genial!“ — „freue ich mich erneut über die Magie.“ — „Man sollte alles nach
  > Wellenlänge sortieren!“

**Leseransprache:** Der Leser wird direkt eingebunden und seine Gedanken werden
vorweggenommen:
> „Ich sehe wie in genau diesem Moment im Geist des Lesers die Frage … auftaucht.“
> „Nur zu, kopiert diese Symbole in einen Editor eurer Wahl …“
> „Wer kennt das nicht: Man hat sich ein Python Skript geschrieben …“

**Fachjargon wird erklärt:** Begriffe werden eingeführt und kurz definiert, bevor
sie verwendet werden („Die *Dickte* bezeichnet die Breite der Metall-Lettern …“,
„*Ligaturen* sind Kontraktionen von mehreren Glyphen …“). Wikipedia-Links
(bevorzugt `de.wikipedia.org`) ergänzen Begriffe für Neugierige.

**Typografische Eigenheiten:**
- Der doppelte Bindestrich `--` (Gedankenstrich) leitet Einschübe und Pointen
  ein: „… in einer schönen Sprache neu. In C zum Beispiel.“ / „numerisch ist es
  kein Problem“. (`TYPOGRIFY` wandelt `--` beim Rendern in einen Halbgeviertstrich.)
- Hervorhebungen mit *Kursiv* für Fachbegriffe bei der Einführung.
- Inline-Code in Backticks für Befehle, Dateinamen, Operatoren (`make`, `Makefile`, `>=`, `!=`).

---

## 3. Themenwahl

Die Beiträge drehen sich fast immer um **eigene Projekte und Experimente** des
Autors. Wiederkehrende Themen:

- **Rekreative Informatik / eigene Implementierungen:** Snake-Klone in diversen
  Sprachen, Conway's Game of Life, zelluläre Automaten, SHA-256 „in 256 Zeilen“,
  Tic-Tac-Toe.
- **Physik & Chaos:** Doppelpendel, Dreikörperproblem, Lorenz-Attraktor /
  Schmetterlingseffekt, Differentialgleichungen numerisch lösen, Ising-Modell.
- **Mathematik & Visualisierung:** Fraktale, Lissajous-Figuren, Proximity-Graphs,
  Oberflächenkachelungen mit TikZ.
- **Machine Learning:** neuronale Netze (Snake-Autopilot, Stable Diffusion,
  GPT-2-Prompt-Generierung), Twitter-Bots.
- **Eigene wissenschaftliche Veröffentlichungen:** allgemeinverständlich aufbereitet
  (TSP, Longest Increasing Subsequences, konvexe Hüllen in hohen Dimensionen),
  mit `Doi:`-Feld in den Metadaten.
- **Werkzeuge & Tooling:** `make`, git-Tricks, LaTeX/TikZ/Gnuplot, Pelican, PWA.
- **Snips / Oneliner:** sehr kurze, nützliche Befehls-Schnipsel (ffmpeg, optipng,
  ssh-Tricks) zum späteren Nachschlagen.
- **Hardware & Heimautomatisierung:** Raspberry Pi, ESPHome, Home Assistant.
- **Meta & Typografie:** das Blog selbst, Schriftarten (Fira Code).
- **Misc / Ästhetik:** gelegentlich ein einzelnes hübsches Bild mit Pointe.

Roter Faden: ein konkretes, oft kleines technisches Artefakt (ein Bild, ein Video,
ein Algorithmus, ein Befehl), das vorgestellt, eingeordnet und mit Quellcode belegt
wird. Der Autor schreibt explizit auch für sich selbst – „Dinge, … die ich so
nützlich finde, dass ich sie später nachschlagen will.“

---

## 4. Struktur eines typischen Beitrags

Die Länge variiert stark: von zweizeiligen Bild-Posts bis zu langen, mit
Überschriften gegliederten Erklärstücken. Es gibt drei grobe Archetypen.

### A) Der Mini-Post (2–5 Zeilen)
Ein Bild oder eingebettetes Widget plus eine pointierte Zeile. Beispiel komplett:
```markdown
![Der Grüne Punkt](/img/grunerPunkt.jpg)

Das Yin und Yang der Moderne.
```

### B) Der Standard-Post (1–4 Absätze)
Die häufigste Form. Aufbau:
1. **Hook / Einstieg:** ein persönlicher, oft humorvoller Aufhänger oder direkt
   das Ergebnis (Bild/Video).
2. **Einordnung:** Was ist das, warum ist es interessant, etwas Kontext oder
   Theorie (gern mit einer Formel oder einem Code-Schnipsel).
3. **Pointe & Quellcode-Link:** ein abschließender Gedanke und fast immer ein Link
   zum Code (GitHub-Repo oder Gist).

### C) Der Lang-Post (mit `##`-Überschriften)
Für komplexere Projekte (z. B. *Perfect Snake*, Paper-Erklärungen). Gegliedert mit
Markdown-Überschriften der Ebene `##`. Typische Dramaturgie: Motivation →
Grundidee → technische Umsetzung (ggf. mehrere Abschnitte) → Ergebnis/Demo →
ehrliche Einordnung der Grenzen → Link zum Code. Auch hier wird der Leser an der
Hand genommen und die Lösung schrittweise entwickelt.

**Schlusspointe:** Nahezu jeder Beitrag endet mit einem Verweis auf den Quellcode
(„Der Quellcode ist als [Gist auf GitHub] …“) und/oder einem kleinen, runden
Abschlussgedanken. Bei Mini-Posts ist die letzte Zeile die Pointe.

---

## 5. Metadaten (Pelican Front Matter)

Jeder Beitrag beginnt mit Pelican-Metadaten (kein YAML, sondern `Key: Value`-Zeilen,
durch eine Leerzeile vom Inhalt getrennt). Vorlage:

```markdown
Title: Aussagekräftiger Titel
Date: 2024-01-15 18:30
Author: surt91
Category: Code
Tags: Python, Bild, GitHub
Slug: aussagekraeftiger-titel
LargeFeaturedImage: img/teaser.webp
Status: published
Lang: de
```

**Pflichtfelder** (in praktisch jedem Post): `Title`, `Date` (`YYYY-MM-DD HH:MM`),
`Category`, `Status: published`, `Lang` (`de` oder `en`). Sehr häufig zusätzlich
`Slug` (kebab-case, ASCII) und `Author: surt91`. `Tags` sind üblich, aber bei
Snips oft weggelassen.

**Optionale Felder:**
- `LargeFeaturedImage:` bzw. `FeaturedImage:` – Teaserbild (Pfad relativ zu `content`, z. B. `img/foo.webp`).
- `Doi:` – bei Beiträgen über eigene Veröffentlichungen (aktiviert das `doi_details`-Plugin).

**Kategorien** (genau eine pro Post, feste Auswahl):
| Kategorie | Verwendung |
|-----------|------------|
| `Code`    | Programmierprojekte (mit Abstand am häufigsten) |
| `Snip`    | kurze Oneliner / Befehls-Schnipsel (Ordner `oneliner/`) |
| `Meta`    | über das Blog, Typografie, Tooling-Setup |
| `Phys`    | Physik, eigene Paper |
| `Tech`    | Hardware, Gadgets |
| `Misc`    | Ästhetik, Sonstiges |

**Häufige Tags** (frei, aber konsistent großgeschrieben): `GitHub`, `Python`,
`Bild`, `Code`, `Physik`, `Video`, `Game`, `C`, `Snake`, `JavaScript`, `Chaos`,
`Rust`, `Formel`, `Java`, `Neural Networks`, `Veröffentlichung`, `Twitter-Bot`,
`TikZ`, `LaTeX`, `Gnuplot`, `Statistik`. Tags benennen Programmiersprache,
Medientyp (`Bild`, `Video`, `Formel`) und Thema.

Dateiname: `content/<slug>.md` (Snips unter `content/oneliner/`, englische Fassungen
unter `content/en/`).

---

## 6. Technische Bausteine im Markdown

**Bilder** mit beschreibendem Alt-Text (dient zugleich als Bildunterschrift). Bilder,
die auf dunklem Theme invertiert werden sollen, erhalten die Klasse `{: .invertable}`
(typisch für Diagramme/Plots mit weißem Hintergrund, nicht für Fotos). Optional als
Link auf eine größere Version:
```markdown
![Eine längste aufsteigende Teilfolge](/img/lis_example.png){: .invertable}

[![Lorenzattraktor](/img/lorenzattraktor1200.webp)](/img/lorenzattraktor.png)
```

**Videos** werden als HTML eingebettet (oft mit Poster-Bild):
```html
<video controls width="100%" poster="/img/doublePendulum.png">
<source src="/vid/doppelpendel.mp4" type="video/mp4"></source>
</video>
```

**Mathematik** via MathJax. Inline mit `$…$`, abgesetzt mit `$$…$$` oder
`\begin{align}…\end{align}` / `\begin{align*}…\end{align*}`:
```markdown
Die Differentialgleichungen für die Winkel $\vartheta_1$ und $\vartheta_2$:

\begin{align}
    \dot{X} &= a(Y - X) \\
    \dot{Y} &= X(b - Z) - Y \\
    \dot{Z} &= XY - cZ
\end{align}
```

**Code** in Fenced Blocks mit Sprachangabe (`python`, `rust`, `c`, `bash`, `make`,
`java`, …). Kurze Inline-Befehle in Backticks. Längerer Code wird ausgelagert und
verlinkt, statt den Lesefluss zu stören:
> „Der Code ist als Gist auf GitHub, da er in seinen 256 Zeilen ansonsten den
> Lesefluss stören würde.“

**Interne Links** mit Pelicans `{filename}`-Syntax (relativ zum `content`-Ordner):
```markdown
… neben dem [Dreikörperproblem]({filename}/dreikorperproblem.md) …
```
Mehrere verwandte Beiträge werden als nummerierte Referenzliste gebündelt – ein
typisches Stilmittel:
```markdown
… eine Reihe von Snake Clonen [[1]({filename}/snake.md), [2]({filename}/msnake.md), [3]({filename}/jsnake.md)] …
```

**Externe Links** reichlich und inline: Wikipedia (bevorzugt deutsch) zur
Begriffsklärung, GitHub/Gist zum Code, gelegentlich Paper, Quanta Magazine o. Ä.

**Zitate / Pop-Kultur:** Filmzitate werden gern als Blockquote mit `<cite>` und
Jahr eingebettet und humorvoll mit dem Thema verknüpft (Obi-Wan über `make`, Ian
Malcolm über den Schmetterlingseffekt):
```markdown
> This is the weapon of a Jedi Knight.
> Not as clumsy or random as a blaster;
> an elegant weapon for a more civilized age.
>
> -- <cite>Obi-Wan Kenobi</cite> (1977)
```

---

## 7. Zweisprachigkeit

Manche Beiträge existieren zusätzlich auf Englisch unter `content/en/<slug>.md`.
Die englische Fassung trägt **denselben `Slug`** und dieselben Metadaten, nur
`Lang: en`. Wichtig: Es handelt sich **nicht um wörtliche Übersetzungen**, sondern
um frei neu geschriebene Varianten desselben Inhalts mit eigenem, idiomatischem
Einstieg. Der Tonfall (locker, ich-Perspektive, Humor) bleibt erhalten.

---

## 8. Serien / wiederkehrende Reihen (Fallstudie: Snake)

Ein prägendes Merkmal des Blogs sind **lose Serien**, in denen dasselbe einfache
Projekt immer wieder neu umgesetzt wird – jedes Mal als Vehikel, um eine neue
Sprache oder Technologie auszuprobieren. Das Paradebeispiel ist die Snake-Reihe,
die sich über mehr als ein Jahrzehnt zieht:

| Beitrag | Sprache / Technologie | Demo-Form |
|---------|-----------------------|-----------|
| `snake` | C, ncurses | Screenshot |
| `pysnake` | Python 3, PyQt | eingebettetes Video |
| `msnake` | Matlab | verlinktes Bild |
| `jsnake` | JavaScript (ES6) | spielbares `<canvas>` inline |
| `rsnake` | Rust (Autopilot: *smart kinetic walk*) | Video + Build-Anleitung |
| `restfulsnake` | Java, Spring Boot, REST | gehostete Live-Demo |
| `multijsnake` | Java, WebSockets, Multiplayer | GIF + gehostete Demo |
| `perfect-snake` | Python, Keras/TensorFlow, Reinforcement Learning | spielbar im Browser (TensorFlow.js) |

Wer einen Beitrag schreibt, der sich in eine solche Reihe einfügt, sollte diese
wiederkehrenden Muster beachten:

- **Das Projekt ist konstant, die Technologie ist das eigentliche Thema.** Snake
  selbst wird nie ausführlich erklärt – es dient als immer gleiche Messlatte, an
  der eine neue Sprache, ein Framework oder ein Algorithmus vorgeführt wird.
- **Querverweis-Liste auf alle Vorgänger.** Jeder neue Beitrag verlinkt früh die
  bisherigen Teile als nummerierte Referenzliste, die mit jeder Folge länger wird:
  ```markdown
  … eine weitere Snake-Version [[1]({filename}/snake.md), [2]({filename}/pysnake.md), [3]({filename}/msnake.md), [4]({filename}/rsnake.md), [5]({filename}/jsnake.md)].
  ```
  Diese wachsende Liste ist das wichtigste strukturelle Signal dafür, dass ein
  Beitrag zu einer Serie gehört.
- **Selbstironie über die eigene Marotte.** Der Wiederholungszwang wird offen und
  augenzwinkernd thematisiert:
  > „… dauert es nie lange bis ich eine Snake-Abwandlung programmiere.“
  > „Also bin ich jetzt Java-Experte. Und das bedeutet, dass es Zeit ist für eine
  > weitere Snake-Version.“
- **Pointierte Meinung zur jeweiligen Technologie.** Jeder Teil enthält ein kurzes,
  subjektives Urteil über die verwendete Sprache (Python gefällt am besten, Matlab
  ist „irgendwie anders“, Begeisterung über JavaScripts *arrow functions* und
  *spread operator*, Sympathie für Rust). Gern mit einem kleinen, charakteristischen
  Code-Schnipsel, der ein Sprach-Feature zeigt.
- **Anschluss an den nächsten Teil (Cliffhanger).** Manche Beiträge enden mit einem
  Ausblick, der die Folge ankündigt:
  > „Und dieses Design schreit geradezu nach einem Multiplayer-Modus …“
- **Demo und Code-Ablage skalieren mit dem Umfang.** Die Präsentation wächst mit
  der Ambition vom Screenshot über Video bis zur live gehosteten, im Browser
  spielbaren Version. Analog wird die Code-Ablage begründet gewählt: ein paar Zeilen
  landen als Gist, größere Projekte als eigenes GitHub-Repo
  („Da `jsnake` nur ein paar Zeilen … sind und sich ein ganzes GitHub Repository
  deshalb nicht lohnt, habe ich es in einen Gist hochgeladen.“).

Dieses Muster lässt sich auf andere Reihen übertragen (z. B. die Fraktal- und
Paper-Beiträge): ein konstanter inhaltlicher Kern, der durch wechselnde
Blickwinkel, Werkzeuge oder Tiefen variiert und über Querverweise zu einem
zusammenhängenden Ganzen verknüpft wird.

---

## 9. Checkliste: Einen Beitrag in diesem Stil schreiben

1. **Thema wählen:** ein konkretes eigenes Artefakt, das „hübsch, praktisch oder
   interessant“ ist (Code-Projekt, Simulation, Visualisierung, nützlicher Trick).
2. **Metadaten setzen:** `Title`, `Date`, `Author: surt91`, passende `Category`,
   `Tags`, `Slug`, `Status: published`, `Lang: de`; bei vorhandenem Teaserbild
   `LargeFeaturedImage`.
3. **Hook schreiben:** persönlicher, oft humorvoller Einstieg – oder direkt das
   Ergebnis als Bild/Video zeigen und dann „Aber was steckt dahinter?“.
4. **Einordnen & erklären:** Kontext geben, Fachbegriffe einführen und kurz
   definieren, mit Wikipedia-Links versehen. Bei Theorie ggf. eine Formel; bei
   Implementierung ein prägnanter Code-Schnipsel.
5. **Schrittweise entwickeln** (bei längeren Posts): ins „wir“ wechseln und den
   Leser durch Idee → Umsetzung → Ergebnis führen, gegliedert mit `##`.
6. **Ehrlich bleiben:** Grenzen und Schwächen des eigenen Ansatzes
   selbstironisch benennen.
7. **Würzen:** ein trockener Witz, eine augenzwinkernde Übertreibung, evtl. ein
   passendes Pop-Kultur-Zitat als Blockquote.
8. **Abschluss:** runder Schlussgedanke und – fast obligatorisch – ein Link zum
   Quellcode auf GitHub/Gist.
9. **Medien einbauen:** Bilder mit aussagekräftigem Alt-Text (Diagramme mit
   `{: .invertable}`), Code in Fenced Blocks mit Sprachangabe, Mathe in
   MathJax-Notation, interne Verweise mit `{filename}`.
10. **Länge anpassen:** im Zweifel lieber knapp und pointiert. Nicht jeder
    Gedanke braucht einen Absatz; manche Idee trägt nur zwei Zeilen – und das ist
    völlig in Ordnung.

---

## 10. Mini-Beispiel im Stil des Blogs

```markdown
Title: Sortieren mit Schwerkraft
Date: 2024-03-01 21:15
Author: surt91
Category: Code
Tags: Python, GitHub, Bild
Slug: gravity-sort
Status: published
Lang: de

Sortieralgorithmen gibt es wie Sand am Meer -- von elegant ($\mathcal{O}(n \log n)$)
bis absurd. Heute geht es um die absurde Sorte: *Bead Sort*, bei dem man Zahlen als
Stapel von Perlen auf Stäbe steckt und einfach fallen lässt. Die Schwerkraft erledigt
den Rest.

![Bead Sort in Aktion](/img/beadsort.gif){: .invertable}

Das Schöne daran: Der Algorithmus ist physikalisch motiviert und damit fast schon zu
anschaulich, um wahr zu sein. Das weniger Schöne: Auf einem normalen Computer müssen
wir die fallenden Perlen Spalte für Spalte simulieren, und schon ist der vermeintlich
geniale $\mathcal{O}(n)$-Trick wieder dahin.

> Gravity is a harsh mistress.
>
> -- <cite>The Tick</cite> (1994)

Der Code ist als [Gist auf GitHub](https://gist.github.com/surt91) -- in wenigen
Zeilen, versteht sich.
```
