Title: Nightmare before Easter
Date: 2023-09-23 19:45
Category: Code
Tags: Python, Code
Status: published
Slug: easter
Lang: en

Easter is a holiday whose time is determined with an unnecessarily complicated rule. The first Sunday after the first full moon in Spring. Most people have no other choice than to look its date up in a calendar and trust in the calendar manufacturer. But not anymore! I will stick it to Big Calendar and reveal the secret formula to calculate the date of easter!

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

My favorite thing about it is that each line becomes more horrendous than the previous.

This algorithm was developed by Lilius and Clavius at the end of the 16th Century. I became aware of it through a mention in an exercise in Donald Knuth's *The Art of Computer Programming 1* (Third edition, p. 159f).