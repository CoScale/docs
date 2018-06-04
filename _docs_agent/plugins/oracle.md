---
layout: page
title: Monitoring and collecting data from Oracle Database
description: Information on the metrics collected by the CoScale Oracle plugin.
---

>  Oracle Database (commonly referred to as Oracle RDBMS or simply as Oracle) is an object-relational database management system produced and marketed by Oracle Corporation.

More information on: [https://www.oracle.com](https://www.oracle.com)

## How it works

The CoScale Oracle plugin lets you inspect how Oracle performs. The plugin collects metrics like performance statistics, connections, query performance and throughput. This plugins uses the Oracle API.

**The supported versions of Oracle are 11g and 11g.2, please contact support for other versions.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Oracle" %}

## Configuration

### Authentication

In order for CoScale to be able to access the required data these next few queries need to be executed on the server.

{% highlight sql %}
CREATE USER coscale IDENTIFIED BY password;
GRANT CREATE SESSION TO coscale;
GRANT SELECT ANY DICTIONARY TO coscale;
{% endhighlight %}

You can disable gathering query data from your databases but note that the latency and query rate for the databases, tables and queries won't be available when the query stats are disabled.

### Active checks

This plugin can be configured to perform a SQL query on your Oracle database. This active monitoring allows us to calculate the uptime of the service and the response time of the query.

A valid SQL query (eg. `select count(*) from my_table;`) should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/oracle.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
