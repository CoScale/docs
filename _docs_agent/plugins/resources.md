---
layout: page
title: Monitoring and collecting performance data from your servers
description: Information on the metrics collected by the CoScale Resources plugin.
---

> The Resources plugin gathers information about the server resource usage: CPU, Memory, Network, Disk, Filesystem, OS.

## How it works

The plugin gathers OS and hardware metrics from the underlying system. No configuration is required. Below you can find the metrics list for [Linux](#resources--linux--cpu) and [Windows](#resources--windows--cpu).

## Installation

{% include_relative _installation.md orchestrator="false" %}

<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/resources.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>

