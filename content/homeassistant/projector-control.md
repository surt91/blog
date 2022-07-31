Title: Heimkinoautomatisierung
Date: 2022-07-30 17:30
Author: surt91
Category: Tech
Tags: Home Assistant, ESPHome
LargeFeaturedImage: img/heimkinoautomatisierung1200.webp
Status: published
Lang: de

Ich habe seit langem einen Beamer statt eines Fernsehers, was einige Vorteile
mit sich bringt: ein sehr großes Bild, kein im Weg stehender Fernseher und
die perfekte Motivation Hausautomatisierung in Angriff zu nehmen. Schließlich
ist der Ablauf, bevor ein Film starten kann, durchaus aufwendig:

1. Die Jalousien werden geschlossen.
2. Die Leinwand fährt herunter.
3. Der AV-Receiver wird angeschaltet.
4. Der Beamer startet.

Tatsächlich hatte ich vor Jahren einen selbstgeschriebenen Python-Server auf
einem Raspberry Pi aufgesetzt, der diese Steuerung übernommen hat. Aber vor kurzem
habe ich ihn ersetzt durch die Anbindung von einem ESP 8266 mittels
[ESP Home](https://esphome.io/) an [Home Assistant](https://www.home-assistant.io/).
In meinem Setup kommt von Infrarot (IR) Fernbedienung über 433 MHz Funk (RF) und Transistoren,
die über Fernbedienungskontakte gelötet sind, bis zu einer seriellen RS232 Schnittstelle
alles vor. Es sollte also für jeden Leser etwas dabei sein.

## Die Jalousien

Meine Jalousien wurden ursprünglich per Hand mit einem Gurt geöffnet und geschlossen.
Der einfachste Weg solche Rollläden weniger manuell zu machen, sind nachrüstbare Gurtwickler,
die die Muskelkraft durch einen Servomotor ersetzen. Ich habe mir einen relativ günstigen
elektrischen Gurtwickler mit einer 433 MHz Fernbedienung gekauft. Der Plan war eigentlich
mit einem 433 MHz Receiver die Signale aufzuzeichnen und danach mit einem Sender wieder zu
schicken.

Blöderweise hat sich (unter Verwendung von Audacity als Offline-Oszilloskop) herausgestellt,
dass sich das Signal bei jedem Knopfdruck ändert -- anscheinend nutzen meine Gurtwickler
ein Protokoll mit Schlüssel, was beispielsweise für sicherheitsrelevante Anwendungen wie
Garagentore verwendet wird.

Die einfache Lösung dafür ist, die Fernbedienung auseinander zu bauen und die Taster, die
normalerweise per Hand ausgelöst werden, mit Transistoren zu überbrücken, die dann über
GPIO Pins ausgelöst werden können.

[![Das ist zwar die Fernbedienung von der Leinwand, aber das Prinzip ist das gleiche und ich habe es versäumt ein Foto von der Jalousien-Fernbedienung zu machen](/img/screen_switch1200.webp)](/img/screen_switch.webp)

Und die Konfiguration in ESP Home ist selbsterklärend.

```yaml
output:
  - platform: gpio
    id: blinds_up_pin
    pin: D7

button:
  - platform: output
    id: blinds_up
    name: Jalusinen hoch
    icon: "mdi:roller-shade"
    output: blinds_up_pin
    duration: 300ms
# skipped blinds down
```

## Die Leinwand

Motorisierte Leinwände haben oft einen Eingang für einen 3,5 mm Klinkenstecker, den man direkt mit
dem Beamer verbinden kann. Leider nicht die Leinwand, die ich habe. Aber halb so schlimm, denn
sie hat eine Funkfernbedienung und ich habe ja noch die 433 MHz Hardware, die für die Jalousien
gedacht waren. Und tatsächlich nutzt meine Leinwand ein simples Protokoll -- aber auf 315 Mhz.

Sobald wir also einen 315 MHz Transmitter und Receiver haben, können wir die Codes aufzeichnen und die ESP Home
Konfiguration anpassen. Dafür definieren wir einen `remote_transmitter` für den passenden GPIO Pin
und einen `switch`, der den Code für "herunter fahren" sendet, die passende Zeit wartet und dann den Code
für "stopp" sendet. Eine Stolperfalle ist, dass der Code mittels `repeat` mehrmals gesendet werden
muss.

```yaml
remote_receiver:
  - id: RF315_Recv
    pin:
      number: D5
      inverted: yes
      mode: INPUT_PULLUP
    dump: all

remote_transmitter:
  - id: RF315
    pin: D1
    carrier_duty_percent: 100%

switch:
  - platform: template
    name: Screen
    icon: "mdi:projector-screen"
    optimistic: true
    turn_on_action:
      - remote_transmitter.transmit_rc_switch_raw:
          transmitter_id: RF315
          code: '000110110111100111000100'
          protocol: 1
          repeat:
            times: 10
            wait_time: 0s
      - delay: 39.0s
      - remote_transmitter.transmit_rc_switch_raw:
          transmitter_id: RF315
          code: '000110110111100111001000'
          protocol: 1
          repeat:
            times: 10
            wait_time: 0s
    # turn_off_action skipped
```

## Der AV-Receiver

Dies ist die erste Komponente, die nach Plan läuft: Der AV-Receiver hat eine IR Fernbedienung
und der Hersteller veröffentlicht die Codes sogar selbst, sodass ich mir das Aufzeichnen sparen kann.
Falls man diesen Luxus nicht that, kann man an den ESP einen IR Receiver wie einen TSOP 4838
anschließen und mit dem [`remote_receiver`](https://esphome.io/components/remote_receiver.html)
auswerten.

Um die Signale zu senden, reicht eine Infrarotdiode, die ich über einen Transistor schalte.

![Infrarot Sender](/img/ir_esp.svg)

Für ESP Home müssen wir einen weiteren `remote_transmitter` definieren. Damit die Codes über die IR Diode
und nicht über den RF Sender verschickt werden, müssen wir dem Transmitter eine Id zuweisen und diese später
mit `transmitter_id` referenzieren.

```yaml
remote_transmitter:
  - id: IR
    pin: D2
    carrier_duty_percent: 50%

button:
  - platform: template
    id: av_on
    name: AV on
    icon: "mdi:audio-video"
    on_press:
      - remote_transmitter.transmit_pioneer:
          transmitter_id: IR
          rc_code_1: 0xA51A
          repeat:
            times: 2
# skipped other buttons
```

## Der Beamer

Den Beamer könnte man natürlich auch per IR steuern, aber mein Modell, der BenQ W1070, hat eine RS232
Schnittstelle, die nicht nur etwas zuverlässiger als die Infrarotschnittstelle ist, sondern es auch
erlaubt den aktuellen Zustand auszulesen. Dazu können wir bspw. einen MAX3232 an die UART
Pins anschließen und die Beispielkonfiguration für den custom `text_sensor` aus der ESP Home
Dokumentation kopieren.

```yaml
logger:
  # disable logging over uart
  baud_rate: 0

uart:
  id: uart_bus
  tx_pin: 1
  rx_pin: 3
  # choose same value set in the projector settings
  baud_rate: 9600

text_sensor:
  # this needs the .h file from https://esphome.io/cookbook/uart_text_sensor.html
  - platform: custom
    lambda: |-
      auto my_custom_sensor = new UartReadLineSensor(id(uart_bus));
      App.register_component(my_custom_sensor);
      return {my_custom_sensor};
    text_sensors:
      id: "uart_readline"

switch:
  - platform: template
    name: "Projector Power"
    icon: "mdi:projector"
    lambda: |-
      if (id(uart_readline).state == "*POW=ON#") {
        return true;
      } else if(id(uart_readline).state == "*POW=OFF#") {
        return false;
      } else {
        return {};
      }
    turn_on_action:
      - uart.write: "\r*pow=on#\r"
    turn_off_action:
      - uart.write: "\r*pow=off#\r"
```

## Fazit

Da dies doch eine ganze Menge Komponenten sind, die ich per Jumper-Kabel an den ESP
geschlossen habe, ist noch ein Gehäuse nötig. Dazu nutze ich die beste Alternative zu
einem 3D-Drucker: Lego!

[![Alle Komponenten mittels Lego an der Beamerhalterung befestigt](/img/heimkinoautomatisierung1200.webp)](/img/heimkinoautomatisierung.webp)

Die Aufhängung des Beamers bietet dabei den optimalen Ort für eine provisorische
Befestigung, die nahe am RS232-Eingang des Beamers ist und einen guten Blick
auf den IR-Empfänger des AV-Receivers hat.

Die gesamte EPS-Home-Konfigurationsdatei steht auch als
[GitHub Gist](https://gist.github.com/surt91/dde1e7986cda0177a7b790930edb7230)
bereit.

Das ganze Setup wird abgerundet von einem selbstgebauten Schalter (mit Cherry Blue Switches),
um den Kinomodus zu starten und zu beenden, sowie Home-Assistant-Automatisierungen,
die das Licht kontrollieren: Licht aus wenn der Film startet, Licht gedimmt, wenn er pausiert.
