---
layout: page
title: Monitoring and collecting data from PostgreSQL
description: Information on the metrics collected by the CoScale PostgreSQL plugin.
---

> PostgreSQL is a powerful, open source object-relational database system. It is fully ACID compliant, has full support for foreign keys, joins, views, triggers, and stored procedures (in multiple languages). It includes most SQL:2008 data types, including INTEGER, NUMERIC, BOOLEAN, CHAR, VARCHAR, DATE, INTERVAL, and TIMESTAMP. It also supports storage of binary large objects, including pictures, sounds, or video. It has native programming interfaces for C/C++, Java, .Net, Perl, Python, Ruby, Tcl, ODBC, among others, and exceptional documentation.

More information on: [https://www.postgresql.org/](https://www.postgresql.org/)

## How it works

This plugin analyzes the performance of your PostgreSQL database server.

We gather global statistics (eg. number of connections, open files, ...) by using the `pg_stat_statements` PostgreSQL extension. This extension is not installed by default.

Query statistics such as queries per second, latencies and errors are retrieved from the slow query log. By default, PostgreSQL does not track slow queries, the PostgreSQL configuration has to be changed to enable this.

**The minimal supported version of PostgreSQL is 9.0.**

## Installation

{% include_relative _installation.md orchestrator="false" service="PostgreSQL" %}

## Configuration

### Enable pg_stat_statements

Global stats are not enabled in PostgreSQL by default. Enabled PostgreSQL `pg_stat_statements` using the following steps.

Install the postgresql-contrib package:

{% highlight bash %}
sudo apt-get install postgresql-contrib
{% endhighlight %}

Add the following lines to `/etc/postgresql/<version>/main/postgresql.conf`:

{% highlight ini %}
shared_preload_libraries = 'pg_stat_statements'
pg_stat_statements.max = 1000
pg_stat_statements.track = all
{% endhighlight %}

PostgreSQL must be restarted for this to take effect.

Enable the extension in psql for your database. That means, if you wish to gather statistics about the `mydb` database, connect to "mydb" database and execute:

{% highlight sql %}
CREATE EXTENSION pg_stat_statements;
{% endhighlight %}

### Query performance

The slow query log can be used to log all queries executed on the PostgreSQL machine by applying the following configuration in `/etc/postgresql/<version>/main/postgresql.conf`.

{% highlight ini %}
log_destination = 'stderr'
logging_collector = on
log_file_mode = 0600
log_directory = 'pg_log'
log_filename = 'postgresql-%a.log'
log_min_duration_statement = -1
log_duration = on
log_line_prefix = '%m %u@%d %p %r %e '
log_statement = 'all'
{% endhighlight %}

The line prefix must end in a space. Minimum requirements are the database `%d` and either the process id `%p` or the session id `%c`. The logger will not work without this.

Options:

1. The log file and directory can be changed, but these settings should be reflected in the plugin configuration below.
2. If you do not wish to log all queries, but chose to log only slow queries, the log_min_duration should be set to the minimum duration (in milliseconds).
3. If you are already using csv logging (log_destination), set the 'Log Statement' below to 'csv' instead of 'all'.

PostgreSQL must be restarted for this to take effect.

Log rotation has to be configured manually. More information about log rotation can be found on [the knowledge base](https://www.postgresql.org/docs/9.2/static/logfile-maintenance.html).

### Active checks

This plugin can be configured to perform a SQL query on your PostgreSQL. This active monitoring allows us to calculate the uptime of the service and the response time of the query.

A valid SQL query (eg. `select count(*) from my_table;`) should be provided.

## Events

* Service state

## Metrics

| Metric name                                              | Metric unit |
|----------------------------------------------------------|-------------|
| Number of bytes read by all PostgreSQL processes         | b           |
| Number of bytes written by all PostgreSQL processes      | b           |
| Number of connection to PostgreSQL                       | conn        |
| Number of PostgreSQL processes                           | procs       |
| Number of seconds spent by CPU processing                | s           |
| Number of seconds that the PostgreSQL server has been up | s           |
| Number of statements executed                            | queries     |
| Total number of seconds spent in statements              | s           |
