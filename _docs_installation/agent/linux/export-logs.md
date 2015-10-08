---
layout: page
title: Export logs
description: How to export CoScale agent logs for debugging and support on Linux.
---

## Logfile location

* Debian: `/var/log/coscale-agent.log`
* Ubuntu: `/var/log/upstart/coscale-agent.log`
* Centos: `sudo journalctl -u coscale-agent.service`
