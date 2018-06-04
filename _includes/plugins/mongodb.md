## Metrics

### MongoDB 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB active check latency | s |  |
| MongoDB active check uptime | % |  |
| MongoDB estimate uptime | s |  |
| MongoDb oplog replication lag | s | Member |
| MongoDB process uptime | s |  |
| MongoDb total oplog replication lag | s |  |

### MongoDB / Asserts 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB message assertions | msg |  |
| MongoDB regular asserts | # |  |
| MongoDB rollovers asserts | # |  |
| MongoDB user asserts | # |  |
| MongoDB warning asserts | # |  |

### MongoDB / Background Flushing 

| Name | Unit | Dimensions |
|------|------|------------|
| Average MongoDB flush operation time | s |  |
| Last MongoDB flush operation time | s |  |

### MongoDB / Connections 

| Name | Unit | Dimensions |
|------|------|------------|
| Current MongoDB connections | conn |  |
| MongoDB created connections | conn |  |

### MongoDB / Cursors 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB cursors timed out | # |  |
| MongoDB pinned cursors | # |  |
| Total MongoDB open cursors | # |  |

### MongoDB / Durability 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB compression durability | % |  |

### MongoDB / Durability / Time 

| Name | Unit | Dimensions |
|------|------|------------|
| Preparing MongoDB log buffer time | s |  |
| Time spent remap private MongoDB view | s |  |
| Write to MongoDB data files | s |  |
| Write to MongoDB journal | s |  |

### MongoDB / Extra Info 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB heap usage | b |  |
| MongoDB page faults | faults |  |

### MongoDB / Global Lock 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB global lock time | s |  |
| MongoDB total time | s |  |

### MongoDB / Global Lock / Active Clients 

| Name | Unit | Dimensions |
|------|------|------------|
| Active MongoDB client connections | conn |  |
| Global lock active MongoDB clients readers | conn |  |
| Global lock active MongoDB clients writers | # |  |

### MongoDB / Global Lock / Current Queue 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB queue readers | # |  |
| MongoDB queue writers | # |  |
| Total MongoDB queue operations | # |  |

### MongoDB / Index Counters 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB index counters accesses | # |  |
| MongoDB index counters hits | # |  |
| MongoDB index counters misses | # |  |
| MongoDB index counters resets | # |  |
| MongoDB miss ratio | % |  |

### MongoDB / Locks 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB locked % | % |  |
| MongoDB locked read time | s |  |
| MongoDB locked write time | s |  |

### MongoDB / Locks / Oplog 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB locks Oplog accquire count read | # |  |
| MongoDB locks oplog acquire count write | # |  |
| MongoDB locks oplog acquire wait count read | # |  |
| MongoDB locks oplog acquire wait count write | # |  |
| MongoDB locks oplog deadlock count read | # |  |
| MongoDB locks oplog deadlock count write | # |  |
| MongoDB locks oplog time acquiring micros read | # |  |
| MongoDB locks oplog time acquiring micros write | # |  |

### MongoDB / Members 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB health |  | Member |
| MongoDB latency between primary member and other member | s | Member |
| MongoDB state |  | Member |
| MongoDB uptime | s | Member |

### MongoDB / Memory 

| Name | Unit | Dimensions |
|------|------|------------|
| Mapped with MongoDB journal memory | b |  |
| MongoDB resident memory | b |  |
| MongoDB target architecture |  |  |
| MongoDB virtual memory | b |  |

### MongoDB / Metrics / Commands 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB number of connections available from the mongos to the config servers, replica sets, and standalone mongod instances in the cluster | conn |  |
| MongoDB number of times dbHash command was executed | # |  |
| MongoDB number of times features command was executed | # |  |

### MongoDB / Metrics / Cursors 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB open cursors | # |  |
| MongoDB open cursors with noTimeout | # |  |
| MongoDB timed out cursors | # |  |

### MongoDB / Metrics / Document 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB documents deleted | docs |  |
| MongoDB documents inserted | docs |  |
| MongoDB documents returned | docs |  |
| Updated MongoDB documents | docs |  |

### MongoDB / Metrics / Last Error 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB LastError write time | s |  |
| MongoDB lastError writes number | writes |  |
| MongoDB write timeouts | # |  |

### MongoDB / Metrics / Operation 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB fastmod operations | # |  |
| Scan and order MongoDB queries | queries |  |

### MongoDB / Metrics / Query Executor 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB index items scanned | # |  |

### MongoDB / Metrics / Record 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB record moves | # |  |

### MongoDB / Metrics / Replication 

| Name | Unit | Dimensions |
|------|------|------------|
| Applying MongoDB operations time | s |  |
| MongoDB batches number | # |  |

### MongoDB / Metrics / Replication / Buffer 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB buffer max size | b |  |
| MongoDB buffer operations | # |  |
| MongoDB Oplog buffer size | b |  |

### MongoDB / Metrics / Replication / Network 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB getmore operations | # |  |
| MongoDB getmore operations time | s |  |
| MongoDB replication data read | b |  |

### MongoDB / Metrics / Replication / Oplog 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB repl oplog insert num |  |  |
| MongoDB repl oplog insert total | s |  |
| MongoDB replication oplog insert bytes | b |  |

### MongoDB / Metrics / Replication / Preload 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB documents loading time | s |  |
| Preload MongoDB replication indexes number | # |  |
| Time loading MongoDB indexes | s |  |

### MongoDB / Metrics / TTL 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB deleted documents | docs |  |
| MongoDB time to live passes | # |  |

### MongoDB / Network 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB network bytes out | b |  |
| Network requests number to MongoDB server | req |  |

### MongoDB / Operations Counters 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB insert operations | # |  |
| MongoDB query operations | # |  |
| MongoDB update operations | # |  |

### MongoDB / Operations Counters Replication 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB replicated insert operations | # |  |
| MongoDB replicated queries | queries |  |
| Replicated MongoDB delete operations | # |  |

### MongoDB / Record Stats 

| Name | Unit | Dimensions |
|------|------|------------|
| MongoDB access not in memory | # |  |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| MONGODB service state watcher | State watcher | status |

