---
layout: page
title: Monitoring and collecting data from MySQL plugin
description: Information on the metrics collected by the CoScale MySQL plugin.
---

>  The world's most popular open source database. The MySQL™ software delivers a very fast, multi-threaded, multi-user, and robust SQL (Structured Query Language) database server. MySQL Server is intended for mission-critical, heavy-load production systems as well as for embedding into mass-deployed software. The MySQL software is Dual Licensed. Users can choose to use the MySQL software as an Open Source product under the terms of the GNU General Public License (http://www.fsf.org/licenses/) or can purchase a standard commercial license from Oracle.

More information on: [http://www.mysql.com/](http://www.mysql.com/)

## How it works

This plugin analyzes the performance of your MySQL database server.

We gather global statistics (eg. number of connections, open files, ...) by using the SHOW STATUS query on MySQL, this requires access to the database.

There are 2 mechanisms to retrieve performance metrics about your queries. The preferred method is the MySQL performance schema, if this is not available, the slow query log can also be used.

**The minimal supported version of MySQL is 5.1 for the slow query log and 5.7 for performance schema.**

## Installation

{% include_relative _installation.md orchestrator="false" service="MySQL" %}

## Configuration

### Global stats

Global statistics are fetched using the SHOW STATUS query.

A valid database must be provided in order to be able to execute this query. This can be any database.

### Query performance

#### Slow log

For the slow query log, place the following configuration in /etc/mysql/my.cnf.

{% highlight ini %}
[mysqld]
slow_query_log = 1
long_query_time = 0 # log all statements with execution time above 0 s.
slow_query_log_file = /var/log/mysql/slow.log
log_queries_not_using_indexes = 1
event_scheduler = ON
{% endhighlight %}

MySQL must be restarted for this to take effect.

The slow query log does not include the name of database by default. In order to tell the plugin about the current database the following event should be added.

{% highlight sql %}
DELIMITER |
    CREATE EVENT database_detection_event
    ON SCHEDULE EVERY 10 SECOND
    DO BEGIN
        SET @CoScale = concat('select \'coscale_current_database=',
                              database(), '\'');
        prepare CoScale_stmt from @CoScale;
        execute CoScale_stmt;
        deallocate prepare CoScale_stmt;
    END |
DELIMITER ;
{% endhighlight %}

Log rotation has to be configured manually. More information about log rotation can be found on [the knowledge base](https://dev.mysql.com/doc/refman/5.7/en/log-file-maintenance.html).

#### Performance schema

Performance schema is only supported for MySQL version 5.7 and higher.

For performance schema, place the following configuration in `/etc/mysql/my.cnf`.

{% highlight ini %}
[mysqld]
performance_schema=on
performance-schema-consumer-events-statements-history-long=on
performance_schema_events_waits_history_long_size=1000
{% endhighlight %}

MySQL must be restarted for this to take effect.

Create a user and `GRANT` permissions on the `performance_schema`

{% highlight sql %}
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT ON performance_schema.* TO 'username'@'localhost';
{% endhighlight %}

No further configuration is required here, the database credentials from the global stats are used to query the performance schema.

### Active checks

This plugin can be configured to perform a SQL query on your MySQL. This active monitoring allows us to calculate the uptime of the service and the response time of the query.

A valid SQL query (eg. `select count(*) from my_table;`) should be provided.

## Events

* Service state

## Metrics

| Metric name                                                               | Metric unit |
|---------------------------------------------------------------------------|-------------|
| Number of bytes received from all MySQL clients                           | b/s         |
| Maximum number of simultaneous connections in use to MySQL                | conn        |
| Number of bytes sent to all MySQL clients                                 | b/s         |
| Number of connection attempts to MySQL                                    | conn/s      |
| Number of currently open connections to MySQL                             | threads     |
| Number of MySQL cached .frm files                                         | #           |
| Number of MySQL files that are open                                       | files       |
| Number of MySQL queries that have taken more than long_query_time seconds | queries/s   |
| Number of MySQL streams that are open                                     | #           |
| Number of MySQL tables that are open                                      | #           |
| Number of MySQL threads in the thread cache                               | threads     |
| Number of MySQL threads that are not sleeping                             | threads     |
| Number of seconds that the MySQL server has been up                       | s           |
| Number of statements executed in MySQL                                    | queries/s   |
| Number of threads created to handle connections to MySQL                  | threads/s   |

## Extra

### MariaDB

MariaDB is supported by the MySQL plugin, follow the instructions of the MySQL plugin. If you have questions about which version to use, please <a href="mailto:info@coscale.com" class="js-support">contact support</a>.
