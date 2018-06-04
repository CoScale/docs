---
layout: page
title: Monitoring and collecting data from Riak
description: Information on the metrics collected by the CoScale Riak plugin.
---

> Riak KV is a distributed NoSQL database that is highly available, scalable and easy to operate. It automatically distributes data across the cluster to ensure fast performance and fault-tolerance.

More information on: [http://basho.com/](http://basho.com/)

## How it works

This plugin analyzes the performance of your Riak server. No additional configuration is required.

**The minimal supported version of riak-admin is 1.2.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Riak" %}


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/riak.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
