---
layout: page
title: Agent terminate
description: Terminating and uninstalling the CoScale agent on Linux.
---

## Terminate / kill CoScale agent

* Ubuntu / Debian: `sudo service coscale-agent stop`
* CentOS 6.6: `sudo systemctl stop coscale-agent.service`
* CentOS 5.3: `sudo initctl stop coscale-agent`

## Uninstall

* Ubuntu / Debian: `sudo apt-get remove --purge coscale-agent`
* CentOS: `sudo rpm -e coscale-agent-1.0-1.x86_64`
