---
layout: page
title: PagerDuty alert integration
description: Tutorial on how to integrate CoScale alerting with PagerDuty
---

CoScale supports sending alerts to PagerDuty through the CoScale webhook API system. You can find the configuration pages for this on our <a href="http://app.coscale.com" db-href="/alerts/manage/" class="js-dashboard-link">`Alert > Manage`</a> page inside the CoScale application. Keep in mind you need to set this up for each `Notification scheme`.

## Configuration

### 1. Get your PagerDuty API Key

Go to the Configuration menu and select API Access. Click `Create New API Key` and `v2 Current` as API version.

More info on generating API Token key can be found on Pagerduty documentation <a href="https://support.pagerduty.com/hc/en-us/articles/202829310-Generating-an-API-Key" target="_blank">https://support.pagerduty.com/hc/en-us/articles/202829310-Generating-an-API-Key</a>

<img src="{{ site.baseurl }}/gfx/alerting/integrations/pagerduty/01-pagerduty-apikey.jpg" class="img-responsive" alt="PagerDuty API Key" />

### 2. Get your Service ID

* Go to the Service > Service details page in PagerDuty
* The URL has this format: `https://<NAME>.pagerduty.com/services/<SERVICE ID>`
* Copy the `<SERVICE ID>` from the URL

<img src="{{ site.baseurl }}/gfx/alerting/integrations/pagerduty/02-pagerduty-serviceid.png" class="img-responsive" alt="PagerDuty Service ID" />

### 3. CoScale Trigger configuration

In CoScale we will use the API integration to create push alerts to PagerDuty. Please select the notification scheme you would like to push to Pagerduty and click on the `Edit` button.

<img src="{{ site.baseurl }}/gfx/alerting/integrations/notificationscheme_edit.png" class="img-responsive" alt="Edit button location" />

After click `Add contact` and select `API`. Copy the instructions below to the API configuration. Make sure your replace the token `[[your token]]` and email `[[your email]]` in the configuration when needed.

#### Trigger configuration

{% highlight bash %}
# Method:
POST
# URL:
https://api.pagerduty.com/incidents

# Body:
{
	"incident": {
		"type": "incident",
		"title": "Alert {ACTION} for {MSG} {METRIC}{SUBJECT}{DIMENSIONS}at {TIME} ({DATE}) on application {APP_NAME}. {LINK}",
		"service": {
			"id": "PXFL9LI",
			"type": "service_reference"
		}
	}
}

# Headers:
	Content-Type: application/json
	Accept: application/vnd.pagerduty+json;version=2
	Authorization: Token token=[[your token]]
	From: [[your email]]

# Parse response:
JSON: incident.id
{% endhighlight %}

<img alt="" src="{{ site.baseurl }}/gfx/alerting/integrations/pagerduty/03-pagerduty-coscale.png" class="img-responsive" alt="PagerDuty CoScale" />

#### Acknowledge configuration

{% highlight bash %}
# Method:
PUT
# URL:
https://api.pagerduty.com/incidents

# Body:
{
	"incidents": [{
		"id": "{ID}",
		"type": "incident_reference",
		"status": "acknowledged"
	}]
}

# Headers:
	Content-Type: application/json
	Accept: application/vnd.pagerduty+json;version=2
	Authorization: Token token=[[your token]]
	From: [[your email]]
{% endhighlight %}

#### Resolve configuration

{% highlight bash %}
# Method:
PUT
# URL:
https://api.pagerduty.com/incidents

# Body:
{
	"incidents": [{
		"id": "{ID}",
		"type": "incident_reference",
		"status": "resolved"
	}]
}

# Headers:
	Content-Type: application/json
	Accept: application/vnd.pagerduty+json;version=2
	Authorization: Token token=[[your token]]
	From: [[your email]]
{% endhighlight %}

### 4. Test CoScale trigger

Use the `Test trigger` button in the configuration window to test the integration with Pagerduty. You should see an alert appear in a couple of seconds.
