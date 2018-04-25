---
layout: page
title: Oracle plugin
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

## Events

* Service state

## Metrics

| Metric name                                                                                                                                                   | Metric unit |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Oracle-A buffer in the buffer cache was cloned                                                                                                                |             |
| Oracle-A CURRENT buffer (shared or exclusive) is made CR before it can be used                                                                                |             |
| Oracle-Active txn count during cleanout                                                                                                                       |             |
| Oracle-ADG global flush                                                                                                                                       |             |
| Oracle-ADG parselock X get attempts                                                                                                                           |             |
| Oracle-ADG parselock X get successes                                                                                                                          |             |
| Oracle-Application wait time                                                                                                                                  |             |
| Oracle-Auto extends on undo tablespace                                                                                                                        |             |
| Oracle-BA au bytes allocated                                                                                                                                  |             |
| Oracle-BA bytes for file maps                                                                                                                                 |             |
| Oracle-BA bytes read from disk                                                                                                                                |             |
| Oracle-BA bytes read from flash                                                                                                                               |             |
| Oracle-BA count - borrowed from other node                                                                                                                    |             |
| Oracle-BA count - cache denied                                                                                                                                |             |
| Oracle-BA count - cache miss                                                                                                                                  |             |
| Oracle-BA count - searched in pb                                                                                                                              |             |
| Oracle-BA count - short circuit in idn                                                                                                                        |             |
| Oracle-BA count - total allocation requests                                                                                                                   |             |
| Oracle-BA count - unable to short circuit in idn                                                                                                              |             |
| Oracle-BA count when 10% of buckets in pb                                                                                                                     |             |
| Oracle-BA count when 25% of buckets in pb                                                                                                                     |             |
| Oracle-BA count when 50% of buckets in pb                                                                                                                     |             |
| Oracle-BA count when 75% of buckets in pb                                                                                                                     |             |
| Oracle-BA count when 90% of buckets in pb                                                                                                                     |             |
| Oracle-BA file bytes allocated                                                                                                                                |             |
| Oracle-BA file bytes deleted                                                                                                                                  |             |
| Oracle-BA files created count                                                                                                                                 |             |
| Oracle-BA files deleted count                                                                                                                                 |             |
| Oracle-BA flash bytes requested                                                                                                                               |             |
| Oracle-BA non-flash bytes requested                                                                                                                           |             |
| Oracle-BA spare statistic 1                                                                                                                                   |             |
| Oracle-BA spare statistic 2                                                                                                                                   |             |
| Oracle-BA spare statistic 3                                                                                                                                   |             |
| Oracle-BA spare statistic 4                                                                                                                                   |             |
| Oracle-BA spare statistic 5                                                                                                                                   |             |
| Oracle-BA spare statistic 6                                                                                                                                   |             |
| Oracle-BA spare statistic 7                                                                                                                                   |             |
| Oracle-BA spare statistic 8                                                                                                                                   |             |
| Oracle-BA spare statistic 9                                                                                                                                   |             |
| Oracle-BA spare statistic 10                                                                                                                                  |             |
| Oracle-BA spare statistic 11                                                                                                                                  |             |
| Oracle-BA spare statistic 12                                                                                                                                  |             |
| Oracle-Background timeouts                                                                                                                                    |             |
| Oracle-backup compressed data written locally                                                                                                                 |             |
| Oracle-backup compressed data written remotely                                                                                                                |             |
| Oracle-backup data compressed locally                                                                                                                         |             |
| Oracle-backup data compressed remotely                                                                                                                        |             |
| Oracle-backup piece local processing time                                                                                                                     |             |
| Oracle-backup piece remote processing time                                                                                                                    |             |
| Oracle-backup pieces compressed locally                                                                                                                       |             |
| Oracle-backup pieces compressed remotely                                                                                                                      |             |
| Oracle-Batched IO (bound) vector count                                                                                                                        |             |
| Oracle-Batched IO (full) vector count                                                                                                                         |             |
| Oracle-Batched IO (space) vector count                                                                                                                        |             |
| Oracle-Batched IO block miss count                                                                                                                            |             |
| Oracle-Batched IO buffer defrag count                                                                                                                         |             |
| Oracle-Batched IO double miss count                                                                                                                           |             |
| Oracle-Batched IO same unit count                                                                                                                             |             |
| Oracle-Batched IO single block count                                                                                                                          |             |
| Oracle-Batched IO slow jump count                                                                                                                             |             |
| Oracle-Batched IO vector block count                                                                                                                          |             |
| Oracle-Batched IO vector read count                                                                                                                           |             |
| Oracle-Batched IO zero block count                                                                                                                            |             |
| Oracle-Block Cleanout Optim referenced                                                                                                                        |             |
| Oracle-Blocks decrypted                                                                                                                                       |             |
| Oracle-Blocks encrypted                                                                                                                                       |             |
| Oracle-Branch node splits                                                                                                                                     |             |
| Oracle-Buffer is not pinned count                                                                                                                             |             |
| Oracle-Buffer is pinned count                                                                                                                                 |             |
| Oracle-Bytes via SQL*Net vector from client                                                                                                                   | bytes       |
| Oracle-Bytes via SQL*Net vector from dblink                                                                                                                   | bytes       |
| Oracle-Bytes via SQL*Net vector to client                                                                                                                     | bytes       |
| Oracle-Bytes via SQL*Net vector to dblink                                                                                                                     | bytes       |
| Oracle-Cached Commit SCN referenced                                                                                                                           |             |
| Oracle-Calls to kcmgas                                                                                                                                        |             |
| Oracle-Calls to kcmgcs                                                                                                                                        |             |
| Oracle-Calls to kcmgrs                                                                                                                                        |             |
| Oracle-CCursor + sql area evicted                                                                                                                             |             |
| Oracle-Cell blocks helped by commit cache                                                                                                                     |             |
| Oracle-Cell blocks helped by minscn optimization                                                                                                              |             |
| Oracle-Cell blocks processed by cache layer                                                                                                                   |             |
| Oracle-Cell blocks processed by data layer                                                                                                                    |             |
| Oracle-Cell blocks processed by index layer                                                                                                                   |             |
| Oracle-Cell blocks processed by txn layer                                                                                                                     |             |
| Oracle-Cell commit cache queries                                                                                                                              |             |
| Oracle-Cell CUs processed for compressed                                                                                                                      |             |
| Oracle-Cell CUs processed for uncompressed                                                                                                                    |             |
| Oracle-Cell CUs sent compressed                                                                                                                               |             |
| Oracle-Cell CUs sent head piece                                                                                                                               |             |
| Oracle-Cell CUs sent uncompressed                                                                                                                             |             |
| Oracle-cell flash cache read hits                                                                                                                             |             |
| Oracle-Cell index scans                                                                                                                                       |             |
| Oracle-Cell interconnect bytes returned by XT smart scan                                                                                                      |             |
| Oracle-Cell IO uncompressed bytes                                                                                                                             |             |
| Oracle-cell logical write IO requests                                                                                                                         |             |
| Oracle-cell logical write IO requests eligible for offload                                                                                                    |             |
| Oracle-Cell num block IOs due to a file instant restore in progress                                                                                           |             |
| Oracle-Cell num bytes in block IO during predicate offload                                                                                                    |             |
| Oracle-Cell num bytes in passthru during predicate offload                                                                                                    |             |
| Oracle-Cell num bytes of IO reissued due to relocation                                                                                                        |             |
| Oracle-Cell num fast response sessions                                                                                                                        |             |
| Oracle-Cell num fast response sessions continuing to smart scan                                                                                               |             |
| Oracle-Cell num smart file creation sessions using rdbms block IO mode                                                                                        |             |
| Oracle-Cell num smart IO sessions in rdbms block IO due to big payload                                                                                        |             |
| Oracle-Cell num smart IO sessions in rdbms block IO due to no cell mem                                                                                        |             |
| Oracle-Cell num smart IO sessions in rdbms block IO due to open fail                                                                                          |             |
| Oracle-Cell num smart IO sessions in rdbms block IO due to user                                                                                               |             |
| Oracle-Cell num smart IO sessions using passthru mode due to cellsrv                                                                                          |             |
| Oracle-Cell num smart IO sessions using passthru mode due to timezone                                                                                         |             |
| Oracle-Cell num smart IO sessions using passthru mode due to user                                                                                             |             |
| Oracle-Cell num smartio automem buffer allocation attempts                                                                                                    |             |
| Oracle-Cell num smartio automem buffer allocation failures                                                                                                    |             |
| Oracle-Cell num smartio permanent cell failures                                                                                                               |             |
| Oracle-Cell num smartio transient cell failures                                                                                                               |             |
| Oracle-Cell overwrites in flash cache                                                                                                                         |             |
| Oracle-Cell partial writes in flash cache                                                                                                                     |             |
| Oracle-Cell physical IO bytes eligible for predicate offload                                                                                                  |             |
| Oracle-Cell physical IO bytes saved by columnar cache                                                                                                         |             |
| Oracle-Cell physical IO bytes saved by storage index                                                                                                          |             |
| Oracle-Cell physical IO bytes saved during optimized file creation                                                                                            |             |
| Oracle-Cell physical IO bytes saved during optimized RMAN file restore                                                                                        |             |
| Oracle-Cell physical IO bytes sent directly to DB node to balance CPU                                                                                         |             |
| Oracle-Cell physical IO interconnect bytes                                                                                                                    | bytes       |
| Oracle-Cell physical IO interconnect bytes returned by smart scan                                                                                             |             |
| Oracle-Cell physical write bytes saved by smart file initialization                                                                                           |             |
| Oracle-cell physical write IO bytes eligible for offload                                                                                                      |             |
| Oracle-cell physical write IO host network bytes written during offload                                                                                       | bytes       |
| Oracle-Cell scans                                                                                                                                             |             |
| Oracle-Cell simulated physical IO bytes eligible for predicate offload                                                                                        |             |
| Oracle-Cell simulated physical IO bytes returned by predicate offload                                                                                         |             |
| Oracle-Cell smart IO session cache hard misses                                                                                                                |             |
| Oracle-Cell smart IO session cache hits                                                                                                                       |             |
| Oracle-Cell smart IO session cache hwm                                                                                                                        |             |
| Oracle-Cell smart IO session cache lookups                                                                                                                    |             |
| Oracle-Cell smart IO session cache soft misses                                                                                                                |             |
| Oracle-Cell statistics spare1                                                                                                                                 |             |
| Oracle-Cell statistics spare2                                                                                                                                 |             |
| Oracle-Cell statistics spare3                                                                                                                                 |             |
| Oracle-Cell statistics spare4                                                                                                                                 |             |
| Oracle-Cell statistics spare5                                                                                                                                 |             |
| Oracle-Cell statistics spare6                                                                                                                                 |             |
| Oracle-Cell transactions found in commit cache                                                                                                                |             |
| Oracle-Cell XT granule bytes requested for predicate offload                                                                                                  |             |
| Oracle-Cell XT granule predicate offload retries                                                                                                              |             |
| Oracle-Cell XT granules requested for predicate offload                                                                                                       |             |
| Oracle-Chained rows processed by cell                                                                                                                         |             |
| Oracle-Chained rows rejected by cell                                                                                                                          |             |
| Oracle-Chained rows skipped by cell                                                                                                                           |             |
| Oracle-Checkpoint clones created for ADG recovery                                                                                                             |             |
| Oracle-Cleanout - number of ktugct calls                                                                                                                      |             |
| Oracle-Cleanouts and rollbacks - consistent read gets                                                                                                         |             |
| Oracle-Cleanouts only - consistent read gets                                                                                                                  |             |
| Oracle-CLI BG attempt Flush                                                                                                                                   |             |
| Oracle-CLI BG ENQ                                                                                                                                             |             |
| Oracle-CLI BG Fls done                                                                                                                                        |             |
| Oracle-CLI Buf Wrt                                                                                                                                            |             |
| Oracle-CLI bytes fls to ext                                                                                                                                   |             |
| Oracle-CLI bytes fls to table                                                                                                                                 |             |
| Oracle-CLI Client Flush                                                                                                                                       |             |
| Oracle-CLI Flstask create                                                                                                                                     |             |
| Oracle-CLI Flush                                                                                                                                              |             |
| Oracle-CLI Imm Wrt                                                                                                                                            |             |
| Oracle-CLI Prvtz Lob                                                                                                                                          |             |
| Oracle-CLI SGA Alloc                                                                                                                                          |             |
| Oracle-CLI Thru Wrt                                                                                                                                           |             |
| Oracle-Cluster wait time                                                                                                                                      |             |
| Oracle-Clusterwide global transactions                                                                                                                        |             |
| Oracle-Clusterwide global transactions spanning RAC nodes                                                                                                     |             |
| Oracle-Cold recycle reads                                                                                                                                     |             |
| Oracle-Commit batch performed                                                                                                                                 |             |
| Oracle-Commit batch requested                                                                                                                                 |             |
| Oracle-Commit batch/immediate performed                                                                                                                       |             |
| Oracle-Commit batch/immediate requested                                                                                                                       |             |
| Oracle-Commit immediate performed                                                                                                                             |             |
| Oracle-Commit immediate requested                                                                                                                             |             |
| Oracle-Commit nowait performed                                                                                                                                |             |
| Oracle-Commit nowait requested                                                                                                                                |             |
| Oracle-Commit SCN cached                                                                                                                                      |             |
| Oracle-Commit txn count during cleanout                                                                                                                       |             |
| Oracle-Commit wait performed                                                                                                                                  |             |
| Oracle-Commit wait requested                                                                                                                                  |             |
| Oracle-Commit wait/nowait performed                                                                                                                           |             |
| Oracle-Commit wait/nowait requested                                                                                                                           |             |
| Oracle-Concurrency wait time                                                                                                                                  |             |
| Oracle-Consistent gets direct                                                                                                                                 |             |
| Oracle-Consistent gets examination                                                                                                                            |             |
| Oracle-Consistent gets examination (fastpath)                                                                                                                 |             |
| Oracle-Consistent gets from cache                                                                                                                             |             |
| Oracle-Consistent gets pin                                                                                                                                    |             |
| Oracle-Consistent gets pin (fastpath)                                                                                                                         |             |
| Oracle-Cot buffers moved to head of LRU                                                                                                                       |             |
| Oracle-Count of range scans on tables that have the CACHE option enabled                                                                                      |             |
| Oracle-Count of table scans performed with direct read (bypassing the buffer cache)                                                                           |             |
| Oracle-Count of table scans with specified ROWID endpoints. This is performed for Parallel Query.                                                             |             |
| Oracle-Count of the total number of writes by LGWR to the redo log files                                                                                      |             |
| Oracle-CPU used when call started                                                                                                                             |             |
| Oracle-Cursor authentications                                                                                                                                 |             |
| Oracle-Cursor reload failures                                                                                                                                 |             |
| Oracle-cvmap unavailable                                                                                                                                      |             |
| Oracle-Data blocks consistent reads - undo records applied                                                                                                    |             |
| Oracle-Data warehousing cooling action                                                                                                                        |             |
| Oracle-Data warehousing evicted objects                                                                                                                       |             |
| Oracle-Data warehousing evicted objects - cooling                                                                                                             |             |
| Oracle-Data warehousing evicted objects - replace                                                                                                             |             |
| Oracle-Data warehousing scanned blocks                                                                                                                        |             |
| Oracle-Data warehousing scanned blocks - disk                                                                                                                 |             |
| Oracle-Data warehousing scanned blocks - flash                                                                                                                |             |
| Oracle-Data warehousing scanned blocks - memory                                                                                                               |             |
| Oracle-Data warehousing scanned blocks - offload                                                                                                              |             |
| Oracle-Data warehousing scanned objects                                                                                                                       |             |
| Oracle-DB block gets direct                                                                                                                                   |             |
| Oracle-DB block gets from cache                                                                                                                               |             |
| Oracle-DB block gets from cache (fastpath)                                                                                                                    |             |
| Oracle-DB corrupt blocks detected                                                                                                                             |             |
| Oracle-DB corrupt blocks recovered                                                                                                                            |             |
| Oracle-DB time                                                                                                                                                |             |
| Oracle-DBWR checkpoint buffers written                                                                                                                        |             |
| Oracle-DBWR fusion writes                                                                                                                                     |             |
| Oracle-DBWR object drop buffers written                                                                                                                       |             |
| Oracle-DBWR parallel query checkpoint buffers written                                                                                                         |             |
| Oracle-DBWR revisited being-written buffer                                                                                                                    |             |
| Oracle-DBWR tablespace checkpoint buffers written                                                                                                             |             |
| Oracle-DBWR thread checkpoint buffers written                                                                                                                 |             |
| Oracle-DBWR transaction table writes                                                                                                                          |             |
| Oracle-DBWR undo block writes                                                                                                                                 |             |
| Oracle-Deferred (CURRENT) block cleanout applications                                                                                                         |             |
| Oracle-Deferred CUR cleanouts (index blocks)                                                                                                                  |             |
| Oracle-DFO trees parallelized                                                                                                                                 |             |
| Oracle-Doubling up with imu segment                                                                                                                           |             |
| Oracle-Drop segment calls in space pressure                                                                                                                   |             |
| Oracle-DX/BB enqueue lock background get time                                                                                                                 |             |
| Oracle-DX/BB enqueue lock background gets                                                                                                                     |             |
| Oracle-DX/BB enqueue lock foreground requests                                                                                                                 |             |
| Oracle-DX/BB enqueue lock foreground wait time                                                                                                                |             |
| Oracle-Effective IO time                                                                                                                                      |             |
| Oracle-EHCC Analyze CUs Decompressed                                                                                                                          |             |
| Oracle-EHCC Analyzer Calls                                                                                                                                    |             |
| Oracle-EHCC Archive CUs Compressed                                                                                                                            |             |
| Oracle-EHCC Archive CUs Decompressed                                                                                                                          |             |
| Oracle-EHCC Attempted Block Compressions                                                                                                                      |             |
| Oracle-EHCC Block Compressions                                                                                                                                |             |
| Oracle-EHCC Check CUs Decompressed                                                                                                                            |             |
| Oracle-EHCC Columns Decompressed                                                                                                                              |             |
| Oracle-EHCC Compressed Length Compressed                                                                                                                      |             |
| Oracle-EHCC Compressed Length Decompressed                                                                                                                    |             |
| Oracle-EHCC Conventional DMLs                                                                                                                                 |             |
| Oracle-EHCC CU Row Pieces Compressed                                                                                                                          |             |
| Oracle-EHCC CUs all rows pass minmax                                                                                                                          |             |
| Oracle-EHCC CUs Compressed                                                                                                                                    |             |
| Oracle-EHCC CUs Decompressed                                                                                                                                  |             |
| Oracle-EHCC CUs no rows pass minmax                                                                                                                           |             |
| Oracle-EHCC CUs some rows pass minmax                                                                                                                         |             |
| Oracle-EHCC Decompressed Length Compressed                                                                                                                    |             |
| Oracle-EHCC Decompressed Length Decompressed                                                                                                                  |             |
| Oracle-EHCC DML CUs Decompressed                                                                                                                              |             |
| Oracle-EHCC Dump CUs Decompressed                                                                                                                             |             |
| Oracle-EHCC Normal Scan CUs Decompressed                                                                                                                      |             |
| Oracle-EHCC Pieces Buffered for Decompression                                                                                                                 |             |
| Oracle-EHCC Preds all rows pass minmax                                                                                                                        |             |
| Oracle-EHCC Preds no rows pass minmax                                                                                                                         |             |
| Oracle-EHCC Preds some rows pass minmax                                                                                                                       |             |
| Oracle-EHCC Query High CUs Compressed                                                                                                                         |             |
| Oracle-EHCC Query High CUs Decompressed                                                                                                                       |             |
| Oracle-EHCC Query Low CUs Compressed                                                                                                                          |             |
| Oracle-EHCC Query Low CUs Decompressed                                                                                                                        |             |
| Oracle-EHCC Rowid CUs Decompressed                                                                                                                            |             |
| Oracle-EHCC Rows Compressed                                                                                                                                   |             |
| Oracle-EHCC Rows Not Compressed                                                                                                                               |             |
| Oracle-EHCC Total Columns for Decompression                                                                                                                   |             |
| Oracle-EHCC Total Pieces for Decompression                                                                                                                    |             |
| Oracle-EHCC Total Rows for Decompression                                                                                                                      |             |
| Oracle-EHCC Turbo Scan CUs Decompressed                                                                                                                       |             |
| Oracle-EHCC Used on Pillar Tablespace                                                                                                                         |             |
| Oracle-EHCC Used on ZFS Tablespace                                                                                                                            |             |
| Oracle-Error count cleared by cell                                                                                                                            |             |
| Oracle-Failed probes on index block reclamation                                                                                                               |             |
| Oracle-Fastpath consistent get quota limit                                                                                                                    |             |
| Oracle-fbda woken up                                                                                                                                          |             |
| Oracle-File io service time                                                                                                                                   |             |
| Oracle-File io wait time                                                                                                                                      |             |
| Oracle-Filtered blocks failed block check                                                                                                                     |             |
| Oracle-Flash cache eviction: aged out                                                                                                                         |             |
| Oracle-Flash cache eviction: buffer pinned                                                                                                                    |             |
| Oracle-Flash cache eviction: invalidated                                                                                                                      |             |
| Oracle-Flash cache insert skip: corrupt                                                                                                                       |             |
| Oracle-Flash cache insert skip: DBWR overloaded                                                                                                               |             |
| Oracle-Flash cache insert skip: exists                                                                                                                        |             |
| Oracle-Flash cache insert skip: modification                                                                                                                  |             |
| Oracle-Flash cache insert skip: not current                                                                                                                   |             |
| Oracle-Flash cache insert skip: not useful                                                                                                                    |             |
| Oracle-Flash cache inserts                                                                                                                                    |             |
| Oracle-Flashback cache read optimizations for block new                                                                                                       |             |
| Oracle-Flashback direct read optimizations for block new                                                                                                      |             |
| Oracle-Flashback log write bytes                                                                                                                              |             |
| Oracle-Flashback log writes                                                                                                                                   |             |
| Oracle-Flashback securefile cache read optimizations for block new                                                                                            |             |
| Oracle-Flashback securefile direct read optimizations for block new                                                                                           |             |
| Oracle-Foreground propagated tracked transactions                                                                                                             |             |
| Oracle-Forwarded 2PC commands across RAC nodes                                                                                                                |             |
| Oracle-Frame signature mismatch                                                                                                                               |             |
| Oracle-gc blocks compressed                                                                                                                                   |             |
| Oracle-gc blocks corrupt                                                                                                                                      |             |
| Oracle-gc blocks lost                                                                                                                                         |             |
| Oracle-gc claim blocks lost                                                                                                                                   |             |
| Oracle-gc cleanout applied                                                                                                                                    |             |
| Oracle-gc cleanout no space                                                                                                                                   |             |
| Oracle-gc cleanout saved                                                                                                                                      |             |
| Oracle-gc cluster flash cache reads failure                                                                                                                   |             |
| Oracle-gc cluster flash cache reads received                                                                                                                  |             |
| Oracle-gc cluster flash cache reads served                                                                                                                    |             |
| Oracle-gc cluster flash cache received read time                                                                                                              |             |
| Oracle-gc CPU used by this session                                                                                                                            |             |
| Oracle-gc cr block build time                                                                                                                                 |             |
| Oracle-gc cr block flush time                                                                                                                                 |             |
| Oracle-gc cr block receive time                                                                                                                               |             |
| Oracle-gc cr block send time                                                                                                                                  |             |
| Oracle-gc cr blocks flushed                                                                                                                                   |             |
| Oracle-gc cr blocks received                                                                                                                                  |             |
| Oracle-gc cr blocks received with BPS                                                                                                                         |             |
| Oracle-gc cr blocks served                                                                                                                                    |             |
| Oracle-gc cr blocks served with BPS                                                                                                                           |             |
| Oracle-gc current block flush time                                                                                                                            |             |
| Oracle-gc current block pin time                                                                                                                              |             |
| Oracle-gc current block receive time                                                                                                                          |             |
| Oracle-gc current block send time                                                                                                                             |             |
| Oracle-gc current blocks flushed                                                                                                                              |             |
| Oracle-gc current blocks pinned                                                                                                                               |             |
| Oracle-gc current blocks received                                                                                                                             |             |
| Oracle-gc current blocks received with BPS                                                                                                                    |             |
| Oracle-gc current blocks served                                                                                                                               |             |
| Oracle-gc current blocks served with BPS                                                                                                                      |             |
| Oracle-gc flash cache reads served                                                                                                                            |             |
| Oracle-gc flash cache served read time                                                                                                                        |             |
| Oracle-gc force cr read cr                                                                                                                                    |             |
| Oracle-gc force cr read current                                                                                                                               |             |
| Oracle-gc IM blocks invalidated                                                                                                                               |             |
| Oracle-gc IM expands                                                                                                                                          |             |
| Oracle-gc IM grants                                                                                                                                           |             |
| Oracle-gc IM shrinks                                                                                                                                          |             |
| Oracle-gc ka grant receive time                                                                                                                               |             |
| Oracle-gc ka grants received                                                                                                                                  |             |
| Oracle-gc kbytes saved                                                                                                                                        |             |
| Oracle-gc kbytes sent                                                                                                                                         |             |
| Oracle-gc local grants                                                                                                                                        |             |
| Oracle-gc read time waited                                                                                                                                    |             |
| Oracle-gc read wait failures                                                                                                                                  |             |
| Oracle-gc read wait timeouts                                                                                                                                  |             |
| Oracle-gc read waits                                                                                                                                          |             |
| Oracle-gc reader bypass grants                                                                                                                                |             |
| Oracle-gc reader bypass waits                                                                                                                                 |             |
| Oracle-gc remote grants                                                                                                                                       |             |
| Oracle-gcs messages sent                                                                                                                                      |             |
| Oracle-ges messages sent                                                                                                                                      |             |
| Oracle-global enqueue CPU used by this session                                                                                                                |             |
| Oracle-Global enqueue get time                                                                                                                                |             |
| Oracle-Global enqueue gets async                                                                                                                              |             |
| Oracle-Global enqueue gets sync                                                                                                                               |             |
| Oracle-Global enqueue releases                                                                                                                                |             |
| Oracle-Global undo segment hints helped                                                                                                                       |             |
| Oracle-Global undo segment hints were stale                                                                                                                   |             |
| Oracle-GTX processes spawned by autotune                                                                                                                      |             |
| Oracle-GTX processes stopped by autotune                                                                                                                      |             |
| Oracle-Heap block compress                                                                                                                                    |             |
| Oracle-Heap Segment Array Inserts                                                                                                                             |             |
| Oracle-Heap Segment Array Updates                                                                                                                             |             |
| Oracle-Heatmap Blklevel Flush Task Count                                                                                                                      |             |
| Oracle-Heatmap BlkLevel Flush Task Create                                                                                                                     |             |
| Oracle-Heatmap BlkLevel Flushed                                                                                                                               |             |
| Oracle-Heatmap BlkLevel Flushed to BF                                                                                                                         |             |
| Oracle-Heatmap BlkLevel Flushed to SYSAUX                                                                                                                     |             |
| Oracle-Heatmap BlkLevel Not Tracked - Memory                                                                                                                  |             |
| Oracle-Heatmap BlkLevel Not Updated - Repeat                                                                                                                  |             |
| Oracle-Heatmap BlkLevel Ranges Flushed                                                                                                                        |             |
| Oracle-Heatmap BlkLevel Ranges Skipped                                                                                                                        |             |
| Oracle-Heatmap BlkLevel Tracked                                                                                                                               |             |
| Oracle-Heatmap SegLevel - Flush                                                                                                                               |             |
| Oracle-Heatmap SegLevel - Full Table Scan                                                                                                                     |             |
| Oracle-Heatmap SegLevel - IndexLookup                                                                                                                         |             |
| Oracle-Heatmap SegLevel - Segments flushed                                                                                                                    |             |
| Oracle-Heatmap SegLevel - TableLookup                                                                                                                         |             |
| Oracle-Heatmap SegLevel - Write                                                                                                                               |             |
| Oracle-HSC Compressed Segment Block Changes                                                                                                                   |             |
| Oracle-HSC Heap Segment Block Changes                                                                                                                         |             |
| Oracle-HSC IDL Compressed Blocks                                                                                                                              |             |
| Oracle-HSC OLTP Compressed Blocks                                                                                                                             |             |
| Oracle-HSC OLTP compression block checked                                                                                                                     |             |
| Oracle-HSC OLTP Compression skipped rows                                                                                                                      |             |
| Oracle-HSC OLTP Compression wide compressed row pieces                                                                                                        |             |
| Oracle-HSC OLTP Drop Column                                                                                                                                   |             |
| Oracle-HSC OLTP inline compression                                                                                                                            |             |
| Oracle-HSC OLTP negative compression                                                                                                                          |             |
| Oracle-HSC OLTP Non Compressible Blocks                                                                                                                       |             |
| Oracle-HSC OLTP positive compression                                                                                                                          |             |
| Oracle-HSC OLTP recursive compression                                                                                                                         |             |
| Oracle-HSC OLTP Space Saving                                                                                                                                  |             |
| Oracle-If the number of disk writes is non-zero for a given sort operation, then this statistic is incremented                                                |             |
| Oracle-If the number of disk writes is zero, then the sort was performed completely in memory and this statistic is incremented.                              |             |
| Oracle-IM fetches by rowid from disk                                                                                                                          |             |
| Oracle-IM fetches by rowid from fetch list                                                                                                                    |             |
| Oracle-IM fetches by rowid from IMCU                                                                                                                          |             |
| Oracle-IM fetches by rowid from journal                                                                                                                       |             |
| Oracle-IM fetches by rowid row invalid in IMCU                                                                                                                |             |
| Oracle-IM populate (faststart) accumulated time (ms)                                                                                                          |             |
| Oracle-IM populate (faststart) CUs accumulated write time (ms)                                                                                                |             |
| Oracle-IM populate (faststart) CUs bytes read                                                                                                                 |             |
| Oracle-IM populate (faststart) CUs bytes written                                                                                                              |             |
| Oracle-IM populate (faststart) CUs read                                                                                                                       |             |
| Oracle-IM populate (faststart) CUs read attempts                                                                                                              |             |
| Oracle-IM populate (faststart) CUs verified                                                                                                                   |             |
| Oracle-IM populate (faststart) CUs wall clock write time (ms)                                                                                                 |             |
| Oracle-IM populate (faststart) CUs write requests                                                                                                             |             |
| Oracle-IM populate (faststart) CUs writes                                                                                                                     |             |
| Oracle-IM populate (faststart) number of incompatible savepoints                                                                                              |             |
| Oracle-IM populate (faststart) number of invalid savepoints                                                                                                   |             |
| Oracle-IM populate (faststart) number of savepoints updated                                                                                                   |             |
| Oracle-IM populate accumulated time (ms)                                                                                                                      |             |
| Oracle-IM populate blocks invalid                                                                                                                             |             |
| Oracle-IM populate bytes from storage                                                                                                                         | bytes       |
| Oracle-IM populate bytes in-memory data                                                                                                                       | bytes       |
| Oracle-IM populate bytes uncompressed data                                                                                                                    | bytes       |
| Oracle-IM populate CUs                                                                                                                                        |             |
| Oracle-IM populate CUs chain pieces                                                                                                                           |             |
| Oracle-IM populate CUs columns                                                                                                                                |             |
| Oracle-IM populate CUs empty                                                                                                                                  |             |
| Oracle-IM populate CUs memcompress for capacity high                                                                                                          |             |
| Oracle-IM populate CUs memcompress for capacity low                                                                                                           |             |
| Oracle-IM populate CUs memcompress for dml                                                                                                                    |             |
| Oracle-IM populate CUs memcompress for query high                                                                                                             |             |
| Oracle-IM populate CUs memcompress for query low                                                                                                              |             |
| Oracle-IM populate CUs no memcompress                                                                                                                         |             |
| Oracle-IM populate CUs requested                                                                                                                              |             |
| Oracle-IM populate CUs resubmitted                                                                                                                            |             |
| Oracle-IM populate rows                                                                                                                                       |             |
| Oracle-IM populate segments                                                                                                                                   |             |
| Oracle-IM populate segments requested                                                                                                                         |             |
| Oracle-IM populate transactions active                                                                                                                        |             |
| Oracle-IM populate transactions check                                                                                                                         |             |
| Oracle-IM populate undo records applied                                                                                                                       |             |
| Oracle-IM populate undo segheader rollback                                                                                                                    |             |
| Oracle-IM prepopulate accumulated time (ms)                                                                                                                   |             |
| Oracle-IM prepopulate bytes from storage                                                                                                                      | bytes       |
| Oracle-IM prepopulate bytes in-memory data                                                                                                                    | bytes       |
| Oracle-IM prepopulate bytes uncompressed data                                                                                                                 | bytes       |
| Oracle-IM prepopulate CUs                                                                                                                                     |             |
| Oracle-IM prepopulate CUs chain pieces                                                                                                                        |             |
| Oracle-IM prepopulate CUs columns                                                                                                                             |             |
| Oracle-IM prepopulate CUs empty                                                                                                                               |             |
| Oracle-IM prepopulate CUs memcompress for capacity high                                                                                                       |             |
| Oracle-IM prepopulate CUs memcompress for capacity low                                                                                                        |             |
| Oracle-IM prepopulate CUs memcompress for dml                                                                                                                 |             |
| Oracle-IM prepopulate CUs memcompress for query high                                                                                                          |             |
| Oracle-IM prepopulate CUs memcompress for query low                                                                                                           |             |
| Oracle-IM prepopulate CUs no memcompress                                                                                                                      |             |
| Oracle-IM prepopulate CUs requested                                                                                                                           |             |
| Oracle-IM prepopulate CUs resubmitted                                                                                                                         |             |
| Oracle-IM prepopulate rows                                                                                                                                    |             |
| Oracle-IM prepopulate segments                                                                                                                                |             |
| Oracle-IM prepopulate segments requested                                                                                                                      |             |
| Oracle-IM rac blocks invalid                                                                                                                                  |             |
| Oracle-IM rac CUs invalid                                                                                                                                     |             |
| Oracle-IM repopulate (scan) CUs                                                                                                                               |             |
| Oracle-IM repopulate (scan) CUs requested                                                                                                                     |             |
| Oracle-IM repopulate (scan) CUs resubmitted                                                                                                                   |             |
| Oracle-IM repopulate (trickle) accumulated time (ms)                                                                                                          |             |
| Oracle-IM repopulate (trickle) bytes from storage                                                                                                             | bytes       |
| Oracle-IM repopulate (trickle) bytes in-memory data                                                                                                           | bytes       |
| Oracle-IM repopulate (trickle) bytes uncompressed data                                                                                                        | bytes       |
| Oracle-IM repopulate (trickle) CUs                                                                                                                            |             |
| Oracle-IM repopulate (trickle) CUs chain pieces                                                                                                               |             |
| Oracle-IM repopulate (trickle) CUs columns                                                                                                                    |             |
| Oracle-IM repopulate (trickle) CUs empty                                                                                                                      |             |
| Oracle-IM repopulate (trickle) CUs memcompress for capacity high                                                                                              |             |
| Oracle-IM repopulate (trickle) CUs memcompress for capacity low                                                                                               |             |
| Oracle-IM repopulate (trickle) CUs memcompress for dml                                                                                                        |             |
| Oracle-IM repopulate (trickle) CUs memcompress for query high                                                                                                 |             |
| Oracle-IM repopulate (trickle) CUs memcompress for query low                                                                                                  |             |
| Oracle-IM repopulate (trickle) CUs no memcompress                                                                                                             |             |
| Oracle-IM repopulate (trickle) CUs requested                                                                                                                  |             |
| Oracle-IM repopulate (trickle) CUs resubmitted                                                                                                                |             |
| Oracle-IM repopulate (trickle) rows                                                                                                                           |             |
| Oracle-IM repopulate accumulated time (ms)                                                                                                                    |             |
| Oracle-IM repopulate blocks invalid                                                                                                                           |             |
| Oracle-IM repopulate bytes from storage                                                                                                                       | bytes       |
| Oracle-IM repopulate bytes in-memory data                                                                                                                     | bytes       |
| Oracle-IM repopulate bytes uncompressed data                                                                                                                  | bytes       |
| Oracle-IM repopulate CUs                                                                                                                                      |             |
| Oracle-IM repopulate CUs chain pieces                                                                                                                         |             |
| Oracle-IM repopulate CUs columns                                                                                                                              |             |
| Oracle-IM repopulate CUs empty                                                                                                                                |             |
| Oracle-IM repopulate CUs memcompress for capacity high                                                                                                        |             |
| Oracle-IM repopulate CUs memcompress for capacity low                                                                                                         |             |
| Oracle-IM repopulate CUs memcompress for dml                                                                                                                  |             |
| Oracle-IM repopulate CUs memcompress for query high                                                                                                           |             |
| Oracle-IM repopulate CUs memcompress for query low                                                                                                            |             |
| Oracle-IM repopulate CUs no memcompress                                                                                                                       |             |
| Oracle-IM repopulate CUs requested                                                                                                                            |             |
| Oracle-IM repopulate CUs resubmitted                                                                                                                          |             |
| Oracle-IM repopulate rows                                                                                                                                     |             |
| Oracle-IM repopulate segments                                                                                                                                 |             |
| Oracle-IM repopulate segments requested                                                                                                                       |             |
| Oracle-IM repopulate transactions active                                                                                                                      |             |
| Oracle-IM repopulate transactions check                                                                                                                       |             |
| Oracle-IM repopulate undo records applied                                                                                                                     |             |
| Oracle-IM repopulate undo segheader rollback                                                                                                                  |             |
| Oracle-IM scan blocks cache                                                                                                                                   |             |
| Oracle-IM scan bytes in-memory                                                                                                                                |             |
| Oracle-IM scan bytes uncompressed                                                                                                                             |             |
| Oracle-IM scan CUs cleanout                                                                                                                                   |             |
| Oracle-IM scan CUs column not in memory                                                                                                                       |             |
| Oracle-IM scan CUs columns accessed                                                                                                                           |             |
| Oracle-IM scan CUs columns decompressed                                                                                                                       |             |
| Oracle-IM scan CUs columns theoretical max                                                                                                                    |             |
| Oracle-IM scan CUs failed to reget pin                                                                                                                        |             |
| Oracle-IM scan CUs invalid                                                                                                                                    |             |
| Oracle-IM scan CUs invalid (all rows are invalid)                                                                                                             |             |
| Oracle-IM scan CUs invalid or missing revert to on disk extent                                                                                                |             |
| Oracle-IM scan CUs memcompress for capacity high                                                                                                              |             |
| Oracle-IM scan CUs memcompress for capacity low                                                                                                               |             |
| Oracle-IM scan CUs memcompress for dml                                                                                                                        |             |
| Oracle-IM scan CUs memcompress for query high                                                                                                                 |             |
| Oracle-IM scan CUs memcompress for query low                                                                                                                  |             |
| Oracle-IM scan CUs no cleanout                                                                                                                                |             |
| Oracle-IM scan CUs no memcompress                                                                                                                             |             |
| Oracle-IM scan CUs no rollback                                                                                                                                |             |
| Oracle-IM scan CUs optimized read                                                                                                                             |             |
| Oracle-IM scan CUs predicates applied                                                                                                                         |             |
| Oracle-IM scan CUs predicates optimized                                                                                                                       |             |
| Oracle-IM scan CUs predicates received                                                                                                                        |             |
| Oracle-IM scan CUs pruned                                                                                                                                     |             |
| Oracle-IM scan CUs rollback                                                                                                                                   |             |
| Oracle-IM scan CUs split pieces                                                                                                                               |             |
| Oracle-IM scan CUs undo records applied                                                                                                                       |             |
| Oracle-IM scan fetches journal                                                                                                                                |             |
| Oracle-IM scan found invalid smu                                                                                                                              |             |
| Oracle-IM scan invalid all blocks                                                                                                                             |             |
| Oracle-IM scan journal                                                                                                                                        |             |
| Oracle-IM scan journal cleanout                                                                                                                               |             |
| Oracle-IM scan journal no cleanout                                                                                                                            |             |
| Oracle-IM scan rows                                                                                                                                           |             |
| Oracle-IM scan rows cache                                                                                                                                     |             |
| Oracle-IM scan rows discontinuous                                                                                                                             |             |
| Oracle-IM scan rows excluded                                                                                                                                  |             |
| Oracle-IM scan rows journal                                                                                                                                   |             |
| Oracle-IM scan rows journal total                                                                                                                             |             |
| Oracle-IM scan rows optimized                                                                                                                                 |             |
| Oracle-IM scan rows projected                                                                                                                                 |             |
| Oracle-IM scan rows range excluded                                                                                                                            |             |
| Oracle-IM scan rows valid                                                                                                                                     |             |
| Oracle-IM scan segments disk                                                                                                                                  |             |
| Oracle-IM scan segments minmax eligible                                                                                                                       |             |
| Oracle-IM space CU bytes allocated                                                                                                                            |             |
| Oracle-IM space CU bytes freed                                                                                                                                |             |
| Oracle-IM space CU creations committed                                                                                                                        |             |
| Oracle-IM space CU creations initiated                                                                                                                        |             |
| Oracle-IM space CU extents allocated                                                                                                                          |             |
| Oracle-IM space CU extents freed                                                                                                                              |             |
| Oracle-IM space private journal bytes allocated                                                                                                               |             |
| Oracle-IM space private journal bytes freed                                                                                                                   |             |
| Oracle-IM space private journal extents allocated                                                                                                             |             |
| Oracle-IM space private journal extents freed                                                                                                                 |             |
| Oracle-IM space private journal segments allocated                                                                                                            |             |
| Oracle-IM space private journal segments freed                                                                                                                |             |
| Oracle-IM space segments allocated                                                                                                                            |             |
| Oracle-IM space segments freed                                                                                                                                |             |
| Oracle-IM space shared journal bytes allocated                                                                                                                |             |
| Oracle-IM space shared journal bytes freed                                                                                                                    |             |
| Oracle-IM space shared journal extents allocated                                                                                                              |             |
| Oracle-IM space shared journal extents freed                                                                                                                  |             |
| Oracle-IM space shared journal segments allocated                                                                                                             |             |
| Oracle-IM space shared journal segments freed                                                                                                                 |             |
| Oracle-IM space SMU bytes allocated                                                                                                                           |             |
| Oracle-IM space SMU bytes freed                                                                                                                               |             |
| Oracle-IM space SMU creations committed                                                                                                                       |             |
| Oracle-IM space SMU creations initiated                                                                                                                       |             |
| Oracle-IM space SMU extents allocated                                                                                                                         |             |
| Oracle-IM space SMU extents freed                                                                                                                             |             |
| Oracle-IM transactions                                                                                                                                        |             |
| Oracle-IM transactions blocks invalidated                                                                                                                     |             |
| Oracle-IM transactions CU cleanout                                                                                                                            |             |
| Oracle-IM transactions CUs invalid                                                                                                                            |             |
| Oracle-IM transactions downgrade mode                                                                                                                         |             |
| Oracle-IM transactions found invalid CU                                                                                                                       |             |
| Oracle-IM transactions journal cleanout                                                                                                                       |             |
| Oracle-IM transactions rows invalidated                                                                                                                       |             |
| Oracle-IM transactions rows journaled                                                                                                                         |             |
| Oracle-Immediate (CR) block cleanout applications                                                                                                             |             |
| Oracle-Immediate (CURRENT) block cleanout applications                                                                                                        |             |
| Oracle-Immediate CR cleanouts (index blocks)                                                                                                                  |             |
| Oracle-IMU bind flushes                                                                                                                                       |             |
| Oracle-IMU commits                                                                                                                                            |             |
| Oracle-IMU contention                                                                                                                                         |             |
| Oracle-IMU CR rollbacks                                                                                                                                       |             |
| Oracle-IMU Flushes                                                                                                                                            |             |
| Oracle-IMU ktichg flush                                                                                                                                       |             |
| Oracle-IMU mbu flush                                                                                                                                          |             |
| Oracle-IMU pool not allocated                                                                                                                                 |             |
| Oracle-IMU recursive-transaction flush                                                                                                                        |             |
| Oracle-IMU Redo allocation size                                                                                                                               |             |
| Oracle-IMU undo allocation size                                                                                                                               |             |
| Oracle-IMU undo retention flush                                                                                                                               |             |
| Oracle-IMU- failed to get a private strand                                                                                                                    |             |
| Oracle-In call idle wait time                                                                                                                                 |             |
| Oracle-Index cmph gencu, uncomp sentinals                                                                                                                     |             |
| Oracle-Index cmph ld, CU fit                                                                                                                                  |             |
| Oracle-Index cmph ld, CU fit, add rows                                                                                                                        |             |
| Oracle-Index cmph ld, CU negative comp                                                                                                                        |             |
| Oracle-Index cmph ld, CU over-est                                                                                                                             |             |
| Oracle-Index cmph ld, CU under-est                                                                                                                            |             |
| Oracle-Index cmph ld, lf blks flushed                                                                                                                         |             |
| Oracle-Index cmph ld, lf blks w/ und CU                                                                                                                       |             |
| Oracle-Index cmph ld, lf blks w/o CU                                                                                                                          |             |
| Oracle-Index cmph ld, lf blks w/o unc r                                                                                                                       |             |
| Oracle-Index cmph ld, retry in over-est                                                                                                                       |             |
| Oracle-Index cmph ld, rows compressed                                                                                                                         |             |
| Oracle-Index cmph ld, rows uncompressed                                                                                                                       |             |
| Oracle-Index cmph sp, leaf block 90_10 splits failed                                                                                                          |             |
| Oracle-Index cmph sp, leaf block splits avoided                                                                                                               |             |
| Oracle-Index cmpl co, prefix mismatch                                                                                                                         |             |
| Oracle-Index cmpl ro, blocks not compressed                                                                                                                   |             |
| Oracle-Index cmpl ro, prefix change at block                                                                                                                  |             |
| Oracle-Index cmpl ro, prefix no change at block                                                                                                               |             |
| Oracle-Index cmpl ro, reorg avoid load new block                                                                                                              |             |
| Oracle-Index cmpl ro, reorg avoid split                                                                                                                       |             |
| Oracle-Index crx upgrade (found)                                                                                                                              |             |
| Oracle-Index crx upgrade (positioned)                                                                                                                         |             |
| Oracle-Index crx upgrade (prefetch)                                                                                                                           |             |
| Oracle-Index fast full scans (direct read)                                                                                                                    |             |
| Oracle-Index fast full scans (full)                                                                                                                           |             |
| Oracle-Index fast full scans (rowid ranges)                                                                                                                   |             |
| Oracle-Index fetch by key                                                                                                                                     |             |
| Oracle-Index reclamation/extension switch                                                                                                                     |             |
| Oracle-Index scans kdiixs1                                                                                                                                    |             |
| Oracle-Java call heap collected bytes                                                                                                                         | Bytes       |
| Oracle-Java call heap collected count                                                                                                                         |             |
| Oracle-Java call heap gc count                                                                                                                                |             |
| Oracle-Java call heap live object count                                                                                                                       |             |
| Oracle-Java call heap live object count max                                                                                                                   |             |
| Oracle-Java call heap live size                                                                                                                               |             |
| Oracle-Java call heap live size max                                                                                                                           |             |
| Oracle-Java call heap object count                                                                                                                            |             |
| Oracle-Java call heap object count max                                                                                                                        |             |
| Oracle-Java call heap total size                                                                                                                              |             |
| Oracle-Java call heap total size max                                                                                                                          |             |
| Oracle-Java call heap used size                                                                                                                               |             |
| Oracle-Java call heap used size max                                                                                                                           |             |
| Oracle-Java session heap collected bytes                                                                                                                      |             |
| Oracle-Java session heap collected count                                                                                                                      |             |
| Oracle-Java session heap gc count                                                                                                                             |             |
| Oracle-Java session heap live object count                                                                                                                    |             |
| Oracle-Java session heap live object count max                                                                                                                |             |
| Oracle-Java session heap live size                                                                                                                            |             |
| Oracle-Java session heap live size max                                                                                                                        |             |
| Oracle-Java session heap object count                                                                                                                         |             |
| Oracle-Java session heap object count max                                                                                                                     |             |
| Oracle-Java session heap used size                                                                                                                            |             |
| Oracle-Java session heap used size max                                                                                                                        |             |
| Oracle-ka grants received                                                                                                                                     |             |
| Oracle-ka local message waits                                                                                                                                 |             |
| Oracle-ka local messages received                                                                                                                             |             |
| Oracle-ka messages sent                                                                                                                                       |             |
| Oracle-ka wait calls attempted                                                                                                                                |             |
| Oracle-ka wait calls for invalid kga                                                                                                                          |             |
| Oracle-ka wait calls other                                                                                                                                    |             |
| Oracle-ka wait calls suppressed                                                                                                                               |             |
| Oracle-ka wait due to timeout                                                                                                                                 |             |
| Oracle-ka wait due to trigger                                                                                                                                 |             |
| Oracle-KTFB alloc myinst                                                                                                                                      |             |
| Oracle-KTFB alloc req                                                                                                                                         |             |
| Oracle-KTFB alloc search FFB                                                                                                                                  |             |
| Oracle-KTFB alloc space (block)                                                                                                                               |             |
| Oracle-KTFB alloc steal                                                                                                                                       |             |
| Oracle-KTFB alloc time (ms)                                                                                                                                   |             |
| Oracle-KTFB apply req                                                                                                                                         |             |
| Oracle-KTFB apply time (ms)                                                                                                                                   |             |
| Oracle-KTFB commit req                                                                                                                                        |             |
| Oracle-KTFB commit time (ms)                                                                                                                                  |             |
| Oracle-KTFB free req                                                                                                                                          |             |
| Oracle-KTFB free space (block)                                                                                                                                |             |
| Oracle-KTFB free time (ms)                                                                                                                                    |             |
| Oracle-Large tracked transactions                                                                                                                             |             |
| Oracle-Leaf node 90-10 splits                                                                                                                                 |             |
| Oracle-Leaf node splits                                                                                                                                       |             |
| Oracle-Lob reads                                                                                                                                              |             |
| Oracle-LOB table id lookup cache misses                                                                                                                       |             |
| Oracle-Lob writes                                                                                                                                             |             |
| Oracle-Lob writes unaligned                                                                                                                                   |             |
| Oracle-Local undo segment hints helped                                                                                                                        |             |
| Oracle-Local undo segment hints were stale                                                                                                                    |             |
| Oracle-Logical read bytes from cache                                                                                                                          |             |
| Oracle-Long (or conversely short) tables can be defined as tables that do not meet the short table criteria as described in table scans (short tables) below. |             |
| Oracle-Long (or conversely short) tables can be defined by optimizer hints coming down into the row source access layer of Oracle                             |             |
| Oracle-Max cf enq hold time                                                                                                                                   |             |
| Oracle-Messages received                                                                                                                                      |             |
| Oracle-Messages sent                                                                                                                                          |             |
| Oracle-Min active SCN optimization applied on CR                                                                                                              |             |
| Oracle-Misses for writing mapping                                                                                                                             |             |
| Oracle-No buffer to keep pinned count                                                                                                                         |             |
| Oracle-No work - consistent read gets                                                                                                                         |             |
| Oracle-No. of Decrypt ops                                                                                                                                     |             |
| Oracle-No. of Encrypt ops                                                                                                                                     |             |
| Oracle-No. of Principal Cache Misses                                                                                                                          |             |
| Oracle-No. of Principal Invalidations                                                                                                                         |             |
| Oracle-No. of Roles Enabled or Disabled                                                                                                                       |             |
| Oracle-No. of User Callbacks Executed                                                                                                                         |             |
| Oracle-No. of XS Sessions Attached                                                                                                                            |             |
| Oracle-No. of XS Sessions Created                                                                                                                             |             |
| Oracle-Non-idle wait count                                                                                                                                    |             |
| Oracle-Non-idle wait time                                                                                                                                     |             |
| Oracle-Number of bytes wasted because redo blocks needed to be written before they are completely full                                                        |             |
| Oracle-Number of FORMAT_PRESERVING redactions                                                                                                                 |             |
| Oracle-Number of FULL redactions                                                                                                                              |             |
| Oracle-Number of map misses                                                                                                                                   |             |
| Oracle-Number of map operations                                                                                                                               |             |
| Oracle-Number of messages received requesting DBWR to make some more free buffers for the LRU                                                                 |             |
| Oracle-Number of NONE redactions                                                                                                                              |             |
| Oracle-Number of PARTIAL redactions                                                                                                                           |             |
| Oracle-Number of RANDOM redactions                                                                                                                            |             |
| Oracle-Number of read IOs issued                                                                                                                              |             |
| Oracle-Number of REGEXP redactions                                                                                                                            |             |
| Oracle-Number of times the DBWR was asked to scan the cache and write all blocks marked for a checkpoint                                                      |             |
| Oracle-OLAP Aggregate Function Calc                                                                                                                           |             |
| Oracle-OLAP Aggregate Function Logical NA                                                                                                                     |             |
| Oracle-OLAP Aggregate Function Precompute                                                                                                                     |             |
| Oracle-OLAP Custom Member Limit                                                                                                                               |             |
| Oracle-OLAP Engine Calls                                                                                                                                      |             |
| Oracle-OLAP Fast Limit                                                                                                                                        |             |
| Oracle-OLAP Full Limit                                                                                                                                        |             |
| Oracle-OLAP GID Limit                                                                                                                                         |             |
| Oracle-OLAP Import Rows Loaded                                                                                                                                |             |
| Oracle-OLAP Import Rows Pushed                                                                                                                                |             |
| Oracle-OLAP INHIER Limit                                                                                                                                      |             |
| Oracle-OLAP Limit Time                                                                                                                                        |             |
| Oracle-OLAP Paging Manager Cache Changed Page                                                                                                                 |             |
| Oracle-OLAP Paging Manager Cache Hit                                                                                                                          |             |
| Oracle-OLAP Paging Manager Cache Miss                                                                                                                         |             |
| Oracle-OLAP Paging Manager Cache Write                                                                                                                        |             |
| Oracle-OLAP Paging Manager New Page                                                                                                                           |             |
| Oracle-OLAP Paging Manager Pool Size                                                                                                                          |             |
| Oracle-OLAP Perm LOB Read                                                                                                                                     |             |
| Oracle-OLAP Row Id Limit                                                                                                                                      |             |
| Oracle-OLAP Row Load Time                                                                                                                                     |             |
| Oracle-OLAP Row Source Rows Processed                                                                                                                         |             |
| Oracle-OLAP Session Cache Hit                                                                                                                                 |             |
| Oracle-OLAP Session Cache Miss                                                                                                                                |             |
| Oracle-OLAP Temp Segment Read                                                                                                                                 |             |
| Oracle-OLAP Temp Segments                                                                                                                                     |             |
| Oracle-OLAP Unique Key Attribute Limit                                                                                                                        |             |
| Oracle-Oracle allocates resources (Call State Objects) to keep track of relevant user call data structures every time you log in, parse, or execute.          |             |
| Oracle-Oracle maintains tables used for internal processing                                                                                                   |             |
| Oracle-OS Block input operations                                                                                                                              |             |
| Oracle-OS Block output operations                                                                                                                             |             |
| Oracle-OS CPU Qt wait time                                                                                                                                    |             |
| Oracle-OS Integral shared text size                                                                                                                           |             |
| Oracle-OS Integral unshared data size                                                                                                                         |             |
| Oracle-OS Integral unshared stack size                                                                                                                        |             |
| Oracle-OS Involuntary context switches                                                                                                                        |             |
| Oracle-OS Maximum resident set size                                                                                                                           |             |
| Oracle-OS Page faults                                                                                                                                         |             |
| Oracle-OS Page reclaims                                                                                                                                       |             |
| Oracle-OS Signals received                                                                                                                                    |             |
| Oracle-OS Socket messages received                                                                                                                            |             |
| Oracle-OS Socket messages sent                                                                                                                                |             |
| Oracle-OS Swaps                                                                                                                                               |             |
| Oracle-OS System time used                                                                                                                                    |             |
| Oracle-OS User time used                                                                                                                                      |             |
| Oracle-OS Voluntary context switches                                                                                                                          |             |
| Oracle-OTC commit optimization attempts                                                                                                                       |             |
| Oracle-OTC commit optimization failure - setup                                                                                                                |             |
| Oracle-OTC commit optimization hits                                                                                                                           |             |
| Oracle-Parallel operations downgraded 1 to 25 pct                                                                                                             |             |
| Oracle-Parallel operations downgraded 25 to 50 pct                                                                                                            |             |
| Oracle-Parallel operations downgraded 50 to 75 pct                                                                                                            |             |
| Oracle-Parallel operations downgraded 75 to 99 pct                                                                                                            |             |
| Oracle-Parallel operations downgraded to serial                                                                                                               |             |
| Oracle-Parallel operations not downgraded                                                                                                                     |             |
| Oracle-Parse count (describe)                                                                                                                                 |             |
| Oracle-Parse count (failures)                                                                                                                                 |             |
| Oracle-Physical read bytes                                                                                                                                    |             |
| Oracle-Physical read flash cache hits                                                                                                                         |             |
| Oracle-Physical read IO requests                                                                                                                              |             |
| Oracle-Physical read partial requests                                                                                                                         |             |
| Oracle-Physical read requests optimized                                                                                                                       |             |
| Oracle-Physical read snap bytes base                                                                                                                          | bytes       |
| Oracle-Physical read snap bytes copy                                                                                                                          | bytes       |
| Oracle-Physical read snap IO requests base                                                                                                                    |             |
| Oracle-Physical read snap IO requests copy                                                                                                                    |             |
| Oracle-Physical read snap IO requests no data                                                                                                                 |             |
| Oracle-Physical read total bytes                                                                                                                              | bytes       |
| Oracle-Physical read total IO requests                                                                                                                        |             |
| Oracle-Physical read total multi block requests                                                                                                               |             |
| Oracle-Physical reads cache                                                                                                                                   |             |
| Oracle-Physical reads cache for securefile flashback block new                                                                                                |             |
| Oracle-Physical reads cache prefetch                                                                                                                          |             |
| Oracle-Physical reads direct                                                                                                                                  |             |
| Oracle-Physical reads direct (lob)                                                                                                                            |             |
| Oracle-Physical reads direct for securefile flashback block new                                                                                               |             |
| Oracle-Physical reads direct temporary tablespace                                                                                                             |             |
| Oracle-Physical reads for flashback new                                                                                                                       |             |
| Oracle-Physical reads prefetch warmup                                                                                                                         |             |
| Oracle-Physical reads retry corrupt                                                                                                                           |             |
| Oracle-Physical write bytes                                                                                                                                   |             |
| Oracle-Physical write IO requests                                                                                                                             |             |
| Oracle-Physical write requests optimized                                                                                                                      |             |
| Oracle-Physical write snap IO requests new allocations                                                                                                        |             |
| Oracle-Physical write total bytes                                                                                                                             | bytes       |
| Oracle-Physical write total IO requests                                                                                                                       |             |
| Oracle-Physical write total multi block requests                                                                                                              |             |
| Oracle-Physical writes direct                                                                                                                                 |             |
| Oracle-Physical writes direct (lob)                                                                                                                           |             |
| Oracle-Physical writes direct temporary tablespace                                                                                                            |             |
| Oracle-Physical writes from cache                                                                                                                             |             |
| Oracle-Physical writes non checkpoint                                                                                                                         |             |
| Oracle-Pinned buffers inspected                                                                                                                               |             |
| Oracle-Pinned cursors current                                                                                                                                 |             |
| Oracle-Prefetch clients - 16k                                                                                                                                 |             |
| Oracle-Prefetch clients - 2k                                                                                                                                  |             |
| Oracle-Prefetch clients - 32k                                                                                                                                 |             |
| Oracle-Prefetch clients - 4k                                                                                                                                  |             |
| Oracle-Prefetch clients - 8k                                                                                                                                  |             |
| Oracle-Prefetch clients - default                                                                                                                             |             |
| Oracle-Prefetch clients - keep                                                                                                                                |             |
| Oracle-Prefetch clients - recycle                                                                                                                             |             |
| Oracle-Prefetch warmup blocks aged out before use                                                                                                             |             |
| Oracle-Prefetch warmup blocks flushed out before use                                                                                                          |             |
| Oracle-Prefetched blocks aged out before use                                                                                                                  |             |
| Oracle-Process last non-idle time                                                                                                                             |             |
| Oracle-Queue flush                                                                                                                                            |             |
| Oracle-Queue ocp pages                                                                                                                                        |             |
| Oracle-Queue position update                                                                                                                                  |             |
| Oracle-Queue qno pages                                                                                                                                        |             |
| Oracle-Queue single row                                                                                                                                       |             |
| Oracle-Queue splits                                                                                                                                           |             |
| Oracle-Queue update without cp update                                                                                                                         |             |
| Oracle-Read-only violation count                                                                                                                              |             |
| Oracle-Recieve buffer unavailable                                                                                                                             |             |
| Oracle-Recovery block gets from cache                                                                                                                         |             |
| Oracle-Recovery blocks read for lost write detection                                                                                                          |             |
| Oracle-Recovery blocks skipped lost write checks                                                                                                              |             |
| Oracle-Recovery marker                                                                                                                                        |             |
| Oracle-Recursive aborts on index block reclamation                                                                                                            |             |
| Oracle-Recursive system API invocations                                                                                                                       |             |
| Oracle-Redo blocks checksummed by FG (exclusive)                                                                                                              |             |
| Oracle-Redo blocks checksummed by LGWR                                                                                                                        |             |
| Oracle-Redo blocks read for recovery                                                                                                                          |             |
| Oracle-Redo blocks written                                                                                                                                    |             |
| Oracle-Redo blocks written (group 0)                                                                                                                          |             |
| Oracle-Redo blocks written (group 1)                                                                                                                          |             |
| Oracle-Redo blocks written (group 2)                                                                                                                          |             |
| Oracle-Redo blocks written (group 3)                                                                                                                          |             |
| Oracle-Redo blocks written (group 4)                                                                                                                          |             |
| Oracle-Redo blocks written (group 5)                                                                                                                          |             |
| Oracle-Redo blocks written (group 6)                                                                                                                          |             |
| Oracle-Redo blocks written (group 7)                                                                                                                          |             |
| Oracle-Redo buffer allocation retries                                                                                                                         |             |
| Oracle-Redo entries for lost write detection                                                                                                                  |             |
| Oracle-Redo k-bytes read for recovery                                                                                                                         |             |
| Oracle-Redo k-bytes read for terminal recovery                                                                                                                |             |
| Oracle-Redo KB read                                                                                                                                           |             |
| Oracle-Redo KB read (memory)                                                                                                                                  |             |
| Oracle-Redo KB read (memory) for transport                                                                                                                    |             |
| Oracle-Redo KB read for transport                                                                                                                             |             |
| Oracle-Redo non-durable records skipped                                                                                                                       |             |
| Oracle-Redo size for direct writes                                                                                                                            |             |
| Oracle-Redo size for lost write detection                                                                                                                     |             |
| Oracle-Redo subscn max counts                                                                                                                                 |             |
| Oracle-Redo synch long waits                                                                                                                                  |             |
| Oracle-Redo synch poll writes                                                                                                                                 |             |
| Oracle-Redo synch polls                                                                                                                                       |             |
| Oracle-Redo synch time (usec)                                                                                                                                 |             |
| Oracle-Redo synch time overhead (usec)                                                                                                                        |             |
| Oracle-Redo synch time overhead count (  2ms)                                                                                                                 |             |
| Oracle-Redo synch time overhead count (  8ms)                                                                                                                 |             |
| Oracle-Redo synch time overhead count ( 32ms)                                                                                                                 |             |
| Oracle-Redo synch time overhead count (128ms)                                                                                                                 |             |
| Oracle-Redo synch time overhead count (inf)                                                                                                                   |             |
| Oracle-Redo synch writes                                                                                                                                      |             |
| Oracle-Redo write broadcast ack count                                                                                                                         |             |
| Oracle-Redo write broadcast ack time                                                                                                                          |             |
| Oracle-Redo write broadcast lgwr post count                                                                                                                   |             |
| Oracle-Redo write finish time                                                                                                                                 |             |
| Oracle-Redo write gather time                                                                                                                                 |             |
| Oracle-Redo write info find                                                                                                                                   |             |
| Oracle-Redo write info find fail                                                                                                                              |             |
| Oracle-Redo write issue time                                                                                                                                  |             |
| Oracle-Redo write schedule time                                                                                                                               |             |
| Oracle-Redo write size count (   4KB)                                                                                                                         |             |
| Oracle-Redo write size count (   8KB)                                                                                                                         |             |
| Oracle-Redo write size count (  16KB)                                                                                                                         |             |
| Oracle-Redo write size count (  32KB)                                                                                                                         |             |
| Oracle-Redo write size count (  64KB)                                                                                                                         |             |
| Oracle-Redo write size count ( 128KB)                                                                                                                         |             |
| Oracle-Redo write size count ( 256KB)                                                                                                                         |             |
| Oracle-Redo write size count ( 512KB)                                                                                                                         |             |
| Oracle-Redo write size count (1024KB)                                                                                                                         |             |
| Oracle-Redo write size count (inf)                                                                                                                            |             |
| Oracle-Redo write time (usec)                                                                                                                                 |             |
| Oracle-Redo write total time                                                                                                                                  |             |
| Oracle-Redo write worker delay (usec)                                                                                                                         |             |
| Oracle-Redo writes adaptive all                                                                                                                               |             |
| Oracle-Redo writes adaptive worker                                                                                                                            |             |
| Oracle-Remote Oradebug requests                                                                                                                               |             |
| Oracle-Requests to/from client                                                                                                                                |             |
| Oracle-Rollback changes - undo records applied                                                                                                                |             |
| Oracle-Rollbacks only - consistent read gets                                                                                                                  |             |
| Oracle-Root node splits                                                                                                                                       |             |
| Oracle-RowCR - resume                                                                                                                                         |             |
| Oracle-RowCR - row contention                                                                                                                                 |             |
| Oracle-RowCR attempts                                                                                                                                         |             |
| Oracle-RowCR hits                                                                                                                                             |             |
| Oracle-Rows fetched via callback                                                                                                                              |             |
| Oracle-Sage send block by cell                                                                                                                                |             |
| Oracle-Scheduler wait time                                                                                                                                    |             |
| Oracle-SCN increments due to another database                                                                                                                 |             |
| Oracle-Securefile add dedupd lob to set                                                                                                                       |             |
| Oracle-Securefile allocation bytes                                                                                                                            |             |
| Oracle-Securefile allocation chunks                                                                                                                           |             |
| Oracle-Securefile bytes cleartext                                                                                                                             |             |
| Oracle-Securefile bytes deduplicated                                                                                                                          |             |
| Oracle-Securefile bytes encrypted                                                                                                                             |             |
| Oracle-Securefile bytes non-transformed                                                                                                                       |             |
| Oracle-Securefile compressed bytes                                                                                                                            |             |
| Oracle-Securefile create dedup set                                                                                                                            |             |
| Oracle-Securefile dedup callback oper final                                                                                                                   |             |
| Oracle-Securefile dedup fits inline                                                                                                                           |             |
| Oracle-Securefile dedup flush too low                                                                                                                         |             |
| Oracle-Securefile dedup hash collision                                                                                                                        |             |
| Oracle-Securefile dedup prefix hash match                                                                                                                     |             |
| Oracle-Securefile dedup wapp cache miss                                                                                                                       |             |
| Oracle-Securefile destroy dedup set                                                                                                                           |             |
| Oracle-Securefile direct read bytes                                                                                                                           |             |
| Oracle-Securefile direct read ops                                                                                                                             |             |
| Oracle-Securefile direct write bytes                                                                                                                          |             |
| Oracle-Securefile direct write ops                                                                                                                            |             |
| Oracle-Securefile inode ioreap time                                                                                                                           |             |
| Oracle-Securefile inode read time                                                                                                                             |             |
| Oracle-Securefile inode write time                                                                                                                            |             |
| Oracle-Securefile number of flushes                                                                                                                           |             |
| Oracle-Securefile number of non-transformed flushes                                                                                                           |             |
| Oracle-Securefile reject deduplication                                                                                                                        |             |
| Oracle-Securefile rmv from dedup set                                                                                                                          |             |
| Oracle-Securefile uncompressed bytes                                                                                                                          |             |
| Oracle-SecureFiles Copy from DBFS Link                                                                                                                        |             |
| Oracle-SecureFiles DBFS Link Operations                                                                                                                       |             |
| Oracle-SecureFiles DBFS Link Overwrites                                                                                                                       |             |
| Oracle-SecureFiles DBFS Link streaming reads                                                                                                                  |             |
| Oracle-SecureFiles Get DBFS Link Reference                                                                                                                    |             |
| Oracle-SecureFiles Implicit Copy from DBFS Link                                                                                                               |             |
| Oracle-SecureFiles Move to DBFS Link                                                                                                                          |             |
| Oracle-SecureFiles Put DBFS Link Reference                                                                                                                    |             |
| Oracle-Segment cfs allocations                                                                                                                                |             |
| Oracle-Segment chunks allocation from disepnser                                                                                                               |             |
| Oracle-Segment dispenser allocations                                                                                                                          |             |
| Oracle-Segment dispenser load empty                                                                                                                           |             |
| Oracle-Segment dispenser load tasks                                                                                                                           |             |
| Oracle-Segment prealloc bytes                                                                                                                                 |             |
| Oracle-Segment prealloc ops                                                                                                                                   |             |
| Oracle-Segment prealloc tasks                                                                                                                                 |             |
| Oracle-Segment prealloc time (ms)                                                                                                                             |             |
| Oracle-Segment prealloc ufs2cfs bytes                                                                                                                         |             |
| Oracle-Segment total chunk allocation                                                                                                                         |             |
| Oracle-Session logical reads                                                                                                                                  |             |
| Oracle-Session logical reads - IM                                                                                                                             |             |
| Oracle-Session logical reads in local numa group                                                                                                              |             |
| Oracle-Session logical reads in remote numa group                                                                                                             |             |
| Oracle-Shared hash latch upgrades - no wait                                                                                                                   |             |
| Oracle-Shared hash latch upgrades - wait                                                                                                                      |             |
| Oracle-Shared io pool buffer get failure                                                                                                                      |             |
| Oracle-Shared io pool buffer get success                                                                                                                      |             |
| Oracle-Slave propagated tracked transactions                                                                                                                  |             |
| Oracle-SMON posted for dropping temp segment                                                                                                                  |             |
| Oracle-SMON posted for instance recovery                                                                                                                      |             |
| Oracle-SMON posted for txn recovery for other instances                                                                                                       |             |
| Oracle-SMON posted for undo segment recovery                                                                                                                  |             |
| Oracle-SMON posted for undo segment shrink                                                                                                                    |             |
| Oracle-Space was found by tune down                                                                                                                           |             |
| Oracle-Space was not found by tune down                                                                                                                       |             |
| Oracle-Sql area evicted                                                                                                                                       |             |
| Oracle-Sql area purged                                                                                                                                        |             |
| Oracle-Steps of tune down ret. in space pressure                                                                                                              |             |
| Oracle-Streaming No-Stall Reap                                                                                                                                |             |
| Oracle-Streaming Stall Reap                                                                                                                                   |             |
| Oracle-Switch current to new buffer                                                                                                                           |             |
| Oracle-Table scan disk IMC fallback                                                                                                                           |             |
| Oracle-Table scan disk non-IMC rows gotten                                                                                                                    |             |
| Oracle-Table scans (IM)                                                                                                                                       |             |
| Oracle-TBS Extension: bytes extended                                                                                                                          |             |
| Oracle-TBS Extension: files extended                                                                                                                          |             |
| Oracle-TBS Extension: tasks created                                                                                                                           |             |
| Oracle-TBS Extension: tasks executed                                                                                                                          |             |
| Oracle-Temp space allocated (bytes)                                                                                                                           |             |
| Oracle-The active log file is full and Oracle is waiting for disk space to be allocated for the redo log entries                                              |             |
| Oracle-The connect time for the session                                                                                                                       | sec         |
| Oracle-The count of the number of hits in the session cursor cache                                                                                            |             |
| Oracle-The count of the number of times a reusable buffer or a free buffer was requested to create or load a block                                            |             |
| Oracle-The current scan depth (number of buffers examined by DBWR) is added to this statistic every time DBWR scans the LRU for dirty buffers                 |             |
| Oracle-The DBWR didn't find any dirty buffers for an object that was flushed from the cache                                                                   |             |
| Oracle-The elapsed time for redo write for changes made to CURRENT blocks                                                                                     |             |
| Oracle-The elapsed time need by LWGR to obtain and release each copy latch                                                                                    |             |
| Oracle-The elapsed time of all redo sync writes calls                                                                                                         |             |
| Oracle-The elapsed time of all synchronous global lock releases                                                                                               |             |
| Oracle-The elapsed time of I/O while doing recovery                                                                                                           |             |
