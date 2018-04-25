---
layout: page
title: Tomcat plugin
description: Information on the metrics collected by the CoScale Tomcat plugin.
---

> The Apache Tomcat® software is an open source implementation of the Java Servlet, JavaServer Pages, Java Expression Language and Java WebSocket technologies. Apache Tomcat software powers numerous large-scale, mission-critical web applications across a diverse range of industries and organizations.

More information on: [http://tomcat.apache.org/](http://tomcat.apache.org/)

## How it works

This plugin analyzes the performance of your Tomcat web server. It captures traffic rates, latencies and response codes of http requests sent to the web server by parsing the Tomcat access log file.

The plugin can optionally get global statistics (eg. the number of connections, the number of workers, etc.) by parsing the JMX proxy of the Tomcat web server.

Both the access log and JMX proxy require a bit of configuration, see next steps.

**The minimal supported version of Tomcat is 7.0.**

## Installation

{% include_relative _installation.md orchestrator="false" service="Tomcat" %}

## Configuration

### Configure JMX proxy

To gather global statistics the agent needs access to the JMX proxy.

Add the following lines in `$CATALINA_BASE}/conf/tomcat-users.xml` and fill in `<username>` and `<password>`.

{% highlight xml %}
<role rolename="manager"/>
<role rolename="manager-jmx"/>
<user username="<username>" password="<password>" roles="manager, manager-jmx" />
{% endhighlight %}

Install Tomcat manager using the following command, fill in `<version>` with your current Tomcat version:

{% highlight bash %}
apt-get install tomcat<version>-admin
{% endhighlight %}

Restart Tomcat to apply these changes.

### Configure your Tomcat access logs

Enable the Tomcat access log format. Add the following configuration to {$CATALINA_BASE}/conf/server.xml

{% highlight xml %}
<Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
prefix="localhost_access_log." suffix=".txt" fileDateFormat="yyyy-MM-dd"
pattern="%h %v %D %T %B %l %u %t &quot;%r&quot; %s %b" />
{% endhighlight %}

Restart Tomcat to apply these changes.

#### Log format

Example of a log format configuration so that we can have all the information that we need:

`%v \"%r\" %D %T %s %B`

| Value       | Original Value | Remarks                     |
|-------------|----------------|-----------------------------|
| Hostname    | %v             | -                           |
| Request     | \"%r\"         | -                           |
| Latency     | %D             | represented in milliseconds |
| Latency     | %T             | represented in seconds      |
| Status Code | %s             | -                           |
| Bytes Sent  | %B             | -                           |

`"%h %v %D %T %B %l %u %t \"%r\" %s %b %{User-Agent}i %{Referer}i"`

### Active checks

This plugin can be configured to perform a HTTP GET on your JBoss. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost/TestPage.jsp`) should be provided.

## Events

* Service state

## Metrics

| Metric name                                           | Metric unit |
|-------------------------------------------------------|-------------|
| Tomcat total number of accesses                       | access      |
| Tomcat total number of hits                           | hits        |
| Total number of bytes sent by Tomcat                  | b           |
| Total number of bytes received by Tomcat              | b           |
| Total number of requests to Tomcat                    | req         |
| Total number of Tomcat threads busy                   | threads     |
| Number of seconds that the Tomcat server has been up  | s           |
| Total Tomcat processes CPU Time                       | s           |
