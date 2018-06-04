---
layout: page
title: Monitoring and collecting data from CouchDB
description: Information on the metrics collected by the CoScale CouchDB plugin.
---

> Apache CouchDB is open source database software that focuses on ease of use and having an architecture that "completely embraces the Web". It has a document-oriented NoSQL database architecture and is implemented in the concurrency-oriented language Erlang; it uses JSON to store data, JavaScript as its query language using MapReduce, and HTTP for an API.

More information on: [http://couchdb.apache.org/](http://couchdb.apache.org/)

## How it works

CouchDB CoScale plugin lets you inspect how CouchDB performs. The plugin collects metrics like requests per second, request sizes, http requests methods, CouchDB database reads/writes and a multitude of other useful metrics. This plugins uses the CouchDB API, which is exposed by default and no additional configuration is required.

**The minimal supported version of CouchDB is 1.5**

## Installation

{% include_relative _installation.md orchestrator="false" service="CouchDB" %}

## Configuration

### Active checks

This plugin can be configured to query a view on your CouchDb. This active monitoring allows us to calculate the uptime of the service and the response time of the query.

A database, username, password, design id and view id should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/couchdb.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
