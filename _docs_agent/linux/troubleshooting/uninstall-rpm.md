---
layout: page
title: Uninstall RPM on Redhat based systems
description: Custom uninstall command for Redhat based systems
---

## Problem

{% highlight bash %}
initctl: Unknown instance:
rm: cannot remove `/opt/coscale/agent/etc/agent.conf': No such file or directory
rm: cannot remove `/opt/coscale/agent/plugins': No such file or directory
rm: cannot remove `/opt/coscale/agent/update': No such file or directory
rm: cannot remove `/etc/logrotate.d/coscale-agent': No such file or directory
error: %preun(coscale-agent-1.0-1.x86_64) scriptlet failed, exit status 1
{% endhighlight %}

## Solution

`rpm -ev --noscripts coscale-agent`
