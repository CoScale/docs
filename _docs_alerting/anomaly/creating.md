---
layout: page
title: Anomaly alerts
description: Tutorial on how to setup a anomaly alert on the CoScale platform
---

To create an anomaly alert, go to your desired notification block and click the 'Add alert' button to add a new alert to that group.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/addAlert.png" class="img-responsive" />

The alert flow will appear and you can start configuring the details for the alert. First step is selecting the `Anomaly` option on the alert type screen.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/anomaly/anomaly1.png" class="img-responsive" />    

After you need to select the type of metric you would like to receive anomalies from.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/anomaly/anomaly2.png" class="img-responsive" />    

Then you have the option to blacklist certain servers, server groups, metrics or metric groups. You could for example blacklist your development and staging servers, so you only receive anomalies for your production environment.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/anomaly/anomaly3.png" class="img-responsive" />    

I've chosen here to blacklist the metric group `CollectD`. You can blacklist as many thing as you'd like.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/anomaly/anomaly4.png" class="img-responsive" />    

The last step is to give the alert a name and a description.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/anomaly/anomaly5.png" class="img-responsive" />    

You will now receive anomaly emails for the type of metric you've selected, but without the metrics/servers you blacklisted. 
