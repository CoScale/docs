---
layout: page
title: Agent restart
description: Restarting the CoScale agent on Linux.
---

Follow these steps to restart the CoScale agent.

## Unix

* Ubuntu / Debian: `sudo service coscale-agent restart`
* CentOS 6.6: `sudo systemctl restart coscale-agent.service`
* CentOS 5.3: `sudo initctl restart coscale-agent`

## Microsoft Windows

1. Open Task Manager

2. Open the tab 'Services' (You might have to click on 'More details' first to see the different tabs)

3. Right-click on the CoScaleAgent service and click on restart
