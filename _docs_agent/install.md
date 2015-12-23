---
layout: page
title: Installing the agent
description: Instructions on how to install and configure the CoScale agent.
---

## What is an agent
The CoScale agent is the primary tool used to capture resource and application metrics from your servers. It is easy to configure and deployed in minutes. The same agent can be installed on multiple servers, for example you create a webserver agent which you install on each of your webservers.

{% include alert.html type="warning" text="The following steps require root or administrator access to the servers that host your application. If you don't have access, please <a href=\"mailto:info@coscale.com\" class=\"js-support\">contact support</a> so they can provide alternatives." %}

In the video below you can see a quick walkthrough on how to configure and install the CoScale agent. For further instructions you can check the documentation below the video.

<div id="video" class="embed-responsive embed-responsive-16by9">
    <iframe class="js-video embed-responsive-item" src="https://www.youtube-nocookie.com/embed/8b5mk3wHFdE?rel=0" frameborder="0" allowfullscreen></iframe>
</div>

## Creating the agent
To start with the configuration, go to your dashboard and use the sidebar to navigate to <a href="http://app.coscale.com" db-href="/datasources/agentnew/" class="js-dashboard-link">`DataSources > CoScale agent > Manage`</a>. On this page you can  configure the agent(s) you want to install on your servers. There is no limit on the amount of agents you can create.

### Step 1: Select your operating system

Select the type and flavor of operating system on which the agent will be installed and click `Next step`.

{% include alert.html type="info" text="We only support 64 bit operating systems, <a href=\"mailto:info@coscale.com\" class=\"js-support\">contact support</a> for more information" %}


### Step 2: Enable some plugins

Enable all plugins you want to activate for this agent. The resource plugin is enabled by default, but you probably also want to enable other plugins. For a web server running Tomcat i.e. you would enable the Tomcat plugin by clicking on it. You can enable as many plugins as you like.

Some plugins require further configuration. Read and follow the instructions carefully.
If necessary, apply the proposed changes to the server as shown in the instructions and fill in the required fields. Click  `Next step` when you have finished configuring your plugins.

{% include alert.html type="info" text="You can easily activate more plugins later and reconfigure them without having to re-install the agent." %}

### Step 3: Almost ready. Your agent is configured as follows

Verify the configuration of your agent. Then you can give your agent a clear, recognizable name: i.e. ‘Webserver’ and press the `Save agent` button.

### Step 4: Download and install your agent

You have now created an agent which you can deploy on as many servers as you'd like. A download link will appear with the installation files for your operating system. The instructions for installing the agent on your operating system will be shown after you click the 'Download agent' button.

<!-- INSERT javascript to see installation instructions from /agent/agent-install -->
<!-- Go to [agent install]({{ site.baseurl }}/agent/agent-install) page, to find the install instructions for your operating system. -->

After installing the agent it will check the configuration of all the selected plugins and will start to communicate with the CoScale platform. This can take a couple of minutes.

{% capture text %}Our agent requires port 443 to be open for outbound traffic. Checkout our <a href="{{ site.baseurl }}/advanced/security/">security page</a> for more information. {% endcapture %}
{% include alert.html type="info" text=text %}

## Checking the installation

You can get an overview of installed agents on the <a href="http://app.coscale.com" db-href="/datasources/agentinstalled/" class="js-dashboard-link">`DataSources > CoScale agent > Installed`</a> page, accessible through the sidebar. Any configuration problems we detect will be shown here.

To get more information about the agent, you can always click the service icon, it will provide you with the latest log and status of all the plugins.

## Agent successfully installed

The agent is now installed and running on your system. You can now repeat this process for servers that require a different set of plugins or configuration.
