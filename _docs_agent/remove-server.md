---
layout: page
title: Remove server
description: How to remove a server and/or an agent from your app
---

## Prerequisites

Make sure CoScale [CLI]({{ site.baseurl }}/tools/cli/installation) is installed.

## Steps

* Check the API URL in your browser. In our example we will use `https://app.coscale.com/`

* Go to your dashboard, Users -> Access Tokens and copy the token for the agent you wish to remove.

* Use your application ID and the token from the previous step to list all the servers on that agent:  
`coscale-cli server list --api-url=https://app.coscale.com/ --app-id=<app-id> --access-token=<access-token>`

* Copy the ID of the server you wish to remove and use it in the "server delete" command:  
`coscale-cli server delete --api-url=https://app.coscale.com/ --app-id=<app-id> --access-token=<access-token> --id=<server-id>`

* Once all servers for an agent have been deleted, the agent can be removed as well. Go to your dashboard, Datasources -> Agent and select "Delete agent" from the menu:

<img alt="Delete agent" src="{{ site.baseurl }}/gfx/agent/delete-agent.png" style="img-responsive"/>
