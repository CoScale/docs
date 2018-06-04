## Metrics

### Redis 

| Name | Unit | Dimensions |
|------|------|------------|
| Flag indicating a Redis RDB save is on-going |  | Redis port |
| Last successful RedisDB save |  | Redis port |
| Number of changes since the last Redis dump | # | Redis port |
| Pub/sub Redis channels | # | Redis port |
| Pub/sub Redis patterns | # | Redis port |
| Redis active check latency | s | Redis port |
| Redis active check uptime | % | Redis port |
| Redis AOF base size | b | Redis port |
| Redis AOF buffer length | b | Redis port |
| Redis AOF current rewrite time sec | s | Redis port |
| Redis AOF current size | b | Redis port |
| Redis AOF delayed fsync | # | Redis port |
| Redis AOF enabled |  | Redis port |
| Redis AOF last rewrite time sec | s | Redis port |
| Redis AOF pending bio fsync | b | Redis port |
| Redis AOF pending rewrite |  | Redis port |
| Redis AOF rewrite buffer length | b | Redis port |
| Redis AOF rewrite in progress |  | Redis port |
| Redis AOF rewrite scheduled |  | Redis port |
| Redis blocked clients | # | Redis port |
| Redis client biggest input buffer | b | Redis port |
| Redis client longest output list |  | Redis port |
| Redis cluster enabled |  | Redis port |
| Redis connected clients | conn | Redis port |
| Redis connected slaves | # | Redis port |
| Redis instantaneous operations per sec | #/s | Redis port |
| Redis keys | # | Database, Redis port |
| Redis keys average time to live | s | Database, Redis port |
| Redis keys evicted | # | Redis port |
| Redis keys expired | # | Redis port |
| Redis keys with an expiration | # | Database, Redis port |
| Redis keyspace hits | hits/s | Redis port |
| Redis keyspace misses | misses/s | Redis port |
| Redis latest fork usec | s | Redis port |
| Redis loading eta seconds | s | Redis port |
| Redis loading flang | b | Redis port |
| Redis loading loaded bytes | b | Redis port |
| Redis loading start time |  | Redis port |
| Redis loading total bytes | b | Redis port |
| Redis master last io (seconds ago) | s | Redis port |
| Redis master replication offset |  | Redis port |
| Redis master sync in progress |  | Redis port |
| Redis memory fragmentation ratio | b | Redis port |
| Redis replication backlog active |  | Redis port |
| Redis replication backlog first byte offset |  | Redis port |
| Redis replication backlog histlen | b | Redis port |
| Redis replication backlog size | b | Redis port |
| Redis slave replication offset |  | Redis port |
| Redis uptime | s | Redis port |
| Redis used CPU system children | s | Redis port |
| Redis used CPU user | s | Redis port |
| Redis used CPU user children | s | Redis port |
| Redis used memory | b | Redis port |
| Redis used memory Lua | b | Redis port |
| Redis used peak memory | b | Redis port |
| Redis used rss memory | b | Redis port |
| RedisDB current save time sec | s | Redis port |
| RedisDB last save time sec | s | Redis port |
| Rejected Redis connections | conn | Redis port |
| Total Redis commands processed | # | Redis port |
| Total Redis connections received | conn | Redis port |
| Used CPU by the Redis system | s | Redis port |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| REDIS service state watcher | State watcher | status |

