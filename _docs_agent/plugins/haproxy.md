---
layout: page
title: Monitoring and collecting data from HAProxy
description: Information on the metrics collected by the CoScale HAProxy plugin.
---

> HAProxy is a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications.

More information on: [http://www.haproxy.org/](http://www.haproxy.org/)

## How it works

This plugin analyzes the performance of your HaProxy load balancer.

The plugin gathers statistics like: number of requests, bytes sent and received, number of errors, http requests statuses and many other useful metrics. Both the access log and server-status require a bit of configuration.

**The minimal supported version of HaProxy is 1.5.**

## Installation

{% include_relative _installation.md orchestrator="false" service="HAProxy" %}

## Configuration

### Global stats
For gathering global stats you need to add the next lines in `/etc/haproxy/haproxy.cfg`

{% highlight haproxy %}
listen http-in
    bind localhost:1936
    stats enable
    stats hide-version
    stats refresh 60s
    stats auth someuser:somepass
    stats uri  /haproxy?stats
{% endhighlight %}

### Log configuration

To enable custom logs on haproxy add next lines to `/etc/haproxy/haproxy.cfg` under defaults section

If you are using a custom log format, make sure that option httplog is not enabled.
{% highlight haproxy %}
defaults
    mode    http
    log-format %hr\ %{+Q}r\ %Tt\ %ST\ %B
    #option httplog
{% endhighlight %}

Additionally an extra line has to be added to the frontend section:

{% highlight haproxy %}
frontend http-frontend
    capture request header Host len 50
{% endhighlight %}

#### Plugin configuration
When using Rsyslog some extra data will be prepended to your logformat. Either add `&a\` before your configured log format below or configure Rsyslog to use a different template for HAProxy as folows: `/etc/rsyslog.d/49-haproxy.conf`

{% highlight syslog %}
# Create an additional socket in haproxy's chroot in order to allow logging
# via /dev/log to chroot'ed HAProxy processes
$AddUnixListenSocket /var/lib/haproxy/dev/log

$template Haproxy,"%msg%\n"

# Send HAProxy messages to a dedicated logfile
if $programname startswith 'haproxy' then /var/log/haproxy.log;Haproxy
&~
{% endhighlight %}


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/haproxy.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
