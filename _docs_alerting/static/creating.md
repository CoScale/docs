---
layout: page
title: Adding alerts to a notification scheme
description: Steps on how to add alerts to a notification scheme.
---
To create a static alert, go to your desired notification block and click the 'Add alert' button to add a new alert to that group.

<img alt="Add alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/addAlert.png" class="img-responsive" />

The alert dialog will appear and you can start configuring the details for the alert.

* **Name:** The name for the alert.

* **Description:** A description for the alert.

* **Datatype:** Which datatype do you want to monitor?

* **Use forecast data?:** Do you wish to include fore-casted data in the alert so you can preemptively be alerted?

* **Subject:** The level on which the alert should monitor. If you choose server you will also be able to specify a specific server or servergroup.

* **Alert rule:** You have several different inputs that together will define the exact rule for the alert.

* **Automatically resolve alert?:** If you wish for CoScale to automatically resolve emails for you after a specific period then leave this turned on. (Our recommendation is to keep it turned on)

* **Automatically resolve after:** The time after which the alert will get auto resolved.

The widget with the red line is a visual representation of when the alert should be triggered.

<img alt="Alert setup screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/alertDialog.png" class="img-responsive" />

Once you are finished configured all the parameters click `Save` in the dialog and you will see the alert appear in the list in the notification scheme block.

<img alt="Alert created screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/alertCreated.png" class="img-responsive" />

When hovering over a row you will see the `Edit` and `Delete` buttons appear, use these if you wish to change your alert.

<img alt="Edit alert button screenshot" src="{{ site.baseurl }}/gfx/alerting/createAlert/editAlert.png" class="img-responsive" />
