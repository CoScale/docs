---
layout: page
title: Monitoring and collecting data from CollectD
description: Information on the metrics collected by the CoScale CollectD plugin.
---

> CollectD is a daemon which collects system and application performance metrics periodically and provides mechanisms to store the values in a variety of ways.

More information on: [https://collectd.org/](https://collectd.org/)

## How it works

Collectd gathers statistics about the system it is running on and stores this information. Those statistics can then be used to find current performance bottlenecks (i.e. performance analysis) and predict future system load (i.e. capacity planning).

The UnixSock collectd plugin opens a UNIX domain socket and accepts connections. Using this socket CoScale Agent can send commands to the daemon and receive information.

## Installation

{% include_relative _installation.md orchestrator="false" service="CollectD" %}

## Configuration

CoScale agent communicates with collectd through UnixSock collectd plugin .

To activate UnixSock plugin on collectd, edit the configuration file: `/etc/collectd.conf`

Uncomment the following line:
`#LoadPlugin unixsock`

Add to the end of the configuration file (before include directive), the following lines:

{% highlight xml %}
<Plugin unixsock>
    SocketFile "/var/run/csplugin-unixsock"
    SocketGroup "collectd"
    SocketPerms "0660"
    DeleteSocket false
</Plugin>
{% endhighlight %}

## Metrics

There are no default metrics. We gather the metrics specified by the customer.
