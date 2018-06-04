---
layout: page
title: Monitoring and collecting data from Nginx
description: Information on the metrics collected by the CoScale NGINX plugin.
---

> NGINX [engine x] is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server.

More information on: [https://nginx.org](https://nginx.org)

## How it works

This plugin analyzes the performance of your Nginx web server. It captures traffic rates, latencies and response codes of http requests sent to the web server by parsing the Nginx access log file.

The plugin can also get some global statistics (the number of connections, the number of workers, etc.) by parsing the status page of the Nginx web server.

Both the access log and server-status require a bit of configuration, see next steps.

**The minimal supported version of Nginx is 0.5.38.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Nginx" %}

## Configuration

### Configure Nginx status page

For gathering global statistics, the `nginx_status` page should be enabled.

Enable the status page by adding the following lines inside the http section of your `<install-dir>/nginx.conf`.

{% highlight nginx %}
http {
    ...
    server {
        listen localhost;

        location /nginx_status {
            stub_status on;
            access_log off;
            allow all;
        }
    }
    ...
}
{% endhighlight %}

Restart Nginx to apply these changes.

### Configure your Nginx access logs

For the plugin to be able to collect statistics about http requests, the access log has to be enabled. Enable the access log by adding the following lines inside the http section of your `<install-dir>/nginx.conf`.

Make sure to update the default access_log `/var/log/nginx/access.log` line with the one provided below.

{% highlight nginx %}
http {
    ...
    log_format CoScale '$server_name "$request" $request_time $status $request_length $bytes_sent';
    access_log /var/log/nginx/access.log CoScale;
    ...
}
{% endhighlight %}

Restart Nginx to apply these changes.

#### Log format

A log format must contain request, $request
Example of a log format configuration so that we can have all the information that we need:

`$server_name \"$request\" $request_time $status $request_length $bytes_sent`

| Value          | Original Value  | Remarks                                           |
|----------------|-----------------|---------------------------------------------------|
| Hostname       | $server_name    | -                                                 |
| Request        | $request        | -                                                 |
| Latency        | $request_time   | Latency in seconds with a milliseconds resolution |
| Status Code    | $status         | -                                                 |
| Bytes Received | $request_length | -                                                 |
| Bytes Sent     | $bytes_sent     | -                                                 |

Other examples of log formats that will work:

`"$server_name $remote_addr $remote_user [$time_local] \"$request\" $request_time $status $request_length $bytes_sent \"$sent_http_referer\" \"$sent_http_user\" $query_string"`

### Active checks

This plugin can be configured to perform a HTTP GET on your Nginx. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost/test_page`) should be provided.


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/nginx.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
