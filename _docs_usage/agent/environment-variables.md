---
layout: page
title: Environment variables configuration
---

Our agent can get its configuration values for plugins from environment values configured on the server. This allows you to use the same agent for a lot of servers without having to generate a new agent for different configuration setups. An example where this might be used is with database plugin where the status user password isn't the same on all machines.

{% include alert.html type="warning" text="At the moment we only support Linux." %}

## How to get started

1. Create a `/etc/default/coscale-agent` and add the following content
    
   {% highlight bash %}
#!/bin/bash

# You can choose your own variable names and content, you can add as many as you like
CS_MYSQL_HOST=localhost
CS_MYSQL_PORT=3306
CS_MYSQL_USER=user
CS_MYSQL_PASSWORD=password
CS_MYSQL_TABLE=product

   {% endhighlight %}

2. In the plugin configuration you set the configuration settings to the variable names you created. In this example I'm configuring the MySQL database plugin with custom variables.

![Environment values setup in MySQL plugin]({{ site.baseurl }}/gfx/usage/agent/environment-variables/env_var_mysql_setup.png)
