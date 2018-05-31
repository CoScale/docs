---
layout: page
title: Monitoring and collecting data from JMX
description: Information on the metrics collected by the CoScale JMX plugin.
---

> The JMX technology provides a simple, standard way of managing resources such as applications, devices, and services. Because the JMX technology is dynamic, you can use it to monitor and manage resources as they are created, installed and implemented. You can also use the JMX technology to monitor and manage the Java Virtual Machine (Java VM).

More information on: [http://docs.oracle.com/javase/tutorial/jmx/](http://docs.oracle.com/javase/tutorial/jmx/)

## How it works

CoScale JMX plugin collects custom metrics from your local JMX server using a JMX endpoint. By default CoScale will gather JVM metrics like CPU, Memory, GC, Threads. Custom metrics can be gathered by providing a bean or metric definition. CoScale also supports parsing metrics from JMX using [Jolokia]({{ site.baseurl }}/agent/plugins/jolokia).

## Installation

{% include_relative _installation.md orchestrator="false" service="JMX" %}

## Configuration

## JMX Connection

Provide JMX hostname and port

<img src="/gfx/agent/plugins/jmx/JMX-Configuration-01.png" alt="JMX Configuration Step 1">

## Bean configuration

You can add custom bean names and attributes.

If you want the same bean to have multiple attributes, add a new bean with the same name and your prefered attribute. To configure JMX metrics, you can choose between two configuration formats:

* MBEANS format

    Requires only the bean name and attributes, the metric details will be automatically generated.

    `BEANS:<"mbean"> <"attribute1"> ["attribute2"]`

* METRIC format

    Allows to define custom metrics. Note: This format doesn't accept multiple attributes on the same configuration line.

    `METRIC:<"mbean> <"attribute"> <"Custom Name"> <"unit"> <"dimension1:dimensionValue1,dimension2:dimensionValue2">`

<img src="/gfx/agent/plugins/jmx/JMX-Configuration-02.png" alt="JMX Configuration Step 2">


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/jmx.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
