---
layout: page
title: Monitoring and collecting data from Zookeeper
description: Information on the metrics collected by the CoScale Zookeeper plugin.
---

> ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.

More information on: [https://zookeeper.apache.org/](https://zookeeper.apache.org/)

## How it works

This plugin gathers metrics for your Zookeeper cluster from the Zookeeper JMX interface.

## Installation

{% include_relative _installation.md orchestrator="false" service="Solr" %}

## Configuration

### Enable JMX

You can find the configuration to setup JMX for Zookeeper on the [Zookeeper documentation](https://zookeeper.apache.org/doc/current/zookeeperJMX.html#ch_starting).

### Provide configuration

Fill in the hostname and the JMX port.

### Active checks

This plugin can be configured to periodically list the top level znodes. The plugin measures the response time for that operation and calculates the uptime of the service.

A Client port should be provided.

<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/zookeeper.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
