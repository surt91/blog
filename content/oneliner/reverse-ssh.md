Title: reverse ssh
Date: 2017-12-11 15:35
Author: surt91
Category: Snip
Slug: reverse-ssh
Status: published

Führe auf dem Computer, der per SSH erreichbar sein soll folgendes aus

```bash
ssh -f -N -R 0.0.0.0:19999:localhost:22 user@example.com
```

Auf dem Server (hier `example.com`) muss noch die `/etc/ssh/sshd_config`
angepasst werden:

```
GatewayPorts yes
```

Jetzt kann man von beliebigen Clients auf den Computer zugreifen per

```bash
ssh -p 19999 user@example.com
```

So kann man beispielsweise auch sshfs nutzen.

```bash
sshfs -p 19999 user@example.com:folder ~/sshfs
```
