---
layout: page
title: Monitoring and collecting data from Elasticsearch
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


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/elasticsearch.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
