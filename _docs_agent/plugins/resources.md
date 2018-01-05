---
layout: page
title: Resources plugin
description: Information on the metrics collected by the CoScale Resources plugin.
---

> The Resources plugin gathers information about the server resource usage: CPU, Memory, Network, Disk, Filesystem, OS.

## How it works

The plugin gathers OS and hardware metrics from the underlying system. No configuration is required. Below you can find the metrics list for [Linux](#Linux) and [Windows](#Windows).

## <a id="Linux"></a> Linux Metrics

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


## <a id="Windows"></a> Windows Metrics

### CPU

| Metric name                   | Metric unit |
|-------------------------------|-------------|
| CPU Percent Privileged Time   | %           |
| CPU Percent DPC Time          | %           |
| CPU Percent Interrupt Time    | %           |
| CPU Percent Processor Time    | %           |
| CPU Percent User Time         | %           |
| CPU DPC Rate                  | msg/s       |
| CPU Queued Per Second         | msg/s       |
| CPU Interrupts Per Second     | int/s       |
| Total Percent Privileged Time | %           |
| Total Percent DPC Time        | %           |
| Total Percent Interrupt Time  | %           |
| Total Percent Processor Time  | %           |
| Total Percent User Time       | %           |
| Total DPC Rate                | msg/s       |
| Total DPCs Queued Per Second  | msg/s       |
| Total Interrupts Per Second   | int/s       |
| Number Of Threads             | threads     |

### Filesystem

| Metric name                         | Metric unit |
|-------------------------------------|-------------|
| Volume Percent Read Time            | %           |
| Volume Percent Time                 | %           |
| Volume Percent Write Time           | %           |
| Volume Percent Free Space           | %           |
| Volume Percent Idle Time            | %           |
| Volume Average Queue Length         | b           |
| Volume Average Read Queue Length    | b           |
| Volume Average Write Queue Length   | b           |
| Volume Average Seconds Per Read     | s           |
| Volume Average Seconds Per Transfer | s           |
| Volume Average Seconds Per Write    | s           |
| Volume Current Queue Length         | b           |
| Volume Bytes Per Second             | b/s         |
| Volume Read Bytes Per Second        | b/s         |
| Volume Reads Per Second             | reads/s     |
| Volume Transfers Per Second         | trans/s     |
| Volume Write Bytes Per Second       | b/s         |
| Volume Writes Per Second            | writes/s    |
| Volume Free Bytes                   | b           |
| Volume Split IO Per Second          | splits/s    |
| Total Percent Read Time             | %           |
| Total Percent Time                  | %           |
| Total Percent Write Time            | %           |
| Total Percent Free Space            | %           |
| Total Percent Idle Time             | %           |
| Total Average Queue Length          | %           |
| Total Average Read Queue Length     | b           |
| Total Average Write Queue Length    | b           |
| Total Average Seconds Per Read      | s           |
| Total Average Seconds Per Transfer  | s           |
| Total Average Seconds Per Write     | s           |
| Total Current Queue Length          | b           |
| Total Bytes Per Second              | b/s         |
| Total Read Bytes Per Second         | b/s         |
| Total Reads Per Second              | reads/s     |
| Total Transfers Per Second          | trans/s     |
| Total Write Bytes Per Second        | b/s         |
| Total Writes Per Second             | writes/s    |
| Total Free Bytes                    | b           |
| Total Split IO Per Second           | splits/s    |

### Memory

| Metric name                                      | Metric unit |
|--------------------------------------------------|-------------|
| Available Bytes                                  | b           |
| Committed Bytes                                  | b           |
| The ratio of Committed Bytes to the Commit Limit | %           |
| Cache Bytes                                      | b           |
| Cache Bytes Peak                                 | b           |
| Page Faults Per Second                           | faults/s    |
| Pages Input Per Second                           | pages/s     |
| Pages Output Per Second                          | pages/s     |
| Pages Per Sec                                    | pages/sec   |
| Pool Non Paged Bytes                             | b           |
| Pool Paged Bytes                                 | b           |
| Pool Paged Resident Bytes                        | b           |
| System Cache Resident Bytes                      | b           |
| System Code Resident Bytes                       | b           |
| System Code Total Bytes                          | b           |
| System Driver Resident Bytes                     | b           |
| System Driver Total Bytes                        | b           |
| Page File Usage                                  | %           |
| Total Visible Memory Size                        | b           |
| Free Physical Memory                             | b           |
| Free Physical Memory Percentage                  | %           |
| Used Physical Memory                             | b           |
| Used Physical Memory Percentage                  | %           |
| Total Virtual Memory Size                        | b           |
| Free Virtual Memory                              | b           |
| Free Virtual Memory Percentage                   | %           |
| Used Virtual Memory                              | b           |
| Used Virtual Memory Percentage                   | %           |


### Network

| Metric name                                   | Metric unit |
|-----------------------------------------------|-------------|
| Network Interface Bytes Received Per Second   | b/s         |
| Network Interface Bytes Sent Per Second       | b/s         |
| Network Interface Bytes Total Per Second      | b/s         |
| Network Interface Current Bandwidth           | b           |
| Network Interface Output Queue Length         | b           |
| Network Interface Packets Outbound Discarded  | #           |
| Network Interface Packets Outbound Errors     | errors      |
| Network Interface Packets Received Discarded  | #           |
| Network Interface Packets Received Errors     | errors      |
| Network Interface Packets Received Unknown    | #           |
| Network Interface Packets Received Per Second | pack/s      |
| Network Interface Packets Sent Per Second     | pack/s      |
| Network Interface Packets Per Second          | pack/s      |
| Total Bytes Received Per Second               | b/s         |
| Total Bytes Sent Per Second                   | b/s         |

### Processes

| Metric name         | Metric unit |
|---------------------|-------------|
| Number of processes | procs       |
