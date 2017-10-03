---
layout: page
title: Custom metrics
description: Information on how to push custom metrics to the CoScale platform.
---

Custom metrics allow you to monitor aspects of your application that are not monitored by default with CoScale. CoScale provides a couple of methods of integrating these metrics into our platform. With the [generic script]({{ site.baseurl }}/custom-metrics/generic-script/index), [log plugin]({{ site.baserurl }}/agent/plugins/log/) and [CLI]({{ site.baseurl }}/custom-metrics/cli/) it's possible to write small custom integrations for your environment. CoScale also supports pushing metrics from within your code using [StatsD]({{ site.baseurl }}/custom-metrics/statsd/index), [JMX]({{ site.baserurl }}/agent/plugins/jmx/) or [Prometheus]({{ site.baserurl }}/agent/plugins/prometheus/). 

## Methods

### [Pulling metrics from your application with generic script]({{ site.baseurl }}/custom-metrics/generic-script/index)

The CoScale agent can execute scripts or executables to gathers metrics from your application and pushes those to the platform. We provide some example scripts and guide your in configuring it for your application.

### [Pushing metrics with our CLI]({{ site.baseurl }}/custom-metrics/cli/)

The CoScale CLI allows you to push multiple metrics at the same time from the command line. You can use it together with Bash scripts to get your custom data inside CoScale. The CoScale CLI is available as an executable or Docker image. When using our CoScale agent package installion it is installed by default.

### [Pulling metrics with Agent Log plugin]({{ site.baserurl }}/agent/plugins/log/)

The CoScale agent supports retrieving data from existing log files using a regular expression. The plugin can be used to count the number of lines that match a certain regex, as well as get information from within the log lines. 

### [JMX Plugin]({{ site.baserurl }}/agent/plugins/jmx/)

The CoScale agent can retrieve metrics from JMX endpoints. By default the agent will retrieve JVM related information, but other metrics can be added using the `MBEANS` or `METRICS` format.

### [Prometheus Plugin]({{ site.baserurl }}/agent/plugins/prometheus/)

The CoScale agent can retrieve metrics and events from Prometheus endpoints. The plugin will parse all available information coming from the endpoint, including dimensions. 

### [StatsD]({{ site.baseurl }}/custom-metrics/statsd/index)

CoScale provides a StatsD plugin to push data gathered in the StatsD or CollectD daemons immediatly to CoScale.

### [CoScale API]({{ site.baseurl }}/api/)

As a last resort the CoScale API is available for advanced configuration and integration. An SDK is available for Java and PHP. 

