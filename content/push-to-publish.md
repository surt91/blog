Title: Push to Publish
Date: 2017-08-11 17:00
Author: surt91
Category: Meta
Tags: Hosting
Slug: push-to-publish
FeaturedImage: img/octocat.png
Status: published


Seit Anfang August wird dieses Blog nicht mehr
[von einem Raspberry aus den eigenen vier Wänden ausgeliefert]({filename}/blogumzug.md),
sondern von GitHub pages. Da die Quellen dieses Blogs bereits [auf GitHub](https://github.com/surt91/blog)
sind, ist dies ein konsequenter Schritt.


## Hosting auf GitHub Pages [![GitHub Logo]({filename}/img/octocat.png){: .icon}](https://github.com/)

GitHub bietet hosting von statischen Seiten an, was perfekt zu diesem Pelican
Blog passt. Die Verwaltung ist denkbar einfach: Für jedes Repository ist der
Branch `gh-pages` unter `[username].github.io/[reponame]`, hier z.B.
[surt91.github.io/blog](https://surt91.github.io/blog), erreichbar.

Will man unter einer eigenen Domain error sein, reicht es aus im DNS für die
Domain einen CNAME Eintrag auf `[username].github.io` anzulegen und im root des
`gh-pages` Branches eine Datei `CNAME` mit der eigenen Domain anzulegen, hier z.B.

``` bash
echo blog.schawe.me > CNAME
```

Primär dient GitHub pages dazu Jekyll Seiten zu erstellen und auszuliefern, was
zu Konflikten führen kann, wenn man einfach nur statische Seiten im `gh-pages`
Branch vorhält. Dies lässt sich einfach vermeiden, indem man eine Datei
`.nojekyll` im root anlegt.


## Automatische Erstellung durch Travis CI [![Travis CI Logo]({filename}/img/travis.png){: .icon}](https://travis-ci.org/)

Natürlich könnte man das statische HTML auf einem lokalen Computer erstellen
und per Hand in den `gh-pages` Branch pushen. Aber man kann das auch einem
Dienst wie Travis [CI](https://de.wikipedia.org/wiki/Kontinuierliche_Integration)
überlassen.

Die Idee ist, dass jedes Mal wenn man die Quellen seiner Seite ändert -- im
Fall von Pelican werden die Blogeinträge in Markdown geschrieben und dann in
HTML konvertiert -- ein Server die Seite erstellt und das Ergebnis in den
`gh-pages` Branch pusht. Dadurch wird ein Update der Website auf ein einfaches
`git push` reduziert.

Die Konfiguration von Travis CI wird durch eine denkbar einfache YAML Datei
definiert.
Eine (vereinfachte) Konfiguration für dieses Blog sieht beispielsweise so aus:

``` yaml
# pelican is a python program
language: python
python:
  - "3.5"

# install pelican and some more packages
install: "pip install -r requirements.txt"

# generate static html through pelican's makefile
script:
  - make publish

# deploy to github pages
deploy:
  provider: pages
  skip_cleanup: true
  github_token: $GITHUB_TOKEN
  local_dir: output
  on:
    branch: master
```

Falls Fehler beim Erstellen auftreten, schickt Travis eine Email und bricht die
Veröffentlichung ab. Wenn keine Fehler auftreten, wird wenige Sekunden später
die neue Version von GitHub ausgeliefert.


## SSL verschlüsselt von Cloudflare®

Die `github.io` Domains werden zwar verschlüsselt ausgeliefert, aber natürlich
kann GitHub keine SSL Zertifikate für die eigene Domain ausstellen lassen.
Man kann auch kein eigenes Zertifikat hochladen. Aber die Situation ist nicht
so aussichtslos wie sie scheint. Cloudflare ermöglicht es, allerdings müssen
ein paar Bedingungen erfüllt sein.

Cloudflare muss

* als DNS Service für die gewünschte Domain genutzt werden und
* als Proxy vor der Seite benutzt werden.

Als Bonus können wir Cloudflares [CDN](https://de.wikipedia.org/wiki/Content_Delivery_Network)
nutzen.

Sobald sich Cloudflare um das DNS der Domain kümmert, kann über das Dashboard
SSL aktiviert werden -- und wenn man schon dabei ist, sollte man nicht auch die
`Always use HTTPS` und `HSTS` Option aktivieren möchte.
