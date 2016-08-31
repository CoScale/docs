---
layout: page
title: Adding alerts to a notification scheme
description: Steps on how to add alerts to a notification scheme.
---
To create a static alert, go to Alerts -> Manage, select the desired notification scheme and click the 'Add alert' button to add a new alert to that group.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/01-Add-New-Alert.png" class="img-responsive" />

The alert dialog will appear and you can start configuring the details for the alert.

<ul>
    <li>Select alert type: <strong>Static</strong></li>
    <img alt="Add alert screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/02-Alert-Type.png" style="margin-bottom: 15px;"/>
    <li>Select the type of data. E.g.: Server Metric.</li>
    <img alt="Add alert screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/03-Server-Metric.png" style="margin-bottom: 15px;"/>
    <li>Configure <strong>alert rule</strong>
      <ul>
        <li>Configure all the parameters. Auto resolving is turned on by default and we recommend to leave it on. The widget with the red line is a visual representation of when the alert should be triggered.</li>
        <img alt="Add alert screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/04-Alert-Rule.png" style="margin-bottom: 15px;"/>
      </ul>
    </li>
    <li>Give your alert a <strong> name </strong></li>
    <img alt="Add alert screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/05-Alert-Name.png" style="margin-bottom: 15px;"/>
    <li>Click on <strong> Finish </strong> and your new alert will appear in the list in the notification scheme block.</li>
    <img alt="Add alert screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/06-Finish.png" style="margin-bottom: 15px;"/>
</ul>

When hovering over a row you will see the `Edit` and `Delete` buttons appear, use these if you wish to change your alert.

<img alt="Edit alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/07-Edit-Delete-Alert.png" class="img-responsive" />
