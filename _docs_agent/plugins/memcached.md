---
layout: page
title: Monitoring and collecting data from Memcached
description: Information on the metrics collected by the CoScale Memcached plugin.
---

> Memcached is a free & open source, high-performance, distributed memory object caching system, generic in nature, but intended for use in speeding up dynamic web applications by alleviating database load. Memcached is an in-memory key-value store for small chunks of arbitrary data (strings, objects) from results of database calls, API calls, or page rendering.

More information on: [https://memcached.org/](https://memcached.org/)

## How it works

The Memcached plugin gathers statistics such as the number of connections, the number of gets, etc. using the Memcached interface.

These statistics are gathered in Memcached by default and no additional configuration is required. Just provide the connection details for the Memcached server and the plugin is ready to go.

**The minimal supported version of Memcached is 1.4.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Memcached" %}

## Configuration

### Connection details

The CoScale plugin requires the host and port to the local Memcached service. It is possible to supply multiple hosts and ports if you are running multiple Memcached instances on the same machine.

## Active checks

This plugin can be configured to perform a command on your Memcached. This active monitoring allows us to calculate the uptime of the service and the response time of the command.

A valid Memcached command (eg. get my-test-key) should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/memcached.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
