---
layout: page
title: Monitoring and collecting data from Dropwizard
description: Information on the metrics collected by the CoScale Dropwizard plugin.
---

> Dropwizard is a Java framework for developing ops-friendly, high-performance, RESTful web services. Dropwizard pulls together stable, mature libraries from the Java ecosystem into a simple, light-weight package that lets you focus on getting things done. Dropwizard has out-of-the-box support for sophisticated configuration, application metrics, logging, operational tools, and much more, allowing you and your team to ship a production-quality web service in the shortest time possible.

More information on: [http://www.dropwizard.io](http://www.dropwizard.io)

## How it works

This plugin analyzes the performance of your Dropwizard web application. It captures traffic rates, latencies and response codes of http requests sent to the web server by parsing the Dropwizard access log file. The plugin can optionally get global statistics (eg. the number of connections, JVM metrics, etc.) by parsing the metrics reported by AdminServlet of the Dropwizard application. Both, the access log and AdminServlet require a bit of configuration, see steps below.

**The minimal supported version of Dropwizard is 1.0.0.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Dropwizard" %}

## Global statistics

For gathering global statistics (eg. number of connections, etc.), the metrics page should be enabled.

Add the following lines in your application YAML configuration file:

{% highlight dropwizard %}
server:
  adminConnectors:
    - type: http
      port: 8081
{% endhighlight %}

Restart the application to apply these changes.
Provide the metrics URL, as you configured it on your server.

## Log configuration

Enable the Dropwizard application access log format. Add the following lines to your application YAML configuration file:

{% highlight dropwizard %}
server:
  requestLog:
    appenders:
      - type: file
        logFormat: '%h "%r" %D %s %b'
        currentLogFilename: /var/log/dropwizard-app/access.log
        archivedLogFilenamePattern: /var/log/dropwizard-app/accedd-%d.log.gz
{% endhighlight %}

Restart Dropwizard application to apply these changes.

Provide the location of the access log file you configured and the log format.

For example,

Filename: `/var/log/dropwizard-app/access.log`
Log format: `%h "%r" %D %s %b`

| Value          | Original Value | Remarks                     |
|----------------|----------------|-----------------------------|
| Hostname       | %h             |                             |
| Request        | \"%r\"         |                             |
| Latency        | %D             | represented in milliseconds |
| Latency        | %T             | represented in seconds      |
| Status Code    | %s             |                             |
| Bytes Sent     | %b             |                             |


## Active checks

This plugin can be configured to perform a HTTP GET on your Dropwizard application. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost/test_page.php`) should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/dropwizard.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
