Title: pirShow
Date: 2022-10-08 12:31
Author: surt91
Category: Code
Tags: Python
LargeFeaturedImage: img/pirShow1200.webp
Status: published
Lang: de

Alte Monitore sind zu Schade zum Entsorgen. Als Upcycling habe ich deshalb
einen alten Monitor zu einem digitalen Bilderrahmen in meinem Flur umfunktioniert.
Sinnvollerweise sollte er natürlich nur dann ein Bild zeigen, wenn auch jemand da ist,
der es betrachten kann. Hier möchte ich einmal kurz beschreiben, wie ich einen
Raspberry Pi, einen passiven Bewegungssensor und etwas Python-Code zu diesem Zweck benutze.

## Bildquellen definieren

Die Hauptfunktionalität eines digitalen Bilderrahmens ist es natürlich Bilder anzuzeigen.
Diese Bilder sollen aus mehreren Quellen zufällig ausgewählt werden. Dabei habe ich mir
einige Flickr-Accounts über Raumfahrt und meine Twitter-Bots ausgesucht. Zuerst brauchen
wir also etwas Code, um die Bilder herunterzuladen.

```python
def flickr(user_id):
    import flickrapi
    from keys_and_secrets import keys_and_secrets

    url_template = 'http://farm%(farm_id)s.staticflickr.com/%(server_id)s/%(photo_id)s_%(secret)s_b.jpg'

    def url_for_photo(p):
        return url_template % {
            'server_id': p.get('server'),
            'farm_id': p.get('farm'),
            'photo_id': p.get('id'),
            'secret': p.get('secret'),
        }

    flickr = flickrapi.FlickrAPI(keys_and_secrets["flickr_key"], keys_and_secrets["flickr_secret"])

    photo = random.choice(flickr.photos.search(user_id=user_id, per_page=500)[0])
    purl = url_for_photo(photo)
    title = photo.get('title')

    fname = save_image(purl, title)

    return fname


def twitter(atname):
    import tweepy
    from keys_and_secrets import keys_and_secrets

    auth = tweepy.OAuthHandler(keys_and_secrets["consumer_key"], keys_and_secrets["consumer_secret"])
    auth.set_access_token(keys_and_secrets["access_token_key"], keys_and_secrets["access_token_secret"])

    api = tweepy.API(auth)
    tweets = api.user_timeline(atname, count=30)

    urls = []
    for i in tweets:
        if "media" in i.entities:
            for j in i.entities["media"]:
                url = j["media_url"]
                if "thumb" not in url:
                    urls.append((url, i.id_str))

    purl, title = random.choice(urls)

    fname = save_image(purl, title)

    return fname
```

Dann bauen wir uns einen praktischen Decorator, den wir nutzen, um unterschiedliche Accounts
als Bildquellen zu registrieren.

```python
sources = {}

def source(source_name):
    def source_decorator(func):
        sources[source_name] = func

        @wraps(func)
        def func_wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return func_wrapper
    return source_decorator


@source("apollo")
def apollo():
    return flickr("projectapolloarchive")


@source("randomGraphs")
def randomGraphs():
    return twitter("@randomGraphs")


@source("AFractalADay")
def AFractalADay():
    return twitter("@AFractalADay")
```

Dies ermöglicht es dann sehr komfortabel zufällige Bilder herunterzuladen und anzuzeigen.

```python
def random_image():
    image_getter = random.choice(list(sources.values()))
    fname = image_getter()
    # show image
    # skipped terminating old instance of feh and aquiring a mutex
    env = os.environ
    env["DISPLAY"] = ":0"
    VIEWER = subprocess.Popen(
        ["feh", "-FZYx", fname],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
```

## Monitor ein- und ausschalten

Jetzt, da wir Bilder zum Anzeigen haben, müssen wir den Monitor ein- und ausschalten, damit man sie sieht
bzw. damit wir nicht sinnlos Strom verbrauchen. Hier rufen wir wieder Kommandozeilen-Werkzeuge auf:
`tvservice` schaltet den Standby-Modus des Monitors um und `chvt` wechselt einmal vom X-Server weg und
wieder zurück, was den Bildschirmschoner beendet.

```python
from threading import Timer, Lock

MUTEX = Lock()
STATE = False

def monitor(status):
    global STATE
    # needs to run as root
    # make sure that sudo will not ask for a password for these commands
    # e.g. use visudo to add
    # piruser ALL=(ALL) NOPASSWD: /usr/bin/tvservice, /bin/chvt
    with MUTEX:
        if status:
            if not STATE:
                os.system("sudo tvservice -p; sleep 0.5; sudo chvt 6; sleep 0.5; sudo chvt 7")
            STATE = True
        else:
            if STATE:
                os.system("sudo tvservice -o")
                # download and show the next image
                random_image()
            STATE = False
```

## PIR

Jetzt müssen wir diese Funktionalität nur noch durch einen Bewegungssensor auslösen. Dazu
schließen wir einfach einen Pyroelektrischen Infrarot Sensor (PIR) an beispielsweise Pin 23 und
sagen dem Raspberry, dass er dort horchen soll, ob ein Signal anliegt.

[![Ein PIR Bewegungsensor, der an einen Raspberry Pi angeschlossen ist](/img/pirShow1200.webp)](/img/pirShow.webp)

```python

import RPi.GPIO as GPIO

SENSOR_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

if __name__ == "__main__":
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=pir_callback)
```

Der `pir_callback` schaltet dann einfach den Monitor an und startet einen Timer,
der den Monitor wieder ausstellt (dieser Timer wird abgebrochen sobald der Callback
erneut aufgerufen wird, damit der Monitor an bleibt, solange jemand das Bild betrachtet.)

Der `pir_callback` sendet außerdem auch eine MQTT-Nachricht, um die Bewegungsmeldung
auch für Home-Assistant-Automatisierungen zu nutzen, sodass die Beleuchtung im Flur
nach Sonnenuntergang nun auch durch Bewegungen ausgelöst wird.
