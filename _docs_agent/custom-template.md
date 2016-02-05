---
layout: page
title: Custom agent
description: Specific configuration for custom agents.
---

Custom agents allow you to configure new agents on the fly using a configuration file. This is advanced functionality and requires some knowledge of the CoScale system to setup. If you're stuck or need help, don't hesitate to contact our support.


A custom agent is created similarly to a regular agent. Follow the regular instructions on <a href="http://app.coscale.com" db-href="/agent/install/" class="js-dashboard-link">`Agent > Install`</a>, but check "I will manage my plugins on my servers instead of through the UI." and don't enable any plugins.

![Manage my plugins on my servers instead of through the UI checkbox]({{ site.baseurl }}/gfx/agent/agent_manage_plugins.png)


## Configuration

Custom agents read their plugins from a special config file located in `/opt/coscale/agent/plugins.conf`.
This file contains a JSON string similar to what the CoScale API sends. Use this file to configure plugins for a custom agent.

### Constructing your configuration

1. Configure a [regular agent]({{ site.baseurl }}/agent/install/) with the plugins you want and save it with a clear name.


    This will give you an initial configuration which you can change when deploying specific agents.


2. Perform an API call to get the configuration of your agents. <small>(This call is not available in our CLI tool)</small>

   First get an authorization token by logging in. This can be done using our [API documentation]({{ site.baseurl }}/api/#!/Login/post_users_login) or by performing the call yourself, for example using curl:

   `curl -d "email=[EMAIL]&password=[PASSWORD]" "http://app.coscale.com/api/v1/users/login/"`

   Then view all your agent configurations. The following command will pretty-print the response and fix the formatting so it can be used by the custom agent:

   `curl -H "HttpAuthorization: [TOKEN]" "http://app.coscale.com/api/v1/app/[APPID]/agenttemplates/?expand=plugins&fields=name%2Cconfig%2CpluginType" | python -m json.tool | sed -e 's/\\\\/\\/g; s/\\\"/\"/g; s/\"{/{/g; s/}\"/}/g; s/\"config\"/\"Configuration\"/g; s/\"pluginType\"/\"\PluginType"/g'`

   <small>Don't forget filling in [EMAIL], [PASSWORD], [TOKEN] and [APPID].</small>


#### 3. Copy the plugin configuration:
   The response is a JSON array. Each index in the array should have the following format:
   <pre>
    {
        "Configuration": null,
        "name": "customAgentTemplate",
        "plugins": [
            {
                "Configuration": {"FILE":["\"/var/log/apache2/access.log\" \"%V \"%r\" %D %s %I %O\""],"STATS URL":["http://localhost/server-status"]},
                "PluginType": "APACHE"
            },
            {
                "Configuration": {},
                "PluginType": "RESOURCES"
            }
        ]
    }
   </pre>   

   Copy the value of the "plugins" key and simply paste in the `plugins.conf` file discussed above. The file can be created if it is not yet present.


#### 4. [Restart]({{ site.baseurl }}/agent/agent-restart/) the agent.

   If everything went well, your custom agent should now be running a RESOURCES and an APACHE plugin.

   {% include alert.html type="warning" text="If this server previously had an agent installed, it is important to first run the new agent again with an empty configuration!" %}
