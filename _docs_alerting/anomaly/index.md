---
layout: page
title: Anomaly detection
description: Smart analysis of server metrics
---

## What is anomaly detection

The goal of automated anomaly detection is to relieve the user from having to watch all metrics all of the time to detect when things go wrong. Instead, the incoming data is analyzed automatically and compared to the behavior observed in the recent past. Only when the new data is significantly different from what was expected, the user will be signaled.

CoScale runs anomaly detection on the data received from the different sources: installed agents, third-party plugins and real-user monitoring. Depending on the type of data, different algorithms or parameters are used. For example, some data typically exhibits seasonal behavior, like number of visitors to a web page, while other data, e.g. the memory consumption on server, does not. 

## Inspecting anomalies
You can inspect anomalies by creating an `Anomaly Timeline` chart:

<img src="{{ site.baseurl}}/gfx/installation/alerting/anomaly/anomalywidget_selection.png" alt="Anomaly widget selection" class="img-responsive" />

That looks as follows:

<img src="{{ site.baseurl}}/gfx/installation/alerting/anomaly/anomaly_overview.png" alt="Anomaly overview" class="img-responsive" />

All detected anomalies appear on this chart, categorized by the impact they have:

* Anomalies reported as `Business` mean that they may affect you business, e.g. a sudden drop in the number of orders.
* Anomalies reported as `User` mean that visitors to your site may be affected by the detected anomaly, e.g. when a significant increased latency was observed.
* Anomalies reported as `Server` mean that an anomaly was detected on your infrastructure, like an unexpected increase or drop in CPU, memory, disk or network usage.

More details about the anomalies can be obtained by clicking on the chart. This will select a certain time range and for each anomaly in that time range a tile with more information on the anomaly is shown on the dashboard:

<img src="{{ site.baseurl}}/gfx/installation/alerting/anomaly/anomaly_tiles.png" alt="Anomaly tiles" class="img-responsive" />

When clicking on the graph button on a tile, a widget showing the actual anomaly is added to the dashboard, which look as follows:

<img src="{{ site.baseurl}}/gfx/installation/alerting/anomaly/anomaly_metric.png" alt="Anomaly visualization" class="img-responsive" />

The light red background indicates the time range during which the anomaly was detected. 

As on any dashboard, one can add other widgets as well, which can be useful for interpreting the anomaly in a broader context.
