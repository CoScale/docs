---
layout: page
title: Kafka plugin
description: Information on the metrics collected by the CoScale Kafka plugin.
---

> Kafka is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.

More information on: [http://kafka.apache.org/](http://kafka.apache.org/)

## Events

* Service state

## Metrics

| Metric name                                               | Metric unit |
|-----------------------------------------------------------|-------------|
| Aggregate incoming byte rate                              | b/s         |
| Aggregate incoming byte rate for topic %s                 | b/s         |
| Aggregate outgoing byte rate                              | b/s         |
| Aggregate outgoing byte rate for topic %s                 | b/s         |
| Leader election rate and latency                          | s           |
| Mean max lag for consumer %s                              | msg         |
| Number of active controllers in cluster                   |             |
| Number of messages received per topic %s                  | msg/s       |
| Number of offline partitions                              |             |
| Number of unclean elections per second                    | elections/s |
| Number of unreplicated partitions                         |             |
| Rate at which the pool of in-sync replicas (ISRs) expands | expands/s   |
| Rate at which the pool of in-sync replicas (ISRs) shrinks | shrinks/s   |
| Request queue size                                        |             |
| Total number of messages received                         | msg/s       |
| Total offset commit time                                  | s           |
| Total offset fetch time                                   | s           |
| Total offsets time                                        | s           |
| Total time to serve the FetchConsumer request             | s           |
| Total time to serve the FetchFollower request             | s           |
| Total time to serve the Produce request                   | s           |
