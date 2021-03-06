---
layout: page
title: Monitoring and collecting data from Kafka
description: Information on the metrics collected by the CoScale Kafka plugin.
---

> Kafka is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.

More information on: [http://kafka.apache.org/](http://kafka.apache.org/)

## How it works

This plugin analyzes the performance of your Kafka messaging system.

The plugin can get statistics (the number of connections, the number of partitions, etc.) using the JMX interface of the Kafka service and consumers.

**The minimal supported version of Kafka is 0.8.0.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Kafka" %}

## Configuration

### JMX Connection

To gather statistics Kafka should be configured to expose JMX. This can be done by setting the JMX_PORT environment variable before running the kafka-server-start command:

`JMX_PORT=9997 ${KAFKA}/bin/kafka-server-start.sh ${KAFKA}/config/server.properties`

Restart Kafka to apply these changes.

In order to monitor the consumer lags, the agent needs to be installed on the servers running the Kafka consumer and needs to have access to the JMX interface of the consumer. Multiple JMX ports can be provided below in case the Kafka server and consumers are running on the same host.

### Active checks

This plugin can be configured to insert and retrieve a message into your Kafka. This active monitoring allows us to calculate the uptime of the service and the response time of the insert and retrieval of the message.

An existing topic should be provided. This topic should be dedicated for this check, since we will insert and retrieve messages from the topic.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/kafka.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
