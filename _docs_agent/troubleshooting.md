---
layout: page
title: Troubleshooting a CoScale agent
description: Tips and tricks on how to troubleshoot a CoScale agent
---

Here we describe issues you might have with the CoScale agent and how to debug them. More importantly we share with you the information that you can send to our support department in the case you are not able to debug the issue yourself.

## Debug steps

When a CoScale agent is unable to communicate with the CoScale platform you will receive an 'Agent timeout' alert. In most cases this means there is something wrong with the machine the CoScale agent is running on, but sometimes it can be a network issue.

<img src="{{ site.baseurl}}/gfx/agent/troubleshooting-timeout.png" alt="Agent timeout" class="img-responsive" />

If you are able to connect to your machine and execute commands it usually means somewhere in the network chain communication is lost to the CoScale platform. Please use the commands below to debug this issue:

1. Check if the CoScale agent is running: `docker inspect coscale-agent --format="{{.State.Status}}"` should return `running`

2. Check if the host can retrieve data from the CoScale SAAS instances
    * EU: `curl -L -s --head https://app.coscale.com/app/login/ | grep HTTP/` should return `HTTP/1.1 200 OK`
    * US: `curl -L -s --head https://use.coscale.com/app/login/ | grep HTTP/` should return `HTTP/1.1 200 OK`

3. Check if the containers can retrieve data from the CoScale SAAS instances
    * EU: `docker run --rm tutum/curl curl -L -s --head https://app.coscale.com/app/login/ | grep HTTP/` should return `HTTP/1.1 200 OK`
    * US: `docker run --rm tutum/curl curl -L -s --head https://use.coscale.com/app/login/ | grep HTTP/` should return `HTTP/1.1 200 OK`

4. Check CoScale agent logs for timeouts: `docker logs --tail 100 coscale-agent`

5. Insufficiant disk space: `df -h`

## Debug information for support

When you're unable to pinpoint the issue with the CoScale, please don't hesitate to contact our support department. To speed up the process please send along the following information:

* Your operating system information: `uname -a`
* CoScale Agent logs: `docker logs coscale-agent > coscale-agent-logs.txt`

