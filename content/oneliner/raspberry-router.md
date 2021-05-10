Title: Raspberry Router
Date: 2021-05-10 20:19
Author: surt91
Category: Snip
Slug: raspberry-router
Status: published
Lang: de

Für die Fälle, in denen man nur per WLAN einen Zugang
zum Internet und nur einen Raspberry PI dabei hat, aber dennoch
kabelgebundenes Internet braucht, notiere ich diesen Eintrag.
Für weitergehende Informationen ist das [Arch Linux Wiki](https://wiki.archlinux.org/index.php/Internet_sharing),
wie immer, empfehlenswert.

Wir müssen unseren Raspberry nur mit dem WLAN verbinden, das Ethernetkabel
einstecken und spezifizieren, dass der Traffic vom einen zum
anderen weitergeleitet werden sollen.

```bash
sysctl net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
```

Da unser Raspberry jetzt ein Router ist, muss er natürlich auch die üblichen Aufgaben
eines Routers übernehmen und die Geräte, die per Ethernet verbunden werden
per DHCP mit IP Adressen versorgen, beispielsweise mittels [dnsmasq](https://wiki.archlinux.org/title/Dnsmasq)
mit folgender Konfiguration in `/etc/dnsmasq.conf`:

```plain
#disable dns
port=0

dhcp-range=192.168.13.50,192.168.13.150,12h
bind-interfaces
dhcp-option=3,0.0.0.0
dhcp-option=6,1.1.1.1,8.8.8.8
```

Bei der Gelegenheit kann man auch dafür sorgen, dass sämtlicher Traffic
durch ein VPN geleitet wird, indem man das `wlan0` Interface oben durch
das konfigurierte VPN-Interface austauscht (zB. durch `tun0` für OpenVPN
oder `wg0` für WireGuard).
