---
layout: page
title: Monitoring and collecting data from Fluentd
description: Information on the metrics collected by the CoScale Fluentd plugin.
---

> Fluentd is an open source data collector for unified logging layer. Fluentd tries to structure data as JSON as much as possible: this allows Fluentd to unify all facets of processing log data: collecting, filtering, buffering, and outputting logs across multiple sources and destinations (Unified Logging Layer). Fluentd supports memory- and file-based buffering to prevent inter-node data loss. Fluentd also support robust failover and can be set up for high availability.

More information on: [https://www.fluentd.org](https://www.fluentd.org)

## How it works

This plugin gets statistics about Fluentd.

## Installation

{% include_relative _installation.md orchestrator="false" service="FluentD" %}

## Configuration

Fluentd has a monitoring agent to retrieve internal metrics in JSON via HTTP. Please add the following lines to your configuration file:

{% highlight fluentd %}
<source>
  @type monitor_agent
  bind 0.0.0.0
  port 24220
</source>
{% endhighlight %}

Also, provide the hostname and port.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/fluentd.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
