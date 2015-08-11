---
layout: page
title: Infrastructure agent
---

## Installing the Agent
The CoScale agent is the primary tool used to capture resource and application metrics from your servers. It is easy to configure and deploy. To start with the configuration go to your dashboard and use to sidebar navigation to go to `DataSources` and then `Manage` On this page, you will be configuring the agent(s) you want to install on your servers. For this example we will configure 1 agent to install on a web servers and 1 agent to install on a database servers.

1. Select the operating system and flavor of your server(s)
2. Enable all plugins you want to activate for this agent, the resource plugin is enabled by default, but you probably also want to enabled other plugins. For a web server running Tomcat i.e. you would enable the Tomcat plugin by clicking on it.

<div class="alert alert-info">You can later always activate more plugins without having to re-install the agent.</div>

<p class="text-center"><img class="img-responsive" src="{{ site.baseurl }}/gfx/installation/agent/agent_configuration.png" alt="CoScale agent configuration page" /></p>

For some plugins, some configuration is necessary. Read the instructions carefully.
If necessary, apply the proposed changes to the server as shown in the instructions.
If necessary, fill in the required fields. Press the save button when finished.
<p class="text-center"><img class="img-responsive" src="{{ site.baseurl }}/gfx/installation/agent/plugin_configuration.png" alt="CoScale agent plugin configuration page" /></p>
Give your agent a reasonable name: i.e. ‘Webserver’. Press ‘Save agent’

<div class="alert alert-warning">For the following steps you will need root or administrator access to the servers you will be installing the CoScale agent on.</div>

Press ‘Download agent’, download the agent binary to your computer and then copy it to all the servers where you want to install this agent on. The web interface is now waiting for you to install at least one agent.

<p class="text-center"><img src="{{ site.baseurl }}/gfx/installation/agent/agent_detection_install.png" alt="CoScale agent detection install widget" /></p>

To install the agent, do the following:
Debian, Ubuntu: sudo dpkg -i coscale-agent.deb
RedHat, CentOS: sudo rpm -iUvh coscale-agent.rpm
Windows: double click the installer and follow the instructions

Wait until the agent is detected, make sure it can communicate to https://api.coscale.com (using port 443). When at least one agent is detected, you can continue the installation by pressing the button.

<p class="text-center"><img src="{{ site.baseurl }}/gfx/installation/agent/agent_detection_searching.png" alt="CoScale agent detection searching widget" /></p>

## Updating the Agent

## Security

* All communication goes through a secured SSL connection.
* Agents communicate with unique token that can be revoked by CoScale when necessary.
* Our agent only needs a connection to the outside, so no port forwarding.
* All plugins are signed and checked by agent before deploying.
* When requested the agent auto update procedure can be disabled.
