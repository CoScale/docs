---
layout: page
title: Using environment variables or secrets for configuration
description: Configure the CoScale agent and plugins using environment variables.
---

## Option 1: Using docker Labels
When creating your Docker image you can add a label to tell the CoScale agent how to monitor this image when it's detected. To make this work in an environment where you sensitive data is stored in a secret. You can also tell the agent to read usernames and passwords from environment variables.

### Example 1
In this example we have created an image with RabbitMQ running on it, we added a Docker label to automatically run the RabbitMQ plugin on the container once it starts. We tell the agent to get the password from an environment variable $RABBIT_MQ_PASSWORD by defining `$RABBIT_MQ_PASSWORD` in the Docker LABEL.

{% highlight bash %}
FROM rabbitmq:3.6

RUN rabbitmq-plugins enable rabbitmq_management

# Here we set USERNAME and PASSWWORD in the RabbitMQ configuration taken from environement variables
LABEL com.coscale.monitoring='[{"PluginType":"RABBITMQ","Configuration":{"HOSTNAME":["localhost"],"PORT":["15672"],"USERNAME":["$RABBIT_MQ_USERNAME"],"PASSWORD":["$RABBIT_MQ_PASSWORD"]}}]'
{% endhighlight %}

### Example 2
In this example we have created an image with RabbitMQ running on it, we added a Docker label to automatically run the RabbitMQ plugin on the container once it starts. We tell the agent to get the password from a secret on the filesystem located at `/run/secrets/rabbitmq_password` by defining `$/run/secrets/rabbitmq_password` in the Docker LABEL.

{% highlight bash %}
FROM rabbitmq:3.6

RUN rabbitmq-plugins enable rabbitmq_management

# Here we set USERNAME and PASSWWORD in the RabbitMQ configuration taken from secrets on the disk
LABEL com.coscale.monitoring='[{"PluginType":"RABBITMQ","Configuration":{"HOSTNAME":["localhost"],"PORT":["15672"],"USERNAME":["$/run/secrets/rabbitmq_username"],"PASSWORD":["$/run/secrets/rabbitmq_password"]}}]'
{% endhighlight %}

## Option 2: Using a packaged agent
Our agent can get its configuration values for plugins from environment values configured on the server. This allows you to use the same agent for a lot of servers without having to generate a new agent for different configuration setups. An example where this might be used is with database plugin where the status user password isn't the same on all machines.

{% include alert.html type="warning" text="At the moment we only support Linux." %}
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

[Restart the agent]({{ site.baseurl }}/agent/agent-restart), afterwards the config will be read from file.
