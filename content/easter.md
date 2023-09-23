Title: Osteralbtraum
Date: 2023-09-23 19:45
Category: Code
Tags: Python, Code
Status: published
Slug: easter
Lang: de

Ostern ist ein Feiertag, dessen Zeitpunkt mit einer Regel festgelegt wird, die unnötig kompliziert scheint. Der erste Sonntag nach dem ersten Vollmond im Frühling. Den meisten bleibt da als Lösung nicht viel mehr übrig als in einem Kalender nachzusehen welches Datum es denn wohl ist und sich auf den Kalenderhersteller zu verlassen. Aber nicht mit mir! Ich werde es Big-Calendar zeigen und hier die geheime Formel veröffentlichen, mit der man das Osterdatum berechnet!

```python
from datetime import date

def easter(year: int) -> date:
    y = year
    g = y % 19 + 1                    # golden number
    c = y // 100 + 1                  # century
    x = (3 * c) // 4 - 12             # correction: dropped leap years
    z = (8 * c + 5) // 25 - 5         # correction: synchronize with moon's orbit
    d = (5 * y) // 4 - x - 10         # find sunday
    e = (11 * g + 20 + z - x) % 30    # epact
    if e == 25 and g > 11 or e == 24:
        e += 1
    n = 44 - e                        # full moon in march
    if n < 21:
        n += 30
    n = n + 7 - (d + n) % 7           # advance to next sunday
    month, day = (4, n - 31) if n > 31 else (3, n)

    return date(year, month, day)
```

Mir persönlich gefällt besonders gut, dass jede Zeile schlimmer ist als die vorherige.

Dieser Algorithmus ist übrigens von Lilius und Clavius Ende des 16. Jahrunderts entwickelt worden. Ich bin durch eine Erwähnung in einer Übungsaufgabe in Donald Knuths *The Art of Computer Programming 1* (Third edition, S. 159f) darauf gestoßen.
