---
layout: page
title: HAProxy plugin
description: Information on the metrics collected by the CoScale HAProxy plugin.
---

> HAProxy is a free, very fast and reliable solution offering high availability, load balancing, and proxying for TCP and HTTP-based applications.

More information on: [http://www.haproxy.org/](http://www.haproxy.org/)

## How it works

This plugin analyzes the performance of your HaProxy load balancer.

The plugin gathers statistics like: number of requests, bytes sent and received, number of errors, http requests statuses and many other useful metrics. Both the access log and server-status require a bit of configuration.

**The minimal supported version of HaProxy is 1.5.**

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

## Events

* Service state

## Metrics

| Metric name                                                                                               | Metric unit |
|-----------------------------------------------------------------------------------------------------------|-------------|
| HAProxy current queued requests (qcur) on %s                                                              | req         |
| HAProxy (check_duration) on %s                                                                            | ms          |
| HAProxy (cli_abrt) on %s                                                                                  | trans       |
| HAProxy (comp_byp) on %s                                                                                  | b           |
| HAProxy (comp_in) on %s                                                                                   |             |
| HAProxy (comp_out) on %s                                                                                  |             |
| HAProxy (comp_rsp) on %s                                                                                  | b           |
| HAProxy (ctime) on %s                                                                                     | ms/rec      |
| HAProxy (hanafail) on %s                                                                                  | #           |
| HAProxy (last_agt) on %s                                                                                  |             |
| HAProxy (lastsess) on %s                                                                                  | s           |
| HAProxy (qtime) on %s                                                                                     | ms/rec      |
| HAProxy (rtime) on %s                                                                                     | ms/rec      |
| HAProxy (srv_abrt) on %s                                                                                  | trans       |
| HAProxy (ttime) on %s                                                                                     | ms/rec      |
| HAProxy bytes in (IEEE 1541-2002) (bin) on %s                                                             | b           |
| HAProxy bytes out (IEEE 1541-2002) (bout) on %s                                                           | b           |
| HAProxy connection errors (econ) on %s                                                                    | conn        |
| HAProxy current sessions (scur) on %s                                                                     | session     |
| HAProxy denied requests (dreq) on %s                                                                      | req         |
| HAProxy denied responses (dresp) on %s                                                                    | resp        |
| HAProxy HTTP requests per second over last elapsed second (req_rate) on %s                                | req/s       |
| HAProxy last status change (in seconds) (lastchg) on %s                                                   | change      |
| HAProxy max number of HTTP requests per second observed (req_rate_max) on %s                              | req/s       |
| HAProxy max number of new sessions per second (rate_max) on %s                                            | session     |
| HAProxy max queued requests (qmax) on %s                                                                  | req         |
| HAProxy max sessions (smax) on %s                                                                         | session     |
| HAProxy number of failed checks (chkfail) on %s                                                           | checks      |
| HAProxy number of HTTP responses with 1xx code (hrsp_1xx) on %s                                           | session     |
| HAProxy number of HTTP responses with 2xx code (hrsp_2xx) on %s                                           | session     |
| HAProxy number of HTTP responses with 3xx code (hrsp_3xx) on %s                                           | session     |
| HAProxy number of HTTP responses with 4xx code (hrsp_4xx) on %s                                           | session     |
| HAProxy number of HTTP responses with 5xx code (hrsp_5xx) on %s                                           | session     |
| HAProxy number of HTTP responses with other codes (protocol error) (hrsp_other) on %s                     | session     |
| HAProxy number of sessions per second over last elapsed second (rate) on %s                               | session     |
| HAProxy number of UP->DOWN transitions (chkdown) on %s                                                    | change      |
| HAProxy queue limit (qlimit) on %s                                                                        | msg         |
| HAProxy redispatches (warning) (wredis) on %s                                                             | redis       |
| HAProxy request errors (ereq) on %s                                                                       | req         |
| HAProxy response errors (eresp) on %s                                                                     | resp        |
| HAProxy server is active (server), number of active servers (backend) (act) on %s                         | #           |
| HAProxy server is active (server), total number of active servers (backend) (act) (over all backends)     |             |
| HAProxy server is backup (server), number of backup servers (backend) (bck) on %s                         | #           |
| HAProxy server is backup (server), total number of backup servers (backend) (bck) (over all backends)     |             |
| HAProxy sessions limit (slim) on %s                                                                       | session     |
| HAProxy total (check_duration) (over all backends)                                                        |             |
| HAProxy total downtime (downtime) (over all backends)                                                     | s           |
| HAProxy total downtime (downtime) on %s                                                                   | s           |
| HAProxy total max number of HTTP requests per second observed (req_rate_max) (over all backends)          |             |
| HAProxy total max number of new sessions per second (rate_max) (over all backends)                        |             |
| HAProxy total number of (cli_abrt) (over all backends)                                                    |             |
| HAProxy total number of (comp_byp) (over all backends)                                                    |             |
| HAProxy total number of (comp_in) (over all backends)                                                     |             |
| HAProxy total number of (comp_out) (over all backends)                                                    |             |
| HAProxy total number of (comp_rsp) (over all backends)                                                    |             |
| HAProxy total number of (ctime) (over all backends)                                                       |             |
| HAProxy total number of (hanafail) (over all backends)                                                    |             |
| HAProxy total number of (last_agt) (over all backends)                                                    |             |
| HAProxy total number of (last_chk) (over all backends)                                                    |             |
| HAProxy total number of (lastsess) (over all backends)                                                    |             |
| HAProxy total number of (qtime) (over all backends)                                                       |             |
| HAProxy total number of (rtime) (over all backends)                                                       |             |
| HAProxy total number of (srv_abrt) (over all backends)                                                    |             |
| HAProxy total number of (ttime) (over all backends)                                                       |             |
| HAProxy total number of bytes in (IEEE 1541-2002) (bin) (over all backends)                               | b           |
| HAProxy total number of bytes out (IEEE 1541-2002) (bout) (over all backends)                             | b           |
| HAProxy total number of connection errors (econ) (over all backends)                                      |             |
| HAProxy total number of current queued requests (qcur) (over all backends)                                |             |
| HAProxy total number of current sessions (scur) (over all backends)                                       |             |
| HAProxy total number of denied requests (dreq) (over all backends)                                        | req         |
| HAProxy total number of denied responses (dresp) (over all backends)                                      |             |
| HAProxy total number of failed checks (chkfail) (over all backends)                                       |             |
| HAProxy total number of HTTP requests per second over last elapsed second (req_rate) (over all backends)  |             |
| HAProxy total number of HTTP requests received (req_tot) (over all backends)                              |             |
| HAProxy total number of HTTP requests received (req_tot) on %s                                            | req         |
| HAProxy total number of HTTP responses with 1xx code (hrsp_1xx) (over all backends)                       |             |
| HAProxy total number of HTTP responses with 2xx code (hrsp_2xx) (over all backends)                       |             |
| HAProxy total number of HTTP responses with 3xx code (hrsp_3xx) (over all backends)                       |             |
| HAProxy total number of HTTP responses with 4xx code (hrsp_4xx) (over all backends)                       |             |
| HAProxy total number of HTTP responses with 5xx code (hrsp_5xx) (over all backends)                       |             |
| HAProxy total number of HTTP responses with other codes (protocol error) (hrsp_other) (over all backends) |             |
| HAProxy total number of max queued requests (qmax) (over all backends)                                    |             |
| HAProxy total number of max sessions (smax) (over all backends)                                           |             |
| HAProxy total number of redispatches (warning) (wredis) (over all backends)                               |             |
| HAProxy total number of request errors (ereq) (over all backends)                                         | req         |
| HAProxy total number of response errors (eresp) (over all backends)                                       |             |
| HAProxy total number of seconds from last status change (lastchg) (over all backends)                     | s           |
| HAProxy total number of sessions (stot) (over all backends)                                               |             |
| HAProxy total number of sessions limit (slim) (over all backends)                                         |             |
| HAProxy total number of sessions per second over last elapsed second (rate) (over all backends)           | conn/s      |
| HAProxy total number of times a server was selected (lbtot) (over all backends)                           |             |
| HAProxy total number of times a server was selected (lbtot) on %s                                         | #           |
| HAProxy total number of UP->DOWN transitions (chkdown) (over all backends)                                |             |
| HAProxy total queue limit (qlimit) (over all backends)                                                    |             |
| HAProxy total sessions (stot) on %s                                                                       | session     |
| HAProxy warm up status (throttle) (over all backends)                                                     |             |
| HAProxy warm up status (throttle) on %s                                                                   | %           |
