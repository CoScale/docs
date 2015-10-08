---
layout: page
title: Environment variables configuration
description: Configure the CoScale agent and plugins using environment variables.
---

Our agent can get its configuration values for plugins from environment values configured on the server. This allows you to use the same agent for a lot of servers without having to generate a new agent for different configuration setups. An example where this might be used is with database plugin where the status user password isn't the same on all machines.

{% include alert.html type="warning" text="At the moment we only support Linux." %}

## How to get started

### 1. Create environment file
Create a `/etc/default/coscale-agent` and add the following content

   {% highlight bash %}
#!/bin/bash

# You can choose your own variable names and content, you can add as many as you like
export CS_MYSQL_HOST=localhost
export CS_MYSQL_PORT=3306
export CS_MYSQL_USER=user
export CS_MYSQL_PASSWORD=password
export CS_MYSQL_DATABASE=product

   {% endhighlight %}

### 2. Configure agent
In the plugin configuration you set the configuration settings to the variable names you created. In this example I'm configuring the MySQL database plugin with custom variables.

![Environment values setup in MySQL plugin]({{ site.baseurl }}/gfx/installation/agent/linux/environment-variables/env_var_mysql_setup.png)

### 3. Restart the Agent

[Restart the agent]({{ site.baseurl }}/installation/agent/commands#restart), afterwards the config will be read from file.
