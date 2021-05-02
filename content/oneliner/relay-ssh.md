Title: relay ssh
Date: 2018-03-21 10:46
Author: surt91
Category: Snip
Slug: relay-ssh
Status: published
Lang: de

Um sich per Server `relay` mit `target` zu verbinden. Nützlich wenn `target`
hinter einer Firewall versteckt, aber von `relay` erreichbar ist.

```bash
ssh -J user1@relay user2@target
```

Dies kann mit anderen Optionen kombiniert werden, sodass eine Portweiterleitung
stattfinden kann, über die bspw. `sshfs` genutzt werden kann.

```bash
ssh -L 9999:localhost:22 -J user1@relay user2@target
sshfs user2@localhost:/path /mountpoint -C -p 9999
```

Eine Kombination mit [reverse-ssh]({filename}/oneliner/reverse-ssh.md)
könnte so aussehen:

```bash
ssh -L 9999:localhost:22 -J user1@relay -p 19999 user2@localhost
```
