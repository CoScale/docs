---
layout: page
title: Pushing server status to CoScale on boot and shutdown
---

## Prerequisite
* [CoScale CLI installed]({{ site.baseurl }}/installation/cli/installation)

## Configuration

### Unix systems

#### Enabling a server on boot

Edit /etc/rc.local and add the following command

`/opt/coscale/cli/coscale-cli server update --name=$(hostname) --state=ENABLED || true`

#### Disabling a server on shutdown

Create a new file in `/etc/rc0.d/` called `K5coscale`.

`touch /etc/rc0.d/K5coscale`

Open it with your favorite text editor and add the following content.

{% highlight bash %}
#!/bin/sh
#
# Command to disable the server on the CoScale platform on shutdown
#
/opt/coscale/cli/coscale-cli server update --name=$(hostname) --state=DISABLED
{% endhighlight %}

Make the script executable: `chmod +x /etc/rc0.d/K5coscale`
