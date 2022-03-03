Title: Platzhalterbilder
Date: 2017-11-29 10:21
Author: surt91
Category: Meta
Tags: Bild, JavaScript, Python
Slug: image-preview
Status: published
Lang: de

Große Bilder können die Ladezeit von Webseiten dramatisch verschlechtern.
Schlimmer als weiße Flächen ist das sprungartige Verschieben des Textes, wenn
weiter oben gerade ein Bild fertig geladen wurde. Allerdings müssen Bilder bei
immer weiter steigenden Pixeldichten der Anzeigegeräte auch immer
hochaufgelöster werden und gleichzeitig über langsame 3G-Verbindungen
geladen werden.

Da der [Eintrag über Fraktale]({filename}/randomFractals.md) einige recht große
Bilder enthält, habe ich ein Pelican-Plugin geschrieben, das

1.  Vorschau-.jpg erzeugt, die in der Regel kleiner als 1 kB sind,
2.  jedes Bild durch die data-uri des Previews ersetzt und dies verschwommen anzeigt, bis das Originalbild per JavaScript nachgeladen ist.

Das sieht dann etwa so aus:

<video controls width="800" height="460">
<source src="/vid/image_preview.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

Glücklicherweise ist es recht einfach mit Python html zu parsen und data-uri
zu erzeugen, sodass mein Plugin im Wesentlichen fertig generiertes html nimmt
und folgendes tut:

``` py
import base64
from bs4 import BeautifulSoup

with open("file.html") as f:
    soup = BeautifulSoup(f, "html.parser")

    for img in soup.find_all("img"):
        thumbnail = create_thumbnail(img)
        b64 = base64.b64encode(open(thumbnail, "rb").read()).decode("utf-8")
        data_uri = f"data:image/jpeg;base64,{b64}"
        # TODO: replace img source by the data-uri
```

Nachdem alles vorbereitet ist, ist die clientseitige Logik mit ein paar Zeilen
[JavaScript](https://github.com/surt91/purepelican/blob/1e1371d644de4b3af733e78bebe4869bc9121681/static/js/img.js)
und [CSS](https://github.com/surt91/purepelican/blob/1e1371d644de4b3af733e78bebe4869bc9121681/static/sass/_images.scss)
recht simpel.

Die Idee ist, dynamisch die voll aufgelösten Bilder per JavaScript zu laden und
mit dem `onLoad` Event sichtbar zu machen.
