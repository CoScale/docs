---
layout: page
title: Slack alert integration
description: Tutorial on how to integrate alerting with slack
---
<p>
    To integrate alerts with slack all you need to do is add a contact to an alert and set the <strong>contact method</strong> to <strong>Slack</strong> and set the <strong>slack url</strong>.
</p>

<p>
    <img src="{{ site.baseurl }}/gfx/alerting/integrations/slack/slackContactMethod.png"/>
</p>

<h3>Slack URL integration setup</h3>

<p>To obtain the slack URL you must configure an incoming webhook for your slack</p>

<p>
    <a href="https://api.slack.com/incoming-webhooks">Incoming Webhooks</a> is a mechanism to send messages to your Slack Channel from external sources. These external sources could be any application or service that is capable of sending a JSON payload over HTTP into a Slack Channel. Each Channel will be identified by a unique Incoming Webhook URL to which you can post the message from outside. This configuration is done via the Integrations for your channel.
</p>

<p>
    Assuming that you are the Administrator for your Slack Team Account, log in to the Slack Team Portal and go to Configure Integrations as shown below:
</p>

<p>
    <img src="{{ site.baseurl }}/gfx/alerting/integrations/slack/02-slack-configure-integration_0.png"/>
</p>

<p>
    This will bring up the Configure Integrations page where you can add various integration services to your Team. Since we are interested in Incoming Webhooks Integration, just type “incoming” in the filter search input box as shown below:
</p>

<p>
    <img src="{{ site.baseurl }}/gfx/alerting/integrations/slack/03-slack-filter-search-incoming.png"/>
</p>

<p>
    Click on View and it should bring up a form to configure the Incoming Webhooks Integration.
</p>

<p>
    The first step is to specify the channel that you want to send the messages to as shown below. We have chosen the #general channel over here.
</p>

<p>
    <img src="{{ site.baseurl }}/gfx/alerting/integrations/slack/04-slack-channel-general.png"/>
</p>

<p>
    Click on Add Incoming Webhooks Integration. This will setup the Integration for you and provide you with a publicly reachable Webhook URL. Scroll down to the Integration Settings section and you should see the details with the channel that you selected the URL that you need to post the message to.
</p>

<p>
    <img src="{{ site.baseurl }}/gfx/alerting/integrations/slack/05-slack-add-incoming-webhooks-integration.png"/>
</p>

<p>
    Remember to click on Save Settings and you should be all set with the Incoming Webhook configured and waiting for your message.
</p>




