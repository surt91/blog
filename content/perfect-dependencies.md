Title: Perfect Dependencies
Date: 2016-09-17 20:27
Category: Code
Tags: make, C++
Status: published
Lang: de

Man hat ein großes C++ Projekt, ändert einen Header, führt `make` aus und
ein seltsamer Fehler tritt im Programm auf. Das liegt natürlich daran, dass
`make` nicht alle Quelldateien neu kompiliert hat, die den Header einbinden.
Woher sollte `make` das auch wissen? Alle Header per Hand in der `Makefile`
einzutragen und zu pflegen, ist Wahnsinn und wird den Programmierer in denselben
treiben.

`make` ist ein sehr allgemein gehaltenes Programm, wie ich in einem [vorherigen Eintrag]({filename}/make.md)
gezeigt habe. Sich um Eigenheiten von C oder C++ zu kümmern fällt also nicht
in den Aufgabenbereich von `make`. Aber glücklicherweise gibt es ein Programm,
dessen Hauptaufgabe es ist, sich mit den Eigenheiten von C bzw. C++ auszukennen:
den Compiler.
Tatsächlich bietet (zumindest GCC) die Option eine C oder C++ Datei zu parsen
und alle inkludierten Header auszugeben.

```bash
g++ -MM myCode.cpp
```

Das ausnutzend, bietet die [offizielle Dokumentation](https://www.gnu.org/software/make/manual/)
von `GNU make` folgende Rule, um je eine "dependency" `Makefile`
pro `.c` Datei zu erzeugen und automatisch einzubinden.

```make
%.d: %.c
	@set -e; rm -f $@; \
	$(CC) -M $(CPPFLAGS) $< > $@.$$$$; \
	sed ’s,\($*\)\.o[ :]*,\1.o $@ : ,g’ < $@.$$$$ > $@; \
	rm -f $@.$$$$

include $(sources:.c=.d)
```

Falls man `.o` Dateien in ein `obj/` Verzeichnis speichert, muss man die
Regex anpassen. In meinen Projekten leistet mir diese Rule gute Dienste.

Alternativ könnte man natürlich auf ein anderes Buildsystem statt handgepflegter
Makefiles umsteigen.
