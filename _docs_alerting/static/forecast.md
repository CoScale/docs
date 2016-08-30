---
layout: page
title: Forecast alerts
description: Tutorial on how to setup a forecast alert on the CoScale platform
---

To create a forecast alert, go to your desired notification block and click the 'Add alert' button to add a new alert to that group.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/addAlert.png" class="img-responsive" />

The alert flow will appear and you can start configuring the details for the alert. First step is selecting the `Forecast` option on the alert type screen.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/forecast/forecast1.png" class="img-responsive" />    

After you need to select the type of metric you would like to forecast on.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/forecast/forecast2.png" class="img-responsive" />    

After we need to define the past data we will use to forecast on, and how many days we want to forecast in the future. You get an immediate example of the forecasted metric, including a red line to show the threshold you've set the alert on. You can chose to automatically resolve alerts when they no longer hit the threshold you've set.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/forecast/forecast3.png" class="img-responsive" />    

The last step is to give the alert a name and a description.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/forecast/forecast4.png" class="img-responsive" />    

You have now setup an alert that will trigger days before a certain threshold is met, this gives you more to respond.
