---
layout: page
title: Hana plugin
description: Information on the metrics collected by the CoScale Hana plugin.
---

>  SAP HANA is an in-memory, column-oriented, relational database management system developed and marketed by SAP SE. Its primary function as database server is to store and retrieve data as requested by the applications. In addition, it performs advanced analytics (predictive analytics, spatial data processing, text analytics, text search, streaming analytics, graph data processing) and includes ETL capabilities as well as an application server.

More information on: [https://www.sap.com/products/hana.html](https://www.sap.com/products/hana.html)

## How it works

The plugin gathers statistics for Hana DB.

## Installation

{% include_relative _installation.md orchestrator="false" service="Hana" %}

## Configuration

### Connection

Provide the Hana DB connection details: hostname, port, username and password.

### Filesystem

The plugin gathers statistics about the percentage used, free and size of the filesystem. The system paths you want to use need to be added.

### Active checks

This plugin can be configured to perform a SQL query on your Hana DB. This active monitoring allows us to calculate the uptime of the service and the response time of the query.
A valid SQL query (eg. `select count(*) from my_table;`) should be provided.

## Events

* Service state

## Metrics

| Metric name                        | Metric unit |
|------------------------------------|-------------|
| Hana DB CPU Usage                  | s           |
| Hana DB system alert               | #           |
| Hana DB system alert count         | #           |
| Hana DB version                    | #           |
| Hana DB process status             | %           |
| Hana DB active check uptime        | %           |
| Hana DB filesystem size            | b           |
| Hana DB filesystem used            | b           |
| Hana DB filesystem available       | b           |
| Hana DB filesystem percentage used | b           |
| Hana DB host memory                | b           |
| Hana DB active check latency       | s           |
