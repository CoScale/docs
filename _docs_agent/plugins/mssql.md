---
layout: page
title: Monitoring and collecting data from MSSQL - Microsoft SQL Server
description: Information on the metrics collected by the CoScale MSSQL plugin.
---

>  Microsoft SQL Server is a relational database management system developed by Microsoft. As a database server, it is a software product with the primary function of storing and retrieving data as requested by other software applications—which may run either on the same computer or on another computer across a network (including the Internet). Microsoft markets at least a dozen different editions of Microsoft SQL Server, aimed at different audiences and for workloads ranging from small single-machine applications to large Internet-facing applications with many concurrent users.

More information on: [https://www.microsoft.com/en-us/sql-server/](https://www.microsoft.com/en-us/sql-server/)

## How it works

The plugin gathers global stats using the performance counter client. The MSSQL performance schema is used to retrieved query stats such as queries per second, latencies and errors.

**The minimal supported version of MSSQL is 2008 R2.**

## Installation

{% include_relative _installation.md orchestrator="false" service="MSSQL" %}

## Configuration

### Database connection

The authentication to the database can be done using integrated security (SSPI) or username/password.

When using integrated security (SSPI), the plugin connects to MSSQL using the credentials from the Windows/Domain user configured to run the Windows Service. In MSSQL Server, ensure a login is configured for this Windows/Domain user.

If you want to use a Login authentification type, deselect integrated security and then set a username (with the right credentials) and a password.

### Active checks

This plugin can be configured to perform a SQL query on your MSSQL. This active monitoring allows us to calculate the uptime of the service and the response time of the query.

A valid SQL query (eg. `select count(*) from my_table;`) should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/mssql.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
