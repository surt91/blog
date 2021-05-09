Title: relay ssh
Date: 2018-03-21 10:46
Author: surt91
Category: Snip
Slug: relay-ssh
Status: published
Lang: en

Connect via a server `relay` with `target`. Useful if `target` is behind a
firewall, but reachable from `relay`.

```bash
ssh -J user1@relay user2@target
```

This can be combined with other options. This way a port forwarding can
be established over which, e.g., `sshfs` can be used.

```bash
ssh -L 9999:localhost:22 -J user1@relay user2@target
sshfs user2@localhost:/path /mountpoint -C -p 9999
```

A combination with [reverse-ssh]({filename}/en/oneliner/reverse-ssh.md)
could look like this:

```bash
ssh -L 9999:localhost:22 -J user1@relay -p 19999 user2@localhost
```
