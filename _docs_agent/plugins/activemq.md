---
layout: page
title: Monitoring and collecting data from ActiveMQ
description: Information on the metrics collected by the CoScale ActiveMQ plugin.
---

> Apache ActiveMQ is the most popular and powerful open source messaging and Integration Patterns server. Apache ActiveMQ is fast, supports many Cross Language Clients and Protocols, comes with easy to use Enterprise Integration Patterns and many advanced features while fully supporting JMS 1.1 and J2EE 1.4. Apache ActiveMQ is released under the Apache 2.0 License

More information on: [http://activemq.apache.org/](http://activemq.apache.org/)

## How it works

The plugin can get statistics about ActiveMQ topics and queues using the JMX interface.

**The minimal supported version of ActiveMQ is 5.10.0**

## Installation

{% include_relative _installation.md orchestrator="false" service="ActiveMQ" %}

## Configuration

### Enable JMX

Update activemq.xml config file with the following. The useJMX field of the broker needs to be set to true.

{% highlight xml %}
<broker xmlns="http://activemq.apache.org/schema/core"
        useJmx="true"
        brokerName="localhost"
        dataDirectory="${activemq.base}/data">
{% endhighlight %}

The management context needs to be present and enabled

{% highlight xml %}
<!-- Use the following to configure how ActiveMQ is exposed in JMX -->
<managementContext>
    <managementContext createConnector="true" />
</managementContext>
{% endhighlight %}

The connector will be created in by default on localhost:1099.

### Active checks

This plugin can be configured to post and receive a message to an ActiveMQ queue. This active monitoring allows us to calculate the uptime of the service and the response time of the insert and retrieval of the message.

The plugin uses the STOMP protocol in order to send and receive messages from the ActiveMQ broker. This needs to be enabled for active checks to work.
{% highlight xml %}
<transportConnectors>
    ...
    <transportConnector name="stomp" uri="stomp://0.0.0.0:61613?maximumConnections=1000&amp;wireFormat.maxFrameSize=104857600"/>
    ...
</transportConnectors>
{% endhighlight %}
The STOMP port and an optional login and password need to be provided. Also an existing queue should be specified. This queue should be dedicated for this check, since we will insert and retrieve messages from it.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/activemq.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
