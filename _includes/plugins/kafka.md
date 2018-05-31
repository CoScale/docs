## Metrics

### Kafka 

| Name | Unit | Dimensions |
|------|------|------------|
| Kafka active check latency | s |  |
| Kafka active check uptime | % |  |
| Kafka current lag |  | ConsumerGroup, Topic, Partition |
| Kafka current Offset of a Broker |  | Topic, Partition |
| Kafka Current offset of a ConsumerGroup |  | ConsumerGroup, Topic, Partition |
| Kafka leader Broker ID |  | Topic, Partition |
| Kafka number of Brokers in the Cluster | # |  |
| Kafka number of In-Sync Replicas |  | Topic, Partition |
| Kafka number of partitions per topic | # | Topic |
| Kafka number of Replicas |  | Topic, Partition |
| Kafka oldest Offset of a Broker |  | Topic, Partition |

### Kafka / JMX 

| Name | Unit | Dimensions |
|------|------|------------|
| Kafka active controller count |  |  |
| Kafka fetch consumer total time | s |  |
| Kafka fetch follower total time | s |  |
| Kafka isr expands per sec | expands/s |  |
| Kafka isr shrinks per sec | shrinks/s |  |
| Kafka leader election rate and time | s |  |
| Kafka offline partitions count |  |  |
| Kafka offset commit total time | s |  |
| Kafka offset fetch total time | s |  |
| Kafka offsets total time | s |  |
| Kafka produce total time | s |  |
| Kafka request queue size |  |  |
| Kafka unclean leader elections per sec | elections/s |  |
| Kafka under replicated partitions |  |  |

### Kafka / JMX / Consumer 

| Name | Unit | Dimensions |
|------|------|------------|
| Kafka average number of bytes consumed per second | b/s | Client Id, Topic |
| Kafka average number of bytes fetched per request | b | Client Id, Topic |
| Kafka average number of records consumed per second | records/s | Client Id, Topic |
| Kafka average number of records in each request | records | Client Id, Topic |
| Kafka average throttle time | s | Client Id |
| Kafka average time taken for a fetch request | s | Client Id |
| Kafka max lag for consumer | msg | Client Id |
| Kafka max time taken for a fetch request | s | Client Id |
| Kafka maximum number of bytes fetched per request | b | Client Id |
| Kafka maximum throttle time in ms | s | Client Id |
| Kafka number of fetch requests per second | records/s | Client Id |

### Kafka / JMX / Producer 

| Name | Unit | Dimensions |
|------|------|------------|
| Kafka average length of time for I/O per select call | s | Client Id |
| Kafka average number of incoming bytes received from all servers | b/s | Client Id |
| Kafka average number of outgoing bytes sent to all servers | b/s | Client Id |
| Kafka average number of requests sent per second | req/s | Client Id |
| Kafka average number of responses received | res/s | Client Id |
| Kafka average request latency | s | Client Id |
| Kafka connections closed in the window | conn/s | Client Id |
| Kafka current number of active connections | conn | Client Id |
| Kafka fraction of time the I/O thread spent doing I/O |  | Client Id |
| Kafka maximum request latency | s | Client Id |
| Kafka new connections established in the window | conn/s | Client Id |
| Kafka number of times the I/O layer checked for new I/O to perform | s | Client Id |
| Kafka the average compression rate of record batches for a topic |  | Client Id, Topic |
| Kafka the average length of time the I/O thread spent waiting for a socket ready for reads or writes | s | Client Id |
| Kafka the average number of bytes received per second from the broker | b/s | Client Id, Node |
| Kafka the average number of bytes sent per second for a topic | b/s | Client Id, Topic |
| Kafka the average number of bytes sent per second to the broker | b/s | Client Id, Node |
| Kafka the average number of records sent per second for a topic | records/s | Client Id, Topic |
| Kafka the average number of requests sent per second to the broker | req/s | Client Id, Node |
| Kafka the average number of responses received per second from the broker | res/s | Client Id, Node |
| Kafka the average per-second number of record sends that resulted in errors for a topic | #/s | Client Id, Topic |
| Kafka the average per-second number of retried record sends for a topic | #/s | Client Id, Topic |
| Kafka the average size of all requests in the window for a broker | b | Client Id, Node |
| Kafka the fraction of time the I/O thread spent waiting |  | Client Id |
| Kafka the maximum size of any request sent in the window for a broker | b | Client Id, Node |

### Kafka / JMX / Topic 

| Name | Unit | Dimensions |
|------|------|------------|
| Kafka bytes in per sec for topic | b/s | Topic |
| Kafka bytes out per sec for topic | b/s | Topic |
| Kafka messages in for topic | msg/s | Topic |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| KAFKA service state watcher | State watcher | status |

