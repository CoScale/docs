---
layout: page
title: Memcached plugin
description: Information on the metrics collected by the CoScale Memcached plugin.
---

> Memcached is a free & open source, high-performance, distributed memory object caching system, generic in nature, but intended for use in speeding up dynamic web applications by alleviating database load. Memcached is an in-memory key-value store for small chunks of arbitrary data (strings, objects) from results of database calls, API calls, or page rendering.

More information on: [https://memcached.org/](https://memcached.org/)

## How it works

The Memcached plugin gathers statistics such as the number of connections, the number of gets, etc. using the Memcached interface.

These statistics are gathered in Memcached by default and no additional configuration is required. Just provide the connection details for the Memcached server and the plugin is ready to go.

**The minimal supported version of Memcached is 1.4.**

## Configuration

### Connection details

The CoScale plugin requires the host and port to the local Memcached service. It is possible to supply multiple hosts and ports if you are running multiple Memcached instances on the same machine.

## Active checks

This plugin can be configured to perform a command on your Memcached. This active monitoring allows us to calculate the uptime of the service and the response time of the command.

A valid Memcached command (eg. get my-test-key) should be provided.

## Events

* Service state

## Metrics

| Metric name                                                                                | Metric unit |
|--------------------------------------------------------------------------------------------|-------------|
| Accepting connections by Memcached                                                         | conn        |
| Bytes currently used by Memcached hash tables                                              | b           |
| Current connections to Memcached                                                           | conn        |
| Expired Memcached items that were never touched.                                           | #/s         |
| Max connections reached to Memcached                                                       | conn        |
| Memcached auth commands                                                                    | #/s         |
| Memcached auth errors                                                                      | #/s         |
| Memcached bytes in cache                                                                   | b           |
| Memcached bytes read from the network                                                      | b           |
| Memcached bytes written to the network                                                     | b           |
| Memcached check and set bad value                                                          | #/s         |
| Memcached check and set hits                                                               | #/s         |
| Memcached check and set misses                                                             | #/s         |
| Memcached connection structures                                                            | #           |
| Memcached decrement hits                                                                   | #/s         |
| Memcached decrement misses                                                                 | #/s         |
| Memcached delete hits                                                                      | #/s         |
| Memcached delete misses                                                                    | #/s         |
| Memcached evicted items that were never touched.                                           | #/s         |
| Memcached evictions                                                                        | #/s         |
| Memcached flush commands                                                                   | #/s         |
| Memcached get commands                                                                     | #/s         |
| Memcached get hits                                                                         | #/s         |
| Memcached get misses                                                                       | #/s         |
| Memcached increment hits                                                                   | #/s         |
| Memcached increment misses                                                                 | #/s         |
| Memcached items in cache                                                                   | items       |
| Memcached max size cache                                                                   | b           |
| Memcached reclaimed                                                                        | #/s         |
| Memcached reversed file descriptors                                                        | #           |
| Memcached set commands                                                                     | #/s         |
| Memcached system time                                                                      | %           |
| Memcached touch commands                                                                   | #/s         |
| Memcached touch hits                                                                       | #/s         |
| Memcached touch misses                                                                     | #/s         |
| Memcached user time                                                                        | %           |
| Number of Memcached worker threads requested                                               | threads     |
| Number of secs since the Memcached server started                                          | s           |
| Number of times any connection to Memcached yielded to another due to hitting the -R limit | conn        |
| Process id of Memcached server process                                                     |             |
| Total connections to Memcached                                                             | conn        |
| Total Memcached items                                                                      | items       |
