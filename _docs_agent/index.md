---
layout: page
title: Agent
description: Overview of information on how to configure, install and maintain the CoScale agent.
---

<a href="{{ site.baseurl }}/agent/install" id="installation" class="btn btn-primary btn-lg pull-right">Create and install the Agent</a>
The CoScale lightweight agent is used to monitor server infrastructure and services, it uses log parsing and global status pages to gather its data and pushes the data to the CoScale platform through HTTPS calls. Below you can find a list of supported plugins and more advanced features.

## Integrations
CoScale gathers data from lots of different orchestrators and application services. Click the icons below to get more information on the metrics, events and installation of a certain integrations. Integrations in CoScale are also sometimes referred to as plugins.

{% include_relative plugins/_technologies.md %}

## GNU Linux / Unix

* [Installing the agent]({{ site.baseurl }}/agent/agent-install#unix)
* [Restarting the agent]({{ site.baseurl }}/agent/agent-restart#unix)
* [Uninstalling the agent]({{ site.baseurl }}/agent/agent-uninstall#unix)
* [Exporting logs for support]({{ site.baseurl }}/agent/export-logs#unix)
* [Configure with environment variables]({{ site.baseurl }}/agent/linux/environment-variables)

## Microsoft Windows

* [Installing the agent]({{ site.baseurl }}/agent/agent-install#microsoft-windows)
* [Restarting the agent]({{ site.baseurl }}/agent/agent-restart#microsoft-windows)
* [Uninstalling the agent]({{ site.baseurl }}/agent/agent-uninstall#microsoft-windows)
* [Exporting logs for support]({{ site.baseurl }}/agent/export-logs#microsoft-windows)
* [RAM disk]({{ site.baseurl }}/agent/windows/ram-disk)

## Extra

### Tips and tricks

* [Cloud environments]({{ site.baseurl }}/agent/cloud/index)
    Specific configuration, agent management and autoscaling tips & tricks for Cloud based providers like Amazon Web Services and Microsoft Azure.

* [Remove a server]({{ site.baseurl }}/agent/remove-server)
    Removing a server or an agent from your application.

* [Troubleshooting]({{ site.baseurl }}/agent/troubleshooting)
    Debugging a running agent to find and fix issues

### Advanced configuration

* [HOST feature]({{ site.baseurl }}/agent/host-feature)
    Monitor services that run on a host from our Container Agent.

* [Firewall / Proxy]({{ site.baseurl }}/agent/firewall-proxy)
    Information about CoScale agent firewall settings and proxy configuration.

* [Environment flags]({{ site.baseurl}}/agent/advanced)
    Advanced environment flags you can use to customize the agent hostname, auto updating functionality and log level.

* [Custom templates]({{ site.baseurl }}/agent/custom-template)
    Specific configuration for config management systems.

### Other
* [Accept webrequests]({{ site.baseurl }}/agent/accept-webrequests)
    Manually accept specific web requests.

* [Refine webrequests]({{ site.baseurl }}/agent/webrequest-method)
    Specific configuration for tracking web requests by their HTTP method.



