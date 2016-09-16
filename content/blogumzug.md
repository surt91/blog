Title: Blogumzug
Date: 2016-09-14 21:12
Category: Tech
Tags: Python, Meta, Code, Formel
Status: published

Soeben habe ich mein Blog von Blogger auf einen kleinen Raspberry Pi 2 in meiner
Wohnung verschoben. Als Engine benutze ich [Pelican](http://blog.getpelican.com/),
ein statischer Blog Generator in Python, der mir auf den ersten Blick sehr gefällt.

Nicht nur, dass ich alle Einträge jetzt in [Markdown](https://de.wikipedia.org/wiki/Markdown)
schreiben kann, was es ermöglicht das ganze Blog per [git](https://de.wikipedia.org/wiki/Git)
zu verwalten (dementsprechend gibt es den Quellcode auf [GitHub](https://github.com/surt91/blog)),
sondern es steht mit [Pygments](http://pygments.org/) ein sehr 
hübsches Syntax Highlighting zur Verfügung.

    #!C
    float Q_rsqrt( float number )
    {
        long i;
        float x2, y;
        const float threehalfs = 1.5F;

        x2 = number * 0.5F;
        y  = number;
        i  = * ( long * ) &y;                       // evil floating point bit level hacking
        i  = 0x5f3759df - ( i >> 1 );               // what the fuck? 
        y  = * ( float * ) &i;
        y  = y * ( threehalfs - ( x2 * y * y ) );   // 1st iteration
        // y  = y * ( threehalfs - ( x2 * y * y ) );   // 2nd iteration, this can be removed

        return y;
    }

Außerdem Formeln in $\LaTeX$ Notation dank [MathJax](https://www.mathjax.org/)

$$\mathcal H = \sum_{\left< i, j \right>} s_i s_j$$

Ich werde diese Gelegenheit außerdem nutzen die meisten Einträge meines Blogs
zu verwerfen und nur einige ausgewählte zu überarbeiten und hier zu
veröffentlichen.

