---
layout: page
title: Solr plugin
description: Information on the metrics collected by the CoScale Solr plugin.
---

> Solr is highly reliable, scalable and fault tolerant, providing distributed indexing, replication and load-balanced querying, automated failover and recovery, centralized configuration and more. Solr powers the search and navigation features of many of the world's largest Internet sites.

More information on: [http://lucene.apache.org/solr/](http://lucene.apache.org/solr/)

## How it works

The plugin can get statistics about Solr collections using the JMX interface.

**The minimal supported version of Solr is 5.2.0**

## Configuration

### Enable JMX

In the solrconfig.xml file of a core/collection (e.g.: {install_dir}/server/solr/gettingstarted/conf/solrconfig.xml) place this directive:

`<jmx />`

and start the Solr server by explicitly allowing access to JMX:
`bin/solr start -a -Dcom.sun.management.jmxremote -Djava.rmi.server.hostname=127.0.0.1 -Dcom.sun.management.jmxremote.port=9999 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false`


### Provide configuration

Fill in the hostname and the JMX port.

### Active checks

This plugin can be configured to perform a HTTP GET on your Solr. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost:8983/solr/gettingstarted/select?q=*&wt=json`) should be provided.

## Events

* Service state

## Metrics

| Metric name                                                 | Metric unit |
|-------------------------------------------------------------|-------------|
| Solr heap memory size                                       | b           |
| Number of seconds that the Solr server has been up          | s           |
| Solr auto commits per second                                | req/s       |
| Solr cache evictions per second                             | req/s       |
| Solr cache hit ratio                                        | %           |
| Solr cache inserts per second                               | req/s       |
| Solr commits per second                                     | req/s       |
| Solr ConcurrentMarkSweep garbage collector collection count | #           |
| Solr ConcurrentMarkSweep garbage collector collection time  | s           |
| Solr CPU Time                                               | s           |
| Solr deleted docs per second                                | doc/s       |
| Solr deletes by id per second                               | req/s       |
| Solr deletes by query per second                            | req/s       |
| Solr docs per second                                        | doc/s       |
| Solr errors per second                                      | req/s       |
| Solr free physical memory size                              | b           |
| Solr free swap space size                                   | b           |
| Solr highlight per second                                   | req/s       |
| Solr non heap memory size                                   | b           |
| Solr ParNew garbage collector collection count              | #           |
| Solr ParNew garbage collector collection time               | s           |
| Solr Process CPU Load                                       |             |
| Solr requests per second                                    | req/s       |
| Solr select time per request                                | s           |
| Solr soft auto commits per second                           | req/s       |
| Solr System CPU Load                                        |             |
| Solr System load average                                    |             |
| Solr threading daemon thread count                          | threads     |
| Solr threading Peak thread count                            | threads     |
| Solr threading thread count                                 | threads     |
| Solr threading total started thread count                   | threads     |
| Solr total swap space size                                  | b           |
