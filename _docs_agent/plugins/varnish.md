---
layout: page
title: Varnish plugin
description: Information on the metrics collected by the CoScale Varnish plugin.
---

> Varnish Cache is a web application accelerator also known as a caching HTTP reverse proxy. You install it in front of any server that speaks HTTP and configure it to cache the contents. Varnish Cache is really, really fast. It typically speeds up delivery with a factor of 300 - 1000x, depending on your architecture.

More information on: [https://varnish-cache.org/](https://varnish-cache.org/)

## Events

* Service state

## Metrics

| Metric name                                                                                    | Metric unit |
|------------------------------------------------------------------------------------------------|-------------|
| Client connections accepted                                                                    | conn        |
| Number of Varnish thread pools                                                                 | #           |
| Number of times more threads were needed, but limit was reached in a thread pool               | #           |
| Number of times creating a thread failed                                                       | #           |
| Number of times session was queued waiting for a thread                                        | #           |
| Number of times session was dropped because the queue were too long already                    | #           |
| Varnish struct objects                                                                         | #           |
| Varnish unresurrected objects                                                                  | #           |
| Varnish struct objectcore                                                                      | #           |
| Varnish struct objecthead                                                                      | #           |
| Varnish struct waitinglist                                                                     | #           |
| Varnish backends                                                                               | #           |
| Varnish expired objects                                                                        | #           |
| Varnish LRU nuked objects                                                                      | #           |
| Varnish LRU moved objects                                                                      | #           |
| Varnish HTTP header overflows                                                                  | #           |
| Varnish SHM records                                                                            | #           |
| Varnish SHM writes                                                                             | #           |
| Varnish SHM flushes due to overflow                                                            | #           |
| Varnish SHM MTX contention                                                                     | #           |
| Varnish SHM cycles through buffer                                                              | #           |
| Varnish SMS outstanding allocations                                                            | #           |
| Varnish configuration Language total                                                           | #           |
| Varnish configuration Language available                                                       | #           |
| Varnish configuration Language discarded                                                       | #           |
| Count of bans replaced by later identical bans                                                 | #           |
| Number of bans which are no longer active                                                      | #           |
| Number of bans which use obj.* variables. These bans can possibly be washed by the ban-lurker. | #           |
| Number of bans which use req.* variables. These bans can not be washed by the ban-lurker       | #           |
| Counter of bans added to ban list                                                              | #           |
| Counter of bans deleted from ban list                                                          | #           |
| Count of how many bans and objects have been tested against each other during hash lookup      | #           |
| Number of objects killed by bans during object lookup                                          | #           |
| Count of how many bans and objects have been tested against each other by the ban-lurker       | #           |
| Count of how many tests and objects have been tested against each other during lookup          | #           |
| Count of how many bans and objects have been tested against each other by the ban-lurker       | #           |
| Number of objects killed by bans during object lookup                                          | #           |
| Count of bans replaced by later identical bans                                                 | #           |
| Number of times the ban-lurker had to wait for lookups                                         | #           |
| Number of Varnish purge operations                                                             | #           |
| Number of Varnish purged objects                                                               | #           |
| Number of objects mailed to expiry thread for handling                                         | #           |
| Number of objects received by expiry thread for handling                                       | #           |
| Varnish HCB Lookups without lock                                                               | #           |
| Varnish HCB Lookups with lock                                                                  | #           |
| Varnish HCB Inserts                                                                            | #           |
| Varnish ESI parse warnings (unlock)                                                            | #           |
| Loaded Varnish VMODs                                                                           | #           |
| Gzip Varnish operations                                                                        | #           |
| Gunzip Varnish operations                                                                      | #           |
| Varnish %s In use                                                                              | #           |
| Varnish %s In Pool                                                                             | #           |
| Varnish %s allocations                                                                         | #           |
| Varnish %s frees                                                                               | #           |
| Varnish %s recycled from pool                                                                  | #           |
| Varnish %s timed out from pool                                                                 | #           |
| Varnish %s too small to recycle                                                                | #           |
| Varnish %s too many for pool                                                                   | #           |
| Varnish %s pool ran dry                                                                        | #           |
| Varnish %s allocator requests                                                                  | #           |
| Varnish %s allocator failures                                                                  | #           |
| Varnish %s allocations outstanding                                                             | #           |
| Varnish configuration Language references to %s                                                | #           |
| Varnish %s happy health probes                                                                 | #           |
| Varnish %s created locks                                                                       | #           |
| Varnish %s destroyed locks                                                                     | #           |
| Varnish %s lock operations                                                                     | #           |
| Total request header bytes received from %s                                                    | b           |
| Total request body bytes received from %s                                                      | b           |
| Total backend response header bytes received from %s                                           | b           |
| Total response body bytes transmitted                                                          | b           |
| Total request bytes sent for piped sessions for %s                                             | b           |
| Piped bytes from Varnish client                                                                | b           |
| Total number of bytes forwarded to clients in pipe sessions                                    | b           |
| Varnish SMS outstanding bytes                                                                  | b           |
| Varnish SMS bytes allocated                                                                    | b           |
| Varnish SMS bytes freed                                                                        | b           |
| Number of bytes used by the persisted ban lists                                                | b           |
| Extra bytes in persisted Varnish ban lists due to fragmentation                                | b           |
| Number of bytes free in the shared memory                                                      | b           |
| Number of bytes used in the shared memory                                                      | b           |
| Number of bytes which will soon (max 1 minute) be freed in the shared memory                   | b           |
| Number of bytes which does not fit in the shared memory                                        | b           |
| Total number of bytes which did not fit in the shared memory                                   | b           |
| Varnish %s size requested                                                                      | b           |
| Varnish %s size allocated                                                                      | b           |
| Varnish %s bytes allocated                                                                     | b           |
| Varnish %s bytes freed                                                                         | b           |
| Varnish %s bytes outstanding                                                                   | b           |
| Varnish %s bytes available                                                                     | b           |
| Total backend response body bytes received from %s                                             | b           |
| Total number of bytes forwarded to %s backend in pipe sessions                                 | b           |
| Total number of bytes forwarded from %s backend in pipe sessions                               | b           |
| Connection dropped, no sess/wrk                                                                | conn        |
| Varnish backend connections success                                                            | conn        |
| Varnish backend connections not attempted                                                      | conn        |
| Varnish backend connections too many                                                           | conn        |
| Varnish backend connections failures                                                           | conn        |
| Count  of  backend  connection reuses                                                          | conn        |
| Varnish backend connections was closed                                                         | conn        |
| Count of backend connection recycles                                                           | conn        |
| Varnish backend connections retry                                                              | conn        |
| Varnish ESI parse errors (unlock)                                                              | errors      |
| Count of cache hits                                                                            | hits        |
| Count of hits for pass                                                                         | hits        |
| Count of misses                                                                                | misses      |
| Varnish child process started                                                                  | procs       |
| Varnish child process normal exit                                                              | procs       |
| Varnish child process unexpected exit                                                          | procs       |
| Varnish child process died (signal)                                                            | procs       |
| Varnish child process core dumped                                                              | procs       |
| Varnish child process panic                                                                    | procs       |
| Client requests received                                                                       | req         |
| Varnish client requests received, subject to 400 errors                                        | req         |
| Varnish client requests received, subject to 411 errors                                        | req         |
| Varnish client requests received, subject to 413 errors                                        | req         |
| Varnish client requests received, subject to 417 errors                                        | req         |
| Good Varnish client requests received                                                          | req         |
| Length of session queue waiting for threads                                                    | req         |
| Number of requests sent to sleep without a worker threads because they found a busy object     | req         |
| Number of requests taken of the busy object sleep list and and rescheduled                     | req         |
| Total Varnish requests                                                                         | req         |
| Varnish SMS allocator requests                                                                 | req         |
| Varnish backend requests made                                                                  | req         |
| Fetch head                                                                                     | resp        |
| Fetch had bad headers                                                                          | resp        |
| Backend response with no body because the request is HEAD                                      | resp        |
| Backend response with Content-Length                                                           | resp        |
| Backend response with Chunked                                                                  | resp        |
| Backend response with EOF from lack of other info                                              | resp        |
| Backend response failed due to unknown Transfer-Encoding                                       | resp        |
| Backend response with EOF due to Connection: Close                                             | resp        |
| Backend response with EOF due to HTTP < 1.1                                                    | resp        |
| Backend response with EOF due to keep-live but neither Chunked or Len                          | resp        |
| Backend response with no body because of 1XX response                                          | resp        |
| Backend response with no body because of 204 response                                          | resp        |
| Backend response with no body because of 304 response                                          | resp        |
| Backend response body fetch failed                                                             | resp        |
| Varnish total fetch                                                                            | resp        |
| Varnish total synth                                                                            | resp        |
| Varnish child process uptime                                                                   | s           |
| Management Varnish process uptime                                                              | s           |
| Count of sessions succesfully accepted                                                         | session     |
| Count of sessions dropped due to the session pipe overflowing                                  | session     |
| Count of failures to accept TCP connection                                                     | session     |
| Count of sessions dropped due to the session pipe overflowing                                  | session     |
| Total Varnish sessions                                                                         | session     |
| Total Varnish pipes                                                                            | session     |
| Total Varnish pass                                                                             | session     |
| Varnish session closed                                                                         | session     |
| Varnish session pipeline                                                                       | session     |
| Varnish session read ahead                                                                     | session     |
| Varnish session herd                                                                           | session     |
| Number of threads in all pools                                                                 | threads     |
| Total number of threads created in all pools                                                   | threads     |
| Total number of threads destroyed in all pools                                                 | threads     |
