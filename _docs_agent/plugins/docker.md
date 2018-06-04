---
layout: page
title: Monitoring and collecting data from Docker
description: Information on how to install the docker plugin and configure your container monitoring
---

> Docker is the world’s leading software containerization platform. Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications, whether on laptops, data center VMs, or the cloud. Docker containers wrap a piece of software in a complete filesystem that contains everything needed to run: code, runtime, system tools, system libraries – anything that can be installed on a server. This guarantees that the software will always run the same, regardless of its environment.

More information on: [https://www.docker.com/](https://www.docker.com/)

## How it works
The CoScale agent detects running containers on your system and starts gathering resources without any configuration. To have a more in-depth view on the process within the container you need to active the CoScale incontainer monitoring system.

The in-container system uses CoScale plugins to gather data from the process running in the container. You can find a full [list of our plugins on the Agent page](/agent/index/#integrations). CoScale requires some configuration to be able to detect which containers to monitor. You can find [more information on our application monitoring documentation]({{ site.baseurl }}/agent/application-monitoring).

The plugin will be started within the namespace of the running container, this has the advantage that you do not have to expose any ports or mount the filesystem for the CoScale in-container monitoring to be able to do its job.

## Installation

{% include_relative _installation.md orchestrator="false" %}


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/docker.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
