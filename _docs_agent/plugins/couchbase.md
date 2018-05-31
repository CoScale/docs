---
layout: page
title: Monitoring and collecting data from Couchbase
description: Information on the metrics collected by the CoScale Couchbase plugin.
---

> Couchbase Server is an open source, distributed, NoSQL document-oriented database. It exposes a fast key-value store with managed cache for submillisecond data operations, purpose-built indexers for fast queries and a query engine for executing SQL-like queries. For mobile and Internet of Things environments Couchbase Lite runs natively on-device and manages synchronization to Couchbase Server. Couchbase Server is specialized to provide low-latency data management for large-scale interactive web, mobile, and IoT applications.

More information on: [https://www.couchbase.com/](https://www.couchbase.com/)

## How it works

The Couchbase plugin gathers statistics such as the number of operations, connections, items and a multitude of other useful metrics. This plugins uses the Couchbase API, which is exposed by default and no additional configuration is required. Just provide the connection details for the Couchbase server and the plugin is ready to go.

**The minimal supported version of Couchbase is 2.5**

## Installation

{% include_relative _installation.md orchestrator="false" service="Couchbase" %}

## Configuration

### Active checks

This plugin can be configured to execute a URI query on your Couchbase. This active monitoring allows us to calculate the uptime of the service and the response time of the query.

A valid URI query (eg. /pools/default) should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/couchbase.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
