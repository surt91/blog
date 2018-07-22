Title: make
Date: 2016-11-02 15:41
Category: Code
Tags: make, LaTeX, TikZ, Gnuplot
Status: published
Lang: de

Als Obi-Wan zu Luke gesagt hat

> This is the weapon of a Jedi Knight.
> Not as clumsy or random as a blaster;
> an elegant weapon for a more civilized age.
>
> -- <cite>Obi-Wan Kenobi</cite> (1977)

Meinte er vermutlich `make`. (Fun Fact: `make` wurde auch [1977 veröffentlicht](https://en.wikipedia.org/wiki/Make_(software)).)

Mit wenigen Zeilen im `Makefile` kann man nicht nur sein $\LaTeX$ Projekt
kompilieren, sondern auch alle plots neu zeichnen, die sich geändert haben.
Ausgehend davon, dass zum Plotten gnuplot mit dem `epslatex` Terminal genutzt
wird und folgende Verzeichnisstruktur des Projektes vorliegt.

```
.
+-- data
|   + datafile1.dat
|   + datafile2.dat
+-- images
|   +-- img1.svg
|   +-- img2.tex
+-- plots
|   +-- style.gps
|   +-- plot1.gp
|   +-- plot2.gp
+-- myDocument.tex
+-- chapter1.tex
+-- chapter2.tex
+-- lit.bib
```

könnte das folgende `Makefile` sich darum kümmern, dass die Daten für die Plots
heruntergeladen werden, alle Plots, TikZ und .svg parallel zu .pdf gerendert
werden und sobald das geschehen ist, das Dokument kompiliert wird.

```make
DOCUMENT = myDocument

# get all image files from their directories
PLOTS := $(wildcard plots/*.gp)
TIKZ := $(wildcard images/*.tex)
SVG := $(wildcard images/*.svg)

# we want the images to be pdf
PLOTS := $(PLOTS:%.gp=%.pdf)
SVG := $(SVG:%.svg=%.pdf)
TIKZ := $(TIKZ:%.tex=%.pdf)

IMAGES := $(PLOTS) $(SVG) $(TIKZ)

# get all tex files
TEX := $(wildcard *.tex)
BIBFILE := lit.bib

all: $(DOKUMENT).pdf

# we need chapters, images and the bib file to create our document
# also recompile, whenever one of those changes
$(DOCUMENT).pdf: $(TEX) $(IMAGES) $(BIBFILE)
$(DOCUMENT).pdf: %.pdf: %.tex
	pdflatex -interaction=batchmode $* > /dev/null
	biber $* > /dev/null
	pdflatex -interaction=batchmode $* > /dev/null
	pdflatex -interaction=batchmode $* > /dev/null

# gnuplot generates texfiles from the .gp files
# make sure to regenerate all tex files, if the style
# or the data changes
%.tex: %.gp plots/style.gps | data
	cd $(<D) && gnuplot $(<F) > /dev/null 2>&1

# use this rule to convert .svg to pdf
$(SVG): %.pdf: %.svg
	cd $(<D) && inkscape -z -A $(*F).pdf -h 1080 $(<F)

# use this rule only to generate .pdf from the "image type" .tex files
$(TIKZ) $(PLOTS): %.pdf: %.tex
	cd $(<D) && pdflatex -interaction=batchmode $(<F) > /dev/null
	rm -f $*.{log,aux} $*-inc.eps $*-inc-eps-converted-to.pdf

# rule to extract data from its archive
data: %: %.tar.xz
	tar -xf $<

# rule to download the archive with the data
%.tar.xz:
	wget -nv https://some.domain.tld/where/your/data/is/$@

clean: proper
	rm -rf data
	rm -f $(DOCUMENT).pdf

# delete temporary files
proper:
	rm -f data.tar.xz
	rm -f $(PLOTS) $(PLOTS:.pdf=.eps) *-inc.eps *-inc-eps-converted-to.pdf $(PLOTS:.pdf=.tex) plots/fit.log $(TIKZ) $(SVG)
	rm -f {$(DOCUMENT)}.{log,aux,bbl,blg,toc,out,lof,lot,snm,nav,tec,glg,glo,gls,xdy,acn,acr,alg,bcf,run.xml}
```

Dazu baut `make` einen gerichteten azyklischen Graphen (DAG) aus den
Abhängigkeiten auf und führt die Dinge, deren Abhängigkeiten erfüllt sind
parallel aus.

Das grundlegende Element einer `Makefile` sind die Rules, die generell so
aufgebaut sind

```
targets : prerequisites
<tab> recipe
```

Dabei gibt die erste Zeile die Abhängigkeiten welche `prerequisites` bestehen
müssen, um durch Ausführung des `recipe` die `targets` zu erstellen.

Die Nützlichkeit von `make` wird zu großen Teilen durch automatische
Variablen (zB. `$*`) oder Pattern Rules (`%.pdf`) hergestellt.
Dazu verweise ich allerdings lieber auf die [offizielle Dokumentation](https://www.gnu.org/software/make/manual/).
