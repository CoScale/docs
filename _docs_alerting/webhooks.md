---
layout: page
title: Webhooks
description: Using webhooks to route alerts to other systems
---

Webhooks allow you to route CoScale alerts to other systems. You can use a webhook on an alert to route it to services that send messages to a team, or any other type of action.

In order to use webhooks, follow the steps below:

## Go to Alerts -> Manage

Click on the "Create a notification scheme" button.

## Click on "Add contact"

Select "Webhook" as a contact method.

<img alt="Add notification scheme buttons screenshot" src="{{ site.baseurl }}/gfx/alerting/notificationScheme/webhooks.png"/>

## Customize your webhook

You can use the following Alert fields in the body:
* {ALERT_ID}: the alert ID
* {SUBJECT}: the server or server group name
* {METRIC}: name of the metric
* {DIMENSIONS}: Dimensions of the metric
* {APP_NAME}: the name of the application
* {ACTION}: triggered / acknowledged / resolved
* {MSG}: the message of the alert
* {LINK}: the link to the alert page
* {DATE}:  alert date
* {TIME}: alert time
