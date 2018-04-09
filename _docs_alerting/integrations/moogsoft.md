---
layout: page
title: Moogsoft alert integration
description: Tutorial on how to integrate CoScale alerting with Moogsoft
---

CoScale supports sending alerts to Moogsoft through the CoScale webhook system. You can find the configuration pages for this on our <a href="http://app.coscale.com" db-href="/alerts/manage/" class="js-dashboard-link">`Alert > Manage`</a> page inside the CoScale application. Keep in mind you need to set this up for each `Notification scheme`.

## Configuration

### 1. Select the Webhook solution pack in Moogsoft

Use the navigation bar at the top of the page in Moogsoft to navigate to `Integrations`. At the button of the page you will find the `Webhook integration`.

<img src="{{ site.baseurl }}/gfx/alerting/integrations/moogsoft/moogsoft_webhook.png" class="img-responsive" alt="Moogsoft webhook button" />

After clickin on the webhook icon please enter `CoScale` into the integration name field on the following page and click `Save`.

### 2. CoScale Trigger configuration

In CoScale we will use the webhook integration to create push alerts to Moogsoft. Please select the notification scheme you would like to push to Moogsoft and click on the `Edit` button.

<img src="{{ site.baseurl }}/gfx/alerting/integrations/notificationscheme_edit.png" class="img-responsive" alt="Edit button location" />

After click `Add contact` and select `Webhook`. Follow the instructions below to setup the integration.

### 3. Configuration

You can find the webhook url on the Moogsoft integration page, copy it to the `WebHook URL` field. After copy the following to the `Format` field. You don't need to change anything here.

{% highlight json %}
{
"source": "{SUBJECT}",
"external_id": "{ALERT_ID}",
"type": "{METRIC}",
"class": "{ACTION}",
"description": "{MSG}",
"agent_time": "{TIMESTAMP}"
}
{% endhighlight %}

Next you need to add two headers by clicking on the `Add Header` button twice.

* The first header field will contain the authentication data. Please add `Authorization: Basic [[token]]`. The token value can be generated using [using this tool](https://www.base64encode.org/). This is because Moogosft requires the authentication to be base64 encoded. Enter the `username/password` (you can find the values in Moogsoft) in the top field of the tool and click on `Encode`. The result field contains the value of `[[token]]`.

* The second header field contains the following `Content-Type": "application/json`



### 4. Test CoScale trigger

Use the `Test trigger` button in the configuration window to test the integration with Pagerduty. You should see an alert appear in a couple of seconds.
