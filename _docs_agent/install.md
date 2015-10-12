---
layout: page
title: Installing the agent
description: Instructions on how to install and configure the CoScale agent.
---

## Precautions
Before we get started with installing the agent it is important to note that the following steps require root or administrator access to the servers that host your application. If you don't have access, please <a href="mailto:info@coscale.com" class="support">contact our support</a> so they can provide alternatives and press the button to the right to skip this step for now.

## Creating the agent
The CoScale agent is the primary tool used to capture resource and application metrics from your servers. It is easy to configure and deployed in minutes. To start with the configuration go to your dashboard and use to sidebar navigation to go to `DataSources` and then `Manage`. On this page, you will be configuring the agent(s) you want to install on your servers.

{% include alert.html type="warning" text="We only support 64 bit operating systems, <a href=\"mailto:info@coscale.com\" class=\"support\">contact support</a> for more information" %}


To get started:

1. Select the operating system and flavor of your server(s)
2. Enable all plugins you want to activate for this agent, the resource plugin is enabled by default, but you probably also want to enabled other plugins. For a web server running Tomcat i.e. you would enable the Tomcat plugin by clicking on it. You can enable as many plugins as you'd like.

{% include alert.html type="info" text="You can later always activate more plugins without having to re-install the agent." %}


<p class="text-center"><img class="img-responsive" src="{{ site.baseurl }}/gfx/getting-started/install-agent/agent_configuration.png" alt="CoScale agent configuration page" /></p>

For some plugins, configuration is necessary. Read and follow the instructions carefully.
If necessary, apply the proposed changes to the server as shown in the instructions and fill in the required fields. Press the save button when finished.

<p class="text-center"><img class="img-responsive" src="{{ site.baseurl }}/gfx/getting-started/install-agent/plugin_configuration.png" alt="CoScale agent plugin configuration page" /></p>
Give your agent a reasonable name: i.e. ‘Webserver’. Then press the ‘Save agent’ button, a download link will appear with the installation files for your operating system. You have now created an agent configuration which you can deploy on as many servers as you'd like.

## Installing the agent

Now that you have configured the agent, it is time to install it on you server.

{% include alert.html type="warning" text="For the following steps you will need root or administrator access to the servers you will be installing the CoScale agent on." %}


Press ‘Download agent’, download the agent binary to your computer and then copy it to all the servers where you want to install this agent on. The web interface is now waiting for you to install at least one agent.

<p class="text-center"><img src="{{ site.baseurl }}/gfx/getting-started/install-agent/agent_detection_searching.png" alt="CoScale agent detection searching widget" /></p>

Go to [agent install]({{ site.baseurl }}/agent/agent-install) page, to find the install instructions for your operating system.

Wait until the agent is detected. When at least one agent is detected, you can continue the installation by pressing the button.

{% capture text %}Our agent requires port 443 to be open to outbound traffic. Checkout our <a href="{{ site.baseurl }}/advanced/security/">security page</a> for more information. {% endcapture %}
{% include alert.html type="info" text=text %}

<p class="text-center"><img src="{{ site.baseurl }}/gfx/getting-started/install-agent/agent_detection_install.png" alt="CoScale agent detection install widget" /></p>

When you see this screen the agent is installed successfully. It will start downloading all configured plugins, check the configuration and start sending data to our platform.

You can get an overview of installed agents on the `Datasources` > `Installed` page, accessible through the sidebar. Any configuration problems we detect will be shown here.

To get more information about the agent, you can always click the service, as it will provide you with the latest log and status of all the plugins.

## Agent successfully installed

The agent is now installed and running on your system, if necessary repeat this process for all your servers.