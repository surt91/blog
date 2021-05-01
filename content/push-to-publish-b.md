Title: Push to Publish 2
Date: 2017-08-27 13:36
Category: Meta
Tags: Hosting
Slug: push-to-publish-b
FeaturedImage: img/netlify.png
Status: published
Lang: de

Nachdem ich vor Kurzem einen [euphorischen Eintrag]({filename}/push-to-publish.md)
über mein automatisiertes Update dieses Blogs via Travis-CI und GitHub pages
geschrieben habe, bin ich jetzt auf eine einfachere Lösung gestoßen.

### Alles unter einem Dach bei Netlify [![Netlify Logo](/img/netlify.png){: .icon}](https://www.netlify.com/)

Es gibt einen einfachen Buildservice, der zwar nicht so flexibel ist wie
Travis-CI, aber für dieses Blog ausreicht. Netlify baut die Seite also bei
jedem Push in ein beobachtetes GitHub Repository. Nach Konfiguration des DNS
und einem weiteren Knopfdruck ist die Seite mit einem SSL Zertifikat von
*Let's Encrypt* ausgestattet und erreichbar.
Also Bonus kann man selbst HTTP-Header bestimmen über eine `_headers` Datei:

```
/*
    Strict-Transport-Security: max-age=31536000; includeSubDomains
```

Also kann man HTTP/2 Server Push ausprobieren, ohne einen Server betreiben zu
müssen.
