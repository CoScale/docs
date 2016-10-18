---
layout: page
title: CollectD plugin
description: Information on the metrics collected by the CoScale CollectD plugin.
---

> CollectD is a daemon which collects system and application performance metrics periodically and provides mechanisms to store the values in a variety of ways.

More information on: [https://collectd.org/](https://collectd.org/)

## Configuration

collectd gathers statistics about the system it is running on and stores this information. Those statistics can then be used to find current performance bottlenecks (i.e. performance analysis) and predict future system load (i.e. capacity planning).

The UnixSock collectd plugin opens a UNIX domain socket and accepts connections. Using this socket CoScale Agent can send commands to the daemon and receive information.

<img src="/gfx/agent/plugins/collectd/collectd-configuration.png" alt="CollectD Configuration">

## Metrics

There are no default metrics. We gather the metrics specified by the customer.
