---
layout: page
title: Monitoring and collecting data from Sentry
description: Information on the metrics collected by the CoScale Sentry plugin.
---

> Sentry’s real-time error tracking gives you insight into production deployments and information to reproduce and fix crashes.

More information on: [https://sentry.io/](https://sentry.io/)

## Installation

{% include_relative _thirdparty.md %}


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/sentry.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
