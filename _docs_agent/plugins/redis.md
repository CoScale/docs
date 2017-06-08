---
layout: page
title: Redis plugin
description: Information on the metrics collected by the CoScale Redis plugin.
---

> Redis is an open source (BSD licensed), in-memory data structure store, used as database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries.

More information on: [http://redis.io/](http://redis.io/)

## How it works

Redis provides statistics on memory usage, client connections, AOF file operations, etc through the Redis interface.

These statistics are gathered by default and no additional configuration is required. Just provide the connection details and the plugin is ready to go.

**The minimal supported version of Redis is 2.6.**

## Configuration

### Connection

The CoScale plugin requires the host, port, username and password to connect to the local Redis service. It is possible to supply multiple if you are running multiple Redis instances on the same machine.

### Active checks

This plugin can be configured to perform a command on your Redis. This active monitoring allows us to calculate the uptime of the service and the response time of the command.

A valid Redis command (eg. GET my-test-key) should be provided.

## Events

* Service state

## Metrics

| Metric name                                                                                       | Metric unit |
|---------------------------------------------------------------------------------------------------|-------------|
| Number of seconds since Redis server start                                                        | s           |
| AOF current file size                                                                             | b           |
| AOF file size on latest startup or rewrite                                                        | b           |
| Biggest input buffer among current client connections to Redis                                    | b           |
| Delayed fsync counter                                                                             | #           |
| Duration of the last AOF rewrite operation in seconds                                             | s           |
| Duration of the last RDB save operation in seconds                                                | s           |
| Duration of the latest fork operation                                                             | s           |
| Duration of the on-going AOF rewrite operation if any                                             | s           |
| Duration of the on-going RDB save operation if any                                                | s           |
| Epoch-based timestamp of last successful RDB save                                                 |             |
| Epoch-based timestamp of the start of the load operation                                          |             |
| ETA in seconds for the load to be complete                                                        | s           |
| Flag indicating a AOF rewrite operation is on-going                                               |             |
| Flag indicating a Redis RDB save is on-going                                                      |             |
| Flag indicating an AOF rewrite operation will be scheduled once the on-going RDB save is complete |             |
| Flag indicating an AOF rewrite operation will be scheduled once the on-going RDB save is complete |             |
| Flag indicating AOF logging is activated                                                          |             |
| Flag indicating if the load of a dump file is on-going                                            | b           |
| Global number of pub/sub Redis channels with client subscriptions                                 | #           |
| Global number of pub/sub Redis pattern with client subscriptions                                  | #           |
| Indicate Redis cluster is enabled                                                                 |             |
| Longest output list among current Redis client connections                                        |             |
| Number of bytes already loaded                                                                    | b           |
| Number of bytes that Redis allocated as seen by the operating system                              | b           |
| Number of bytes used by the Lua engine                                                            | b           |
| Number of changes since the last Redis dump                                                       | #           |
| Number of commands processed per second by the Redis server                                       | #/s         |
| Number of connected slaves to Redis                                                               | #           |
| Number of connections to Redis rejected because of maxclients limit                               | conn        |
| Number of evicted keys due to maxmemory limit                                                     | #           |
| Number of failed lookup of keys in the main dictionary                                            | misses/s    |
| Number of fsync pending jobs in background I/O queue                                              | b           |
| Number of Redis client connections                                                                | conn        |
| Number of Redis clients pending on a blocking call                                                | #           |
| Number of successful lookup of keys in the main dictionary                                        | hits/s      |
| Peak memory consumed by Redis                                                                     | b           |
| Ratio between used_memory_rss and used_memory                                                     | b           |
| Redis %s keys average time to live                                                                | s           |
| Redis %s number of keys                                                                           | #           |
| Redis %s number of keys with an expiration                                                        | #           |
| Redis master last io (seconds ago)                                                                | s           |
| Redis master sync in progress                                                                     |             |
| Redis replication backlog active                                                                  |             |
| Redis replication backlog first byte offset                                                       |             |
| Redis replication backlog histlen                                                                 | b           |
| Redis replication backlog size                                                                    | b           |
| Redis replication offset reported by the master                                                   |             |
| Redis slave replication offset                                                                    |             |
| Size of the AOF buffer                                                                            | b           |
| Size of the AOF rewrite buffer                                                                    | b           |
| System CPU consumed by the background processes                                                   | s           |
| System CPU consumed by the Redis server                                                           | s           |
| Total file size                                                                                   | b           |
| Total number of bytes allocated by Redis using its allocator                                      | b           |
| Total number of commands processed by the Redis server                                            | #           |
| Total number of connections accepted by the Redis server                                          | conn        |
| Total number of Redis key expiration events                                                       | #           |
| User CPU consumed by the background processes                                                     | s           |
| User CPU consumed by the Redis server                                                             | s           |
