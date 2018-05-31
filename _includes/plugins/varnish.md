## Metrics

### Varnish 

| Name | Unit | Dimensions |
|------|------|------------|
| Ban tests tested against Varnish objects (lookup) | # |  |
| Ban tests tested against Varnish objects (lurker) | # |  |
| Bans tested against Varnish objects (lurker) | # |  |
| Bytes used by the persisted Varnish ban lists | b |  |
| Client connections accepted | conn |  |
| Client requests received | req |  |
| Connection dropped, no sess/wrk | conn |  |
| Cooling Varnish shared memory space | b |  |
| Extra bytes in persisted Varnish ban lists due to fragmentation | b |  |
| Fetch had bad headers | resp |  |
| Fetch head | resp |  |
| Free Varnish shared memory space | b |  |
| Good Varnish client requests received | req |  |
| Gunzip Varnish operations | # |  |
| Gzip Varnish operations | # |  |
| Length of Varnish session queue | req |  |
| Loaded Varnish VMODs | # |  |
| Management Varnish process uptime | s |  |
| Number of Varnish objects mailed to expiry thread | # |  |
| Number of Varnish objects received by expiry thread | # |  |
| Number of Varnish purge operations | # |  |
| Number of Varnish purged objects | # |  |
| Number of Varnish requests sent to sleep on busy objhdr | req |  |
| Number of Varnish requests woken after sleep on busy objhdr | req |  |
| Number of Varnish thread pools | # |  |
| Overflow Varnish shared memory space | b |  |
| Overflowed Varnish shared memory space | b |  |
| Piped bytes from Varnish client | b |  |
| Piped bytes to Varnish client | b |  |
| Sessions dropped for Varnish thread | # |  |
| Sessions queued for Varnish thread | # |  |
| Total number of Varnish threads | threads |  |
| Total Varnish pass | session |  |
| Total Varnish pipes | session |  |
| Total Varnish requests | req |  |
| Total Varnish sessions | session |  |
| Used Varnish shared memory space | b |  |
| Varnish active check latency | s |  |
| Varnish active check uptime | % |  |
| Varnish allocations | # | Memory pool |
| Varnish allocations outstanding | # | MALLOC Storage |
| Varnish allocator failures | # | MALLOC Storage |
| Varnish allocator requests | # | MALLOC Storage |
| Varnish backend connections failures | conn |  |
| Varnish backend connections not attempted | conn |  |
| Varnish backend connections recycles | conn |  |
| Varnish backend connections retry | conn |  |
| Varnish backend connections reuses | conn |  |
| Varnish backend connections success | conn |  |
| Varnish backend connections too many | conn |  |
| Varnish backend connections was closed | conn |  |
| Varnish backend requests made | req |  |
| Varnish backends | # |  |
| Varnish bans added | # |  |
| Varnish bans deleted | # |  |
| Varnish bans superseded by other bans | # |  |
| Varnish bans tested against objects (lookup) | # |  |
| Varnish bytes allocated | b | MALLOC Storage |
| Varnish bytes available | b | MALLOC Storage |
| Varnish bytes freed | b | MALLOC Storage |
| Varnish bytes outstanding | b | MALLOC Storage |
| Varnish cache hits | hits |  |
| Varnish cache hits for pass | hits |  |
| Varnish cache misses | misses |  |
| Varnish child process core dumped | procs |  |
| Varnish child process died (signal) | procs |  |
| Varnish child process normal exit | procs |  |
| Varnish child process panic | procs |  |
| Varnish child process started | procs |  |
| Varnish child process unexpected exit | procs |  |
| Varnish child process uptime | s |  |
| Varnish client requests received, subject to 400 errors | req |  |
| Varnish client requests received, subject to 411 errors | req |  |
| Varnish client requests received, subject to 413 errors | req |  |
| Varnish client requests received, subject to 417 errors | req |  |
| Varnish configuration Language available | # |  |
| Varnish configuration Language discarded | # |  |
| Varnish configuration Language references by backend | # | Backend |
| Varnish configuration Language total | # |  |
| Varnish count of bans | # |  |
| Varnish created locks | # | Lock |
| Varnish destroyed locks | # | Lock |
| Varnish ESI parse errors (unlock) | errors |  |
| Varnish ESI parse warnings (unlock) | # |  |
| Varnish expired objects | # |  |
| Varnish fetch bad T-E | resp |  |
| Varnish fetch body failed | resp |  |
| Varnish fetch chunked | resp |  |
| Varnish fetch EOF | resp |  |
| Varnish fetch no body (1xx) | resp |  |
| Varnish fetch no body (204) | resp |  |
| Varnish fetch no body (304) | resp |  |
| Varnish fetch no body (HEAD) | resp |  |
| Varnish fetch pre HTTP/1.1 closed | resp |  |
| Varnish fetch wanted close | resp |  |
| Varnish fetch with Length | resp |  |
| Varnish fetch zero len body | resp |  |
| Varnish frees | # | Memory pool |
| Varnish happy health probes by backend | # | Backend |
| Varnish HCB Inserts | # |  |
| Varnish HCB Lookups with lock | # |  |
| Varnish HCB Lookups without lock | # |  |
| Varnish HTTP header overflows | # |  |
| Varnish In Pool | # | Memory pool |
| Varnish In use | # | Memory pool |
| Varnish lock operations | # | Lock |
| Varnish LRU moved objects | # |  |
| Varnish LRU nuked objects | # |  |
| Varnish lurker gave way for lookup | # |  |
| Varnish number of bans marked 'completed' | # |  |
| Varnish number of bans using obj.* | # |  |
| Varnish number of bans using req.* | # |  |
| Varnish objects killed by bans (lookup) | # |  |
| Varnish objects killed by bans (lurker) | # |  |
| Varnish pipe request header bytes by backend | b | Backend |
| Varnish piped bytes from backend | b | Backend |
| Varnish piped bytes to backend | b | Backend |
| Varnish pool ran dry | # | Memory pool |
| Varnish recycled from pool | # | Memory pool |
| Varnish reponse body bytes | b |  |
| Varnish request body bytes by backend | b | Backend |
| Varnish request header bytes by backend | b | Backend |
| Varnish response body bytes by backend | b | Backend |
| Varnish response header bytes by backend | b | Backend |
| Varnish session accept failures | session |  |
| Varnish session closed | session |  |
| Varnish session herd | session |  |
| Varnish session pipe overflow | session |  |
| Varnish session pipeline | session |  |
| Varnish session read ahead | session |  |
| Varnish sessions accepted | session |  |
| Varnish sessions dropped | session |  |
| Varnish SHM cycles through buffer | # |  |
| Varnish SHM flushes due to overflow | # |  |
| Varnish SHM MTX contention | # |  |
| Varnish SHM records | # |  |
| Varnish SHM writes | # |  |
| Varnish size allocated | b | Memory pool |
| Varnish size requested | b | Memory pool |
| Varnish SMS allocator requests | req |  |
| Varnish SMS bytes allocated | b |  |
| Varnish SMS bytes freed | b |  |
| Varnish SMS outstanding allocations | # |  |
| Varnish SMS outstanding bytes | b |  |
| Varnish struct objectcore | # |  |
| Varnish struct objecthead | # |  |
| Varnish struct objects | # |  |
| Varnish struct waitinglist | # |  |
| Varnish thread creation failed | # |  |
| Varnish threads created | threads |  |
| Varnish threads destroyed | threads |  |
| Varnish threads hit max | # |  |
| Varnish timed out from pool | # | Memory pool |
| Varnish too many for pool | # | Memory pool |
| Varnish too small to recycle | # | Memory pool |
| Varnish total fetch | resp |  |
| Varnish total synth | resp |  |
| Varnish unresurrected objects | # |  |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| VARNISH service state watcher | State watcher | status |

