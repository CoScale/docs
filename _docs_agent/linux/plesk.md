---
layout: page
title: Plesk
description: Configuration for Plesk management system
---

Quick overview on how to configure Plesk to work with the CoScale agent and plugins.

## Apache

1. Open Plesk administration interface
1. Go to domains and select the domain you want to monitor
1. Open "Apache & nginx Settings"
1. Add the following lines in the "Additional Apache directives” section, both HTTP and HTTPS

    LogFormat "%V \"%r\" %D %s %I %O" coscale
    CustomLog /var/log/apache2/coscale-access.log coscale

1. Manually restart apache or wait for Plesk to restart it
1. Add "/var/log/apache2/coscale-access.log” to your CoScale agent
