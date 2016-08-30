---
layout: page
title: Tutorial - CoScale Docker monitoring
description: Using CoScale to monitor your Docker environment
---

This tutorial will guide you into configuring and installing CoScale into a Docker environment.

## 1. Create CoScale agent

The first thing that needs to be done is to create a CoScale agent for your machine.

1. To start go to `Datasources > Agent` inside our dashboard.
2. Select your operating system and version
3. Select your orchestrator plugin (Kubernetes or Docker swarm) and configure it for your environment
4. Select the Docker plugin, add your images (you can use wildcard `*` for tag) and add the plugins you want to run for each container.
    For more information you can check out our [Docker]({{ site.baseurl }}/agent/plugins/docker/) documentation.

## 2. Deploy CoScale agent

After saving your agent and giving it a name you will receive two ways to install it on your machines.

First is the installation through a package manager:

*Example:*
`curl 'https://app.coscale.com/api/v1/app/xxxxxxxx-yyyy-xxxx-yyyy-xxxxxxxxxxx/agenttemplates/zzzz/download/?token=xxxxxxxx-yyyy-xxxx-yyyy-xxxxxxxxxxx' > coscale-Ubuntu-14.04-agent-container.deb && sudo dpkg -i coscale-Ubuntu-14.04-agent-container.deb`

This method is advised for machines running a standard Linux OS with an apt or yum package manager. If you are running CoreOS or prefer to run everything from a container, you can also use our agent in a container option. This way of installing is only available when you've selected an orchestrator like Docker Swarm or Kubernetes:

*Example:*
`docker run -it --rm --privileged --net=host --pid=host --name coscale-agent -e APP_ID=xxxxxxxx-yyyy-xxxx-yyyy-xxxxxxxxxxx -e ACCESS_TOKEN=xxxxxxxx-yyyy-xxxx-yyyy-xxxxxxxxxxx -e TEMPLATE_ID=zzzz -v /var/run/docker.sock:/var/run/docker.sock -v /:/host/:ro coscale-agent`

Just run the command you received after confirming the agent name on each machines you would like to monitor. As long as the configuration is identical, you can reinstall the same agent on as many machines as you'd like.

## 3. Setup in-container monitoring

After installing our agent it will monitor the containers running on the server and will automatically start and stop the required plugins you've setup in step 1. It is always possible to change the configuration of the Docker plugin by clicking its icon on the `Datasources > Agent` page.

<img src="{{ site.baseurl}}/gfx/tutorials/docker-monitoring/agents.png" alt="Agent overview" class="img-responsive" />

**A & B**: Show you the amount of containers detected by your configuration and also shows you if there are any issues. You can click the icons to get more information.

**C**: If you wish to reconfigure your server you can do so by clicking the `Configure` button. You can add, change and remove plugins without the need to reinstall the agent.
