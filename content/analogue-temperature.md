Title: Analog-Digital-Analoges Thermometer
Date: 2022-10-03 15:18
Author: surt91
Category: Tech
Tags: C, Code, Bild, Microcontroller
LargeFeaturedImage: img/analogue_temperature1200.webp
Status: published
Lang: de

Ich habe mir ein analoges Voltmeter zugelegt und möchte es als Thermometer benutzen.

Da der Widerstand von Metallen mit der Temperatur steigt, kann man Temperatur relativ gut messen, indem man
einen kalibrierten Widerstand misst. Daher kann man mit den meisten Multimetern und einer passenden Sonde
auch die Temperatur messen.

Da ich mir aber keine Gedanken darüber machen möchte, wie ich eine Schaltung aussehen müsste, um $15°\mathrm{C}$
in $1.5 \mathrm{V}$ umzusetzen (vielleicht würde eine [Brückenschaltung](https://de.wikipedia.org/wiki/Br%C3%BCckenschaltung)
funktionieren?), wähle ich den einfachen Weg mit einer Reihe integrierter Schaltkreise und einem Microcontroller.

![Schaltplan meines Analog-Digital-Analog-Thermometers](/img/analogue_temperature_circuit.svg)

Hier ist ein günstiger DS18B20 Temperatursensor, der von einem ESP8266 ausgelesen wird. Dieser steuert dann einen
MCP4725 Digital-Analog-Wandler so an, dass er eine Spannung ausgibt, deren Wert in Volt ein Zehntel der gemessenen
Temperatur ist. Diese Spannung wird dann von meinem alten Voltmeter gemessen und angezeigt. Hier ist es also gerade $24°\mathrm{C}$.

[![Foto meines Analog-Digital-Analog-Thermometers](/img/analogue_temperature1200.webp)](/img/analogue_temperature.webp)

Hier ist übrigens der simple Code, der beispielsweise mit der Arduino IDE auf einen ESP8266 geflasht werden kann:

```c++
#include <Wire.h>
#include <Adafruit_MCP4725.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS D4
#define MCP4725In A0

Adafruit_MCP4725 MCP4725;

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature DS18B20(&oneWire);

void setup() {
    Serial.begin(9600);

    DS18B20.begin();
    // 0x60 is the I2C address of my MCP4725A0
    MCP4725.begin(0x60);
}

float getTemperature() {
    float temp;
    do {
      DS18B20.requestTemperatures();
      temp = DS18B20.getTempCByIndex(0);
      delay(100);
    } while (temp == 85.0 || temp == (-127.0));
    return temp;
}

void setVoltage(float value) {
    value /= 10;
    float voltageOut = value*4096/3.3;
    MCP4725.setVoltage(voltageOut, false);

    // read it for testing and maybe calibrating
    int adcInput = analogRead(MCP4725In);
    float voltageIn = (adcInput * 3.3 )/ 1024.0;
    Serial.print("Expected Voltage: ");
    Serial.println(value, 3);

    Serial.print("Measured Voltage: ");
    Serial.println(voltageIn, 3);
}

void loop() {

    float temperature = getTemperature();
    setVoltage(temperature);

    // send temperature to the serial console
    dtostrf(temperature, 2, 2, temperatureString);
    Serial.println(temperatureString);

    delay(1e3);
}
```
