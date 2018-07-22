Title: Oberflächenkachelung mit TikZ
Date: 2013-12-08 12:37
Author: surt91
Category: Code
Tags: LaTeX, TikZ, Bild, Code
Slug: oberflachenkachelung-mit-tikz
Status: published
Lang: de

Man arbeitet an einem Seminarvortrag und will ein Modell auf einem
periodischen Gitter erklären. Natürlich kann man sich nicht entscheiden,
wie viele [Elementarzellen](http://de.wikipedia.org/wiki/Elementarzelle)
man darstellen möchte. Außerdem ist es einem zuwider mehrere
Elementarzellen per Hand zu schreiben.

Wer kennt das nicht?

Glücklicherweise gibt es eine Lösung. Weil man alle seine Aufzeichnungen
sowieso in LaTeX setzt, benutzt
man [TikZ](http://www.texample.net/tikz/examples/), bastelt eine
Elementarzelle und kachelt sie über die Ebene, bis man das Gefühl hat,
dass es genau passend für die Präsentation ist.  
Als Bonus kann man noch mit den Parametern spielen, um einen möglichst
überzeugenden pseudo 3D-Effekt zu erzielen.

```latex
\documentclass{standalone}

\usepackage{tikz}

\begin{document}
    \begin{tikzpicture}
        \newcommand*{\shear}{0.2}
        \newcommand*{\height}{1.0}
        \newcommand*{\radius}{0.1}
        \newcommand*{\xspacing}{1}
        \newcommand*{\yspacing}{0.5}

        % two-dimensional lattice, with three dimensional basis
        % decreasing counter, otherwise there will be lines through the circles
        \foreach \x in {4,...,0}{
            \foreach \y/\dx in {3,...,0}{
                % primitive vectors
                \draw (\x+\y*\shear-\xspacing/2 , \y*\yspacing            )
                    -- (\x+\y*\shear+\xspacing/2, \y*\yspacing            );
                \draw (\x+\y*\shear-\shear/2    , \y*\yspacing-\yspacing/2)
                    -- (\x+\y*\shear+\shear/2   , \y*\yspacing+\yspacing/2);
                \draw (\x+\y*\shear             , \y*\yspacing            )
                    -- (\x+\y*\shear            , \y*\yspacing+\height    );

                % base
                \fill[white] (\x+\y*\shear, \y*\yspacing        ) circle(\radius);
                \draw        (\x+\y*\shear, \y*\yspacing        ) circle(\radius);

                \fill[gray]  (\x+\y*\shear, \y*\yspacing+\height) circle(\radius);
                \draw        (\x+\y*\shear, \y*\yspacing+\height) circle(\radius);
            }
        }
    \end{tikzpicture}
\end{document}
```

![Isingmodell mit Kopplung]({filename}/img/standaloneIsing.svg){width="100%"}

Und damit wäre wiedereinmal die Vorliebe dieses Blogs für [schwarz-weiße
Bilder]({filename}/conways-game-of-life.md),
die entweder [Linien und Kreise]({filename}/proximity-graphs.md)
oder [zu große]({filename}/seltsamer-attraktor.md)
[Pixel]({filename}/rule-90.md)
enthalten, bestätigt.
