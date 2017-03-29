---
layout: page
title: JMX plugin
description: Information on the metrics collected by the CoScale JMX plugin.
---

> The JMX technology provides a simple, standard way of managing resources such as applications, devices, and services. Because the JMX technology is dynamic, you can use it to monitor and manage resources as they are created, installed and implemented. You can also use the JMX technology to monitor and manage the Java Virtual Machine (Java VM).

More information on: [http://docs.oracle.com/javase/tutorial/jmx/](http://docs.oracle.com/javase/tutorial/jmx/)

## Configuration

Step 1: Provide JMX hostname and port:

<img src="/gfx/agent/plugins/jmx/JMX-Configuration-01.png" alt="JMX Configuration Step 1">

Step 2: Bean configuration:

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
