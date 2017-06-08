---
layout: page
title: Uninstalling and stopping the CoScale agent
description: Terminating and uninstalling the CoScale agent.
---

## Container

## Terminate / stop

* Docker: `docker stop coscale-agent`
* Docker Swarm / Docker Datacenter: `docker service rm coscale-agent`
* Kubernetes: `kubectl delete ds coscale-agent`
* Azure Container Service: `kubectl delete ds coscale-agent`
* OpenShift: 
    
    `kubectl delete ds coscale-agent`
    
    `oc delete serviceaccount coscale`
    
    `kubectl delete SecurityContextConstraints coscale-scc`
    
    `oc delete project coscale`

* Google Container Engine

    `kubectl delete ds coscale-agent`

    `kubectl delete ds coscale-agent-kubernetes-master`

* IBM Bluemix

    `kubectl delete ds coscale-agent`

    `kubectl delete ds coscale-agent-kubernetes-master`
    

## Unix

### Terminate / stop
* Ubuntu / Debian: `sudo service coscale-agent stop`
* CentOS 6.6: `sudo systemctl stop coscale-agent.service`
* CentOS 5.3: `sudo initctl stop coscale-agent`

### Uninstall

* Ubuntu / Debian: `sudo apt-get remove --purge coscale-agent`
* CentOS: `sudo rpm -e coscale-agent-1.0-1.x86_64`

## Microsoft Windows

### Terminate / stop
Follow these steps to terminate / kill the CoScale agent.

1. Open Task Manager

2. Open the tab 'Processes' (You might have to click on 'More details' first to see the different tabs)

3. Kill the following processes

    * Agent GO container: agent.exe
    * IIS plugin: plugin.exe
    * MS SQL Server plugin: sql
    * Resource plugin: ResourceMonitoring


### Uninstall

Go to `Control Panel`, `Programs` > `Uninstall a program`, right-click 'CoScale Agent' and select `Uninstall`.
