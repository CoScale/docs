## Metrics

### ZooKeeper 

| Name | Unit | Dimensions |
|------|------|------------|
| ZooKeeper active check latency | s |  |
| ZooKeeper active check uptime | % |  |
| ZooKeeper average request latency | ms | ServerID, Endpoint |
| ZooKeeper current tick count | # | ServerID, Endpoint |
| ZooKeeper election time taken | ms | ServerID, Endpoint |
| ZooKeeper init limit | ms | ServerID, Endpoint |
| ZooKeeper max session timeout | ms | ServerID, Endpoint |
| ZooKeeper maximum number of client connections | # | ServerID, Endpoint |
| ZooKeeper maximum request latency | ms | ServerID, Endpoint |
| ZooKeeper min session timeout | ms | ServerID, Endpoint |
| ZooKeeper minimum request latency | ms | ServerID, Endpoint |
| ZooKeeper node is leader | # | ServerID, Endpoint |
| ZooKeeper number of alive connections | # | ServerID, Endpoint |
| ZooKeeper outstanding requests | # | ServerID, Endpoint |
| ZooKeeper packets received | # | ServerID, Endpoint |
| ZooKeeper packets sent | # | ServerID, Endpoint |
| ZooKeeper pending revalidation count | # | ServerID, Endpoint |
| ZooKeeper quorum size | # | ServerID, Endpoint |
| ZooKeeper sync limit | ms | ServerID, Endpoint |
| ZooKeeper tick time | ms | ServerID, Endpoint |
| ZooKeeper Uptime | ms | ServerID, Endpoint |
| ZooKeeper watch count | # | ServerID, Endpoint |
| ZooKeeper znode count | # | ServerID, Endpoint |

### ZooKeeper / Buffer Pool 

| Name | Unit | Dimensions |
|------|------|------------|
| ZooKeeper BufferPool Count |  | Collector, ServerID, Endpoint |
| ZooKeeper BufferPool Memory Used | b | Collector, ServerID, Endpoint |

### ZooKeeper / Classes 

| Name | Unit | Dimensions |
|------|------|------------|
| ZooKeeper Loaded Class Count |  | ServerID, Endpoint |
| ZooKeeper Unloaded Class Count |  | ServerID, Endpoint |

### ZooKeeper / CPU 

| Name | Unit | Dimensions |
|------|------|------------|
| ZooKeeper Compilation Time | ms | ServerID, Endpoint |
| ZooKeeper Process CPU time | ms | ServerID, Endpoint |

### ZooKeeper / Garbage Collection 

| Name | Unit | Dimensions |
|------|------|------------|
| ZooKeeper Garbage Collections | # | Collector, ServerID, Endpoint |
| ZooKeeper GC Collection Time | ms | Collector, ServerID, Endpoint |

### ZooKeeper / Memory 

| Name | Unit | Dimensions |
|------|------|------------|
| ZooKeeper Memory Usage Committed | b | MemoryPool, ServerID, Endpoint |
| ZooKeeper Memory Usage Init | b | MemoryPool, ServerID, Endpoint |
| ZooKeeper Memory Usage Max | b | MemoryPool, ServerID, Endpoint |
| ZooKeeper Memory Usage Used | b | MemoryPool, ServerID, Endpoint |

### ZooKeeper / Open files 

| Name | Unit | Dimensions |
|------|------|------------|
| ZooKeeper Max File Descriptor Count |  | ServerID, Endpoint |
| ZooKeeper Open File Descriptor Count |  | ServerID, Endpoint |

### ZooKeeper / Threads 

| Name | Unit | Dimensions |
|------|------|------------|
| ZooKeeper Daemon Thread Count |  | ServerID, Endpoint |
| ZooKeeper Started Threads |  | ServerID, Endpoint |
| ZooKeeper Thread Count |  | ServerID, Endpoint |
| ZooKeeper Thread CPU Time | % | ServerID, Endpoint |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| ZOOKEEPER service state watcher | State watcher | status |

