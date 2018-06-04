---
layout: page
title: Monitoring and collecting data from Solr
description: Information on the metrics collected by the CoScale Solr plugin.
---

> Solr is highly reliable, scalable and fault tolerant, providing distributed indexing, replication and load-balanced querying, automated failover and recovery, centralized configuration and more. Solr powers the search and navigation features of many of the world's largest Internet sites.

More information on: [http://lucene.apache.org/solr/](http://lucene.apache.org/solr/)

## How it works

The plugin can get statistics about Solr collections using the JMX interface. It captures queries and requests statistics, as well as used resources information (CPU load, memory size, swap, etc).

**The minimal supported version of Solr is 5.2.0**

## Installation

{% include_relative _installation.md orchestrator="false" service="Solr" %}

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

<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/solr.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
