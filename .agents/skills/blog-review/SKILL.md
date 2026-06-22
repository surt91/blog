---
name: blog-review
description: Reviewt einen vom User selbst geschriebenen Blog-Entwurf für blog.schawe.me gegen den Stil-Guide stil.md und die Pelican-Konventionen. Nutzen, wenn der User Feedback zu einem eigenen Blog-Artikel, Draft oder Entwurf möchte. Gibt strukturiertes, umsetzbares Feedback (Metadaten, Sprachstil, Struktur, technische Bausteine), schreibt den Beitrag nicht eigenmächtig um; der Autor bleibt surt91.
compatibility: Pelican-Blog im Repo blog.schawe.me; Inhalte als Markdown in content/, Stil-Guide in stil.md (Repo-Root)
metadata:
  author: Claude
  version: "1.0"
---

# Blog-Entwurf für blog.schawe.me reviewen

Diese Skill prüft einen **vom User selbst geschriebenen** Entwurf gegen den Stil und
die technischen Konventionen von `blog.schawe.me`. Ziel ist konstruktives, konkretes
Feedback — **kein** vollständiges Umschreiben.

## Schritt 0 — Stil-Guide laden (Pflicht)
Lies **immer zuerst** `stil.md` im Repo-Root vollständig. Das ist die maßgebliche
Referenz für Sprachstil, Struktur, Metadaten, technische Bausteine und das
Serien-Muster. Lies anschließend den zu reviewenden Entwurf (Pfad vom User; falls
unklar, danach fragen).

## Schritt 1 — Prüfen gegen folgende Kriterien

**Metadaten (Pelican Front Matter):**
- Vorhanden & korrekt: `Title`, `Date` (`YYYY-MM-DD HH:MM`), `Category` (genau eine
  aus `Code`/`Snip`/`Meta`/`Phys`/`Tech`/`Misc`), `Status`, `Lang`.
- `Author: surt91` — bei einem Beitrag des Blog-Inhabers ist das korrekt; **nicht**
  ändern. (Nur Gastbeiträge tragen einen abweichenden Autor.)
- `Slug` in kebab-case/ASCII, `Tags` konsistent großgeschrieben (Sprache +
  Medientyp + Thema). Teaserbild-Feld sinnvoll? `Doi:` bei eigener Veröffentlichung?

**Sprachstil & Tonfall:**
- Passt es zum Blog: locker, ich-Perspektive, trockener Humor, Selbstironie, direkte
  Leseransprache, Begeisterung für Eleganz?
- Werden Fachbegriffe eingeführt und erklärt (mit Wikipedia-Links)?
- Gedankenstrich `--` für Einschübe genutzt? Fachbegriffe bei Einführung *kursiv*?

**Struktur & Dramaturgie:**
- Klarer Hook am Anfang? Logischer Aufbau (Hook → Einordnung → Entwicklung →
  Schluss)? Bei Lang-Posts `##`-Überschriften?
- **Endet der Beitrag mit einem Link zum Quellcode** (GitHub/Gist)? Das ist nahezu
  obligatorisch.
- Gehört der Beitrag zu einer Reihe (z. B. Snake)? Dann: ist die wachsende
  nummerierte Querverweis-Liste auf alle Vorgänger vorhanden und vollständig?
  (Abschnitt 8 in `stil.md`.)

**Technische Bausteine:**
- Bilder mit aussagekräftigem Alt-Text? Diagramme/Plots mit `{: .invertable}`?
- Code in Fenced Blocks **mit Sprachangabe**? Sehr langer Code besser auslagern?
- Mathe in korrekter MathJax-Notation (`$…$`, `$$…$$`, `\begin{align}`)?
- Interne Links via `{filename}/post.md` (nicht hartkodierte URLs)?
- Videos als `<video>`-HTML eingebettet?

**Korrektheit:**
- Tippfehler, Grammatik, kaputte Links, fehlende Bild-/Video-Dateien
  (Pfade gegen `content/img/`, `content/vid/` prüfen, wenn möglich).

## Schritt 2 — Feedback strukturiert ausgeben
Gliedere das Feedback in drei Kategorien, jeweils mit Zeilenbezug/Zitat und
konkretem Vorschlag:
1. **Muss korrigiert werden** — fehlende/falsche Metadaten, kaputte Konventionen,
   defekte Links, fehlender Quellcode-Link.
2. **Stil-Empfehlungen** — Tonfall, Dramaturgie, Humor, Klarheit; passend zum Blog.
3. **Optional / Geschmackssache** — kleinere Verbesserungsideen.

Sei konkret und zitiere die betroffene Stelle. Lobe, was bereits gut zum Stil passt.

## Schritt 3 — Grenzen
- Den Beitrag **nicht eigenmächtig umschreiben**. Einzelne Formulierungsvorschläge
  als Beispiel sind in Ordnung; eine vollständige Überarbeitung nur auf
  ausdrückliche Bitte des Users.
- Inhaltliche/fachliche Aussagen des Users nicht verfälschen — bei Unklarheit oder
  Verdacht auf einen Fehler nachfragen statt korrigieren.
