---
layout: page
title: OpsGenie alert integration
description: Tutorial on how to integrate CoScale alerting with OpsGenie
---

CoScale supports sending alerts to Opsgenie through the CoScale webhook API system. You can find the configuration pages for this on our <a href="http://app.coscale.com" db-href="/alerts/manage/" class="js-dashboard-link">`Alert > Manage`</a> page inside the CoScale application. Keep in mind you need to set this up for each `Notification scheme`.

## Configuration

### 1. Get your OpsGenie API Key

Go to Integrations and copy the Default API key.

<img alt="" src="{{ site.baseurl }}/gfx/alerting/integrations/opsgenie/opsgenie.jpg" class="img-responsive" alt="OpsGenie API Key" />

In CoScale we will use the API integration to create push alerts to OpsGenie.

### 2. Trigger configuration

In CoScale we will use the API integration to create push alerts to OpsGenie. Please select the notification scheme you would like to push to OpsGenie and click on the `Edit` button.

<img src="{{ site.baseurl }}/gfx/alerting/integrations/notificationscheme_edit.png" class="img-responsive" alt="Edit button location" />

After click `Add contact` and select `API`. Copy the instructions below to the API configuration. Make sure your replace the apiKey `[[api key]]` and teams in the configuration when needed.

#### Trigger

{% highlight bash %}
# Method:
POST
# URL:
https://api.opsgenie.com/v1/json/alert

# Body:
{
     "apiKey": "[[api key]]",
     "message" : "Alert {ACTION} for {MSG} {METRIC}{SUBJECT}{DIMENSIONS}at {TIME} ({DATE}) on application {APP_NAME}. {LINK}",
     "teams" : ["operations", "developers"]
}

# Headers:
      Content-type: application/json

# Parse Response:
JSON: alertId
{% endhighlight %}

#### Acknowledge

{% highlight bash %}
# Method:
POST
# URL:
https://api.opsgenie.com/v1/json/alert/acknowledge

# Body:
{
      "apiKey": "[[api key]]",
      "id": "{ID}"
}

# Headers:
      Content-type: application/json
{% endhighlight %}

#### Resolve

{% highlight bash %}
# Method:
POST
# URL:
https://api.opsgenie.com/v1/json/alert/close

# Body:
{
      "apiKey": "[[api key]]",
      "id": "{ID}"
}

# Headers:
      Content-type: application/json
{% endhighlight %}

### 4. Test CoScale trigger

Use the `Test trigger` button in the configuration window to test the integration with Opsgenie. You should see an alert appear in a couple of seconds.
