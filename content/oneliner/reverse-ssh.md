Title: reverse ssh
Date: 2017-12-11 15:35
Author: surt91
Category: Snip
Slug: reverse-ssh
Status: published
Lang: de

Führe auf dem Computer `target`, der hinter einer Firewall steht und dennoch
per SSH erreichbar sein soll folgendes aus

```bash
ssh -f -N -R 0.0.0.0:19999:localhost:22 user@server
```

`server` muss erreichbar sein und in `/etc/ssh/sshd_config`
folgende Option aktiviert haben

```text
GatewayPorts yes
```

Jetzt kann man von beliebigen Clients auf den Computer `target` zugreifen per

```bash
ssh -p 19999 user@server
```

So kann man beispielsweise auch `sshfs` nutzen.

```bash
sshfs -p 19999 user@server:folder ~/sshfs
```
