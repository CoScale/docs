---
layout: page
title: Apache plugin
description: Information on the metrics collected by the CoScale Apache plugin.
---

> The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server for modern operating systems including UNIX and Windows.

More information on: [https://httpd.apache.org/](https://httpd.apache.org/)

## How it works

This plugin analyzes the performance of your Apache web server.

It captures traffic rates, latencies and response codes of http requests sent to the web server by parsing the Apache access log file.

This plugin can also get some global statistics (eg. the number of connections, the number of workers, etc.) by parsing the server-status page of the Apache web server.

**The minimal supported version of Apache is 2.0.**

## Configuration

### Configure Apache server-status
For gathering global statistics (eg. number of connections, etc.), the server-status page should be enabled.

Add or uncomment the following lines in `/etc/httpd/conf/httpd.conf`

{% highlight apache %} 
<Location /server-status>
    SetHandler server-status
    Order deny,allow
    Deny from all
    Allow from localhost
</Location>
{% endhighlight %}

Make sure the status module is also enabled, add or uncomment the following line in the same file.
`LoadModule status_module modules/mod_status.so`
Restart Apache to apply these changes.

### Configure your Apache access logs
The standard access log format for Apache does not include the request latency.

To fix this, update the log format in /etc/httpd/conf/httpd.conf or /etc/httpd/sites-enabled/<virtual host>.conf

Replace `CustomLog logs/access.log combined` with `LogFormat "%V \"%r\" %D %s %I %O" coscale
CustomLog logs/access.log coscale`

Restart Apache to apply these changes.

#### Log format

A log format must contain server name and request, %V and %r ( or their substitutes )
Example of a log format configuration with all the information CoScale needs:

`%V \"%r\" %D %s %I %O`

| Value          | Original Value | Remarks                                                        |
|----------------|----------------|----------------------------------------------------------------|
| Hostname       | %V             | %V,%V can be replaced with %v                                  |
| Request        | \"%r\"         | \"%r\",%r can use modifier: < or >                             |
| Latency        | %D             | %D can be replaced with %T, and can also use modifiers: < or > |
| Status Code    | %s             | %s can use modifiers: < or >                                   |
| Bytes Received | %I             |                                                                |
| Bytes Sent     | %O             |                                                                |


Other examples of log formats that will work:`
`%V %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%!400{User-agent}i\" %X %I %O %q %D`

## Events

* Service state

## Metrics

| Metric name                                       | Metric unit |
|---------------------------------------------------|-------------|
| Apache total number of accesses                   | access      |
| Apache bytes per request                          | b/req       |
| Apache bytes per second                           | b/s         |
| Apache ConnsAsyncClosing                          | conn        |
| Apache ConnsAsyncKeepAlive                        | conn        |
| Apache ConnsAsyncWriting                          | conn        |
| Apache CPULoad                                    | %           |
| Apache requests per second                        | req/s       |
| Apache total bytes transferred                    | b           |
| Busy Apache workers                               | workers     |
| Idle Apache workers                               | workers     |
| Number of connections to Apache                   | conn        |
| Number of seconds since the Apache server started | s           |

## Notes

* `ExtendedStatus` has to be `On` for global statistics
