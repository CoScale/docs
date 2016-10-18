---
layout: page
title: Resources plugin
description: Information on the metrics collected by the CoScale Resources plugin.
---

> The Resources plugin gathers information about the server resource usage: CPU, Memory, Network, Disk, Filesystem, OS.


## Metrics

### CPU

| Metric name             |Metric unit |
|-------------------------|-------------|
| CPU idle time average   | %           |
| CPU idle time cpuX      | %           |
| CPU idle time total     | %           |
| CPU iowait time average | %           |
| CPU iowait time cpuX    | %           |
| CPU iowait time total   | %           |
| CPU nice time average   | %           |
| CPU nice time cpuX      | %           |
| CPU nice time total     | %           |
| CPU system time average | %           |
| CPU system time cpuX    | %           |
| CPU system time total   | %           |
| CPU user time average   | %           |
| CPU user time cpuX      | %           |
| CPU user time total     | %           |
| Processor load          | %           |
| Total CPU usage         | %           |


### Disk

| Metric name                           |Metric unit |
|---------------------------------------|-------------|
| All disks bytes per second            | b/s         |
| All disks percent disk read time      | %           |
| All disks percent disk time           | %           |
| All disks percent disk write time     | %           |
| All disks percent idle time           | %           |
| All disks read bytes per second       | b/s         |
| All disks reads per second            | %           |
| All disks transfers per second        | trans/s     |
| All disks write bytes per second      | b/s         |
| All disks writes per second           | writes/s    |
| Average disk seconds per read         | s           |
| Average disk seconds per transfer     | s           |
| Average disk seconds per write        | s           |
| Current all disks queue length        | b           |

*Besides the metrics listed above, there will also be metrics of the same type for every disk or device.*
*Example: Disk write bytes per second /dev/docker-vg/root or Disk percent disk write time sda*


### Filesystem

| Metric name                                |Metric unit|
|--------------------------------------------|-----------|
| Free disk space on partition X             | b         |
| Free disk space on partition X in %        | %         |
| Free swap space                            | b         |
| Free swap space in %                       | %         |
| Total disk space on partition X            | b         |
| Total number of inodes on partition X      | #         |
| Total swap space                           | b         |
| Used disk space on partition X             | b         |
| Used number of inodes on partition X       | #         |


### Memory

| Metric name                                |Metric unit|
|--------------------------------------------|-----------|
| % Active memory                            | %         |
| % Buffered memory                          | %         |
| % Cached memory                            | %         |
| % Free memory                              | %         |
| % Free memory (+buffers/cache)             | %         |
| % Shared memory                            | %         |
| Active memory                              | %         |
| Amount of memory swapped in from disk      | %         |
| Amount of memory swapped to disk           | %         |
| Buffered memory                            | %         |
| Cached memory                              | %         |
| Free memory                                | %         |
| Free memory (+buffers/cache)               | %         |
| Shared memory                              | %         |
| Swap space used                            | %         |
| Swap space used in %                       | %         |
| Total memory                               | %         |
| Used memory                                | %         |


### Network

| Metric name                                |Metric unit|
|--------------------------------------------|-----------|
| Incoming traffic on all interfaces         | b/s       |
| Incoming traffic on interface X            | b/s       |
| Outgoing traffic on all interfaces         | b/s       |
| Outgoing traffic on interface X            | b/s       |


### OS

| Metric name                                |Metric unit|
|--------------------------------------------|-----------|
| Host local time                            | s         |
| Host uptime in seconds                     | s         |
| Maximum number of opened files             | files     |
| Maximum number of processes                | procs     |
| Number of processes                        | procs     |
