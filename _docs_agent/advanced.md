---
layout: page
title: Advanced configuration
description: Advanced configuration of the CoScale agent by using environment variables.
---

## Environment flags

The CoScale agent can be configured using environment variables. The variables are picket up on boot, so an [agent restart]({{ site.baseurl }}/agent/agent-restart/) is required to enable them.

`COSCALE_HOSTNAME=[custom hostname]`

By default the CoScale agent will use the system hostname and will not add a new server if the hostname already exists on our service. Change this value if you would like to set a custom hostname or to force adding a new server to the CoScale environment. This can used in cases where two machines share the same hostname.

`COSCALE_API_LOGLEVEL=debug`

Will increase the verbosity of the CoScale agent, this should only be used for debugging purposes or when requested by CoScale support. The possible levels are: `trace`, `debug`, `info`, `warn`, `error`


## Configuration

### Linux

On the Linux operating systems you can add the environment variables to the `/etc/default/coscale-agent` file.

{% highlight bash %}
export COSCALE_HOSTNAME=my-server-name
export COSCALE_API_LOGLEVEL=debug
{% endhighlight %}

### Windows

#### Application level

Application level environment variables are added through the registry. Open the registry editor `regedit` and go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CoScaleAgent`

Now create a new value by rightclicking on the right side on the Window and going to `New` and then `Multi-String Value`. The name of the new item should be `Environment`. You can then edit the item by double clicking on it.

**Example content:**
{% highlight bash %}
COSCALE_HOSTNAME=my-server-name
COSCALE_API_LOGLEVEL=debug
{% endhighlight %}

After changing the file you need to [restart the CoScale agent]({{ site.baseurl }}/agent/agent-restart/).

#### System wide

You can also define [system wide env variables](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682653(v=vs.85).aspx).

**Example content:**
{% highlight bash %}
COSCALE_HOSTNAME=my-server-name\0
COSCALE_API_LOGLEVEL=debug\0
{% endhighlight %}
