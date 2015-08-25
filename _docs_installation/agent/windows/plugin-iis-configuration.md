---
layout: page
title: Configure IIS - Internet Information Services
---

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
