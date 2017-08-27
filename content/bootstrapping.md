Title: Bootstrapping
Date: 2013-09-26 19:13
Author: surt91
Category: Code
Tags: Python, Statistik, Code
Slug: bootstrapping
Status: published

Wer kennt das nicht: Man hat sich ein Python Skript geschrieben, um
seine Daten per [Bootstrap Resampling](http://en.wikipedia.org/wiki/Bootstrapping_(statistics))
auszuwerten und stellt fest, dass das Konstrukt zur Bildung des "Samples
mit Ersetzungen"

```python
    import random
    x = [1,2,3]

    bootstrapSample = [random.choice(x) for _ in x]
```

einfach nicht schnell genug ist.  
Aber glücklicherweise gibt es [numpy](http://www.numpy.org/)!

```python
    import numpy
    x = [1,2,3]

    bootstrapSample = list(numpy.random.choice(x, len(x)))
```

Das ist -- zumindest in meinem Anwendungsfall -- spürbar schneller. Ich
werde in Zukunft also immer optimale Fehlerbalken erzeugen.
