---
layout: page
title: Monitoring and collecting data from Cassandra
description: Information on the metrics collected by the CoScale Cassandra plugin.
---


>  The Apache Cassandra database is the right choice when you need scalability and high availability without compromising performance. Linear scalability and proven fault-tolerance on commodity hardware or cloud infrastructure make it the perfect platform for mission-critical data. Cassandra's support for replicating across multiple datacenters is best-in-class, providing lower latency for your users and the peace of mind of knowing that you can survive regional outages.

More information on: [http://cassandra.apache.org/](http://cassandra.apache.org/)

## How it works

This plugin gathers some global statistics from your Cassandra server.

It gets these statistics using Cassandra's JMX interface.

## Installation

{% include_relative _installation.md orchestrator="false" service="Cassandra" %}

## Configuration

### Enable JMX Connection
To enable JMX in Cassandra, add the following line in `<instalation_folder>/conf/cassandra-env.sh`.

`JVM_OPTS="$JVM_OPTS -Djava.rmi.server.hostname=localhost"`

Restart Cassandra to apply these changes.

### Active checks
This plugin can be configured to perform a CQL query on your Cassandra. This active monitoring allows us to calculate the uptime of the service and the response time of the provided query.

A keyspace and valid CQL query (eg. `SELECT * FROM users WHERE first_name = 'jane' and last_name='smith';`) should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/cassandra.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
