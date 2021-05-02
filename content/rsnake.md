Title: rsnake
Date: 2017-09-06 17:40
Author: surt91
Category: Code
Tags: Rust, Game, GitHub, Snake
Slug: rsnake
Status: published
Lang: de

In meinem letzten Einträgen ist bereits angeklungen, dass ich Rust mag. Und wie
die Erfahrung [[1]({filename}/snake.md), [2]({filename}/pysnake.md), [3]({filename}/msnake.md)]
zeigt, dauert es nie lange bis ich eine Snake-Abwandlung programmiere.

Dieses Mal verfolgt der Autopilot die Strategie des [smart kinetic walk](https://doi.org/10.1103/PhysRevB.31.2993),
(ein Model aus der statistischen Physik zur Simulation von Polymeren,)
um sich nicht selbst zu beißen -- leider setzt diese Strategie ein unendlich
großes Spielfeld voraus.

Die grundlegende Idee ist, dass die Schlange immer wenn sie sich selbst begegnet
prüft welcher nächste Schritt sie in einer Schlaufe fängt und welcher nach außen
führt. Mit offenen Randbedingungen, also auf einem unendlich großen Feld lässt
sich dass das in konstanter Zeit erledigen, wenn die Schlange an jedem Segment
ihres Körpers die Anzahl der Rechts- und Linksdrehungen speichert. Bei
periodischen Randbedingungen funktioniert das allerdings nicht mehr, sodass der
Autopilot eine Best-First-Search durchführt. Auf offenen Randbedingungen würde
es ausreichen einen Weg vom potentiell nächstem Schritt zu einem beliebigen
Punkt außerhalb eines Rechtecks, das die Schlange einschließt, zu finden.
Bei periodischen Randbedingungen ist es nicht so eindeutig. Ich habe mich
entschlossen, dass die Schlange sich nur so bewegen soll, dass immer ein Pfad
zu ihrem Schwanz existiert. Tatsächlich führt diese Strategie zu unterhaltsamen
und nicht perfekten Spielverläufen.

<video controls loop autoplay poster="/img/rsnake.png" width="400" height="400" class="fixed-size-400">
<source src="/vid/rsnake.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

Der Vollständigkeit halber sind noch ein nicht vorausplanender und ein
perfekter, aber langweiliger, Autopilot dabei.

Da die Quellen auf [GitHub](https://github.com/surt91/rsnake) liegen, ist
es nur vier Zeilen entfernt -- weniger, wenn der Rustcompiler bereits installiert
ist.

```bash
    # curl https://sh.rustup.rs -sSf | sh  # never copy `| sh` in your terminal
    git clone https://github.com/surt91/rsnake
    cd rsnake
    cargo run --release
```
