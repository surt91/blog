---
name: blog-gastbeitrag
description: Schreibt einen neuen Gastbeitrag für blog.schawe.me (statischer Pelican-Blog) im dokumentierten Stil. Nutzen, wenn der User einen Blog-Artikel, Gastbeitrag oder Post für sein Blog verfasst haben möchte. Trägt als Autor den eigenen Namen (Claude) ein statt surt91, weil es ein Gastbeitrag ist, und folgt den Konventionen aus stil.md (Sprachstil, Struktur, Pelican-Metadaten, Bild-/Code-/Mathe-Einbettung).
compatibility: Pelican-Blog im Repo blog.schawe.me; Inhalte als Markdown in content/, Stil-Guide in stil.md (Repo-Root)
metadata:
  author: Claude
  version: "1.0"
---

# Gastbeitrag für blog.schawe.me schreiben

Diese Skill erstellt einen neuen, fertig formatierten Blogeintrag im Stil von
`blog.schawe.me` (statischer Pelican-Blog, Inhalte als Markdown in `content/`).

## Schritt 0 — Stil-Guide laden (Pflicht)
Lies **immer zuerst** `stil.md` im Repo-Root vollständig. Dort sind Sprachstil,
Tonfall, Struktur, Metadaten, technische Bausteine und das Serien-Muster im Detail
dokumentiert. Der Beitrag muss diesen Konventionen folgen. Dieses SKILL.md fasst nur
das Wichtigste zusammen — bei Zweifeln gilt `stil.md`.

## Schritt 1 — Thema & Rahmen klären
Wenn der User kein Thema genannt hat, frage knapp nach:
- Worum geht es (eigenes Code-Projekt, Physik/Mathe-Spielerei, Visualisierung,
  Tooling-Trick, …)? Das Blog stellt konkrete, eigene Artefakte vor.
- Gibt es zugehörigen Quellcode / GitHub-Repo / Gist, ein Bild oder Video?
- Soll es ein eigenständiger Beitrag sein oder Teil einer bestehenden Reihe
  (z. B. Snake, Fraktale)? Falls Reihe: siehe Abschnitt 8 in `stil.md` und baue die
  wachsende nummerierte Querverweis-Liste auf alle Vorgänger ein.
- Länge/Archetyp: Mini-Post, Standard-Post oder Lang-Post mit `##`-Überschriften.

## Schritt 2 — Datei & Metadaten anlegen
Lege die Datei unter `content/<slug>.md` an (Snips unter `content/oneliner/`).
Pelican-Front-Matter (Key-Value-Zeilen, **kein YAML**), Leerzeile, dann Inhalt:

```markdown
Title: Aussagekräftiger Titel
Date: <heutiges Datum, YYYY-MM-DD HH:MM>
Author: Claude
Category: Code
Tags: Python, Bild, GitHub
Slug: aussagekraeftiger-titel
Status: draft
Lang: de
```

Regeln:
- **`Author: Claude`** — den **eigenen Namen** eintragen, NICHT `surt91`. Es ist ein
  Gastbeitrag; die abweichende Autorenangabe macht das transparent. (Erwähne im
  Gespräch, dass die Byline angepasst werden kann.)
- `Category`: genau eine aus `Code` | `Snip` | `Meta` | `Phys` | `Tech` | `Misc`
  (Auswahltabelle in `stil.md`).
- `Tags`: konsistent großgeschrieben; Sprache + Medientyp (`Bild`/`Video`/`Formel`)
  + Thema. Bei Snips oft weggelassen.
- `Slug`: kebab-case, ASCII.
- `Status: draft` als Default, damit der User vor Veröffentlichung gegenliest. Weise
  darauf hin, dass er auf `published` umgestellt werden muss, um live zu gehen.
- `Lang: de` (Default). Teaserbild optional via `LargeFeaturedImage:`/`FeaturedImage:`.
  Eigene Veröffentlichung → `Doi:`.

## Schritt 3 — Inhalt im Blog-Stil schreiben
Orientiere dich eng an `stil.md`:
- **Tonfall:** locker, ich-Perspektive (bzw. erklärendes „wir“ bei Herleitungen),
  trockener Humor, Selbstironie, direkte Leseransprache. Begeisterung für Eleganz
  zeigen. Fachbegriffe einführen und kurz erklären, mit `de.wikipedia.org`-Links.
- **Dramaturgie:** Hook → Einordnung/Theorie → schrittweise Entwicklung → ehrliche
  Einordnung der Grenzen → runder Schluss. Fast immer mit **Link zum Quellcode**
  (GitHub-Repo oder Gist) enden.
- **Technische Bausteine:** Bilder mit aussagekräftigem Alt-Text (Diagramme/Plots
  mit `{: .invertable}`), Videos als `<video>`-HTML, Mathe via MathJax
  (`$…$`, `$$…$$`, `\begin{align}…\end{align}`), Code in Fenced Blocks **mit
  Sprachangabe**, interne Links mit `{filename}/post.md`. Gedankenstrich `--` für
  Einschübe/Pointen. Optional ein passendes Pop-Kultur-Zitat als Blockquote mit
  `<cite>`.
- Längeren Code auslagern (Gist) und verlinken statt einbetten, wenn er den
  Lesefluss stört.

## Schritt 4 — Optionale englische Fassung
Wenn gewünscht: `content/en/<slug>.md` mit **demselben Slug**, `Lang: en`. Keine
wörtliche Übersetzung, sondern frei neu geschrieben mit eigenem, idiomatischem
Einstieg; Tonfall bleibt erhalten.

## Schritt 5 — Abschluss
- Nenne dem User Dateipfad und Slug.
- Erinnere an `Status: draft` → `published` und biete eine lokale Vorschau an
  (siehe `develop_server.sh` / `Makefile` im Repo).
- Erfinde keine Fakten, Links oder Repos. Platzhalter (z. B. Bildpfade,
  GitHub-URLs) klar als solche markieren und beim User nachfragen.
