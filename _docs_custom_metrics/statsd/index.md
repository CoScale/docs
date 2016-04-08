---
layout: page
title: StatsD
description: Integration and installation of CoScale StatsD plugin to push metrics to the CoScale platform.
---
## Description
The CoScale plugin for StatsD will push all metrics available in the StatsD daemon to the CoScale infrastructure every minute.

## Prerequisite
* [StatsD daemon installed]({{ site.baseurl }}/custom-metrics/statsd/installation)


## Installation
<a href="https://github.com/CoScale/coscale-statsd-plugin" target="_blank" class="btn btn-large btn-info pull-right"><i class="fa fa-3x fa-fw fa-github-square"></i> Github repository</a>

Clone the coscale-statsd-plugin repository to your StatsD directory

{% highlight bash %}
# Go to directory

# Debian / Ubuntu
cd /usr/share/statsd/node_modules/


# Clone repository
sudo git clone https://github.com/CoScale/coscale-statsd-plugin.git
{% endhighlight %}

Now open `/etc/statsd/localConfig.js` with your favorite editor and add the following, make sure you don't forget to change your `app_id` and `accesstoken`.

{% highlight javascript %}
backends: ['coscale-statsd-plugin'],
flushInterval: 10000,

coscaleApiHost: 'https://api.coscale.com',
coscaleAppId: '[[app_id]]',
coscaleAccessToken: '[[accessToken]]'
{% endhighlight %}

It should look something like:
{% highlight javascript %}
{
  graphitePort: 2003
, graphiteHost: "localhost"
, port: 8125
, backends: ['coscale-statsd-plugin']
, flushInterval: 10000

, coscaleApiHost: 'https://api.coscale.com'
, coscaleAppId: '[[app_id]]'
, coscaleAccessToken: '[[accessToken]]'
}
{% endhighlight %}

Now restart the StatsD daemon
{% highlight bash %}
# Debian / Ubuntu
sudo service statsd restart
{% endhighlight %}

## Integrating with your application.

StatsD has many libraries available to push your own data right from application code. You can find a full list <a href="https://github.com/etsy/statsd/wiki" target="_BLANK">here</a>.
