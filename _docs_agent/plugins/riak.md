---
layout: page
title: Riak plugin
description: Information on the metrics collected by the CoScale Riak plugin.
---

> Riak KV is a distributed NoSQL database that is highly available, scalable and easy to operate. It automatically distributes data across the cluster to ensure fast performance and fault-tolerance.

More information on: [http://basho.com/](http://basho.com/)

## Events

* Service state

## Metrics

| Metric name                                                                                                             | Metric unit |
|-------------------------------------------------------------------------------------------------------------------------|-------------|
| Riak - 100th-percentile object size for strongly consistent GETs on this node in the last minute                        | b           |
| Max queue size of all local Riak KV virtual nodes in the last minute                                                    | b           |
| Max queue size of local Riak Pipe virtual nodes in the last minute                                                      | msg         |
| Mean queue size of all local Riak KV virtual nodes in the last minute                                                   | b           |
| Mean queue size of local Riak Pipe virtual nodes in the last minute                                                     | msg         |
| Median queue size of all local Riak KV virtual nodes in the last minute                                                 | b           |
| Median queue size of local Riak Pipe virtual nodes in the last minute                                                   | msg         |
| Minimum queue size of all local Riak KV virtual nodes in the last minute                                                | b           |
| Minimum queue size of local Riak Pipe virtual nodes in the last minute                                                  | msg         |
| Number of local Riak KV virtual nodes running                                                                           | #           |
| Number of local Riak Pipe virtual nodes running                                                                         | #           |
| Riak - 100h percentile node put fsm set time                                                                            | s           |
| Riak - 100th percentile node put fsm counter time                                                                       | s           |
| Riak - 100th percentile node put fsm map time                                                                           | s           |
| Riak - 100th percentile object merge time                                                                               | s           |
| Riak - 100th percentile object size encountered by this node within the last minute                                     | b           |
| Riak - 100th percentile object size encountered by this node's counter within the last minute                           | b           |
| Riak - 100th percentile of siblings encountered during all GET operations by this node within the last minute           | #           |
| Riak - 100th percentile of siblings encountered during all GET operations by this node's counter within the last minute | #           |
| Riak - 100th percentile set actor counts                                                                                | #           |
| Riak - 100th percentile time between reception of client GET request and subsequent response to client                  | s           |
| Riak - 100th percentile time between reception of client GET request and subsequent response to client (counter)        | s           |
| Riak - 100th percentile time between reception of client PUT request and subsequent response to client                  | s           |
| Riak - 100th percentile time it takes to perform an Update Counter operation                                            | #           |
| Riak - 100th percentile time it takes to perform an Update Map operation                                                | s           |
| Riak - 100th percentile time it takes to perform an Update Set operation                                                | s           |
| Riak - 100th percentile time it takes to perform Update Counters operations coordinated by local vnodes                 | s           |
| Riak - 100th percentile vnode get fsm time                                                                              | s           |
| Riak - 100th percentile vnode map update time                                                                           | s           |
| Riak - 100th percentile vnode put fsm time                                                                              | s           |
| Riak - 100th percentile vnode set update time                                                                           | s           |
| Riak - 100th percentile write once put time                                                                             | s           |
| Riak - 100th-percentile actor counter                                                                                   | #           |
| Riak - 100th-percentile map actor counter                                                                               | #           |
| Riak - 100th-percentile node get fsm map objsize                                                                        | b           |
| Riak - 100th-percentile node get fsm map siblings                                                                       | #           |
| Riak - 100th-percentile node get fsm map time                                                                           | s           |
| Riak - 100th-percentile node get fsm set objsize                                                                        | #           |
| Riak - 100th-percentile node get fsm set siblings                                                                       | #           |
| Riak - 100th-percentile node get fsm set time                                                                           | s           |
| Riak - 100th-percentile object size for strongly consistent PUTs on this node in the last minute                        | b           |
| Riak - 100th-percentile time between reception of client GETs to strongly consistent keys and subsequent response       | s           |
| Riak - 100th-percentile time between reception of client PUTs to strongly consistent keys and subsequent response       | s           |
| Riak - 95h percentile node put fsm set time                                                                             | s           |
| Riak - 95th percentile node put fsm counter time                                                                        | s           |
| Riak - 95th percentile node put fsm map time                                                                            | s           |
| Riak - 95th percentile object merge time                                                                                | s           |
| Riak - 95th percentile object size encountered by this node within the last minute                                      | b           |
| Riak - 95th percentile object size encountered by this node's counter within the last minute                            | b           |
| Riak - 95th percentile of siblings encountered during all GET operations by this node within the last minute            | #           |
| Riak - 95th percentile of siblings encountered during all GET operations by this node's counter within the last minute  | #           |
| Riak - 95th percentile set actor counts                                                                                 | #           |
| Riak - 95th percentile time between reception of client GET request and subsequent response to client                   | s           |
| Riak - 95th percentile time between reception of client GET request and subsequent response to client (counter)         | s           |
| Riak - 95th percentile time between reception of client PUT request and subsequent response to client                   | s           |
| Riak - 95th percentile time it takes to perform an Update Counter operation                                             | s           |
| Riak - 95th percentile time it takes to perform an Update Map operation                                                 | s           |
| Riak - 95th percentile time it takes to perform an Update Set operation                                                 | s           |
| Riak - 95th percentile time it takes to perform Update Counters operations coordinated by local vnodes                  | s           |
| Riak - 95th percentile vnode get fsm time                                                                               | s           |
| Riak - 95th percentile vnode map update time                                                                            | s           |
| Riak - 95th percentile vnode put fsm time                                                                               | s           |
| Riak - 95th percentile vnode set update time                                                                            | s           |
| Riak - 95th percentile write once put objsize                                                                           | b           |
| Riak - 95th percentile write once put time                                                                              | s           |
| Riak - 95th-percentile actor counter                                                                                    |             |
| Riak - 95th-percentile map actor counter                                                                                | #           |
| Riak - 95th-percentile node get fsm map objsize                                                                         | b           |
| Riak - 95th-percentile node get fsm map siblings                                                                        | #           |
| Riak - 95th-percentile node get fsm map time                                                                            | s           |
| Riak - 95th-percentile node get fsm set objsize                                                                         | #           |
| Riak - 95th-percentile node get fsm set siblings                                                                        | #           |
| Riak - 95th-percentile node get fsm set time                                                                            | s           |
| Riak - 95th-percentile object size for strongly consistent GETs on this node in the last minute                         | b           |
| Riak - 95th-percentile object size for strongly consistent PUTs on this node in the last minute                         | b           |
| Riak - 95th-percentile time between reception of client GETs to strongly consistent keys and subsequent response        | s           |
| Riak - 95th-percentile time between reception of client PUTs to strongly consistent keys and subsequent response        | s           |
| Riak - 99h percentile node put fsm map time                                                                             | s           |
| Riak - 99h percentile node put fsm set time                                                                             | s           |
| Riak - 99th percentile node put fsm counter time                                                                        | s           |
| Riak - 99th percentile object merge time                                                                                | s           |
| Riak - 99th percentile object size encountered by this node within the last minute                                      | b           |
| Riak - 99th percentile object size encountered by this node's counter within the last minute                            | b           |
| Riak - 99th percentile of siblings encountered during all GET operations by this node within the last minute            | #           |
| Riak - 99th percentile of siblings encountered during all GET operations by this node's counter within the last minute  | #           |
| Riak - 99th percentile set actor counts                                                                                 | #           |
| Riak - 99th percentile time between reception of client GET request and subsequent response to client                   | s           |
| Riak - 99th percentile time between reception of client GET request and subsequent response to client (counter)         | s           |
| Riak - 99th percentile time between reception of client PUT request and subsequent response to client                   | s           |
| Riak - 99th percentile time it takes to perform an Update Counter operation                                             | s           |
| Riak - 99th percentile time it takes to perform an Update Map operation                                                 | s           |
| Riak - 99th percentile time it takes to perform an Update Set operation                                                 | s           |
| Riak - 99th percentile time it takes to perform Update Counters operations coordinated by local vnodes                  | s           |
| Riak - 99th percentile vnode get fsm time                                                                               | s           |
| Riak - 99th percentile vnode map update time                                                                            | s           |
| Riak - 99th percentile vnode put fsm time                                                                               | s           |
| Riak - 99th percentile vnode set update time                                                                            | s           |
| Riak - 99th percentile write once put objsize                                                                           | b           |
| Riak - 99th percentile write once put time                                                                              | s           |
| Riak - 99th-percentile actor counter                                                                                    | #           |
| Riak - 99th-percentile map actor counter                                                                                | #           |
| Riak - 99th-percentile node get fsm map objsize                                                                         | b           |
| Riak - 99th-percentile node get fsm map siblings                                                                        | #           |
| Riak - 99th-percentile node get fsm map time                                                                            | s           |
| Riak - 99th-percentile node get fsm set objsize                                                                         | #           |
| Riak - 99th-percentile node get fsm set siblings                                                                        | #           |
| Riak - 99th-percentile node get fsm set time                                                                            | s           |
| Riak - 99th-percentile object size for strongly consistent GETs on this node in the last minute                         | b           |
| Riak - 99th-percentile object size for strongly consistent PUTs on this node in the last minute                         | b           |
| Riak - 99th-percentile time between reception of client GETs to strongly consistent keys and subsequent response        | s           |
| Riak - 99th-percentile time between reception of client PUTs to strongly consistent keys and subsequent response        | s           |
| Riak - Average number of GET FSMs dequeued by Sidejob                                                                   | #           |
| Riak - Average number of GET FSMs enqueued by Sidejob                                                                   | #           |
| Riak - Average number of PUT FSMs dequeued by Sidejob                                                                   | #           |
| Riak - Average number of PUT FSMs enqueued by Sidejob                                                                   | #           |
| Riak - Executing mappers                                                                                                | #           |
| Riak - Last observed histogram value in milliseconds describing time taken for the ring to converge after ring changes  | s           |
| Riak - Last observed histogram value in milliseconds describing time taken for the ring to rebalance after ring changes | s           |
| Riak - Late put fsm coordinator ack                                                                                     | #           |
| Riak - Maximum time in milliseconds describing time taken for the ring to converge after ring changes                   | s           |
| Riak - Maximum time in milliseconds taken to calculate partition rebalance during a cluster membership change           | s           |
| Riak - Mean actor counter                                                                                               | #           |
| Riak - Mean map actor counter                                                                                           | #           |
| Riak - Mean number of siblings encountered during all GET operations by this node within the last minute                | #           |
| Riak - Mean number of siblings encountered during all GET operations by this node's counter within the last minute      | #           |
| Riak - Mean object size encountered by this node within the last minute                                                 | b           |
| Riak - Mean object size encountered by this node's counter within the last minute                                       | b           |
| Riak - Mean object size for strongly consistent GETs on this node in the last minute                                    | b           |
| Riak - Mean object size for strongly consistent PUTs on this node in the last minute                                    | b           |
| Riak - Mean time between reception of client GET request and subsequent response to client                              | s           |
| Riak - Mean time between reception of client GET request and subsequent response to client (counter)                    | s           |
| Riak - Mean time between reception of client GETs to strongly consistent keys and subsequent response                   | s           |
| Riak - Mean time between reception of client PUT request and subsequent response to client                              | s           |
| Riak - Mean time between reception of client PUTs to strongly consistent keys and subsequent response                   | s           |
| Riak - Mean time in milliseconds describing time taken for the ring to converge after ring changes                      | s           |
| Riak - Mean time in milliseconds describing time taken for the ring to rebalance after ring changes                     | s           |
| Riak - Mean time it takes to perform an Update Counter operation                                                        | s           |
| Riak - Mean time it takes to perform an Update Map operation                                                            | s           |
| Riak - Mean time it takes to perform an Update Set operation                                                            | s           |
| Riak - Mean time it takes to perform Update Counters operations coordinated by local vnodes                             | s           |
| Riak - Median actor counter                                                                                             | #           |
| Riak - Median map actor counter                                                                                         | #           |
| Riak - Median number of siblings encountered during all GET operations by this node within the last minute              | #           |
| Riak - Median number of siblings encountered during all GET operations by this node's counter within the last minute    | #           |
| Riak - Median object size encountered by this node within the last minute                                               | b           |
| Riak - Median object size encountered by this node's counter within the last minute                                     | b           |
| Riak - Median object size for strongly consistent GETs on this node in the last minute                                  | b           |
| Riak - Median object size for strongly consistent PUTs on this node in the last minute                                  | b           |
| Riak - Median time between reception of client GET request and subsequent response to client                            | s           |
| Riak - Median time between reception of client GET request and subsequent response to client (counter)                  | s           |
| Riak - Median time between reception of client GETs to strongly consistent keys and subsequent response                 | s           |
| Riak - Median time between reception of client PUT request and subsequent response to client                            | s           |
| Riak - Median time between reception of client PUTs to strongly consistent keys and subsequent response                 | s           |
| Riak - Median time it takes to perform an Update Counter operation                                                      | s           |
| Riak - Median time it takes to perform an Update Map operation                                                          | s           |
| Riak - Median time it takes to perform an Update Set operation                                                          | s           |
| Riak - Median time it takes to perform Update Counters operations coordinated by local vnodes                           | s           |
| Riak - Minimum time in milliseconds describing time taken for the ring to converge after ring changes                   | s           |
| Riak - Minimum time in milliseconds taken to calculate partition rebalance during a cluster membership change           | s           |
| Riak - Node get fsm errors                                                                                              | errors      |
| Riak - Node get fsm map objsize mean                                                                                    | b           |
| Riak - Node get fsm map objsize median                                                                                  | b           |
| Riak - Node get fsm map siblings mean                                                                                   | #           |
| Riak - Node get fsm map siblings median                                                                                 | #           |
| Riak - Node get fsm map time mean                                                                                       | s           |
| Riak - Node get fsm map time median                                                                                     | s           |
| Riak - Node get fsm set objsize mean                                                                                    | #           |
| Riak - Node get fsm set objsize median                                                                                  | #           |
| Riak - Node get fsm set siblings mean                                                                                   | #           |
| Riak - Node get fsm set siblings median                                                                                 | #           |
| Riak - Node get fsm set time mean                                                                                       | s           |
| Riak - Node get fsm set time median                                                                                     | s           |
| Riak - Node get total fsm errors                                                                                        | errors      |
| Riak - Node gets counter total                                                                                          | #           |
| Riak - Node gets map                                                                                                    | #           |
| Riak - Node gets map total                                                                                              | #           |
| Riak - Node gets set                                                                                                    | #           |
| Riak - Node gets set total                                                                                              | #           |
| Riak - Node gets total                                                                                                  | #           |
| Riak - Node put fsm counter time mean                                                                                   | s           |
| Riak - Node put fsm counter time median                                                                                 | s           |
| Riak - Node put fsm map time mean                                                                                       | s           |
| Riak - Node put fsm map time median                                                                                     | s           |
| Riak - Node put fsm set time mean                                                                                       | s           |
| Riak - Node put fsm set time median                                                                                     | s           |
| Riak - Node puts counter                                                                                                | #           |
| Riak - Node puts counter total                                                                                          | #           |
| Riak - Node puts map                                                                                                    | #           |
| Riak - Node puts map total                                                                                              | #           |
| Riak - Node puts set                                                                                                    | #           |
| Riak - Node puts set total                                                                                              | #           |
| Riak - Number of active GET FSMs                                                                                        | b           |
| Riak - Number of active Keylisting FSMs                                                                                 | #           |
| Riak - Number of active PUT FSMs                                                                                        | #           |
| Riak - Number of active Secondary Index FSMs                                                                            | #           |
| Riak - Number of currently active protocol buffer connections                                                           | conn        |
| Riak - Number of GET FSMs active in the last minute                                                                     | b           |
| Riak - Number of GET FSMs actively being rejected by Sidejob's overload protection                                      | #           |
| Riak - Number of GET FSMs rejected by Sidejob's overload protection in the last minute                                  | #           |
| Riak - Number of GET operations coordinated by vnodes on this node within the last minute                               | #           |
| Riak - Number of GETs coordinated by local vnodes since node startup                                                    | #           |
| Riak - Number of GETs coordinated by this node                                                                          | #           |
| Riak - Number of GETs coordinated by this node, including GETs to non-local vnodes in the last minute                   | #           |
| Riak - Number of gossip messages received in the last minute                                                            | msg         |
| Riak - Number of handoff timeouts encountered by this node                                                              |             |
| Riak - Number of individual secondary index values deleted in the last minute                                           | #           |
| Riak - Number of individual secondary index values written in the last minute                                           | #           |
| Riak - Number of Keylisting FSM creation errors in the last minute                                                      | errors      |
| Riak - Number of Keylisting FSMs created in the last minute                                                             | #           |
| Riak - Number of local replicas participating in secondary index deletes in the last minute                             | #           |
| Riak - Number of local replicas participating in secondary index reads in the last minute                               | #           |
| Riak - Number of local replicas participating in secondary index writes in the last minute                              | #           |
| Riak - Number of logical processors available on the system                                                             | cores       |
| Riak - Number of new protocol buffer connections established during the last minute                                     | conn        |
| Riak - Number of operating system processes                                                                             | procs       |
| Riak - Number of processes currently running in the Erlang VM                                                           | procs       |
| Riak - Number of PUT FSMs active in the last minute                                                                     | #           |
| Riak - Number of PUT FSMs actively being rejected by Sidejob's overload protection                                      | #           |
| Riak - Number of PUT FSMs rejected by Sidejob's overload protection in the last minute                                  | #           |
| Riak - Number of PUT operations coordinated by local vnodes on this node in the last minute                             | #           |
| Riak - Number of PUTs coordinated by this node, including PUTs to non-local vnodes on this node within the last minute  | #           |
| Riak - Number of read repair operations this node has coordinated in the last minute                                    | #           |
| Riak - Number of requests this node has redirected to other nodes for coordination since node startup                   | req         |
| Riak - Number of ring reconciliation operations in the last minute                                                      | #           |
| Riak - Number of Secondary Index query FSM creation errors in the last minute                                           | #           |
| Riak - Number of Secondary Index query FSMs created in the last minute                                                  | #           |
| Riak - Number of secondary indexes refreshed on this node during secondary index anti-entropy in the last minute        | #           |
| Riak - Number of strongly consistent GETs coordinated by this node in the last minute                                   | #           |
| Riak - Number of strongly consistent PUTs coordinated by this node in the last minute                                   | #           |
| Riak - Number of threads in the asynchronous thread pool                                                                | threads     |
| Riak - Object counter merge                                                                                             | #           |
| Riak - Object map merge                                                                                                 | #           |
| Riak - Object merge                                                                                                     | #           |
| Riak - Object merge time mean                                                                                           | s           |
| Riak - Object merge time median                                                                                         | s           |
| Riak - Object merge total                                                                                               | #           |
| Riak - Object set merge                                                                                                 | #           |
| Riak - Read repairs counter                                                                                             | #           |
| Riak - Read repairs counter total                                                                                       | #           |
| Riak - Read repairs map                                                                                                 | #           |
| Riak - Read repairs map total                                                                                           | #           |
| Riak - Read repairs set                                                                                                 | #           |
| Riak - Read repairs set total                                                                                           | #           |
| Riak - Ring creation size                                                                                               | #           |
| Riak - set actor counts mean                                                                                            | #           |
| Riak - set actor counts median                                                                                          | #           |
| Riak - skipped read repairs                                                                                             | #           |
| Riak - skipped read repairs total                                                                                       | #           |
| Riak - sys monitor count                                                                                                | #           |
| Riak - sys port count                                                                                                   | #           |
| Riak - The average number of active processes for the last 1 minute                                                     | procs       |
| Riak - The average number of active processes for the last 15 minutes                                                   | procs       |
| Riak - The average number of active processes for the last 5 minutes                                                    | procs       |
| Riak - The number of partitions in the ring                                                                             | #           |
| Riak - The number of pipeline creation errors in the last 60 seconds                                                    | pipe        |
| Riak - The number of pipelines active in the last 60 seconds                                                            | pipe        |
| Riak - The number of pipelines created in the last 60 seconds                                                           | pipe        |
| Riak - The total number of pipeline creation errors since the node was started                                          | pipe        |
| Riak - The total number of pipelines created since the node was started                                                 | pipe        |
| Riak - Total allocated memory (sum of processes and system)                                                             | b           |
| Riak - Total allocated memory that is not directly related to an Erlang process                                         | b           |
| Riak - Total amount of memory allocated for Erlang code                                                                 | b           |
| Riak - Total amount of memory allocated for Erlang processes                                                            | b           |
| Riak - Total amount of memory currently allocated for atom storage                                                      | b           |
| Riak - Total amount of memory currently used for atom storage                                                           | b           |
| Riak - Total amount of memory used by Erlang processes                                                                  | b           |
| Riak - Total amount of memory used for binaries                                                                         | b           |
| Riak - Total available system memory                                                                                    | b           |
| Riak - Total memory allocated for Erlang Term Storage                                                                   | b           |
| Riak - Total memory allocated for this node                                                                             | b           |
| Riak - Total number of GET FSMs rejected by Sidejob's overload protection                                               | #           |
| Riak - Total number of ignored gossip messages since node was started                                                   | msg         |
| Riak - Total number of indexes refreshed during secondary index anti-entropy                                            | #           |
| Riak - Total number of individual secondary index values deleted                                                        | #           |
| Riak - Total number of individual secondary index values written                                                        | #           |
| Riak - Total number of Keylisting FSM creation errors                                                                   | errors      |
| Riak - Total number of Keylisting FSMs created                                                                          | #           |
| Riak - Total number of local replicas participating in secondary index deletes                                          | #           |
| Riak - Total number of local replicas participating in secondary index reads                                            | #           |
| Riak - Total number of local replicas participating in secondary index writes                                           | #           |
| Riak - Total number of ownership handoff operations rejected by the node since it was started                           | #           |
| Riak - Total number of post-commit hook failures                                                                        | #           |
| Riak - Total number of pre-commit hook failures                                                                         | #           |
| Riak - Total number of Protocol Buffers connections made                                                                | conn        |
| Riak - Total number of PUT FSMs rejected by Sidejob's overload protection                                               | #           |
| Riak - Total number of PUTS coordinated by local vnodes                                                                 | #           |
| Riak - Total number of PUTs coordinated by this node, including PUTs to non-local vnodes                                | #           |
| Riak - Total number of Read Repairs this node has coordinated                                                           | #           |
| Riak - Total number of requests dropped by local vnodes since the node was started                                      | req         |
| Riak - Total number of ring reconciliation operations since node was started                                            | #           |
| Riak - Total number of strongly consistent GETs coordinated by this node                                                | #           |
| Riak - Total number of strongly consistent PUTs coordinated by this node                                                | #           |
| Riak - Total time it takes to perform an Update Counter operation                                                       | s           |
| Riak - Total time it takes to perform an Update Map operation                                                           | s           |
| Riak - Total time it takes to perform an Update Set operation                                                           | s           |
| Riak - Total time it takes to perform Update Counters operations coordinated by local vnodes                            | s           |
| Riak - Update Counters operations coordinated by local vnodes                                                           | #           |
| Riak - Update Maps operations coordinated by local vnodes                                                               | #           |
| Riak - Update Sets operations coordinated by local vnodes                                                               | #           |
| Riak - Vnode get fsm time mean                                                                                          | s           |
| Riak - Vnode get fsm time median                                                                                        | s           |
| Riak - vnode map update time mean                                                                                       | s           |
| Riak - vnode map update time median                                                                                     | s           |
| Riak - vnode map update total                                                                                           | #           |
| Riak - vnode put fsm time mean                                                                                          | s           |
| Riak - vnode put fsm time median                                                                                        | s           |
| Riak - vnode set update time mean                                                                                       | s           |
| Riak - vnode set update time median                                                                                     | s           |
| Riak - vnode set update total                                                                                           | #           |
| Riak - Write once merge                                                                                                 | #           |
| Riak - write once put objsize                                                                                           | b           |
| Riak - Write once put objsize mean                                                                                      | b           |
| Riak - Write once put objsize median                                                                                    | b           |
| Riak - Write once put time mean                                                                                         | s           |
| Riak - Write once put time median                                                                                       | s           |
| Riak - Write once puts                                                                                                  | #           |
| Riak - Write once puts total                                                                                            | #           |
| Total queue size of all local Riak KV virtual nodes in the last minute                                                  | b           |
| Total queue size of all local Riak Pipe virtual nodes in the last minute                                                | msg         |
