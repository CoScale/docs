## Metrics

### Couchbase 

| Name | Unit | Dimensions |
|------|------|------------|
| Couchbase active check latency | s |  |
| Couchbase active check uptime | % |  |
| Couchbase current number of buckets | # |  |
| Couchbase max bucket count | # |  |

### Couchbase / Bucket 

| Name | Unit | Dimensions |
|------|------|------------|
| Couchbase active items in disk queue | # | Bucket |
| Couchbase amount of disk used | b | Bucket |
| Couchbase amount of memory used by the bucket | b | Bucket |
| Couchbase amount of RAM used by the bucket | b | Bucket |
| Couchbase amount of raw RAM used by the bucket | b | Bucket |
| Couchbase bytes read | b | Bucket |
| Couchbase bytes written | b | Bucket |
| Couchbase check and set hits | # | Bucket |
| Couchbase check and set misses | # | Bucket |
| Couchbase current connections | conn | Bucket |
| Couchbase current items | items | Bucket |
| Couchbase current items total | items | Bucket |
| Couchbase decrement hits | hits | Bucket |
| Couchbase decrement misses | misses | Bucket |
| Couchbase delete hits | hits | Bucket |
| Couchbase delete misses | misses | Bucket |
| Couchbase ep_cache_miss_rate |  | Bucket |
| Couchbase ep_diskqueue_drain |  | Bucket |
| Couchbase ep_diskqueue_fill |  | Bucket |
| Couchbase ep_flusher_todo |  | Bucket |
| Couchbase ep_item_commit_failed |  | Bucket |
| Couchbase ep_num_non_resident |  | Bucket |
| Couchbase ep_num_value_ejects |  | Bucket |
| Couchbase ep_queue_size |  | Bucket |
| Couchbase extra memory used by transient data | b | Bucket |
| Couchbase free memory | b | Bucket |
| Couchbase get commands | # | Bucket |
| Couchbase get hits | hits | Bucket |
| Couchbase get misses | misses | Bucket |
| Couchbase high water mark for auto-evictions |  | Bucket |
| Couchbase increment hits | hits | Bucket |
| Couchbase increment misses | misses | Bucket |
| Couchbase low water mark for auto-evictions |  | Bucket |
| Couchbase max amount of data allowed in memory | b | Bucket |
| Couchbase memory used | b | Bucket |
| Couchbase number of active vBuckets. | # | Bucket |
| Couchbase number of create operations | # | Bucket |
| Couchbase number of disk fetches | # | Bucket |
| Couchbase number of disk fetches performed since server was started for a bucket | # | Bucket |
| Couchbase number of items associated with the bucket | # | Bucket |
| Couchbase number of items/documents that are replicas for a bucket | # | Bucket |
| Couchbase number of operations per second | # | Bucket |
| Couchbase number of replica vBuckets | # | Bucket |
| Couchbase number of times temporary OOMs | # | Bucket |
| Couchbase number of times unrecoverable OOMs | # | Bucket |
| Couchbase percentage of RAM used (for active objects) against the configure bucket size | % | Bucket |
| Couchbase replica items in disk queue | # | Bucket |
| Couchbase set commands | # | Bucket |
| Couchbase size of user data within buckets of the specified state that are resident in RAM | % | Bucket |
| Couchbase total drained items | # | Bucket |
| Couchbase total enqueued items | # | Bucket |
| Couchbase total memory | b | Bucket |
| Couchbase total memory used by meta data | b | Bucket |
| Couchbase total metadata memory |  | Bucket |

### Couchbase / Fragmentation 

| Name | Unit | Dimensions |
|------|------|------------|
| Couchbase database fragmentation threshold | % |  |
| Couchbase index fragmentation threshold | % |  |
| Couchbase view fragmentation threshold | % |  |

### Couchbase / HDD 

| Name | Unit | Dimensions |
|------|------|------------|
| Couchbase free harddrive space in the cluster | b |  |
| Couchbase harddrive quota total for the cluster | b |  |
| Couchbase harddrive space used by the cluster | b |  |
| Couchbase harddrive use by the data in the cluster | b |  |
| Couchbase total harddrive space available to cluster | b |  |

### Couchbase / Node 

| Name | Unit | Dimensions |
|------|------|------------|
| Couchbase amount of disk space occupied by Couch views | b |  |
| Couchbase amount of disk space used by Couch docs | b |  |
| Couchbase amount of memcached memory allocated | # |  |
| Couchbase amount of memcached memory reserved | b |  |
| Couchbase cluster compatibility |  |  |
| Couchbase couch spatial data size | b |  |
| Couchbase couch spatial disk size | b |  |
| Couchbase data size of couch documents associated with a node | b |  |
| Couchbase memory used by the node | b |  |
| Couchbase number of current items | # |  |
| Couchbase number of disk fetches performed since server was started | # |  |
| Couchbase number of get hits | # |  |
| Couchbase number of items/documents that are replicas | # |  |
| Couchbase number of operations performed | # |  |
| Couchbase size of object data for Couch views | b |  |
| Couchbase total number of items associated with node | # |  |

### Couchbase / Node / System 

| Name | Unit | Dimensions |
|------|------|------------|
| Couchbase amount of swap space used | b |  |
| Couchbase free memory available to the node | b |  |
| Couchbase number of get commands | # |  |
| Couchbase the CPU utilization rate | % |  |
| Couchbase total memory available to the node | b |  |
| Couchbase total swap size allocated | b |  |

### Couchbase / RAM 

| Name | Unit | Dimensions |
|------|------|------------|
| Couchbase RAM quota total for the cluster | b |  |
| Couchbase RAM quota used by the cluster | b |  |
| Couchbase RAM used by the cluster | b |  |
| Couchbase RAM used by the data in the cluster | b |  |
| Couchbase total RAM available to cluster | b |  |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| COUCHBASE service state watcher | State watcher | status |

