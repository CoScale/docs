---
layout: page
title: JMX plugin
description: Information on the metrics collected by the CoScale JMX plugin.
---

> The JMX technology provides a simple, standard way of managing resources such as applications, devices, and services. Because the JMX technology is dynamic, you can use it to monitor and manage resources as they are created, installed and implemented. You can also use the JMX technology to monitor and manage the Java Virtual Machine (Java VM).

More information on: [http://docs.oracle.com/javase/tutorial/jmx/](http://docs.oracle.com/javase/tutorial/jmx/)

## How it works

CoScale JMX plugin collects custom metrics from your local JMX server using a JMX endpoint. By default CoScale will gather JVM metrics like CPU, Memory, GC, Threads. Custom metrics can be gathered by providing a bean or metric definition.

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

## Metrics

| Metric name                    | Metric unit |
|--------------------------------|-------------|
| JMX Thread CPU Time            | %           |
| JMX active check uptime        | %           |
| JMX BufferPool Memory Used     | b           |
| JMX Memory Usage Committed     | b           |
| JMX Memory Usage Init          | b           |
| JMX Memory Usage Max           | b           |
| JMX Memory Usage Used          | b           |
| JMX GC Collection Time         | ms          |
| JMX Total Process Cpu Time     | ms          |
| JMX Total Compilation Time     | ms          |
| JMX Uptime                     | ms          |
| JMX active check latency       | s           |
| JMX GC Collection Count        |             |
| JMX BufferPool Count           |             |
| JMX Daemon Thread Count        |             |
| JMX Thread Count               |             |
| JMX Total Started Thread Count |             |
| JMX Loaded Class Count         |             |
| JMX Unloaded Class Count       |             |
| JMX Max File Descriptor Count  |             |
| JMX Open File Descriptor Count |             |


# <a name="jolokia"></a>Jolokia

> Jolokia is remote JMX with JSON over HTTP. It's a JMX-HTTP bridge giving an alternative to JSR-160 connectors. It is an agent based approach with support for many platforms. In addition to basic JMX operations it enhances JMX remoting with unique features like bulk requests and fine grained security policies.

## How it works

This plugin will allow you to extract metrics from Jolokia compatible APIs. It will capture the metrics from the metrics endpoint specified.

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

## Metrics

| Metric name                        | Metric unit |
|------------------------------------|-------------|
| Jolokia BufferPool Count           |             |
| Jolokia BufferPool Memory Used     | b           |
| Jolokia Compilation Time           | ms          |
| Jolokia Daemon Thread Count        |             |
| Jolokia Garbage Collections        |             |
| Jolokia GC Collection Time         | ms          |
| Jolokia Loaded Class Count         |             |
| Jolokia Max File Descriptor Count  |             |
| Jolokia Memory Usage Committed     | b           |
| Jolokia Memory Usage Init          | b           |
| Jolokia Memory Usage Max           | b           |
| Jolokia Memory Usage Used          | b           |
| Jolokia Open File Descriptor Count |             |
| Jolokia Process CPU time           | ms          |
| Jolokia Started Threads            |             |
| Jolokia Thread Count               |             |
| Jolokia Thread CPU Time            | %           |
| Jolokia Unloaded Class Count       |             |
| Jolokia Uptime                     | ms          |
