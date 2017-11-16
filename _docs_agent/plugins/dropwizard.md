---
layout: page
title: Dropwizard plugin
description: Information on the metrics collected by the CoScale Dropwizard plugin.
---

> Dropwizard is a Java framework for developing ops-friendly, high-performance, RESTful web services. Dropwizard pulls together stable, mature libraries from the Java ecosystem into a simple, light-weight package that lets you focus on getting things done. Dropwizard has out-of-the-box support for sophisticated configuration, application metrics, logging, operational tools, and much more, allowing you and your team to ship a production-quality web service in the shortest time possible.

More information on: [http://www.dropwizard.io](http://www.dropwizard.io)

## How it works

This plugin analyzes the performance of your Dropwizard web application. It captures traffic rates, latencies and response codes of http requests sent to the web server by parsing the Dropwizard access log file. The plugin can optionally get global statistics (eg. the number of connections, JVM metrics, etc.) by parsing the metrics reported by AdminServlet of the Dropwizard application. Both, the access log and AdminServlet require a bit of configuration, see steps below.

**The minimal supported version of Dropwizard is 1.0.0.**

## Global statistics

For gathering global statistics (eg. number of connections, etc.), the metrics page should be enabled.

Add the following lines in your application YAML configuration file:

{% highlight dropwizard %}
server:
  adminConnectors:
    - type: http
      port: 8081
{% endhighlight %}

Restart the application to apply these changes.  
Provide the metrics URL, as you configured it on your server.

## Log configuration

Enable the Dropwizard application access log format. Add the following lines to your application YAML configuration file:

{% highlight dropwizard %}
server:
  requestLog:
    appenders:
      - type: file
        logFormat: '%h "%r" %D %s %b'
        currentLogFilename: /var/log/dropwizard-app/access.log
        archivedLogFilenamePattern: /var/log/dropwizard-app/accedd-%d.log.gz
{% endhighlight %}

Restart Dropwizard application to apply these changes.  

Provide the location of the access log file you configured and the log format.

For example,

Filename: `/var/log/dropwizard-app/access.log`  
Log format: `%h "%r" %D %s %b`

| Value          | Original Value | Remarks                     |
|----------------|----------------|-----------------------------|
| Hostname       | %h             |                             |
| Request        | \"%r\"         |                             |
| Latency        | %D             | represented in milliseconds |
| Latency        | %T             | represented in seconds      |
| Status Code    | %s             |                             |
| Bytes Sent     | %b             |                             |


## Active checks

This plugin can be configured to perform a HTTP GET on your Dropwizard application. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost/test_page.php`) should be provided.

## Events

* Service state

## Metrics

| Metric name                                                   | Metric unit |
|---------------------------------------------------------------|-------------|
| Dropwizard active check latency                               | s           |
| Dropwizard active check uptime                                | %           |
| Dropwizard DB Managed Pooled Data Source active               | #           |
| Dropwizard DB Managed Pooled Data Source idle                 | #           |
| Dropwizard DB Managed Pooled Data Source size                 | #           |
| Dropwizard DB Managed Pooled Data Source waiting              | #           |
| Dropwizard jetty MutableServletContextHandler percent-4xx     | %           |
| Dropwizard jetty MutableServletContextHandler percent-5xx     | %           |
| Dropwizard JVM blocked threads                                | #           |
| Dropwizard JVM classloader loaded                             | #           |
| Dropwizard JVM classloader unloaded                           | #           |
| Dropwizard JVM Code-Cache memory pools committed              | b           |
| Dropwizard JVM Code-Cache memory pools init                   | b           |
| Dropwizard JVM Code-Cache memory pools max                    | b           |
| Dropwizard JVM Code-Cache memory pools usage                  |             |
| Dropwizard JVM Code-Cache memory pools used                   | b           |
| Dropwizard JVM Compressed-Class-Space memory pools committed  | b           |
| Dropwizard JVM Compressed-Class-Space memory pools init       | b           |
| Dropwizard JVM Compressed-Class-Space memory pools max        | b           |
| Dropwizard JVM Compressed-Class-Space memory pools usage      |             |
| Dropwizard JVM Compressed-Class-Space memory pools used       | b           |
| Dropwizard JVM daemon threads                                 | #           |
| Dropwizard JVM deadlock threads                               | #           |
| Dropwizard JVM direct buffers capacity                        | b           |
| Dropwizard JVM direct buffers count                           | #           |
| Dropwizard JVM direct buffers used                            | b           |
| Dropwizard JVM filedescriptor                                 |             |
| Dropwizard JVM GC PS-MarkSweep count                          | #           |
| Dropwizard JVM GC PS-MarkSweep time                           |             |
| Dropwizard JVM GC PS-Scavenge count                           | #           |
| Dropwizard JVM GC PS-Scavenge time                            |             |
| Dropwizard JVM heap memory committed                          | b           |
| Dropwizard JVM heap memory init                               | b           |
| Dropwizard JVM heap memory max                                | b           |
| Dropwizard JVM heap memory usage                              |             |
| Dropwizard JVM heap memory used                               | b           |
| Dropwizard JVM mapped buffers capacity                        | b           |
| Dropwizard JVM mapped buffers count                           | #           |
| Dropwizard JVM mapped buffers used                            | b           |
| Dropwizard JVM Metaspace memory pools committed               | b           |
| Dropwizard JVM Metaspace memory pools init                    | b           |
| Dropwizard JVM Metaspace memory pools max                     | b           |
| Dropwizard JVM Metaspace memory pools usage                   |             |
| Dropwizard JVM Metaspace memory pools used                    | b           |
| Dropwizard JVM MutableServletContextHandler active dispatches | #           |
| Dropwizard JVM MutableServletContextHandler active requests   | #           |
| Dropwizard JVM MutableServletContextHandler active suspended  | #           |
| Dropwizard JVM new threads                                    | #           |
| Dropwizard JVM non-heap memory committed                      | b           |
| Dropwizard JVM non-heap memory init                           | b           |
| Dropwizard JVM non-heap memory max                            | b           |
| Dropwizard JVM non-heap memory usage                          |             |
| Dropwizard JVM non-heap memory used                           | b           |
| Dropwizard JVM PS-Eden-Space memory pools committed           | b           |
| Dropwizard JVM PS-Eden-Space memory pools init                | b           |
| Dropwizard JVM PS-Eden-Space memory pools max                 | b           |
| Dropwizard JVM PS-Eden-Space memory pools usage               |             |
| Dropwizard JVM PS-Eden-Space memory pools used                | b           |
| Dropwizard JVM PS-Eden-Space memory pools used after gc       | b           |
| Dropwizard JVM PS-Survivor-Space memory pools committed       | b           |
| Dropwizard JVM PS-Survivor-Space memory pools init            | b           |
| Dropwizard JVM PS-Survivor-Space memory pools max             | b           |
| Dropwizard JVM PS-Survivor-Space memory pools usage           |             |
| Dropwizard JVM PS-Survivor-Space memory pools used            | b           |
| Dropwizard JVM PS-Survivor-Space memory pools used after gc   | b           |
| Dropwizard JVM QueuedThreadPool dw jobs                       | #           |
| Dropwizard JVM QueuedThreadPool dw size                       | #           |
| Dropwizard JVM QueuedThreadPool dw utilization                | #           |
| Dropwizard JVM QueuedThreadPool dw utilization-max            | #           |
| Dropwizard JVM runnable threads                               | #           |
| Dropwizard JVM terminated threads                             | #           |
| Dropwizard JVM threads                                        | #           |
| Dropwizard JVM timed_waiting threads                          | #           |
| Dropwizard JVM total memory init                              | b           |
| Dropwizard JVM total memory max                               | b           |
| Dropwizard JVM total memory used                              | b           |
| Dropwizard JVM Uptime                                         | s           |
| Dropwizard JVM waiting threads                                | #           |
