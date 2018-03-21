Title: relay ssh
Date: 2018-03-21 10:46
Author: surt91
Category: Snip
Slug: relay-ssh
Status: published

Um sich per Server `relay` mit `target` zu verbinden.

```bash
ssh -J user1@relay user2@target
```

Dies kann anderen Optionen kombiniert werden, sodass eine Portweiterleitung
stattfinden kann, über die bspw. `sshfs` genutzt werden kann.

```bash
ssh -L 9999:localhost:22 -J user1@relay user2@target
sshfs user2@localhost:/path /mountpoint -C -p 9999
```
