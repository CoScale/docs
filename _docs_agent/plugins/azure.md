---
layout: page
title: Monitoring and collecting data from Azure
description: Information on the metrics collected by the CoScale Azureh plugin.
---

> Microsoft Azure is a growing collection of integrated cloud services that developers and IT professionals use to build, deploy, and manage applications through our global network of datacenters. With Azure, you get the freedom to build and deploy wherever you want, using the tools, applications, and frameworks of your choice. Azure supports a broad selection of operating systems, programming languages, frameworks, databases, and devices.

More information on: [https://azure.microsoft.com](https://azure.microsoft.com)

## Installation

{% include_relative _thirdparty.md %}

## Metrics

### Counters

| Metric name                | Metric unit |
|----------------------------|-------------|
| Azure number of Databases  | #           |
| Azure number of VMs        | #           |
| Azure number of WebApps    | #           |
| Azure number of DocumentDB | #           |

### Databases

| Metric name                                      | Metric unit |
|--------------------------------------------------|-------------|
| Database CPU percentage                          | %           |
| Database data IO percentage                      | %           |
| Database log IO percentage                       | %           |
| Database DTU percentage                          | %           |
| Database total database size                     | b           |
| Database Successful Connections                  | #           |
| Database Failed Connections                      | #           |
| Database Blocked by Firewall                     | #           |
| Database Deadlocks                               | #           |
| Database size percentage                         | %           |
| Database In-Memory OLTP storage percent(Preview) | %           |
| Database workers percentage                      | %           |
| Database sessions percent                        | %           |
| Database DTU limit                               | #           |
| Database DTU used                                | #           |
| Database service level objective of the database | #           |
| Database DWU limit                               | #           |
| Database DWU percentage                          | %           |
| Database DWU used                                | #           |

### Elastic Pools

| Metric name                      | Metric unit |
|----------------------------------|-------------|
| Elastic pools CPU percentage     | %           |
| Elastic pools data IO percentage | %           |
| Elastic pools log IO percentage  | %           |
| Elastic pools DTU percentage     | %           |
| Elastic pools storage percentage | %           |
| Elastic pools workers percent    | %           |
| Elastic pools sessions percent   | %           |
| Elastic pools eDTU limit         | #           |
| Elastic pools storage limit      | b           |
| Elastic pools eDTU used          | #           |
| Elastic pools storage used       | b           |

### Document DB

| Metric name            | Metric unit |
|------------------------|-------------|
| Total Requests         | #           |
| Http 2xx               | #           |
| Http 3xx               | #           |
| Http 400               | #           |
| Http 401               | #           |
| Throttled Requests     | #           |
| Internal Server Error  | #           |
| Service Unavailable    | #           |
| req/s                  | #/s         |
| Data Size              | b           |
| Index Size             | b           |
| Storage Capacity       | b           |
| Available Storage      | b           |
| Total Request Units    | #           |
| Consistency Level      | %           |
| Observed Read Latency  | s           |
| Observed Write Latency | s           |
| Service Availability   | %           |

### Web Applications

| Metric name                                | Metric unit |
|--------------------------------------------|-------------|
| Web Application CPU Time                   | s           |
| Web Application Requests                   | #           |
| Web Application Data In                    | b           |
| Web Application Data Out                   | b           |
| Web Application Http 101                   | #           |
| Web Application Http 2xx                   | #           |
| Web Application Http 3xx                   | #           |
| Web Application Http 401                   | #           |
| Web Application Http 403                   | #           |
| Web Application Http 404                   | #           |
| Web Application Http 406                   | #           |
| Web Application Http 4xx                   | #           |
| Web Application Http 5xx                   | #           |
| Web Application memory working set         | b           |
| Web Application average memory working set | b           |
| Web Application average Response Time      | s           |

### Virtual Machines (Basic)

| Metric name               | Metric unit |
|---------------------------|-------------|
| Percentage CPU            | %           |
| Network In                | b           |
| Network Out               | b           |
| Disk Read Bytes           | b/sec       |
| Disk Write Bytes          | b/sec       |
| Disk Read Operations/Sec  | #/s         |
| Disk Write Operations/Sec | #/s         |

### Virtual Machines (Diagnostic extension)

| Metric name              | Metric unit |
|--------------------------|-------------|
| Swap available           | b           |
| Pages                    | #/s         |
| Page reads               | #/s         |
| Page writes              | #/s         |
| Memory percent available | %           |
| Swap percent available   | %           |
| Memory used by cache     | %           |
| Memory percentage        | %           |
| Swap percent used        | %           |
| Memory used              | b           |
| Swap used                | b           |
| Network in guest OS      | b           |
| Network total bytes      | b           |
| Network out guest OS     | b           |
| Packets received         | #           |
| Packets sent             | #           |
| Network collisions       | #           |
| Packets received errors  | #           |
| Packets sent errors      | #           |
| Disk queue length        | #           |
| Disk read time           | s           |
| Disk transfer time       | s           |
| Disk write time          | s           |
| Disk total bytes         | b/s         |
| Disk read guest OS       | b/s         |
| Disk reads               | #/s         |
| Disk transfers           | #/s         |
| Disk write guest OS      | b/s         |
| Disk writes              | #/s         |
| CPU DPC time             | %           |
| CPU IO wait time         | %           |
| CPU idle time            | %           |
| CPU interrupt time       | %           |
| CPU nice time            | %           |
| CPU privileged time      | %           |
| CPU percentage guest OS  | %           |
| CPU user time            | %           |
