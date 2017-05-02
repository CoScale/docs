---
layout: page
title: JBoss plugin
description: Information on the metrics collected by the CoScale JBoss plugin.
---

> Red Hat® JBoss® Middleware is a family of a lightweight, cloud-friendly, enterprise-grade products that help enterprises innovate faster, in a smarter way.

More information on: [http://www.jboss.org/](http://www.jboss.org/)

## How it works

This plugin analyzes the performance of your JBoss web server.

It captures traffic rates, latencies and response codes of requests sent to the web server by parsing the JBoss access log file. The plugin can get global statistics (the number of connections, the number of workers, etc.) using the JMX interface of the JBoss web server.

**The minimal supported version of JBoss is 7.1.**

## Configuration

### Configure your JBoss JMX connection

To enable collecting general statistics for JBoss, you have to enable JMX. You can do this in two ways, by:

#### 1) Enabling the management endpoint (recommended)

In your `<jboss-install-dir>` update the following lines in `/standalone/configuration/standalone.xml`

Replace
{% highlight xml %} 
<subsystem xmlns="urn:jboss:domain:jmx:1.1">
    <show-model value="true"/>
    <remoting-connector/>
</subsystem>
{% endhighlight %}

With
{% highlight xml %} 
<subsystem xmlns="urn:jboss:domain:jmx:1.1">
    <show-model value="true"/>
    <remoting-connector use-management-endpoint="true"/>
</subsystem>
{% endhighlight %}

Before you can run the JBoss Application Server, you need to ensure that you've configured the `JBOSS_HOME` environment variable.

#### 2) Updating your JBoss configuration

Add the following to your JBoss configuration (eg. `<jboss-install-dir>/bin/standalone.conf`). Don't forget to replace the `<jboss-install-dir>` placeholder by your installation path.

{% highlight bash %} 
JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote.port=1090 \
    -Dcom.sun.management.jmxremote.authenticate=false \
    -Dcom.sun.management.jmxremote \
    -Dcom.sun.management.jmxremote.ssl=false \
    -Djava.util.logging.manager=org.jboss.logmanager.LogManager \
    -Xbootclasspath/p:<jboss-install-dir>/modules/org/jboss/logmanager/main/jboss-logmanager-1.2.2.GA.jar \
    -Xbootclasspath/p:<jboss-install-dir>/modules/org/jboss/logmanager/log4j/main/jboss-logmanager-log4j-1.0.0.GA.jar \
    -Xbootclasspath/p:<jboss-install-dir>/modules/org/apache/log4j/main/log4j-1.2.16.jar -Djboss.modules.system.pkgs=org.jboss.logmanager"
{% endhighlight %}


### Configure JBoss access logs

To measure performance of all http requests, enable the JBoss access log by adding the next lines in the `<virtual-server>` tag in your configuration file:

{% highlight xml %} 
<access-log pattern="%v %B %D &quot;%r&quot; %A %a %t %H %p %U %s %S %T" rotate="true">
    <directory path="." relative-to="jboss.server.log.dir"/>
</access-log>
{% endhighlight %}

Example:
{% highlight xml %} 
<virtual-server name="default-host" enable-welcome-root="true">
    <alias name="localhost"/>
    <alias name="example.com"/>
    <access-log pattern="%v %B %D &quot;%r&quot; %A %a %t %H %p %U %s %S %T" rotate="true">
        <directory path="." relative-to="jboss.server.log.dir"/>
    </access-log>
</virtual-server>
{% endhighlight %}

Restart JBoss to apply these changes.


A log format must contain the request: `%r`
Example of a log format configuration so that we can have all the information that we need:
`%v \"%r\" %D %T %s %B`

| Value       | Original | Value | Remarks                     |
|-------------|----------|-------|-----------------------------|
| Hostname    | %v       | -     |                             |
| Request     | \"%r\"   | -     |                             |
| Latency     | %D       | %D    | represented in milliseconds |
| Latency     | %T       | %T    | represented in seconds      |
| Status Code | %s       | -     |                             |
| Bytes Sent  | %B       | -     |                             |

Another log format that will work:

`"%v %B %D \"%r\" %A %a %t %H %p %U %s %S %T %{xxx}i %{xxx}o"`

Where `xxx` is a servlet of your choice.

To enable access logging in JBoss version 5 and version 6, uncomment these lines in server.xml:
{% highlight xml %} 
<Valve className="org.apache.catalina.valves.AccessLogValve"
   prefix="localhost_access_log." suffix=".log"
   pattern="common" directory="${jboss.server.log.dir}"
   resolveHosts="false" />
{% endhighlight %}

### Active checks

This plugin can be configured to perform a HTTP GET on your JBoss. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost/test_page`) should be provided.

## Events

* Service state


## Metrics

| Metric name                                             | Metric unit |
|---------------------------------------------------------|-------------|
| Free JBoss swap space size                              | b           |
| Free JBoss swap space size                              | b           |
| Total JBoss swap space size                             | b           |
| Total JBoss physical memory size                        | b           |
| JBoss heap memory size %s                               | b           |
| JBoss non heap memory size %s                           | b           |
| Number of seconds that the JBoss server has been up     | s           |
| Total JBoss processes CPU Time                          | s           |
| JBoss datasource %s active count                        | #           |
| JBoss datasource %s available count                     | #           |
| JBoss datasource %s average blocking time               | s           |
| JBoss datasource %s average creation time               | s           |
| JBoss datasource %s created count                       | #           |
| JBoss datasource %s destroyed count                     | #           |
| JBoss datasource %s max creation time                   | s           |
| JBoss datasource %s max used count                      | #           |
| JBoss datasource %s max wait time                       | s           |
| JBoss datasource %s timedOut                            | #           |
| JBoss datasource %s total blocking time                 | s           |
| JBoss datasource %s total creation time                 | s           |
| JBoss transactions default timeout                      | s           |
| JBoss process id socket max ports                       | #           |
| JBoss current thread cpu time                           | s           |
| JBoss current thread user time                          | s           |
| JBoss web %s bytes received                             | b           |
| JBoss web %s bytes sent                                 | b           |
| JBoss web %s enable lookups                             | #           |
| JBoss web %s enabled                                    | #           |
| JBoss web %s error count                                | errors      |
| JBoss web %s max-post-size                              | b           |
| JBoss web %s max-save-post-size                         | b           |
| JBoss web %s max time                                   | s           |
| JBoss web %s processing time                            | s           |
| JBoss web %s request count                              | req         |
| JBoss thread count                                      | threads     |
| JBoss peak thread count                                 | threads     |
| JBoss total started thread count                        | threads     |
| JBoss daemon thread count                               | threads     |
| Peak count of active JBoss threads in the system        | threads     |
| Count of JBoss threads marked as daemons in the system  | threads     |
| Count of JBoss threads started since system start       | threads     |
| JBoss transactions jts                                  | transact    |
| JBoss number of aborted transactions                    | transact    |
| JBoss number of application rollbacks                   | transact    |
| JBoss number of committed transactions                  | transact    |
| JBoss number of heuristics                              | transact    |
| JBoss number of inflight transactions                   | transact    |
| JBoss number of nested transactions                     | transact    |
| JBoss number of resource rollbacks                      | transact    |
| JBoss number of timed out transactions                  | transact    |
| JBoss number of transactions                            | transact    |
