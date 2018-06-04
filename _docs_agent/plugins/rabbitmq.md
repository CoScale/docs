---
layout: page
title: Monitoring and collecting data from RabbitMQ
description: Information on the metrics collected by the CoScale RabbitMQ plugin.
---

> RabbitMQ is a messaging broker - an intermediary for messaging. It gives your applications a common platform to send and receive messages.

More information on: [https://www.rabbitmq.com/](https://www.rabbitmq.com/)

## How it works

The plugin gathers statistics (memory usage, queue length, etc) for RabbitMQ by connecting to the RabbitMQ management plugin. This plugin is not installed by default, see next steps.

**The minimal supported version of RabbitMQ is 2.7.**

## Installation

{% include_relative _installation.md orchestrator="false" service="RabbitMQ" %}

## Configuration

### Enable RabbitMQ management

Enabled the RabbitMQ management plugin by executing the following command line:

`rabbitmq-plugins enable rabbitmq_management`

### Active checks

This plugin can be configured to insert and retrieve a message into your RabbitMQ. This active monitoring allows us to calculate the uptime of the service and the response time of the insert and retrieval of the message.

An existing queue should be provided. This queue should be dedicated for this check, since we will insert and retrieve messages from the queue.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/rabbitmq.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
