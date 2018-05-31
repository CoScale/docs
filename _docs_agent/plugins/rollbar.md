---
layout: page
title: Monitoring and collecting data from Rollbar
description: Information on the metrics collected by the CoScale Rollbar plugin.
---

> Catch code errors before your users. Full-stack error monitoring for all apps in any language. Quickly pinpoint what’s broken and why. Rollbar collects a wide variety of context data, including detailed stack traces, request params, URL, environment, affected users and much more. Review error trends by occurrence, browser, deployment, OS, location, user, host.

More information on: [https://rollbar.com/](https://rollbar.com/)

## Installation

{% include_relative _thirdparty.md %}


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/rollbar.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
