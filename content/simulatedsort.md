Title: SimulatedSort
Date: 2014-06-14 15:20
Author: surt91
Category: Code
Tags: Python
Slug: simulatedsort
Status: published

[Simulated Annealing](http://de.wikipedia.org/wiki/Simulated_annealing)
ist eine Optimierungsmethode, die von natürlichen
Kristallisationsprozessen inspiriert ist. Man startet in der Schmelze
bei hohen Temperaturen und lässt es dann abkühlen, sodass die Atome sich
in einem Zustand minimaler Energie anordnen, dem Kristallgitter. Wenn
man also für ein Optimierungsproblem die zu optimierende Größe als
Energie ansieht, und man eine Lösung durch eine kleine Änderung in eine
andere Lösung verwandeln kann, kann man mit dieser Methode eine Näherung
für das Optimum finden.

Wenn wir also eine Sequenz von Zahlen sortieren wollen, können wir die
Summe der Differenzen zwischen benachbarten Zahlen als Energie
betrachten, denn die ist minimal in einer sortierten Liste. Um eine
Lösung in eine andere zu verwandeln, reicht eine Permutation.

Genug der Theorie: Hier präsentiere ich ein schnell terminierendes
Sortierprogramm, das zwar nicht immer eine sortierte Liste findet, aber
zumindest eine Näherung! Es ist also
[Bogosort](http://de.wikipedia.org/wiki/Bogosort) in mehr als nur einer
Hinsicht überlegen!  

    #!python3
    from random import random, randint, sample
    from math import exp
    from copy import deepcopy
    from time import time


    class SimulatedSort():
        def __init__(self):
            self.T = [300.0, 100.0, 70.0, 30.0, 10.0, 7.0, 3.0, 1.0]
            self.t_steps = 100

        def __call__(self, to_sort):
            self.conf = Configuration(to_sort)
            self.simulated_annealing()
            return self.conf.conf

        def simulated_annealing(self):
            new_conf = self.conf
            best_conf = deepcopy(self.conf)
            for t in self.T:
                for i in range(self.t_steps):
                    old_f = new_conf.f
                    new_conf.change()
                    if new_conf.f < old_f or random() < exp(-(new_conf.f - old_f) / t):
                        if new_conf.f < best_conf.f:
                            best_conf = deepcopy(new_conf)
                    else:
                        new_conf.revert_last_change()
                print(t, self.conf.conf, self.conf.f)


    class Configuration():
        def __init__(self, conf):
            self.conf = conf
            self.update_penalty()

        def update_penalty(self):
            p = 0
            for i in range(len(self.conf) - 1):
                p += abs(self.conf[i] - self.conf[i + 1])
            self.f = p

        def change(self):
            self.x = randint(0, len(self.conf) - 1)
            self.y = randint(0, len(self.conf) - 1)
            self.conf[self.x], self.conf[self.y] = self.conf[self.y], self.conf[self.x]
            self.update_penalty()

        def revert_last_change(self):
            self.conf[self.x], self.conf[self.y] = self.conf[self.y], self.conf[self.x]
            self.update_penalty()


    if __name__ == "__main__":
        l = sample(range(0, 1000), 10)
        print(l)
        a = SimulatedSort()

        start = time()
        s = a(l)
        end = time()
        sa_time = end-start
        print("finished after {:.3f}s".format(sa_time))

        print(s)
        if all(s[i] <= s[i+1] for i in range(len(s)-1)) 
                or all(s[i] >= s[i+1] for i in range(len(s)-1)):
            print("list is sorted!")
        else:
            print("not sorted!")

        start = time()
        s = sorted(l)
        end = time()
        tim_time = end-start
        print("timsort would have needed: "
              "{:.8f}s ({:.0f} times faster)".format(tim_time, sa_time/tim_time))

Wer braucht da noch O(n log(n)) Sortier-Algorithmen?!
