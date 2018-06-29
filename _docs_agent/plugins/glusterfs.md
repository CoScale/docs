---
layout: page
title: Monitoring and collecting data from GlusterFS
description: Information on the metrics collected by the CoScale GlusterFS plugin.
---

> GlusterFS is a scalable network filesystem suitable for data-intensive tasks such as cloud storage and media streaming. GlusterFS is free and open source software and can utilize common off-the-shelf hardware.

More information on: [https://docs.gluster.org/en/latest/](https://docs.gluster.org/en/latest/)

## How it works

This plugin gathers statistics about your GlusterFS storage system. The metrics are collected via the gluster command.

## Installation

{% include_relative _installation.md orchestrator="false" service="GlusterFS" %}

## Configuration

To view volume profile data, like operation latency and counts, you need to start profiling for those volumes:

`gluster volume profile <volume> start`

Keep in mind that his can cause a performance degradation in certain use-cases and should be used for debugging.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/glusterfs.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
