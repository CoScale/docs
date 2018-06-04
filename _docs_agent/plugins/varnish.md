---
layout: page
title: Monitoring and collecting data from Varnish
description: Information on the metrics collected by the CoScale Varnish plugin.
---

> Varnish Cache is a web application accelerator also known as a caching HTTP reverse proxy. You install it in front of any server that speaks HTTP and configure it to cache the contents. Varnish Cache is really, really fast. It typically speeds up delivery with a factor of 300 - 1000x, depending on your architecture.

More information on: [https://varnish-cache.org/](https://varnish-cache.org/)

## How it works

This plugin analyzes the performance of your Varnish web server. It captures traffic rates, latencies and response codes of http requests sent to the web server by parsing the Varnish access log file.

**The minimal supported version of Varnish is 4.0.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Varnish" %}

## Configuration

### Configure your Varnish access logs

Open the `/etc/default/varnishncsa` file

1. To enable access logging: uncomment or add `VARNISHNCSA_ENABLED=1`
2. Set the correct log format:

replace `DAEMON_OPTS="-a -w ${LOGFILE} -D -P ${PIDFILE}"` with:

{% highlight ini %}
LOGFORMAT="%{host}i \"%r\" %D %s %I %O"
DAEMON_OPTS="-a -w ${LOGFILE} -D -P ${PIDFILE} -F \"${LOGFORMAT}\""
{% endhighlight %}

Restart Varnish to apply these changes.

#### Log format

A log format must contain server the following:

| Value          | Original Value | Remarks                     |
|----------------|----------------|-----------------------------|
| Hostname       | %{host}i       | -                           |
| Request        | \"%r\"         | -                           |
| Latency        | %D             | represented in milliseconds |
| Latency        | %T             | represented in seconds      |
| Status Code    | %s             | -                           |
| Bytes Received | %I             | -                           |
| Bytes Sent     | %O             | -                           |

For Latency, only one is needed.

Other examples of log formats that will work:

`"%{host}i %h %l %u %t \"%r\" %D %s %I %O %b \"%{Referer}i\" \"%{User-agent}i\" %{Varnish:time_firstbyte}x"`

### Active checks

This plugin can be configured to perform a HTTP GET on your Varnish. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost/test_page`) should be provided.

<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/varnish.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
