---
layout: page
title: Couchbase plugin
description: Information on the metrics collected by the CoScale Couchbase plugin.
---

> Couchbase Server is an open source, distributed, NoSQL document-oriented database. It exposes a fast key-value store with managed cache for submillisecond data operations, purpose-built indexers for fast queries and a query engine for executing SQL-like queries. For mobile and Internet of Things environments Couchbase Lite runs natively on-device and manages synchronization to Couchbase Server. Couchbase Server is specialized to provide low-latency data management for large-scale interactive web, mobile, and IoT applications. 

More information on: [https://www.couchbase.com/](https://www.couchbase.com/)

## How it works

The Couchbase plugin gathers statistics such as the number of operations, connections, items and a multitude of other useful metrics. This plugins uses the Couchbase API, which is exposed by default and no additional configuration is required. Just provide the connection details for the Couchbase server and the plugin is ready to go.

**The minimal supported version of Couchbase is 2.5**

## Configuration

### Active checks

This plugin can be configured to execute a URI query on your Couchbase. This active monitoring allows us to calculate the uptime of the service and the response time of the query.

A valid URI query (eg. /pools/default) should be provided.

## Events

* Service state

## Metrics

| Metric name                                                                                | Metric unit                                                  |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Couchbase view fragmentation threshold                                                     | %                                                            |
| Couchbase database fragmentation threshold                                                 | %                                                            |
| Couchbase index fragmentation threshold                                                    | %                                                            |
| Couchbase RAM used by the cluster                                                          | b                                                            |
| Couchbase RAM quota used by the cluster                                                    | b                                                            |
| Couchbase total RAM available to cluster                                                   | b                                                            |
| Couchbase RAM quota total for the cluster                                                  | b                                                            |
| Couchbase RAM used by the data in the cluster                                              | b                                                            |
| Couchbase harddrive quota total for the cluster                                            | b                                                            |
| Couchbase harddrive space used by the cluster                                              | b                                                            |
| Couchbase harddrive use by the data in the cluster                                         | b                                                            |
| Couchbase free harddrive space in the cluster                                              | b                                                            |
| Couchbase total harddrive space available to cluster                                       | b                                                            |
| Couchbase memory used by the node                                                          | b                                                            |
| Couchbase number of items/documents that are replicas                                      | #                                                            |
| Couchbase number of get hits                                                               | #                                                            |
| Couchbase number of operations performed                                                   | #                                                            |
| Couchbase size of object data for Couch views                                              | b                                                            |
| Couchbase couch spatial data size                                                          | b                                                            |
| Couchbase couch spatial disk size                                                          | b                                                            |
| Couchbase number of disk fetches performed since server was started                        | #                                                            |
| Couchbase data size of couch documents associated with a node                              | b                                                            |
| Couchbase total number of items associated with node                                       | #                                                            |
| Couchbase amount of disk space occupied by Couch views                                     | b                                                            |
| Couchbase number of current items                                                          | #                                                            |
| Couchbase amount of disk space used by Couch docs                                          | b                                                            |
| Couchbase amount of swap space used                                                        | b                                                            |
| Couchbase total memory available to the node                                               | b                                                            |
| Couchbase free memory available to the node                                                | b                                                            |
| Couchbase number of get commands                                                           | #                                                            |
| Couchbase total swap size allocated                                                        | b                                                            |
| Couchbase the CPU utilization rate                                                         | %                                                            |
| Couchbase amount of memcached memory reserved                                              | b                                                            |
| Couchbase max bucket count                                                                 | #                                                            |
| Couchbase amount of memcached memory allocated                                             | #                                                            |
| Couchbase cluster compatibility                                                            |                                                              |
| Couchbase amount of memory used by the bucket                                              | b                                                            |
| Couchbase amount of disk used                                                              | b                                                            |
| Couchbase number of disk fetches                                                           | #                                                            |
| Couchbase number of items associated with the bucket                                       | #                                                            |
| Couchbase size of user data within buckets of the specified state that are resident in RAM | %                                                            |
| Couchbase number of operations per second                                                  | #                                                            |
| Couchbase percentage of RAM used (for active objects) against the configure bucket size    | %                                                            |
| Couchbase amount of raw RAM used by the bucket                                             | b                                                            |
| Couchbase amount of RAM used by the bucket                                                 | b                                                            |
| Couchbase bytes read                                                                       | b                                                            |
| Couchbase bytes written                                                                    | b                                                            |
| Couchbase check and set hits                                                               | #                                                            |
| Couchbase check and set misses                                                             | #                                                            |
| Couchbase get commands                                                                     | #                                                            |
| Couchbase set commands                                                                     | #                                                            |
| Couchbase current connections                                                              | conn                                                         |
| Couchbase current items                                                                    | items                                                        |
| Couchbase current items total                                                              | items                                                        |
| Couchbase decrement hits                                                                   | hits                                                         |
| Couchbase decrement misses                                                                 | misses                                                       |
| Couchbase delete hits                                                                      | hits                                                         |
| Couchbase delete misses                                                                    | misses                                                       |
| Couchbase number of disk fetches performed since server was started for a bucket           | #                                                            |
| Couchbase ep_cache_miss_rate                                                               |                                                              |
| Couchbase ep_diskqueue_drain                                                               |                                                              |
| Couchbase ep_diskqueue_fill                                                                |                                                              |
| Couchbase ep_flusher_todo                                                                  |                                                              |
| Couchbase ep_item_commit_failed                                                            |                                                              |
| Couchbase max amount of data allowed in memory                                             | b                                                            |
| Couchbase high water mark for auto-evictions                                               |                                                              |
| Couchbase low water mark for auto-evictions                                                |                                                              |
| Couchbase ep_num_non_resident                                                              |                                                              |
| Couchbase ep_num_value_ejects                                                              |                                                              |
| Couchbase number of times unrecoverable OOMs                                               | #                                                            |
| Couchbase extra memory used by transient data                                              | b                                                            |
| Couchbase ep_queue_size                                                                    |                                                              |
| Couchbase number of times temporary OOMs                                                   | #                                                            |
| Couchbase total memory used by meta data                                                   | b                                                            |
| Couchbase get hits                                                                         | hits                                                         |
| Couchbase get misses                                                                       | misses                                                       |
| Couchbase increment hits                                                                   | hits                                                         |
| Couchbase increment misses                                                                 | misses                                                       |
| Couchbase free memory                                                                      | b                                                            |
| Couchbase total memory                                                                     | b                                                            |
| Couchbase memory used                                                                      | b                                                            |
| Couchbase total drained items                                                              | #                                                            |
| Couchbase active items in disk queue                                                       | #                                                            |
| Couchbase number of create operations                                                      | #                                                            |
| Couchbase total enqueued items                                                             | #                                                            |
| Couchbase total metadata memory.                                                           |                                                              |
| Couchbase current number of buckets                                                        | #                                                            |
| Couchbase number of items/documents that are replicas for a bucket                         | #                                                            |
| Couchbase replica items in disk queue                                                      | #                                                            |
