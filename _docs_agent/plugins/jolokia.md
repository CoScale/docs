---
layout: page
title: Monitoring and collecting data from Jolokia
description: Information on the metrics collected by the CoScale Jolokia plugin.
---

> Jolokia is remote JMX with JSON over HTTP. It's a JMX-HTTP bridge giving an alternative to JSR-160 connectors. It is an agent based approach with support for many platforms. In addition to basic JMX operations it enhances JMX remoting with unique features like bulk requests and fine grained security policies.

## How it works

This plugin will allow you to extract metrics from Jolokia compatible APIs. It will capture the metrics from the metrics endpoint specified.

## Installation

{% include_relative _installation.md orchestrator="false" service="Jolokia" %}

## Configuration

### JMX Connection

Provide the JMX hostname and JMX port

<img src="/gfx/agent/plugins/jolokia/01-Jolokia-JMX-Configuration.png" alt="Jolokia Configuration Step 1">

### Bean configuration

You can add custom bean names and attributes.

<img src="/gfx/agent/plugins/jolokia/02-Jolokia-Bean-Configuration.png" alt="Jolokia Configuration Step 2">

### Active checks

This plugin can be configured to perform a HTTP GET on your Jolokia endpoint. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

<img src="/gfx/agent/plugins/jolokia/03-Jolokia-Active-Checks.png" alt="Jolokia Configuration Step 3">


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/jolokia.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
