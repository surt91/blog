Title: rsnake
Date: 2017-08-20 18:18
Author: surt91
Category: Code
Tags: Rust, Game, GitHub, Snake
Slug: rsnake
Status: published

In meinem letzten Eintrag ist bereits angeklungen, dass ich Rust mag. Und wie
die Erfahrung [[1]({filename}/snake.md), [2]({filename}/pysnake.md), [3]({filename}/msnake.md)]
zeigt, dauert es nie lange bis ich eine Snake-Abwandlung programmiere.

![Snake]({filename}/img/rsnake.png)

Dieses Mal verfolgt der Autopilot die Strategie des [smart kinetic walk](https://doi.org/10.1103/PhysRevB.31.2993),
ein Model aus der statistischen Physik zur Simulation von Polymeren,
um sich nicht selbst zu beißen -- leider setzt diese Strategie ein unendlich
großes Spielfeld voraus.

Da die Quellen auf [GitHub](https://github.com/surt91/rsnake) liegen, ist
es nur vier Zeilen entfernt -- weniger, wenn der Rustcompiler bereits installiert
ist.

    #!bash
    # curl https://sh.rustup.rs -sSf | sh  # never copy `| sh` in your terminal
    git clone https://github.com/surt91/rsnake
    cd rsnake
    cargo run --release
