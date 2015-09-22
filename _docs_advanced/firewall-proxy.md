---
layout: page
title: Firewall / Proxy
---

## Firewall
By default, all CoScale agents communicate with the CoScale platform over a secured SSL connection, using the default port 443. The agent communicates with one host, api.coscale.com. CoScale only requires your firewall to allow outgoing connections to api.coscale.com on TCP port 443. No incoming connections are required.

## Proxy
The CoScale agent allows to send data using a proxy. This can be configured by setting an environment variable HTTPS_PROXY.

* For Linux systems this means adding an environment variable to `/opt/coscale/agent/wrapper.sh`

    `export https_proxy=http://[ip]:[port]/`

    After please [restart]({{ site.baseurl }}/installation/agent/linux/agent-restart/) the agent.

* For Microsoft Windows a global environment variable HTTPS_PROXY must be set.
