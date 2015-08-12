---
layout: page
title: Installing the agent
---

## Creating the agent
The CoScale agent is the primary tool used to capture resource and application metrics from your servers. It is easy to configure and deploy. To start with the configuration go to your dashboard and use to sidebar navigation to go to `DataSources` and then `Manage` On this page, you will be configuring the agent(s) you want to install on your servers. For this example we will configure 1 agent to install on a web servers and 1 agent to install on a database servers.

1. Select the operating system and flavor of your server(s)
2. Enable all plugins you want to activate for this agent, the resource plugin is enabled by default, but you probably also want to enabled other plugins. For a web server running Tomcat i.e. you would enable the Tomcat plugin by clicking on it.

{% include alert.html type="info" text="You can later always activate more plugins without having to re-install the agent." %}


<p class="text-center"><img class="img-responsive" src="{{ site.baseurl }}/gfx/getting-started/installing-agent/agent_configuration.png" alt="CoScale agent configuration page" /></p>

For some plugins, some configuration is necessary. Read the instructions carefully.
If necessary, apply the proposed changes to the server as shown in the instructions.
If necessary, fill in the required fields. Press the save button when finished.

<p class="text-center"><img class="img-responsive" src="{{ site.baseurl }}/gfx/getting-started/installing-agent/plugin_configuration.png" alt="CoScale agent plugin configuration page" /></p>
Give your agent a reasonable name: i.e. ‘Webserver’. Press ‘Save agent’

You have now created an agent configuration which you can deploy on as many servers as you'd like.

## Installing the agent

Now that you have configured your agent, it is time to install it on you server.

{% include alert.html type="warning" text="For the following steps you will need root or administrator access to the servers you will be installing the CoScale agent on." %}


Press ‘Download agent’, download the agent binary to your computer and then copy it to all the servers where you want to install this agent on. The web interface is now waiting for you to install at least one agent.

<p class="text-center"><img src="{{ site.baseurl }}/gfx/getting-started/installing-agent/agent_detection_install.png" alt="CoScale agent detection install widget" /></p>

To install the agent, do the following:
Debian, Ubuntu: sudo dpkg -i coscale-agent.deb
RedHat, CentOS: sudo rpm -iUvh coscale-agent.rpm
Windows: double click the installer and follow the instructions

Wait until the agent is detected, make sure it can communicate to https://api.coscale.com (using port 443). When at least one agent is detected, you can continue the installation by pressing the button.

<p class="text-center"><img src="{{ site.baseurl }}/gfx/getting-started/installing-agent/agent_detection_searching.png" alt="CoScale agent detection searching widget" /></p>

## Time for the next step
Now that we have installed the agent it is time to monitor our user experience and get more insights into the performance on users computer. Click on the button below to get started on installing the RUM component.

<a href="{{ site.baseurl }}/getting-started/install-rum.html" class="btn btn-primary btn-lg btn-block spacing-top">Step 3: Installing Real User monitoring component</a>
