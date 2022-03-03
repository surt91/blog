Title: Progressive Web App
Date: 2017-09-01 18:15
Author: surt91
Category: Meta
Tags: JavaScript
Status: published
Lang: de

Seit Anfang September ist dieses Blog eine *Progressive Web App*. Das bedeutet,
dass dieses Blog nun auch offline funktioniert und man es auf dem Smartphone
als App hinzufügen kann.

### Warum? [![Lighthouse](/img/lighthouse.png){: .icon}](https://developers.google.com/web/tools/lighthouse/)

Nun, Chrome bietet mit *Lighthouse* Ratschläge, wie man seine Website verbessern
kann. Einer der vier Unterpunkte heißt *Progressive Web App* und war frustrierend
schlecht bewertet. Die folgenden Schritte habe ich also nur für Lighthouse
gemacht und es hat sich auf jeden Fall gelohnt:

![Lighthouse-Audit Ergebnisse](/img/lighthouse_audit.png)

### Wie?

Lighthouse bietet eine Checkliste, auf der neben einigen Punkten, die
generell eine gute Idee sind, drei Punkte aufgeführt sind, die erfüllt sein
müssen:

* Site is served over HTTPS
    - Dank *Let's Encrypt* ist das kein Problem mehr.
* The start URL (at least) loads while offline
    - Das ist der aufwendigste Teil. Um dies zu erreichen muss man einen
    *service worker* registrieren. Damit der *service worker* weiß, welche
    Dateien notwendig sind, benutze ich nach jedem erfolgreichen Build
    [sw-precache](https://github.com/GoogleChrome/sw-precache) mit einer
    [sehr einfachen Konfiguration](https://github.com/surt91/blog/blob/1d29d7bd848e31bfa4dc3f57bd140e92cbdf6de5/sw-config.js).
    Dadurch benötige ich jetzt Node, um das Blog zu erstellen `¯\_(ツ)_/¯`
* Metadata provided for Add to Home screen
    - Damit ist eine `manifest.json` gemeint. Diese Datei enthält links zu Icons,
    die als Appsymbol benutzt werden, wenn man die Seite auf Android oder Windows
    installiert. Und es legt die Farbe der Adressleiste im mobilen Chrome fest.
    Ein nützlicher Dienst, um ein solches Manifest zu erstellen, ist
    [app-manifest.firebaseapp.com](https://app-manifest.firebaseapp.com/)

## Was jetzt?

Service Worker ermöglichen Benachrichtigungen von einer Website. Ein natürlicher
nächster Schritt wäre es also Benachrichtigungen zu versenden, wenn ein neuer
Post online ist. Auf der anderen Seite bin ich selbst immer etwas genervt von
Websites, die mich benachrichtigen wollen und der Lighthouse Punktestand ist
schon optimal, also wird das wohl nicht passieren.
