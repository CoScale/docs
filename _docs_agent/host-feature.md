---
layout: page
title: HOST feature
description: Monitor services that run on a host from our Container Agent
---

If the CoScale agent is installed as a Container, you can gather data from services running on the host, without installing an agent as a package on the host. This mechanism can be used to parse log files or execute a script on the host instead of a container running on the host. It is typically used to monitor services that are running on the host, but not in a container.

## Steps

* Click on the "Add image" button.

* In the "Repository" filed, write HOST (all caps).

<img alt="HOST feature" src="{{ site.baseurl }}/gfx/agent/extra/host-feature.png" style="img-responsive"/>

* Add the plugins for the services you want to monitor and configure them, by following the instructions on the screen.
