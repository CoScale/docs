---
layout: page
title: Monitoring and collecting data from JBoss
description: Information on the metrics collected by the CoScale JBoss plugin.
---

> Red Hat® JBoss® Middleware is a family of a lightweight, cloud-friendly, enterprise-grade products that help enterprises innovate faster, in a smarter way.

More information on: [http://www.jboss.org/](http://www.jboss.org/)

## How it works

This plugin analyzes the performance of your JBoss web server.

It captures traffic rates, latencies and response codes of requests sent to the web server by parsing the JBoss access log file. The plugin can get global statistics (the number of connections, the number of workers, etc.) using the JMX interface of the JBoss web server.

**The minimal supported version of JBoss is 7.1.**

## Installation

{% include_relative _installation.md orchestrator="false" service="JBoss" %}

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


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/jboss.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
