---
layout: page
title: PagerDuty alert integration
description: Tutorial on how to integrate alerting with PagerDuty
---

### Get your PagerDuty API Key

Go to the Configuration menu and select API Access. Click Create New API Key.

More info on generating API Token key: <a href="https://support.pagerduty.com/hc/en-us/articles/202829310-Generating-an-API-Key" target="_blank">https://support.pagerduty.com/hc/en-us/articles/202829310-Generating-an-API-Key</a>

CoScale uses the v2 PagerDuty API.

<img alt="" src="{{ site.baseurl }}/gfx/alerting/integrations/pagerduty/01-pagerduty-apikey.jpg" class="img-responsive" alt="PagerDuty API Key" />

### Get your Service ID

* Go to the Service > Service details page in PagerDuty
* The URL has this format: `https://<NAME>.pagerduty.com/services/<SERVICE ID>`
* Copy the `<SERVICE ID>` from the URL

<img alt="" src="{{ site.baseurl }}/gfx/alerting/integrations/pagerduty/02-pagerduty-serviceid.png" class="img-responsive" alt="PagerDuty Service ID" />

In CoScale we will use the API integration to create push alerts to PagerDuty.

### Trigger configuration

{% highlight %}
Method: POST
URL: https://api.pagerduty.com/incidents

Body:
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

Headers:
	Content-Type: application/json
	Accept: application/vnd.pagerduty+json;version=2
	Authorization: Token token=zXg83wYr26nyx_3GVPy7
	From: your@email.here

Parse response: JSON incident.id
{% endhighlight %}

<img alt="" src="{{ site.baseurl }}/gfx/alerting/integrations/pagerduty/03-pagerduty-coscale.png" class="img-responsive" alt="PagerDuty CoScale" />

### Acknowledge configuration

{% highlight %}
Method: PUT
URL: https://api.pagerduty.com/incidents

Body:
{
	"incidents": [{
		"id": "{ID}",
		"type": "incident_reference",
		"status": "acknowledged"
	}]
}

Headers:
	Content-Type: application/json
	Accept: application/vnd.pagerduty+json;version=2
	Authorization: Token token=zXg83wYr26nyx_3GVPy7
	From: your@email.here
{% endhighlight %}

### Resolve configuration

{% highlight %}
Method: PUT
URL: https://api.pagerduty.com/incidents
Body:
{
	"incidents": [{
		"id": "{ID}",
		"type": "incident_reference",
		"status": "resolved"
	}]
}

Headers:
	Content-Type: application/json
	Accept: application/vnd.pagerduty+json;version=2
	Authorization: Token token=zXg83wYr26nyx_3GVPy7
	From: your@email.here
{% endhighlight %}
