---
layout: page
title: Custom agent
description: Specific configuration for custom agents.
---

Custom agents allow you to configure new agents on the fly using a configuration file. This is advanced functionality and requires some knowledge of the CoScale system to setup. If you're stuck or need help, don't hesitate to contact our support.


A custom agent is created similarly to a regular agent. Follow the regular instructions on <a href="http://app.coscale.com" db-href="/agent/install/" class="js-dashboard-link">`Agent > Install`</a>, but check "I will manage my plugins on my servers instead of through the UI." and don't enable any plugins. You can already install the agent on the server.

![Manage my plugins on my servers instead of through the UI checkbox]({{ site.baseurl }}/gfx/agent/agent_manage_plugins.png)


## Configuration

Custom agents read their plugins from a special config file located in `/opt/coscale/agent/plugins.conf`.
This file contains a JSON string similar to what the CoScale API sends. Use this file to configure plugins for a custom agent.

### Constructing your configuration

After creating a blank agent you will have the option to create a configuration example for an agent. You can do this by clicking the `Create configuration` button next to the agent name. 

![Create configuration](/gfx/agent/custom-agent/create-configuration.png)

You can now configure your agent with the plugins you want to use to monitor your system. Just click on the plugin you want to activate and follow the instructions on the screen. When you're done with the configuration of the agent you can use the `UI / JSON` toggle to get the content of your `/opt/coscale/agent/plugins.conf` file. 

![UI Toggle](/gfx/agent/custom-agent/toggle-configuration.png)

If in the future you want to change the configuration of an existing agent, you can always paste back the JSON content into the textbox and switch to `UI`. The plugins will then be configured with the information from the JSON. After you make your changes, and get a new JSON.

## Examples

Below you can find some examples of existing configuration with config management tools. We are always looking for other examples, so feel free to send us yours.

* [Ansible](https://github.com/CoScale/coscale-ansible-example)


