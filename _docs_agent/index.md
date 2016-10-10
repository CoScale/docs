---
layout: page
title: Agent
description: Overview of information on how to configure, install and maintain the CoScale agent.
---

<a href="{{ site.baseurl }}/agent/install" id="installation" class="btn btn-primary btn-lg pull-right">Create and install the Agent</a>
The CoScale lightweight agent is used to monitor server infrastructure and services, it uses log parsing and global status pages to gather its data and pushes the data to the CoScale platform through HTTPS calls. Below you can find a list of supported plugins and more advanced features.

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

## Plugins
Overview of all plugins with more information about the metrics gathered and special features.

<div class="row">
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/apache"><img src="/gfx/agent/apache.png" alt="Apache icon"> Apache</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/cassandra"><img src="/gfx/agent/cassandra.png" alt="Cassandra icon"> Cassandra</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/couchdb"><img src="/gfx/agent/couchdb.png" alt="CouchDb icon"> CouchDb</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/elasticsearch"><img src="/gfx/agent/elasticsearch.png" alt="ElasticSearch icon"> ElasticSearch</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/haproxy"><img src="/gfx/agent/haproxy.png" alt="HAProxy icon"> HAProxy</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/iis"><img src="/gfx/agent/iis.png" alt="IIS icon"> IIS</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/log"><img src="/gfx/agent/log_plugin.png" alt="Log icon"> Log</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/magento"><img src="/gfx/agent/magento.png" alt="Magento icon"> Magento</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/custom-metrics/generic-script/index/"><img src="/gfx/agent/genericscript.png" alt="Script icon"> Generic Script</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/mysql"><img src="/gfx/agent/mysql.png" alt="Mysql icon"> Mysql</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/cron"><img src="/gfx/agent/CRON.png" alt="Cron icon"> Cron</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/docker"><img src="/gfx/agent/docker.png" alt="Docker icon"> Docker</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/docker-swarm"><img src="/gfx/agent/dockerswarm.png" alt="Docker icon"> Docker Swarm</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/kubernetes"><img src="/gfx/agent/kubernetes.png" alt="Kubernetes icon"> Kubernetes</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/resources"><img src="/gfx/agent/resources.png" alt="Resources icon"> Resources</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/jboss"><img src="/gfx/agent/jboss.png" alt="JBoss icon"> JBoss</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/nginx"><img src="/gfx/agent/nginx.png" alt="NGINX icon"> NGINX</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/tomcat"><img src="/gfx/agent/tomcat.png" alt="Tomcat icon"> Tomcat</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/varnish"><img src="/gfx/agent/varnish.png" alt="Tomcat icon"> Varnish</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/oracle"><img src="/gfx/agent/oracle.png" alt="Tomcat icon"> Oracle</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/postgresql"><img src="/gfx/agent/postgresql.png" alt="Tomcat icon"> PostgreSQL</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/mongodb"><img src="/gfx/agent/mongodb.png" alt="Tomcat icon"> MongoDB</a></div>
</div>

## Extra

* [Cloud environments]({{ site.baseurl }}/agent/cloud/index)
    Specific configuration, agent management and autoscaling tips & tricks for Cloud based providers like Amazon Web Services and Microsoft Azure.
* [Environment flags]({{ site.baseurl}}/agent/advanced)
    Advanced environment flags you can use to customize the agent hostname, auto updating functionality and log level.
* [Firewall / Proxy]({{ site.baseurl }}/agent/firewall-proxy)
    Information about CoScale agent firewall settings and proxy configuration.
* [Custom templates]({{ site.baseurl }}/agent/custom-template)
    Specific configuration for config management systems.
* [Refine webrequests]({{ site.baseurl }}/agent/webrequest-method)
    Specific configuration for tracking web requests by their HTTP method.
