---
layout: page
title: MongoDB plugin
description: Information on the metrics collected by the CoScale MongoDB plugin.
---

> MongoDB is an open-source, document database designed for ease of development and scaling. MongoDB stores data using a flexible document data model that is similar to JSON. Documents contain one or more fields, including arrays, binary data and sub-documents. Fields can vary from document to document. This flexibility allows development teams to evolve the data model rapidly as their application requirements change. When you need to lock down your data model, optional document validation enforces the rules you choose. Unlike most NoSQL databases, MongoDB provides comprehensive secondary indexes, including geospatial and text search, as well as extensive security and aggregation capabilities. 

More information on: [https://www.mongodb.com/](https://www.mongodb.com/)

## How it works

MongoDB provides statistics on lock timeouts, lock counts, insert/update/remove actions, total index size, etc through the MongoDB interface.

These statistics are gathered by default and no additional configuration is required. Just provide the connection details and the plugin is ready to go.

**The minimal supported version of MongoDB is 2.2.**

## Configuration

### Connection details

Our plugin requires the host, port, username and password to connect to the local MongoDB service.

### Active checks

This plugin can be configured to perform a command on your MongoDB. This active monitoring allows us to calculate the uptime of the service and the response time of the command.

A valid MongoDB command (eg. `{ "find": "my-collection", "filter": "my-document" }`) should be provided.

## Events

* Service state

## Metrics

| Metric name                                                                                                                                    | Metric unit |
|------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Total number of message assertions raised since the MongoDB server process started                                                             | msg     |
| Amount of time that any MongoDB database has held the global read lock                                                                         | s       |
| Amount of time that any MongoDB database has held the global write lock                                                                        | s       |
| Amount of time that the last MongoDB flush operation took to complete                                                                          | s       |
| Delete provides a counter of the total number of replicated delete operations since the mongod instance last started                           | #       |
| Maximum size of the MongoDB buffer                                                                                                             | b       |
| MongoDB health of member %s                                                                                                                    |         |
| MongoDB latency between primary member and %s member                                                                                           | s       |
| MongoDB locks Oplog accquire count read                                                                                                        | #       |
| MongoDB locks oplog acquire count write                                                                                                        | #       |
| MongoDB locks oplog acquire wait count read                                                                                                    | #       |
| MongoDB locks oplog acquire wait count write                                                                                                   | #       |
| MongoDB locks oplog deadlock count read                                                                                                        | #       |
| MongoDB locks oplog deadlock count write                                                                                                       | #       |
| MongoDB locks oplog time acquiring micros read                                                                                                 | #       |
| MongoDB locks oplog time acquiring micros write                                                                                                | #       |
| MongoDB number of connections available from the mongos to the config servers, replica sets, and standalone mongod instances in the cluster    | conn    |
| MongoDB number of times dbHash command was executed                                                                                            | #       |
| MongoDB number of times features command was executed                                                                                          | #       |
| MongoDb oplog replication lag on member %s                                                                                                     | s       |
| MongoDB repl oplog insert num                                                                                                                  |         |
| MongoDB repl oplog insert total                                                                                                                | s       |
| MongoDB replication oplog insert bytes                                                                                                         | b       |
| MongoDB state of member %s                                                                                                                     |         |
| MongoDb total oplog replication lag                                                                                                            | s       |
| MongoDB virtual memory                                                                                                                         | b       |
| Moves reports the total number of times documents move within the on-disk representation of the MongoDB data set                               | #       |
| Number of MongoDB operations that are currently queued and waiting for the read lock                                                           | #       |
| Number of MongoDB operations that are currently queued and waiting for the write lock                                                          | #       |
| Number of user asserts that have occurred since the last time the MongoDB server process started                                               | #       |
| Passes reports the number of times the background MongoDB process removes documents from collections with a ttl index                          | #       |
| Percent of time in global write lock                                                                                                           | %       |
| Readers contains a count of the active client connections to MongoDB performing read operations                                                | conn    |
| The amount of mapped memory including the memory used for journaling                                                                           | b       |
| The amount of network traffic, in bytes, sent from this MongoDB database                                                                       | b       |
| The amount of time spent preparing to write to the journal                                                                                     | s       |
| The amount of time spent remapping copy-on-write memory mapped MongoDB views                                                                   | s       |
| The compression ratio of the data written to the journal                                                                                       | %       |
| The current number of operations in the oplog buffer                                                                                           | #       |
| The current size of the contents of the oplog buffer                                                                                           | b       |
| The network request number field is a counter of the total number of distinct requests that the MongoDB server has received                    | req     |
| The number of “pinned” MongoDB open cursors                                                                                                    | #       |
| The number of active client connections to MongoDB performing write operations                                                                 | #       |
| The number of connections to the MongoDB database server from clients                                                                          | conn    |
| The number of cursors that MongoDB is maintaining for clients                                                                                  | #       |
| The number of cursors that MongoDB is maintaining for clients                                                                                  | #       |
| The number of MongoDB open cursors with the option DBQuery.Option.noTimeout set to prevent timeout after a period of inactivity                | #       |
| The number of MongoDB update operations that neither cause documents to grow nor require updates to the index                                  | #       |
| The number of regular assertions raised since the MongoDB server process started                                                               | #       |
| The number of seconds that the mongos or mongod process has been active                                                                        | s       |
| The number of seconds that the mongos or mongod process has been active on member %s                                                           | s       |
| The number of times mongod needed to access a memory page that was not resident in memory for all databases managed by this mongod instance    | #       |
| The number of times that an index has been accessed and mongod is able to return the index from memory                                         | #       |
| The number of times that an operation attempted to access an MongoDB index that was not in memory                                              | #       |
| The number of times that operations have accessed indexes                                                                                      | #       |
| The number of times that the rollover counters have rolled over since the last time the MongoDB server process started                         | #       |
| The number of warnings raised since the MongoDB server process started                                                                         | #       |
| The ratio of hits to misses                                                                                                                    | %       |
| The relationship between the number of flushes and the total amount of time that the MongoDB database has spent writing data to disk           | s       |
| The resets value reflects the number of times that the index counters have been reset since the MongoDB database last restarted                | #       |
| The time since the MongoDB database last started and creation of the globalLock                                                                | s       |
| The total amount of time in milliseconds that the mongod has spent performing getLastError operations with write concern                       | s       |
| The total amount of time required to collect data from MongoDB getmore operations                                                              | s       |
| The total amount of time the mongod has spent applying operations from the oplog                                                               | s       |
| The total number of cursors that have timed out since the MongoDB server process started                                                       | #       |
| The total number of documents updated                                                                                                          | docs    |
| The total number of index items scanned during queries and query-plan evaluation                                                               | #       |
| The total number of MongoDB update operations since the mongod instance last started                                                           | #       |
| The total number of page faults that require disk operations                                                                                   | faults  |
| The total number of queries that return sorted numbers that cannot perform the sort operation using an index                                   | queries |
| The total number of replicated insert operations since the mongod instance last started                                                        | #       |
| The total size of heap space used by the MongoDB database process                                                                              | b       |
| The uptime as calculated from MongoDB’s internal course-grained time keeping system                                                            | s       |
| The value is either 64 or 32, depending on which target architecture specified during the mongod compilation process                           |         |
| The value of resident is roughly equivalent to the amount of RAM currently used by the MongoDB database process                                | b       |
| The value of total provides a combined total of operations queued waiting for the lock                                                         | #       |
| The write to data files value provides the amount of time spent writing to data files after journaling                                         | s       |
| The write to journal value provides the amount of time spent actually writing to the journal                                                   | s       |
| Time since the MongoDB database last started, that the globalLock has been held                                                                | s       |
| Total amount of data read from the replication sync source                                                                                     | b       |
| Total amount of time spent loading documents as part of the pre-fetch stage of replication                                                     | s       |
| Total amount of time spent loading index entries as part of the pre-fetch stage of replication                                                 | s       |
| Total number of active client connections to the MongoDB database                                                                              | conn    |
| Total number of batches applied across all MongoDB databases                                                                                   | #       |
| Total number of cursors that have timed out since the MongoDB server process started                                                           | #       |
| Total number of documents deleted                                                                                                              | docs    |
| Total number of documents deleted from collections with a ttl index                                                                            | docs    |
| Total number of documents inserted                                                                                                             | docs    |
| Total number of documents returned by queries                                                                                                  | docs    |
| Total number of getLastError operations with a specified write concern                                                                         | writes  |
| Total number of incoming connections created to the MongoDB server                                                                             | conn    |
| Total number of index entries loaded by members before updating documents as part of the pre-fetch stage of replication                        | #       |
| Total number of insert operations since the mongod instance last started                                                                       | #       |
| Total number of MongoDB getmore operations, which are operations that request an additional set of operations from the replication sync source | #       |
| Total number of queries since the mongod instance last started                                                                                 | #       |
| Total number of replicated queries since the mongod instance last started                                                                      | queries |
| Write timeouts reports the number of times that write concern MongoDB operations have timed out                                                | #       |
