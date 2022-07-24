Title: git subtree
Date: 2022-07-24 17:31
Category: Snip
Slug: git-subtree
Status: published
Lang: de

Wir alle kennen die Situation: Eine neue Idee, mit der wir unser bestehendes Projekt mit dem Namen `alt` erweitern, sodass wir sogleich im zugehörigen Repository ein Unterverzeichnis `neueIdee` anlegen. Die Idee stellt sich dann als so gut heraus, dass sie auch außerhalb des Projektes `alt` nützlich wäre. Es wäre also sehr sinnvoll ein neues Repository `neu` anzulegen, das nur den Inhalt des Unterverzeichnisses `neueIdee` enthalten soll. Tatsächlich scheint dieses Problem wohl so oft vorzukommen, dass es seit 2012 ein extra git Subcommand für diesen Zweck (und etwas kompliziertere Fälle) gibt: `git subtree`

## Neues Repository aus einem Unterverzeichnis

```
alt/
├─ neueIdee/
│  ├─ lib.rs
├─ main.rs
```

Wir wechseln also in das Repository `alt` führen dort folgendes Kommando aus:

```bash
git subtree split --prefix=neueIdee/ --branch=nurNeueIdeeBranch
```

Dies erzeugt in diesem Repository zunächst einen neuen Branch `nurNeueIdeeBranch`, der nur den Inhalt von `neueIdee` hat -- also ein anderes Wurzelverzeichnis. Dieser Branch enthält also eine neu geschriebene History, die nur aus Commits besteht, die (auch) Einfluss auf Dateien unterhalb von `neueIdee` hatten.

Nun können wir unser neues Repository `neu` anlegen und den soeben erzeugten Branch pullen.

```bash
cd .. ; mkdir neu ; cd neu
git init
git pull ../alt nurNeueIdeeBranch
```

Und schon haben wir ein neues Repository, das nur den gewünschten Inhalt hat.

```
alt/
├─ main.rs
neu/
├─ lib.rs
```

Möglicherweise wollen wir noch einen Commit im alten Repository tätigen, der das `neueIdee` Unterverzeichnis löscht. Möglicherweise müssen wir im neuen Repository noch Änderungen am Infrastrukturcode vornehmen.

## Verschieben eines Unterverzeichnisses in ein bestehendes Repository

Womöglich fällt uns aber auch auf, dass der Code besser in ein anderes Repository statt eines Neuen passt? Vielleicht weil wir gerade dabei sind unseren Code in einem Monorepo zu sammeln? Auch kein Problem!

```
alt/
├─ neueIdee/
│  ├─ lib.rs
├─ main.rs
monorepo/
├─ project1/
├─ project2/
```

Wir haben oben  bereits den `nurNeueIdeeBranch` erstellt, den wir nun in das Unterverzeichnis `guteIdee`des Repositorys `monorepo` einfügen wollen. Auch hier hilft uns wieder `git subtree` weiter:

```bash
cd monorepo
git branch mitGuterIdeeBranch
git checkout mitGuterIdeeBranch
git subtree add --prefix=guteIdee/ ../alt nurNeueIdeeBranch
```

Sobald wir uns in dem neuen Branch `mitGuterIdeeBranch` überzeugt haben, dass alles zu unserer Zufriedenheit geklappt hat und wir möglicherweise noch Infrastrukturcode angepasst haben, können wir den Branch nach `main` mergen und sind fertig.

```
alt/
├─ neueIdee/
│  ├─ lib.rs
├─ main.rs
monorepo/
├─ project1/
├─ project2/
├─ guteIdee/
│  ├─ lib.rs
```
