Title: SHA-256 in 256 Zeilen
Date: 2014-04-23 20:27
Author: surt91
Category: Code
Tags: C, Python, GitHub
Slug: sha-256-in-256-zeilen
Status: published

Programmiersprachen muss man üben, um sie zu lernen und um sie nicht
wieder zu vergessen. Ich habe also meine Zeit damit vertrieben einen
[SHA-256](http://de.wikipedia.org/wiki/Sha256) zu schreiben -- eine
[kryptographische Hash](http://de.wikipedia.org/wiki/Kryptologische_Hashfunktion)
Funktion. Die [Spezifikation](http://tools.ietf.org/html/rfc6234) ist
glücklicherweise sehr sehr verständlich.  
Und auch wenn es tausende andere Implementationen gibt, die schneller
sind, alle Grenzfälle beachten (ich befürchte, dass mein Programm
Probleme auf Big Endian Systemen bekommt), und sogar Schaltkreise, die
hochoptimiert nur diese Operation beherrschen (Stichwort: Bitcoin ASIC), ist
meiner dennoch sehenswert, da er SHA-256 in 256 Zeilen darstellt.

[Der Code ist als Gist auf GitHub](https://gist.github.com/surt91/11230311), da
er in seinen 256 Zeilen ansonsten den Lesefluss stören würde.

In Python ist es übrigens etwas kürzer.

```python
print(hashlib.sha256(b"Hallo Welt!").hexdigest())
```
