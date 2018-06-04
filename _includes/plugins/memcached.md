## Metrics

### Memcached 

| Name | Unit | Dimensions |
|------|------|------------|
| Memcached active check latency | s | Memcached port |
| Memcached active check uptime | % | Memcached port |

### Memcached / Cache 

| Name | Unit | Dimensions |
|------|------|------------|
| Memcached bytes in cache | b | Memcached port |
| Memcached evictions | #/s | Memcached port |
| Memcached hash table size | b | Memcached port |
| Memcached items in cache | items | Memcached port |
| Memcached max size cache | b | Memcached port |
| Memcached reclaimed | #/s | Memcached port |
| Memcached unfetched evicted | #/s | Memcached port |
| Memcached unfetched expired | #/s | Memcached port |
| Total Memcached items | items | Memcached port |

### Memcached / Commands 

| Name | Unit | Dimensions |
|------|------|------------|
| Memcached auth commands | #/s | Memcached port |
| Memcached auth errors | #/s | Memcached port |
| Memcached flush commands | #/s | Memcached port |
| Memcached get commands | #/s | Memcached port |
| Memcached set commands | #/s | Memcached port |
| Memcached touch commands | #/s | Memcached port |

### Memcached / Connections 

| Name | Unit | Dimensions |
|------|------|------------|
| Accepting connections by Memcached | conn | Memcached port |
| Current connections to Memcached | conn | Memcached port |
| Max connections reached to Memcached | conn | Memcached port |
| Memcached connection structures | # | Memcached port |
| Memcached reversed file descriptors | # | Memcached port |
| Total connections to Memcached | conn | Memcached port |
| Yielded connections to Memcached | conn | Memcached port |

### Memcached / Hits and Misses 

| Name | Unit | Dimensions |
|------|------|------------|
| Memcached check and set bad value | #/s | Memcached port |
| Memcached check and set hits | #/s | Memcached port |
| Memcached check and set misses | #/s | Memcached port |
| Memcached decrement hits | #/s | Memcached port |
| Memcached decrement misses | #/s | Memcached port |
| Memcached delete hits | #/s | Memcached port |
| Memcached delete misses | #/s | Memcached port |
| Memcached get hits | #/s | Memcached port |
| Memcached get misses | #/s | Memcached port |
| Memcached increment hits | #/s | Memcached port |
| Memcached increment misses | #/s | Memcached port |
| Memcached touch hits | #/s | Memcached port |
| Memcached touch misses | #/s | Memcached port |

### Memcached / Resources 

| Name | Unit | Dimensions |
|------|------|------------|
| Memcached bytes read | b | Memcached port |
| Memcached bytes written | b | Memcached port |
| Memcached process id |  | Memcached port |
| Memcached system time | % | Memcached port |
| Memcached threads | threads | Memcached port |
| Memcached uptime | s | Memcached port |
| Memcached user time | % | Memcached port |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| MEMCACHED service state watcher | State watcher | status |

