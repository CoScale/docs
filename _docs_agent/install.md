---
layout: page
title: Installing the agent
description: Instructions on how to install and configure the CoScale agent.
---

## What is an agent
The CoScale agent is the primary tool used to capture resource and application metrics from your servers. It is easy to configure and deploy in just a few minutes. The same agent can be installed on multiple servers. For example, you create one webserver agent that can be later installed on all of your webservers.

{% include alert.html type="warning" text="The following steps require root or administrator access to the servers that host your application. If you don't have access, please <a href=\"mailto:support@coscale.com\" class=\"js-support\">contact support</a> so they can provide alternatives." %}

## Creating the agent
To start with the configuration, go to your dashboard and use the sidebar to navigate to <a href="http://app.coscale.com" db-href="/datasources/agents/" class="js-dashboard-link">`Datasources > Agent`</a>. On this page you can  configure the agent(s) you want to install on your servers. There is no limit on the maximum number of agents that you can create.

Click on the `Create new CoScale agent` button. You have the option to deploy the agent as a package/executable or as a container:

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/01-deployment-type.png" style="img-responsive"/>

The type of agent to choose depends on your environment. In general when running in a Docker environment it's advised to use the [Container install](#option-1-container), and when running on a server without Docker to use the [Package install](#option-2-packageexecutable).

### Option 1: Container

1.1. Select your deployment/orchestration system

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/06-orchestration.png" style="img-responsive"/>

1.2. Add images

The default configuration of the agent will allow CoScale to gather general metrics about the deployment system. We can also gather detailed metrics about the services running inside your Docker containers. Use the `Add image` button to add a set of plugins that run inside of your containers to gather metrics of the running services.

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/07-add-image.png" style="img-responsive"/>

1.3. Configure plugins for images

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/08-image.png" style="img-responsive"/>

Provide the image name and tag (* can be used for tag). Select the plugin type and click on `Add new plugin`. Follow the configuration steps provided on each screen and click `Save` when finished.

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/09-container-images.png" style="img-responsive"/>

1.4. Review & download

Give your agent a clear, recognizable name and press the `Save` button.

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/10-review-download.png" style="img-responsive"/>

1.5. Install instructions

Copy the install instructions on the screen to start the CoScale agent in a Docker container. The CoScale agent will run in the foreground. Typically our users use systemd/upstart to make the agent start on every boot.

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/11-download-install.png" style="img-responsive"/>

You've now created and installed your first CoScale agent. To check if the agent is communicating well, please [check the status](#checking-the-installation).

<hr />

### Option 2: Package/Executable

2.1.Select the operating system on which the agent will be installed.

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/02-operating-system.png" style="img-responsive"/>

{% include alert.html type="info" text="We only support 64 bit operating systems, <a href=\"mailto:info@coscale.com\" class=\"js-support\">contact support</a> for more information" %}


2.2. Enable some plugins

Enable all plugins you want to activate for this agent. The resource plugin is enabled by default, but you probably also want to enable other plugins. For a web server running Tomcat i.e. you would enable the Tomcat plugin by clicking on it. You can enable as many plugins as you like.

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/03-plugins.png" style="img-responsive"/>

Some plugins require further configuration. Read and follow the instructions carefully.
If necessary, apply the proposed changes to the server as shown in the instructions and fill in the required fields.

{% include alert.html type="info" text="You can easily activate more plugins later and reconfigure them without having to re-install the agent." %}

2.3. Review & download

Give your agent a clear, recognizable name: i.e. ‘Webserver’ and press the `Save` button.

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/04-agent-name.png" style="img-responsive"/>

2.4. Download & install

You have now created an agent which you can deploy on as many servers as you'd like. A "Download Agent" button is available with the installation files for your operating system. The instructions for installing the agent on your operating system are also shown on this screen.

<img alt="Deployment type" src="{{ site.baseurl }}/gfx/agent/install/05-download-install.png" style="img-responsive"/>


<!-- INSERT javascript to see installation instructions from /agent/agent-install -->
<!-- Go to [agent install]({{ site.baseurl }}/agent/agent-install) page, to find the install instructions for your operating system. -->

After installing the agent it will check the configuration of all the selected plugins and will start to communicate with the CoScale platform. This can take a couple of minutes.

{% capture text %}Our agent requires port 443 to be open for outbound traffic. Checkout our <a href="{{ site.baseurl }}/advanced/security/">security page</a> for more information. {% endcapture %}
{% include alert.html type="info" text=text %}

You've now created and installed your first CoScale agent. To check if the agent is communicating well, please [check the status](#checking-the-installation).

## Checking the installation

You can get an overview of installed agents on the <a href="http://app.coscale.com" db-href="/datasources/agents/" class="js-dashboard-link">`Datasources > Agent`</a> page, accessible through the sidebar. Any configuration problems we detect will be shown here.

To get more information about the agent, you can always click the service icon, it will provide you with the latest log and status of all the plugins.

## Agent successfully installed

The agent is now installed and running on your system. You can now [repeat this process](#creating-the-agent) for servers that require a different set of plugins or configuration.
