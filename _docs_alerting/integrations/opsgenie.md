---
layout: page
title: OpsGenie alert integration
description: Tutorial on how to integrate alerting with OpsGenie
---

### Get your OpsGenie API Key

Go to Integrations and copy the Default API key.

<img alt="" src="{{ site.baseurl }}/gfx/alerting/integrations/opsgenie/opsgenie.jpg" class="img-responsive" alt="OpsGenie API Key" />

In CoScale we will use the API integration to create push alerts to OpsGenie.

### Trigger configuration

```html
Method: POST
URL: https://api.opsgenie.com/v1/json/alert

Body:
{
     "apiKey": "37a3eab4-c110-4bf0-8b47-f000ed83f470",
     "message" : "Alert {ACTION} for {MSG} {METRIC}{SUBJECT}{DIMENSIONS}at {TIME} ({DATE}) on application {APP_NAME}. {LINK}",
     "teams" : ["operations", "developers"]
}

Headers:
Content-type: application/json

Parse Response: JSON alertId
```

### Acknowledge configuration

```html
Method: POST
URL: https://api.opsgenie.com/v1/json/alert/acknowledge

Body:
{
      "apiKey": "37a3eab4-c110-4bf0-8b47-f000ed83f470",
      "id": "{ID}"
}

Headers:
Content-type: application/json
```

### Resolve configuration

```html
Method: POST
URL: https://api.opsgenie.com/v1/json/alert/close

Body:
{
      "apiKey": "37a3eab4-c110-4bf0-8b47-f000ed83f470",
      "id": "{ID}"
}

Headers:
Content-type: application/json
```
