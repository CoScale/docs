---
layout: page
title: Third party incident manager integration
description: Integration with third party incident managers
---

When the CoScale monitoring service triggers an alert is it possible to send the notification to a third party incident manager. We do this by sending an e-mail to the provider containing information about the incident. Follow the steps to integrate CoScale with your third party provider.

1. **Find your third party e-mail**

    To send alerts to your third party service CoScale needs a custom e-mail as endpoint. Use the guides from third party providers to find the correct e-mail address you have to use for receiving alerts.

    * <a href="https://www.pagerduty.com/docs/guides/email-integration-guide/" target="_blanc">PagerDuty</a>
    * <a href="http://victorops.force.com/knowledgebase/articles/Integration/Generic-Email-Integration" target="_blanc">VictorOps</a>
    * <a href="https://www.opsgenie.com/docs/integrations/creating-alerts-via-email" target="_blanc">OpsGenie</a>

    If you cannot find your favorite third party tool, please don't hesitate to <a href="mailto:info@coscale.com" class="js-support">contact us</a> for more information and support.

2. **Add the e-mail to CoScale**

    Now that you have your third party email it is time to add it to a CoScale notification scheme.

    <img src="/gfx/installation/alerting/static/third-party/alert_notifications.png" alt="Alert view" class="img-responsive" />

    First go to <a href="http://app.coscale.com" db-href="/alerts/manage/" class="js-dashboard-link">`Alerts > Manage`</a> here you can choose to add the third party email to a new or an existing scheme.
    To add it to a new one: click the `Create notification scheme` button and add the e-mail in the `Main contact(s)` field. To add it to an existing one: click the `Edit` button next to the scheme you want to edit and do the same

    <img src="/gfx/installation/alerting/static/third-party/alert_email.png" alt="Where to fill in the e-mail address" class="img-responsive" />

    After filling in the e-mail, click `save` and from now on all alerts will also be sent to your third-party incident manager.
