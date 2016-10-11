---
layout: page
title: Apache plugin
description: Information on the metrics collected by the CoScale Apache plugin.
---

> The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server for modern operating systems including UNIX and Windows.

More information on: [https://httpd.apache.org/](https://httpd.apache.org/)

## Events

* Service state

## Metrics

| Metric name                                       | Metric unit |
|---------------------------------------------------|-------------|
| Apache total number of accesses                   | access      |
| Apache bytes per request                          | b/req       |
| Apache bytes per second                           | b/s         |
| Apache ConnsAsyncClosing                          | conn        |
| Apache ConnsAsyncKeepAlive                        | conn        |
| Apache ConnsAsyncWriting                          | conn        |
| Apache CPULoad                                    | %           |
| Apache requests per second                        | req/s       |
| Apache total bytes transferred                    | b           |
| Busy Apache workers                               | workers     |
| Idle Apache workers                               | workers     |
| Number of connections to Apache                   | conn        |
| Number of seconds since the Apache server started | s           |

## Notes

* `ExtendedStatus` has to be `On` for global statistics
