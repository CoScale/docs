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

### Containers

<div class="row">
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/docker"><img src="/gfx/agent/docker.png" alt="Docker icon"> Docker</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/docker-swarm"><img src="/gfx/agent/dockerswarm.png" alt="Docker icon"> Docker Swarm</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/kubernetes"><img src="/gfx/agent/kubernetes.png" alt="Kubernetes icon"> Kubernetes</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/openshift"><img src="/gfx/agent/openshift.png" alt="Openshift icon"> Openshift</a></div>
</div>  

### Web

<div class="row">
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/apache"><img src="/gfx/agent/apache.png" alt="Apache icon"> Apache</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/nginx"><img src="/gfx/agent/nginx.png" alt="NGINX icon"> NGINX</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/iis"><img src="/gfx/agent/iis.png" alt="IIS icon"> IIS</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/haproxy"><img src="/gfx/agent/haproxy.png" alt="HAProxy icon"> HAProxy</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/tomcat"><img src="/gfx/agent/tomcat.png" alt="Tomcat icon"> Tomcat</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/varnish"><img src="/gfx/agent/varnish.png" alt="Varnish icon"> Varnish</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/jboss"><img src="/gfx/agent/jboss.png" alt="JBoss icon"> JBoss</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/nodejs"><img src="/gfx/agent/nodejs.png" alt="Nodejs icon"> Nodejs</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/dropwizard"><img src="/gfx/agent/dropwizard.png" alt="Dropwizard icon"> Dropwizard</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/dotnetcore"><img src="/gfx/agent/dotnetcore.png" alt="Dotnetcore icon"> .NET Core</a></div>
</div>    

### Caching

<div class="row">
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/memcached"><img src="/gfx/agent/memcached.png" alt="Memcached icon"> Memcached</a></div>
</div>

### Database

<div class="row">    
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/mysql"><img src="/gfx/agent/mysql.png" alt="Mysql icon"> MySQL</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/mssql"><img src="/gfx/agent/mssql.png" alt="Mssql icon"> MSSQL</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/oracle"><img src="/gfx/agent/oracle.png" alt="Oracle icon"> Oracle</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/postgresql"><img src="/gfx/agent/postgresql.png" alt="PostgreSQL icon"> PostgreSQL</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/hana"><img src="/gfx/agent/hanadb.png" alt="Hana icon"> Hana</a></div>
</div>

### NoSQL

<div class="row">
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/mongodb"><img src="/gfx/agent/mongodb.png" alt="MongoDB icon"> MongoDB</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/redis"><img src="/gfx/agent/redis.png" alt="Redis icon"> Redis</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/couchbase"><img src="/gfx/agent/couchbase.png" alt="Couchbase icon"> Couchbase</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/couchdb"><img src="/gfx/agent/couchdb.png" alt="CouchDb icon"> CouchDB</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/cassandra"><img src="/gfx/agent/cassandra.png" alt="Cassandra icon"> Cassandra</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/elasticsearch"><img src="/gfx/agent/elasticsearch.png" alt="ElasticSearch icon"> ElasticSearch</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/riak"><img src="/gfx/agent/riak.png" alt="Riak icon"> Riak</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/solr"><img src="/gfx/agent/solr.png" alt="Solr icon"> Solr</a></div>
</div>

### Queueing

<div class="row">
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/rabbitmq"><img src="/gfx/agent/rabbitmq.png" alt="RabbitMQ icon"> RabbitMQ</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/activemq"><img src="/gfx/agent/activemq.png" alt="ActiveMQ icon"> ActiveMQ</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/kafka"><img src="/gfx/agent/kafka.png" alt="Kafka icon"> Kafka</a></div>
</div>

### Generic monitoring

<div class="row">
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/resources"><img src="/gfx/agent/resources.png" alt="Resources icon"> Resources</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/cron"><img src="/gfx/agent/CRON.png" alt="Cron icon"> Cron</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/custom-metrics/generic-script/index/"><img src="/gfx/agent/genericscript.png" alt="Script icon"> Generic Script</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/log"><img src="/gfx/agent/log_plugin.png" alt="Log icon"> Log</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/collectd"><img src="/gfx/agent/collectd.png" alt="CollectD icon"> CollectD</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/jmx"><img src="/gfx/agent/jmx.png" alt="JMX icon"> JMX</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/jolokia"><img src="/gfx/agent/jolokia.png" alt="Jolokia icon"> Jolokia</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/fluentd"><img src="/gfx/agent/fluentd.png" alt="Fluentd icon"> Fluentd</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/calico"><img src="/gfx/agent/calico.png" alt="Calico icon"> Calico</a></div>
</div>

### 3rd party integrations

<div class="row">
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/amazoncloudwatch"><img src="/gfx/agent/amazon-aws.png" alt="AWS icon"> Amazon CloudWatch</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/azure"><img src="/gfx/agent/azure.png" alt="Azure icon"> Azure</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/prometheus"><img src="/gfx/agent/prometheus.png" alt="Prometheus icon"> Prometheus</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/pingdom"><img src="/gfx/agent/pingdom.png" alt="Pingdom icon"> Pingdom</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/sentry"><img src="/gfx/agent/sentry.png" alt="Sentry icon"> Sentry</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/rollbar"><img src="/gfx/agent/rollbar.png" alt="Rollbar icon"> Rollbar</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/googleanalytics"><img src="/gfx/agent/google-analytics.png" alt="Google Analytics icon"> Google Analytics</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/magento"><img src="/gfx/agent/magento.png" alt="Magento icon"> Magento</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/aweber"><img src="/gfx/agent/aweber.png" alt="AWeber icon"> AWeber</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/constantcontact"><img src="/gfx/agent/constant-contact.png" alt="Constant Contact icon"> Constant Contact</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/campaignmonitor"><img src="/gfx/agent/campaign-monitor.png" alt="Campaign Monitor icon"> Campaign Monitor</a></div>
    <div class="col-sm-3"><a href="{{ site.baseurl }}/agent/plugins/mailchimp"><img src="/gfx/agent/mailchimp.png" alt="Mailchimp icon"> Mailchimp</a></div>
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
* [Accept webrequests]({{ site.baseurl }}/agent/accept-webrequests)
    Manually accept specific web requests.
* [Refine webrequests]({{ site.baseurl }}/agent/webrequest-method)
    Specific configuration for tracking web requests by their HTTP method.
* [Remove a server]({{ site.baseurl }}/agent/remove-server)
    Removing a server or an agent from your application.
* [HOST feature]({{ site.baseurl }}/agent/host-feature)
    Monitor services that run on a host from our Container Agent.
