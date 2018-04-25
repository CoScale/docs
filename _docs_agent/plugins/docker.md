---
layout: page
title: Docker plugin
description: Information on how to install the docker plugin and configure your container monitoring
---

> Docker is the world’s leading software containerization platform. Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications, whether on laptops, data center VMs, or the cloud. Docker containers wrap a piece of software in a complete filesystem that contains everything needed to run: code, runtime, system tools, system libraries – anything that can be installed on a server. This guarantees that the software will always run the same, regardless of its environment.

More information on: [https://www.docker.com/](https://www.docker.com/)

## How it works
The CoScale agent detects running containers on your system and starts gathering resources without any configuration. To have a more in-depth view on the process within the container you need to active the CoScale incontainer monitoring system.

The in-container system uses CoScale plugins to gather data from the process running in the container. You can find a full [list of our plugins on the Agent page](/agent/index/#plugins). CoScale requires some configuration to be able to detect which containers to monitor. You can find more information in the [configuration section](#configuration)

The plugin will be started within the namespace of the running container, this has the advantage that you do not have to expose any ports or mount the filesystem for the CoScale in-container monitoring to be able to do its job.

## Installation

{% include_relative _installation.md orchestrator="false" %}

## Events

* Events reported by Docker
    * Container created
    * Container started
    * Container stopped
    * Container died
    * Container destroyed
    * Container killed
    * Container attach
* Events generated when 'docker exec' is called
    * Creating a plugin inside a container
    * Starting a plugin inside a container
    * Command was ran inside a container
* Docker service state watcher

## Metrics

| Metric name                                                                                               | Metric unit |
|-----------------------------------------------------------------------------------------------------------|-------------|
| Docker container total cpu usage                                                                          | %           |
| Docker container block IO read rate                                                                       | b/s         |
| Docker container block IO write rate                                                                      | b/s         |
| Docker container free memory bytes                                                                        | b           |
| Docker container free memory percentage                                                                   | %           |
| Docker container kernel mode cpu usage                                                                    | %           |
| Docker container memory limit                                                                             | b           |
| Docker container memory usage bytes                                                                       | b           |
| Docker container memory usage percentage                                                                  | %           |
| Docker container network receive errors total                                                             | #           |
| Docker container network receive packets dropped total                                                    | #           |
| Docker container network receive rate                                                                     | b/s         |
| Docker container network transmit errors total                                                            | #           |
| Docker container network transmit packets dropped total                                                   | #           |
| Docker container network transmit rate                                                                    | b/s         |
| Docker container number of CLOSE_WAIT connections                                                         | #           |
| Docker container number of CLOSING connections                                                            | #           |
| Docker container number of ESTABLISHED connections                                                        | #           |
| Docker container number of FIN_WAIT1 connections                                                          | #           |
| Docker container number of FIN_WAIT2 connections                                                          | #           |
| Docker container number of LAST_ACK connections                                                           | #           |
| Docker container number of LISTEN connections                                                             | #           |
| Docker container number of SYN_RECV connections                                                           | #           |
| Docker container number of SYN_SENT connections                                                           | #           |
| Docker container number of TIME_WAIT connections                                                          | #           |
| Docker container pgfault memory failures total                                                            | #           |
| Docker container pgmajfault memory failures total                                                         | #           |
| Docker container shm memory free bytes                                                                    | b           |
| Docker container shm memory free percent                                                                  | %           |
| Docker container shm memory limit                                                                         | b           |
| Docker container shm memory used bytes                                                                    | b           |
| Docker container user mode cpu usage                                                                      | %           |
| Docker running                                                                                            | %           |
| Number of bytes of page cache memory                                                                      | b           |
| The amount of anonymous and swap cache memory(includes transparent hugepages)                             | b           |
| The amount of swap currently used                                                                         | b           |
| The amount of working set memory, this includes recently accessed memory, dirty memory, and kernel memory | b           |
