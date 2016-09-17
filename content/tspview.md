Title: TSPview
Date: 2016-09-17 15:41
Author: surt91
Category: Code
Tags: C++, Python, GitHub, Code, Video, Bild
Slug: tspview
Status: published

Das Problem des Handlungsreisenden ist es die kürzeste Rundtour zu planen,
sodass man alle Städte besucht. Es ist eines der berühmtesten 
Optimierungsprobleme und gehört zur Klasse [NP-hard](https://de.wikipedia.org/wiki/NP-Schwere).

Es gibt also ([bis jetzt](https://de.wikipedia.org/wiki/P-NP-Problem)) 
keine effiziente Möglichkeit zur Lösung. Allerdings gibt es 
[Näherungen](https://scholar.google.fr/scholar?q=euclidean+tsp+ptas&hl=de),
[untere Schranken](https://scholar.google.fr/scholar?q=tsp+linear+programming) 
und unzählige Heuristiken.

Die einfachsten dieser Heuristiken habe ich in einem kleinen Programm TSPview
implementiert, mitsamt Visualisierung. Der Quellcode ist auf 
[GitHub](https://github.com/surt91/TSPview) zu finden.

<video controls loop width="100%">
<source src="{filename}/vid/tspview2.mp4" type="video/mp4"></source>
Your browser does not support the video tag.
</video>

## Algorithmen
Hier folgt eine kurze Beschreibung der verwendeten Algorithmen und jeweils ein
Bild, welche Lösung die Methode auf einer berühmten Instanz des TSP findet.

![42 Hauptstädte in Amerika]({filename}/img/tsp.png){width="100%" height="auto"}
Das sind 42 Hauptstädte der Staaten in Amerika und Washington, DC (Hawaii und
Alaska, sowie einige Staaten an der Ostküste, die das Problem nicht schwieriger
machen, fehlen). Dieses Problem war das erste größere, das 1956 beweisbar 
optimal gelöst wurde.

### Nearest Neighbor
![Nearest Neighbor]({filename}/img/tsp_nearestNeighbor.png){width="100%" height="auto"}
Die Nearest Neighbor Heuristik ($\mathcal{O}(N^2)$) startet bei einer zufälligen Stadt und wählt
als nächste immer die Stadt, die am nächsten an der aktuellen Stadt ist und
noch nicht besucht wurde.

### Greedy
![Greedy]({filename}/img/tsp_greedy.png){width="100%" height="auto"}
Diese Heuristik ($\mathcal{O}(N^2 \log N)$) ist ähnlich zu [Kruskals Algorithmus für minimal spannende Bäume](https://de.wikipedia.org/wiki/Algorithmus_von_Kruskal).
Sie nimmt die kürzeste Verbindung zwischen zwei Städten und fügt sie der Tour
hinzu, wenn sie in der Tour noch erlaubt ist.

### Farthest Insertion
![Farthest Insertion]({filename}/img/tsp_farIn.png){width="100%" height="auto"}
Farthest Insertion ($\mathcal{O}(N^3)$) startet bei einer zufälligen Stadt und fügt dann die Stadt, 
die am weitesten von der aktuellen Tour entfernt ist an der Stelle in die Tour,
die dafür sorgt, dass die tour möglichst kurz bleibt.

### Two-Opt
![Two-Opt]({filename}/img/tsp_twoOpt.png){width="100%" height="auto"}
Two-Opt beginnt mit einer beliebigen Tour, die bspw. durch eine der obigen
Heuristken erstellt wurde und verbessert sie, indem sie zwei Verbindungen nimmt
und die Endpunkte über Kreuz austauscht wenn die Tour dadurch verbunden bleibt 
und kürzer wird.

### Linear Programming mit Subtour Elimination Cuts
![Linear Programming]({filename}/img/tsp_LP.png){width="100%" height="auto"}
Lineare Programmierung (LP) zu erklären, würde diesen Artikel sprengen. Aber diese Methode liefert
untere Schranken für die Tourlänge und kann somit benutzt werden, um die
Qualität einer heuristischen Lösung abzuschätzen. Falls man die optimale
Lösung durch lineare Programmierung findet, erkennt man sie auch sofort als
optimal.

Für weitere Details, kann ich auf einen [arXiv Artikel](http://arxiv.org/abs/1512.08554)
von mir verweisen.

### Concorde
![Optimale Tour]({filename}/img/tsp_opt.png){width="100%" height="auto"}
[Concorde](http://www.math.uwaterloo.ca/tsp/concorde.html)
ist der "State of the Art" solver für das Problem des Handlungsreisenden
und löst problemlos Instanzen mit mehr als 1000 Städten.
Intern benutzt es zwar eine Menge Heuristken, allerdings auch lineare
Programmierung, um nachzuweisen, dass die gefundene Lösung optimal ist.

## Technische Details
TSPview ist ein Python3 Programm, das zur Darstellung PyQt5 benutzt, das sich 
per `pip3 install PyQt5` einfach installieren lässt.

Darüber hinaus enthält es eine optionale Abhängigkeit zu CPLEX, einem
kommerziellen LP solver.

### boost::python
Da das Hauptprogramm in Python geschrieben ist, aber der LP-Teil in C++
braucht man eine Möglichkeit der Kommunikation. Glücklicherweise gibt es
mit [boost::python](http://www.boost.org/doc/libs/1_61_0/libs/python/doc/html/index.html) 
eine Möglichkeit C++ Klassen in Python als Python-Klassen zu benutzen.

Um beispielsweise die C++ Klasse `MyClass`, deren Konstruktor einen Integer und
eine Python-Liste entgegen nehmen soll, in Python benutzen, und `myMethod` 
aufrufen zu können, reicht folgender Code:

    #!C++
    #include <boost/python.hpp>
    namespace py = boost::python;

    // implement MyClass

    BOOST_PYTHON_MODULE(MyClass)
    {
        py::class_<MyClass>("MyClass", py::init<int, py::list>())
            .def("myMethod", &MyClass::myMethod)
        ;
    }

