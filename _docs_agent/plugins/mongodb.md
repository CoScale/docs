---
layout: page
title: Monitoring and collecting data from MongoDB
description: Information on the metrics collected by the CoScale MongoDB plugin.
---

> MongoDB is an open-source, document database designed for ease of development and scaling. MongoDB stores data using a flexible document data model that is similar to JSON. Documents contain one or more fields, including arrays, binary data and sub-documents. Fields can vary from document to document. This flexibility allows development teams to evolve the data model rapidly as their application requirements change. When you need to lock down your data model, optional document validation enforces the rules you choose. Unlike most NoSQL databases, MongoDB provides comprehensive secondary indexes, including geospatial and text search, as well as extensive security and aggregation capabilities.

More information on: [https://www.mongodb.com/](https://www.mongodb.com/)

## How it works

MongoDB provides statistics on lock timeouts, lock counts, insert/update/remove actions, total index size, etc through the MongoDB interface.

These statistics are gathered by default and no additional configuration is required. Just provide the connection details and the plugin is ready to go.

**The minimal supported version of MongoDB is 2.2.**

## Installation

{% include_relative _installation.md orchestrator="false" service="MongoDB" %}

## Configuration

### Connection details

Our plugin requires the host, port, username and password to connect to the local MongoDB service.

### Active checks

This plugin can be configured to perform a command on your MongoDB. This active monitoring allows us to calculate the uptime of the service and the response time of the command.

A valid MongoDB command (eg. `{ "find": "my-collection", "filter": "my-document" }`) should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/mongodb.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
