---
layout: page
title: Agent restart
description: Restarting the CoScale agent on Linux.
---

Follow these steps to restart the CoScale agent.

* Ubuntu / Debian: `sudo service coscale-agent restart`
* CentOS 6.6: `sudo systemctl restart coscale-agent.service`
* CentOS 5.3: `sudo initctl restart coscale-agent`
