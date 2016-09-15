Title: Depth First Search und Labyrinthe
Date: 2013-12-15 12:30
Author: surt91
Category: code
Tags: Python, Video
Slug: depth-first-search-und-labyrinthe
Status: draft

Wenn man alle Knoten eines Graphen besuchen möchte, benutzt meist
entweder eine Breitensuche oder eine Tiefensuche. (Übrigens auch, wenn
man ein bestimmtes Element sucht. Aber die Knoten einfach nur mal so zu
besuchen, ist nett und zeigt, dass man sich um seinen Graphen sorgt.)

1.  Man starte an einem Knoten.
2.  Man schiebe die noch nicht besuchten Nachbarn auf einen Stack (für
    die Tiefensuche) oder eine Queue (für die Breitensuche). 
3.  Man entnehme einen Knoten vom Stack/Queue und fahre bei 2. fort, bis
    der Stack/Queue leer ist.

Und weil ich gerade dabei bin, den
[Wikipedia-Artikel](http://en.wikipedia.org/wiki/Depth-First_Search) zu
wiederholen, mache ich auch weiter damit.

Der beste Anwendungsfall ist nämlich, ein bisschen Zufall in den
Algorithmus zu mischen, ein Labyrinth zu bauen und ein Video davon in HD
zu posten!

<iframe allowfullscreen="" frameborder="0" height="360" src="//www.youtube.com/embed/4BPB5tNOw30?rel=0" width="640"></iframe>

Und weil man dafür weniger als 100 Zeilen Python braucht, spendiere ich
auch den Code, falls irgendjemandem das Video nicht reicht. (Oder etwas
gegen Youtube hat und sich das Video deshalb lieber selbst bauen
würde.)  
Außerdem gibt es mir Gelegenheit `networkx`zu erwähnen. Ein Python
Modul, das sehr schöne Klassen für Graphen bereitstellt.

    #!python3
    #!/usr/bin/env python3
    import networkx as nx
    from random import shuffle

    def dfs(g, seed=0):
        """Introduction to Algorithms (C. L. R. S.)"""
        path = []
        stack = []
        explorer = {seed:seed}
        for n in g.nodes_iter():
            g.node[n]['color'] = "white"

        g.node[seed]['color'] = "gray"
        stack.append(seed)

        while stack:
            u = stack.pop()
            path.append(u)

            neighbors = g.neighbors(u)
            shuffle(neighbors)

            for n in neighbors:
                if g.node[n]['color'] == "white":
                    g.node[n]['color'] = "gray"
                    stack.append(n)
                    explorer.update({n:u})

            g.node[u]['color'] = "black"

        return path, explorer

    def createSquareLattice(x,y):
        G=nx.Graph()

        for i in range(x):
            for j in range(y):
                G.add_node(i+j*x)

        for n in G.nodes():
            if n+1 < x*y and n%x != x-1:
                G.add_edge(n,n+1) # right
            if n+x < x*y:
                G.add_edge(n,n+x) # below

        return G

    def writeSVG(path, explorer, x, y, filename="maze.svg"):
        scale = 30
        offset = scale/2
        thickness = scale/3
        join = width/2

        height = (y-1)*scale+2*offset
        width  = (x-1)*scale+2*offset

        header = "<svg version='1.1' baseProfile='full' width='{x}' height='{y}'>\n"
        header +="<rect fill='white' width='{x}' height='{y}'>\n"
        header = header.format(x=width, y=height)
        line = "<line x1='{x1}' x2='{x2}' y1='{y1}' y2='{y2}' stroke='black' stroke-width='{w}'>\n"
        footer = "</svg>\n"

        with open(filename, "w") as f:
            f.write(header)

            for p1 in path:
                p2 = explorer[p1]
                cX1, cY1 = p1%x, p1//x
                cX2, cY2 = p2%x, p2//x

                # do not draw a line if the jump is longer than one node
                if abs(cX1 - cX2) + abs(cY1 - cY2) == 1:
                    f.write(line.format(x1=cX1*scale+offset+(cX1-cX2)*join,
                                        x2=cX2*scale+offset-(cX1-cX2)*join,
                                        y1=cY1*scale+offset+(cY1-cY2)*join,
                                        y2=cY2*scale+offset-(cY1-cY2)*join,
                                        w=thickness))

            f.write(footer)

    if __name__ == "__main__":
        x,y = 64,36
        G = createSquareLattice(x,y)
        p, ex = dfs(G)
        writeSVG(p, ex ,x,y)
        
        for i in range(len(p)):
            writeSVG(p[:i+1], ex , x, y, "maze_{:03d}.svg".format(i))
        
Wer bis hier hin durchgehalten hat, hat es sich verdient, zwei weitere
Videos anzusehen.  
Hier ist eine Breitensuche, erwartet langweilig:

<iframe allowfullscreen="" frameborder="0" height="360" src="//www.youtube.com/embed/vQu5gaOlWe0?rel=0" width="640"></iframe>

Und hier bin ich mir nicht sicher, was schief gegangen ist. Aber es ist
genial!

<iframe allowfullscreen="" frameborder="0" height="360" src="//www.youtube.com/embed/eP_W_etvGoM?rel=0" width="640"></iframe>




