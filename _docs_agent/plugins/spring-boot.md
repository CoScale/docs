---
layout: page
title: Spring Boot plugin
description: Information on the metrics collected by the CoScale Spring Boot plugin.
---

> Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that you can "just run". We take an opinionated view of the Spring platform and third-party libraries so you can get started with minimum fuss.

More information on: [https://projects.spring.io/spring-boot/](https://projects.spring.io/spring-boot/)

## How it works

This plugin analyzes the performance of your SprintBoot web server. It captures traffic rates, latencies and response codes of http requests sent to the web server by parsing the access log file. The plugin can optionally get global statistics (eg. the number of sessions, the number of workers, etc.) and component health status by using the Spring Boot actuator endpoint.

## Installation

{% include_relative _installation.md orchestrator="false" service="Spring Boot" %}

## Configuration

### Configure the actuator endpoint

The plugin will access the actuator `metrics` endpoint. To enable the actuator metrics functionality, you will need to add `spring-boot-starter-actuator` as a dependency to your project.

#### Spring Boot 1.x
In order to get the actuator metrics we require Spring MVC to expose its endpoints through HTTP. You can decide whether the endpoint will be sensitive (meaning not public and requires a user/password to access) or not. For example, add the following entries in the `application.properties` to customize the `/metrics` endpoint:

{% highlight ini %}
endpoints.metrics.sensitive=false
endpoints.metrics.enabled=true
{% endhighlight %}

#### Spring Boot 2.x

In 2.x Spring Boot simplifies the actuator security model by merging it with the application one and the endpoints have moved to the `/actuator/metrics` location. The metrics endpoint will need to be marked as exposed in your `application.properties`:

{% highlight ini %}
management.endpoints.web.exposure.include=...,metrics,...
{% endhighlight %}

### Configure your Spring Boot access logs

Enable the Spring Boot access log format. Add the following configuration to your `application.properties`. The configuration differs depending on the embedded servlet container you are using.

#### Tomcat

{% highlight ini %}
server.tomcat.basedir=<log_dir>
server.tomcat.accesslog.enabled=true
server.tomcat.accesslog.pattern=%v %B %D "%r" %A %a %t %H %p %U %s %S %T
{% endhighlight %}

#### Undertow

{% highlight ini %}
server.undertow.accesslog.dir=target/logs
server.undertow.accesslog.enabled=true
server.undertow.accesslog.pattern=%v %B %D "%r" %A %a %t %H %p %U %s %S %T
server.undertow.accesslog.prefix=access_log.
server.undertow.accesslog.rotate=true
server.undertow.accesslog.suffix=log
{% endhighlight %}

#### Jetty

{% highlight ini %}
server.jetty.accesslog.enabled=true
server.jetty.accesslog.append=true
server.jetty.accesslog.filename=access.log
server.jetty.accesslog.log-latency=true
server.jetty.accesslog.log-server=true
{% endhighlight %}

#### Log format

Then use this `%h %v %I %u %t "%r" %s %B %D` logformat for the plugin.

### Active checks

The plugin will check the actuator health endpoint, to determine your application latency and health status on a per component basis.

#### Spring Boot 1.x:
The health endpoint can be enabled in your application.properties by the following:

{% highlight ini %}
endpoints.health.sensitive=false
endpoints.health.enabled=true
management.security.enabled=false
{% endhighlight %}

#### Spring Boot 2.x:
The health endpoint will need to be marked as exposed in your application.properties:

{% highlight ini %}
management.endpoints.web.exposure.include=...,health,...
management.endpoint.health.show-details=always
{% endhighlight %}

#### HTTP Check

This plugin can be configured to perform a HTTP GET on your Spring Boot. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost/test_page`) should be provided.

## Events

* Service state

## Metrics

| Metric name                                           | Metric unit |
|-------------------------------------------------------|-------------|
| Spring Boot uptime | s
| Spring Boot application context uptime | s
| Spring Boot commited heap memory | b
| Spring Boot initial heap memory | b
| Spring Boot used heap memory | b
| Spring Boot max heap memory | b
| Spring Boot commited non heap memory | b
| Spring Boot initial non heap memory | b
| Spring Boot used non heap memory | b
| Spring Boot max non heap memory | b
| Spring Boot processors count | #
| Spring Boot total memory | b
| Spring Boot free memory | b
| Spring Boot peak thread count | threads
| Spring Boot daemon thread count | threads
| Spring Boot total started thread count | threads
| Spring Boot thread count | threads
| Spring Boot total classes count | classes
| Spring Boot loaded classes count | classes
| Spring Boot unloaded classes count | classes
| Spring Boot GC collection count | #
| Spring Boot GC collection time | s
| Spring Boot active http sessions | sessions
| Spring Boot max http sessions | sessions
| Spring Boot tomcat expired sessions | sessions
| Spring Boot average system load |
| Spring Boot datasource number of active connections | connections
| Spring Boot datasource current usage of the connection pool | #
| Spring Boot request counts | requests
| Spring Boot gc max size of old generation memory pool | b
| Spring Boot gc memory allocated | b
| Spring Boot size of old generation memory pool after a full gc | b
| Spring Boot jvm buffer pool memory usage | b
| Spring Boot tomcat max threads | threads
| Spring Boot tomcat bytes sent per second | b/s
| Spring Boot tomcat bytes received per second | b/s
| Spring Boot response time | s
| Spring Boot active check uptime | %
| Spring Boot active check uptime | s
