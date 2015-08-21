---
layout: page
title: Salt
---
## Description
The CoScale plugin for Salt will push events to the CoScale infrastructure every time your make a configuration chance.

## Installation
<a href="https://github.com/CoScale/coscale-salt-plugin" target="_blank" class="btn btn-large btn-info"><i class="fa fa-3x fa-fw fa-github-square"></i> Github repository</a>

1. Move the coscale.py to the salt states location (eg: `/srv/salt/_states/`);
2. Distribute the custom state module to the minions:
    `salt '*' saltutil.sync_states`
3. Create a salt state in salt states location by adding a file named `coscale.sls` with the following content:

<pre>
human_friendly_state_id:                                        # An arbitrary state ID declaration.
    coscale.event:                                              # The custom state module name. The function in the custom state module.
        - baseurl: https://api.coscale.com/                     # Specify the required ``baseurl`` parameter.
        - accesstoken: [[accesstoken]]                          # Specify the required ``accesstoken`` parameter.
        - appid: [[appId]]                                      # Specify the required ``appid`` parameter.
        - event_name: 'Software updates'                        # Specify the required ``event_name`` parameter.
        - event_message: 'Updating software'                    # Specify the required ``event_message`` parameter.
        - event_timestamp: 0                                    # Specify the optional ``event_timestamp`` parameter.
</pre>
