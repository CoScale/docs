---
layout: page
title: MSSQL plugin
description: Information on the metrics collected by the CoScale MSSQL plugin.
---

>  Microsoft SQL Server is a relational database management system developed by Microsoft. As a database server, it is a software product with the primary function of storing and retrieving data as requested by other software applications—which may run either on the same computer or on another computer across a network (including the Internet). Microsoft markets at least a dozen different editions of Microsoft SQL Server, aimed at different audiences and for workloads ranging from small single-machine applications to large Internet-facing applications with many concurrent users.

More information on: [https://www.microsoft.com/en-us/sql-server/](https://www.microsoft.com/en-us/sql-server/)

## Events

* Service state

## Metrics

| Metric name                                                                        |Metric unit |
|------------------------------------------------------------------------------------|------------|
| Indicates the number of times the compile code path is entered                     | #/s        |
| Counts the number of times statement recompiles are triggered                      | #/s        |
| Number of index searches per second                                                | #/s        |
| The percentage of pages found in the buffer cache without having to read from disk | %          |
| Amount of memory the server has committed using the memory manager                 | b          |
| The ideal amount of memory the server can consume                                  | b          |
| Number of waits on processes                                                       | b          |
| Total amount of dynamic memory the server is using for the dynamic SQL cache       | b          |
| Counts the number of users currently connected to SQL Server                       | conn       |
| Indicates the number of pages flushed to disk per second                           | pages/s    |
| The number of requests per second to find a page in the buffer pool                | pages/s    |
| The number of physical database page reads that are issued/sec                     | pages/s    |
| The number of physical database page writes that are issued/sec                    | pages/s    |
| Number of currently blocked processes                                              | procs      |
| Number of records per second fetched through forwarded record pointers             | rec/s      |
| Number of unrestricted full scans per second                                       | rec/s      |
| Number of Transact-SQL command batches received per second                         | req/s      |
| Number of lock requests per second that required the caller to wait                | req/s      |
| Number of lock requests per second that timed out (incl. NOWAIT locks)             | req/s      |
| The number of requests per second that had to wait for a free page                 | req/s      |
| Number of lock requests per second that resulted in a deadlock                     | req/s      |
| Mssql Response time of query check                                                 | s          |
| The number of seconds a page will stay in the buffer pool without references       | s          |
| Average latch wait time for latch requests that had to wait                        | s          |
| Number of transactions started for the database/sec                                | transact/s |
| The number of buffers written per second by the buffer manager's lazy writer       | writes/s   |
| Number of page splits/sec that occur as the result of overflowing index pages      | splits/s   |
