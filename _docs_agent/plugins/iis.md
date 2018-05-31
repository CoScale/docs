---
layout: page
title: Monitoring and collecting data from IIS - Internet Information Services
description: Information on the metrics collected by the CoScale IIS plugin.
---

> Internet Information Services (IIS) for Windows® Server is a flexible, secure and manageable Web server for hosting anything on the Web. From media streaming to web applications, IIS's scalable and open architecture is ready to handle the most demanding tasks.

More information on: [https://www.iis.net/](https://www.iis.net/)

## How it works

The plugin gathers global statistics using the performance counter client. No configuration is needed. It captures traffic rates, latencies and response codes of requests sent to the web server by parsing the IIS access log file. See next step for more information.

**The minimal supported version of IIS is 7.0.**

## Installation

{% include_relative _installation.md orchestrator="false" service="IIS" %}

## Configuration

1. Open "Internet Information Services (IIS) Manager"

2. Select the connection to your server.

3. Double click the Logging icon.
![Logging icon location]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/select_logging.png)

4. Select the W3C Format and click Select Fields

    ![W3C format selection]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/w3c_format.png)

5. Select the following fields:
    `cs-uri-stem cs-uri-query sc-status sc-bytes cs-bytes time-taken cs-host`
![W3C format fields]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/w3c_fields1.png)
![W3C format fields]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/w3c_fields2.png)

6. Apply the log format
![Apply format link]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/apply_format.png)

7. Go back to the Server view and restart the IIS service
![Restart server link]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/restart_server.png)



<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/iis.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
