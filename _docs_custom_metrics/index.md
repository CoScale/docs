---
layout: page
title: Custom metrics
description: Information on how to push custom metrics to the CoScale platform.
---

Custom metrics allow you to monitor certain aspects of your application that would otherwise stay hidden to you. CoScale provides a couple of ways of integrating these metrics into our platform. CoScale can pull metrics from [scripts or binary executables]({{ site.baseurl }}/custom-metrics/generic-script/index), or you can [push metrics to CoScale with the help from our CLI tool]({{ site.baseurl }}/custom-metrics/cli/). We also provide integration with third party tools, like [StatsD]({{ site.baseurl }}/custom-metrics/statsd/index).

* [Pulling metrics from your application with generic script]({{ site.baseurl }}/custom-metrics/generic-script/index)

    By running a script or executable every minute the CoScale agent gathers metrics from your application and pushes those to the platform. We provide some example scripts and guide your in configuring it for your application.

* [Pushing metrics with our CLI]({{ site.baseurl }}/custom-metrics/cli/)

    Our CLI allows you to push multiple metrics at the same time from the command line. You can use it together with bash scripts to get your custom data inside CoScale.

## Third party

* [StatsD]({{ site.baseurl }}/custom-metrics/statsd/index)
