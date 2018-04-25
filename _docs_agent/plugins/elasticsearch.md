---
layout: page
title: Elasticsearch plugin
description: Information on the metrics collected by the CoScale ElasticSearch plugin.
---

> Search & Analyze Data in Real Time. Distributed, scalable, and highly available. Real-time search and analytics capabilities. Sophisticated RESTful API.

More information on: [https://www.elastic.co/products/elasticsearch](https://www.elastic.co/products/elasticsearch)

## How it works

The plugin connects to the ElasticSearch server and uses the node stats call to fetch statistics about the server.

These statistics include information about the processes, threads, network and JVM. These statistics are gathered by default and no additional configuration is required. Just provide the connection details and the plugin is ready to go.

**The minimal supported version of ElasticSearch is 0.90.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Elasticsearch" %}

## Configuration

### Active checks

This plugin can be configured to execute a URI query on your ElasticSearch. This active monitoring allows us to calculate the uptime of the service and the response time of the query.

A valid URI query (eg. `http://localhost:9200/twitter/tweet/_search?q=user:kimchy`) should be provided.

## Events

* Service state

## Metrics

| Metric name                                                                                          | Metric unit |
|------------------------------------------------------------------------------------------------------|-------------|
| ElasticSearch transport tx size                                                                      | b           |
| Current number of ElasticSearch search queries                                                       |             |
| ElasticSearch %s collection count                                                                    |             |
| ElasticSearch %s collection time                                                                     | s           |
| ElasticSearch %s count                                                                               |             |
| ElasticSearch %s current                                                                             |             |
| ElasticSearch %s estimated size                                                                      | b           |
| ElasticSearch %s evictions                                                                           |             |
| ElasticSearch %s free                                                                                | b           |
| ElasticSearch %s limit size                                                                          | b           |
| ElasticSearch %s memory size                                                                         | b           |
| ElasticSearch %s overhead                                                                            |             |
| ElasticSearch %s query cache miss count                                                              |             |
| ElasticSearch %s querycache hit count                                                                |             |
| ElasticSearch %s size                                                                                | b           |
| ElasticSearch %s throttle time                                                                       | s           |
| ElasticSearch %s time                                                                                | s           |
| ElasticSearch %s timestamp                                                                           |             |
| ElasticSearch %s total                                                                               | b           |
| ElasticSearch %s total capacity                                                                      | b           |
| ElasticSearch %s total time                                                                          | s           |
| ElasticSearch %s tripped                                                                             |             |
| ElasticSearch %s uptime                                                                              | s           |
| ElasticSearch %s used                                                                                | b           |
| ElasticSearch active primary shards                                                                  |             |
| ElasticSearch active shards                                                                          |             |
| ElasticSearch actual free memory                                                                     | b           |
| ElasticSearch available file system space of all disks                                               | b           |
| ElasticSearch cached memory                                                                          | b           |
| ElasticSearch CPU idle                                                                               |             |
| ElasticSearch CPU stolen                                                                             |             |
| ElasticSearch CPU sys                                                                                |             |
| ElasticSearch CPU sys time                                                                           | s           |
| ElasticSearch CPU usage                                                                              |             |
| ElasticSearch CPU user                                                                               |             |
| ElasticSearch free memory percent                                                                    | %           |
| ElasticSearch fs total disk write size                                                               | b           |
| ElasticSearch http current_open                                                                      |             |
| ElasticSearch http total_opened                                                                      |             |
| ElasticSearch index time                                                                             | s           |
| ElasticSearch indexing Delete current number                                                         |             |
| ElasticSearch indices indexing index current                                                         |             |
| ElasticSearch indices indexing noop update total                                                     |             |
| ElasticSearch indices merges current docs                                                            |             |
| ElasticSearch indices merges current size                                                            | b           |
| ElasticSearch indices merges total size                                                              | b           |
| ElasticSearch indices percolate queries                                                              |             |
| ElasticSearch indices search fetch time                                                              | s           |
| ElasticSearch indices search fetch total                                                             |             |
| ElasticSearch indices search open contexts                                                           |             |
| ElasticSearch indices search queries time                                                            | s           |
| ElasticSearch indices segments fixed bit set memory                                                  | b           |
| ElasticSearch indices segments index writer max memory                                               | b           |
| ElasticSearch indices segments index writer memory                                                   | b           |
| ElasticSearch indices segments memory                                                                | b           |
| ElasticSearch indices segments version map memory                                                    | b           |
| ElasticSearch indices translog operations                                                            |             |
| ElasticSearch initializing shards                                                                    |             |
| ElasticSearch jvm heap max memory                                                                    | b           |
| ElasticSearch jvm heap memory committed                                                              | b           |
| ElasticSearch jvm heap memory used                                                                   | b           |
| ElasticSearch jvm heap memory used percent                                                           | %           |
| ElasticSearch jvm mem non heap committed                                                             | b           |
| ElasticSearch jvm peak number of threads                                                             |             |
| ElasticSearch jvm used non heap memory                                                               | b           |
| ElasticSearch Network tcp attempt fails                                                              |             |
| ElasticSearch network tcp curr_estab                                                                 |             |
| ElasticSearch network tcp out_rsts                                                                   |             |
| ElasticSearch network tcp passive_opens                                                              |             |
| ElasticSearch number of data nodes                                                                   |             |
| ElasticSearch number of delete requests                                                              | req/s       |
| ElasticSearch number of deleted documents                                                            |             |
| ElasticSearch number of get requests                                                                 | req/s       |
| ElasticSearch number of index requests                                                               | req/s       |
| ElasticSearch number of nodes                                                                        |             |
| ElasticSearch OS memory actual used                                                                  | b           |
| ElasticSearch process CPU percent                                                                    | %           |
| ElasticSearch process CPU total time                                                                 | s           |
| ElasticSearch process CPU user                                                                       | s           |
| ElasticSearch process memory resident                                                                | b           |
| ElasticSearch process memory share                                                                   | b           |
| ElasticSearch process open file descriptors                                                          |             |
| ElasticSearch process total virtual memory                                                           | b           |
| ElasticSearch relocating shards                                                                      |             |
| ElasticSearch requests                                                                               | req/s       |
| ElasticSearch Search - Fetch current                                                                 |             |
| ElasticSearch total  gets number for missing indexes                                                 |             |
| ElasticSearch total capacity buffered memory                                                         | b           |
| ElasticSearch total disk IO operation size                                                           | b           |
| ElasticSearch total disk read size                                                                   | b           |
| ElasticSearch total disk reads                                                                       |             |
| ElasticSearch total disk writes                                                                      |             |
| ElasticSearch total gets time for missing indexes                                                    | s           |
| ElasticSearch transport - server open                                                                |             |
| ElasticSearch transport rx_count                                                                     |             |
| ElasticSearch transport rx_size                                                                      | b           |
| ElasticSearch transport tx_count                                                                     |             |
| ElasticSearch unassigned shards                                                                      |             |
| ElasticSearch used buffered memory                                                                   | b           |
| ElasticSearch used memory percent                                                                    | %           |
| fs total ElasticSearch disk IO op                                                                    |             |
| Indexing deletion time                                                                               | s           |
| Indices merges total ElasticSearch docs                                                              |             |
| Indices search ElasticSearch queries total number                                                    | queries/s   |
| Network tcp in ElasticSearch errs                                                                    |             |
| Number of times ElasticSearch TCP connections have made a transition to CLOSE state from ESTABLISHED |             |
| TCP network ElasticSearch active_opens number                                                        |             |
| TCP network ElasticSearch in_segs                                                                    |             |
| TCP network ElasticSearch out_segs                                                                   |             |
| TCP network ElasticSearch segment retransmission number                                              |             |
| Total number of gets on existent indices                                                             |             |
| Total time for gets on existent indices                                                              | s           |
