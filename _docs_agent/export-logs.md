---
layout: page
title: Export logs
description: How to export CoScale agent logs for debugging and support on Linux.
---

## Unix

* Debian: `/var/log/coscale-agent.log`
* Ubuntu: `/var/log/upstart/coscale-agent.log`
* Centos: `sudo journalctl -u coscale-agent.service`

## Docker

* Docker container: `docker logs $(docker ps | awk '/coscale-agent/ {print $1}')`
* Docker Swarm / Docker Datacenter: `docker service logs coscale-agent`
* Kubernetes: `kubectl get pods -n <namespace> | grep coscale-agent` and `kubectl logs -n <namespace> <coscale-agent-pod-name>`

## Microsoft Windows

1. Launch Event Viewer
![Event viewer]({{ site.baseurl}}/gfx/installation/agent/windows/export-logs/event_viewer.png)

2. Create Custom View (By source: CoScaleAgent)
![Create custom view]({{ site.baseurl}}/gfx/installation/agent/windows/export-logs/create_custom_source.png)

3. Save Custom View
![Save custom view]({{ site.baseurl}}/gfx/installation/agent/windows/export-logs/save_custom_view.png)

4. Go to Custom View
![Go to custom view]({{ site.baseurl}}/gfx/installation/agent/windows/export-logs/goto_custom.png)

5. Click 'Save All Events in CoScale'
![Save all events]({{ site.baseurl}}/gfx/installation/agent/windows/export-logs/goto_custom.png)

6. Save them in a .txt file and send them to your CoScale <a href="mailto:info@coscale.com" class="js-support">support agent</a>.
