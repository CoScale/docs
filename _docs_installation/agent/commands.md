---
layout: page
title: Agent commands
---

## Install

### Linux

* Ubuntu / Debian: `sudo dpkg -i [filename]`
* CentOS: `sudo rpm -iUvh [filename]`

### Windows

* All: `Doubleclick`

## Restart

### Linux
* Ubuntu / Debian: `service coscale-agent restart`
* CentOS: `systemctl restart coscale-agent.service`

### Windows

* All: [Restarting windows agent]({{ site.baseurl}}/advanced/windows/agent-restart)

## Uninstall

### Linux

* Ubuntu / Debian: `sudo apt-get remove --purge coscale-agent`
* CentOS: `sudo rpm -e coscale-agent-1.0-1.x86_64`

### Windows

<!-- TODO: Add uninstall -->
