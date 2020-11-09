Title: reverse ssh
Date: 2017-12-11 15:35
Author: surt91
Category: Snip
Slug: reverse-ssh
Status: published
Lang: en

On the computer `target` behind a firewall, in which you want to login in the
future, do

```bash
ssh -f -N -R 0.0.0.0:19999:localhost:22 user@server
```

`server` need to be reachable and needs to have the following option
set in `/etc/ssh/sshd_config`

```text
GatewayPorts yes
```

Now any client can reach `target` with

```bash
ssh -p 19999 user@server
```

This can also used for, e.g., `sshfs`

```bash
sshfs -p 19999 user@server:folder ~/sshfs
```
