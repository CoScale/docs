---
layout: page
title: Linux
description: Information on how to integrate CoScale with auto scaling and cloud providers.
---

## Automatic provisioning
On installation our agent creates an agent.conf file containing a UID. This UID is used to identify the server on our platform. When creating an image it is important to remove the agent.conf file. If you don’t the agent will push metrics for the previous server and not add a new one. You can find the file in `/opt/coscale/agent/etc` on Linux or `C:/Program Files (x86)/CoScale/Agent/` on Windows.


## [Pushing server status to CoScale on boot and shutdown]({{ site.baseurl }}/agent/cloud/server-status)
Enable or disable a server in our platform when it is booted or shut down.
