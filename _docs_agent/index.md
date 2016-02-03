---
layout: page
title: Agent
description: Overview of information on how to configure, install and maintain the CoScale agent.
---

<a href="{{ site.baseurl }}/agent/install" class="btn btn-primary btn-lg pull-right">How to create and install the Agent</a>
The CoScale lightweight agent is used to monitor server infrastructure and services, it uses log parsing and global status pages to gather its data and pushes the data to the CoScale platform through HTTPS calls. Below you can find a list of supported plugins and more advanced features.

## Plugins
Overview of all plugins with more information about the metrics gathered and special features.

<div class="row">
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/apache">Apache</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/cassandra">Cassandra</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/couchdb">CouchDb</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/elasticsearch">ElasticSearch</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/haproxy">HAProxy</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/hhvm">HHVM</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/iis">IIS</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/log">Log</a></div>
</div>

## Commands and information

* [Installing the Agent]({{ site.baseurl }}/agent/agent-install)
* [Restarting the Agent]({{ site.baseurl }}/agent/agent-restart)
* [Stopping the Agent]({{ site.baseurl }}/agent/agent-uninstall)
* [Export logs]({{ site.baseurl }}/agent/export-logs)

## Extra

* [GNU Linux / Unix]({{ site.baseurl }}/agent/linux/index)

    Specific configuration and agent management for Unix based operation systems.

* [Microsoft Windows]({{ site.baseurl }}/agent/windows/index)

    Specific configuration and agent management for Microsoft Windows.

* [Cloud environments]({{ site.baseurl }}/agent/cloud/index)

    Specific configuration, agent management and autoscaling tips & tricks for Cloud based providers like Amazon Web Services and Microsoft Azure.

* [Environment flags]({{ site.baseurl}}/agent/advanced)

    Advanced environment flags you can use to customize the agent hostname, auto updating functionality and log level.

* [Firewall / Proxy]({{ site.baseurl }}/agent/firewall-proxy)

    Information about CoScale agent firewall settings and proxy configuration.

* [Custom templates]({{ site.baseurl }}/agent/custom-template)

    Specific configuration for custom templates.
