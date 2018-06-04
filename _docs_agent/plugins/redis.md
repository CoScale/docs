---
layout: page
title: Monitoring and collecting data from Redis
description: Information on the metrics collected by the CoScale Redis plugin.
---

> Redis is an open source (BSD licensed), in-memory data structure store, used as database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries.

More information on: [http://redis.io/](http://redis.io/)

## How it works

Redis provides statistics on memory usage, client connections, AOF file operations, etc through the Redis interface.

These statistics are gathered by default and no additional configuration is required. Just provide the connection details and the plugin is ready to go.

**The minimal supported version of Redis is 2.6.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Redis" %}

## Configuration

### Connection

The CoScale plugin requires the host, port, username and password to connect to the local Redis service. It is possible to supply multiple if you are running multiple Redis instances on the same machine.

### Active checks

This plugin can be configured to perform a command on your Redis. This active monitoring allows us to calculate the uptime of the service and the response time of the command.

A valid Redis command (eg. GET my-test-key) should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/redis.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
