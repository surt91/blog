Title: Raspberry Router
Date: 2021-05-10 20:19
Author: surt91
Category: Snip
Slug: raspberry-router
Status: published
Lang: en

You need to connect something with an ethernet cable to the
internet, but there is only Wifi and all you have is a Raspberry PI?

No problem, all you need to do is connecting it to the Wifi, plug the
ethernet cable in and tell it to forward all traffic from the one interface
to the other, as described in the [Arch Linux Wiki](https://wiki.archlinux.org/index.php/Internet_sharing).

```bash
sysctl net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
```

Since our Raspberry is now a router, it should also assign IP addresses to the
devices connected to it via DHCP, for example with [dnsmasq](https://wiki.archlinux.org/title/Dnsmasq)
and the following configuration in `/etc/dnsmasq.conf`:

```plain
#disable dns
port=0

dhcp-range=192.168.13.50,192.168.13.150,12h
bind-interfaces
dhcp-option=3,0.0.0.0
dhcp-option=6,1.1.1.1,8.8.8.8
```

This is also a good opportunity to route all traffic through a VPN,
by replacing the `wlan0` interface above by the configured VPN interface
(e.g. `tun0` for OpenVPN or `wg0` for WireGuard).
