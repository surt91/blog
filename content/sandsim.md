Title: sandsim
Date: 2026-10-12 18:10
Author: surt91
Category: Code
Tags: Python, Rust, WebAssembly, Physik, Bild, GitHub
Slug: sandsim
LargeFeaturedImage: img/parasaurolophus1200.webp
Status: published
Lang: de

Ich habe mir einen kinetischen Sandtisch gebaut. Das ist ein Glastisch, bei dem unter
dem Glas Sand liegt und unter dem Sand zwei Schrittmotoren einen Magneten bewegen. Der Magnet zieht eine
Kugel an, die dann Muster in den Sand zieht. Das ganze ist meiner Meinung nach sehr faszinierend und
seitdem ich so etwas zuerst gesehen hatte, wollte ich selber einen bauen (Ich hatte dafür extra Schittmotoren
von einem alten 3D Drucker zurückgelegt.)

[![Ein Parasaurolophus, gezeichnet von einer Kugel in Sand](/img/parasaurolophus1200.webp)](/img/parasaurolophus.webp)

Jetzt habe ich einen gebaut und zuzusehen ist genauso entspannend, wie ich es mir immer vorgestellt hatte.

<video controls loop autoplay poster="/img/sandlorenz.png" width="800" height="800" class="fixed-size-800">
<source src="/vid/sandlorenz.webm" type="video/webm">
Your browser does not support the video tag.
</video>

Muster, die der Tisch zeichnet, müssen durchgehende Striche sein, ohne abzusetzen. Und wenn die Kugel zu nah an
bestehenden Linien entlang läuft, schiebt sie den Sand in die zuvor geschaffene Mulde.

Ich habe natürlich gleich Claude beauftragt mir ein paar Motive zu erstellen, aber um einzuschätzen, ob
es auf dem Tisch auch gut aussieht, reicht eine Strichzeichnung nicht. Und es erst im physischem Tisch
zeichnen zu lassen, ist sehr zeitaufwendig und führt zu langen Iterationszeiten.

Die Lösung ist einfach: Wir simulieren wie die Kugel den Sand schiebt und wie der Sand von zu
steilen Kanten hinabrieselt: [surt91.github.io/sandsim](https://surt91.github.io/sandsim/).
Genau das Sand-Modell, das im Kontext von [self-organized Criticality](https://en.wikipedia.org/wiki/Self-organized_criticality)
berühmt geworden ist. Das Video oben ist übrigens so eine Simulation.
Aber auf dem echten Tisch macht es noch mehr Spaß.