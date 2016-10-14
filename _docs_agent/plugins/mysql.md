---
layout: page
title: MySQL plugin
description: Information on the metrics collected by the CoScale MySQL plugin.
---

>  The world's most popular open source database. The MySQL™ software delivers a very fast, multi-threaded, multi-user, and robust SQL (Structured Query Language) database server. MySQL Server is intended for mission-critical, heavy-load production systems as well as for embedding into mass-deployed software. The MySQL software is Dual Licensed. Users can choose to use the MySQL software as an Open Source product under the terms of the GNU General Public License (http://www.fsf.org/licenses/) or can purchase a standard commercial license from Oracle.

More information on: [http://www.mysql.com/](http://www.mysql.com/)

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
