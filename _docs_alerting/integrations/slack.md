---
layout: page
title: Slack alert integration
description: Tutorial on how to integrate alerting with slack
---

To integrate alerts with slack all you need to do is add a contact to an alert and set the **contact method** to **Slack** and add the **Slack webhook url**. Follow the instructions below to get your webhook url.

<img alt="" src="{{ site.baseurl }}/gfx/alerting/integrations/slack/slackContactMethod.png" class="img-responsive" />

### How to get a Slack webhook url

To obtain a Slack webhook url you have to configure a new incoming webhook for your Slack channel.

*<a href="https://api.slack.com/incoming-webhooks">Incoming Webhooks</a> is a mechanism to send messages to your Slack Channel from external sources. These external sources could be any application or service that is capable of sending a JSON payload over HTTP into a Slack Channel. Each Channel will be identified by a unique Incoming Webhook URL to which you can post the message from outside. This configuration is done via the Integrations for your channel.*

Assuming that you are the Administrator for your Slack Team Account, log in to the Slack Team Portal and go to `Configure Integrations` as shown below:

<img alt="Slack menu screenshot" src="{{ site.baseurl }}/gfx/alerting/integrations/slack/02-slack-configure-integration_0.png"/>

This will bring up the `Configure Integrations` page where you can add various integration services to your Team. Since we are interested in `Incoming Webhooks Integration`, just type “incoming” in the filter search input box as shown below:

<img alt="Slack configuration search screenshot" src="{{ site.baseurl }}/gfx/alerting/integrations/slack/03-slack-filter-search-incoming.png"/>

Click on `View` and it should bring up a form to configure the Incoming Webhooks Integration.

The first step is to specify the channel that you want to send the messages to as shown below. We have chosen the `#general` channel over here.

<img alt="Slack configuration channel screenshot" src="{{ site.baseurl }}/gfx/alerting/integrations/slack/04-slack-channel-general.png"/>

Click on `Add Incoming Webhooks Integration`. This will setup the Integration for you and provide you with a publicly reachable Webhook URL. Scroll down to the `Integration Settings` section and you should see the details with the channel that you selected the URL that you need to post the message to.

<img alt="Slack configuration settings screenshot" src="{{ site.baseurl }}/gfx/alerting/integrations/slack/05-slack-add-incoming-webhooks-integration.png"/>

Remember to click on `Save Settings` and you should be all set with the Incoming Webhook configured and waiting for your message.
