---
layout: page
title: Custom metrics
description: Information on how to push custom metrics to the CoScale platform.
---

Custom metrics allow you to monitor certain aspects of your application that would otherwise stay hidden to you. CoScale provides a couple of ways of integrating these metrics into our platform. CoScale can pull metrics from [scripts or binary executables]({{ site.baseurl }}/custom-metrics/generic-script/index), or you can [push metrics to CoScale with the help from our CLI tool]({{ site.baseurl }}/custom-metrics/cli/). We also provide integration with third party tools, like [StatsD]({{ site.baseurl }}/custom-metrics/statsd/index).

* [Pulling metrics from your application with generic script]({{ site.baseurl }}/custom-metrics/generic-script/index)

    By running a script or executable every minute the CoScale agent gathers metrics from your application and pushes those to the platform. We provide some example scripts and guide your in configuring it for your application.

    Pros:

    * Language agnostic
    * Easy to setup

    Cons:

    * Works best with minute data
    * Script cannot run longer than 5 seconds

* [Pushing metrics with our CLI]({{ site.baseurl }}/custom-metrics/cli/)

    Our CLI allows you to push multiple metrics at the same time from the command line. You can use it together with bash scripts to get your custom data inside CoScale. our CLI is installed automatically with our agent, or you can also install it manually if you don't have an agent installed.

    Pros:

    * Can be integrated with existing scripts
    * Good for long duration commands

    Cons:

    * Might be too low-level for some situations.


* [CoScale API]({{ site.baseurl }}/api/)
    
    Our API provides you with the tools to manage data using your favorite programming language. At the moment you will need to write your own code to manage the whole procedure of communicating with the API. We are investigating possibilities in creating SDKs for the most popular languages.

    Pros:

    * Fine grained control

    Cons:

    * Requires heavy code integration

* [StatsD]({{ site.baseurl }}/custom-metrics/statsd/index)

    If you are using StatsD you can integrate the CoScale StatsD plugin and it will push all metrics available in the StatsD daemon to the CoScale infrastructure every minute

    Pros:

    * Language agnostic
    * Libraries available for all popular [languages](https://github.com/etsy/statsd/wiki) 

    Cons:

    * Daemon on machine
    * Code integration

* CollectD

    If you are using CollectD then you can enabled the CollectD CoScale agent plugin and it will push the data to CoScale.

    Pros:

    * Huge library of [existing scripts](https://collectd.org/wiki/index.php/Table_of_Plugins)

    Cons:

    * Daemon on machine

