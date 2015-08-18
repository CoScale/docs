---
layout: page
title: Technical info / Security
---

This document contains more technical information about how the CoScale agent works, security measures and network requirements.

## Disclosure
The CoScale agent is a downloadable software component for different Operating Systems and Software. CoScale analyzes log files or connects to the Software’s management interface. For example, in the case of Apache web server, the access.log file is parsed and the default Apache server-status page is fetched and parsed for getting general info. CoScale does not interfere with your application stack, CoScale does not do binary instrumentation or we do not dynamically generate and inject code into other processes.

## Data storage
CoScale is using dedicated servers. Most of the servers are in a data center in Roubaix, France. CoScale uses standard best practices to maintain a firewall for our servers and to protect our servers from unauthorized login.
All data is stored in a cluster of PostgreSQL and Cassandra databases. Metric data is not stored encrypted. CoScale data is backed up nightly.

## Security & Firewall

By default, all CoScale agents communicate with the CoScale platform over a secured SSL connection, using the default port 443. The agent communicates with one host, api.coscale.com. CoScale only requires your firewall to allow outgoing connections to api.coscale.com on TCP port 443. No incoming connections are required.

All installed agent plugins are digitally signed by CoScale. This signature is verified when installing or updating plugins.

The agent has a built-in access token (GUID) to authenticate with the CoScale platform. This token can always be revoked when necessary.

## Proxies

The CoScale agent allows to send data using a proxy. This can be configured by setting an environment variable HTTPS_PROXY. For linux systems this means adding and environment variable to /opt/coscale/agent/wrapper.sh. For windows systems a global environment variable HTTPS_PROXY must be set.


## Automatic provisioning

On installation our agent creates an agent.conf file containing a UID. This UID is used to identify the server on our platform. When creating an image it is important to remove the agent.conf file. If you don’t the agent will push metrics for the previous server and not add a new one. You can find the file in “/opt/coscale/agent/etc” on Linux or “C:/Program Files (x86)/CoScale/Agent/” on Windows.
