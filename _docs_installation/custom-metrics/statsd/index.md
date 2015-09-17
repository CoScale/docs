---
layout: page
title: StatsD
---
## Description
The CoScale plugin for StatsD will push all metrics available in the StatsD daemon to the CoScale infrastructure every minute.

## Installation
<a href="https://github.com/CoScale/coscale-statsd-plugin" target="_blank" class="btn btn-large btn-info"><i class="fa fa-3x fa-fw fa-github-square"></i> Github repository</a>

1. Clone repository to your StatsD `node_modules` directory
    `git clone https://github.com/CoScale/coscale-statsd-plugin.git`
2. Change your `config.js` to include the CoScale backend (example below).
3. Restart StatsD daemon

### Config
Make sure you replace `[[app_id]]` and `[[accessToken]]` with your own credentials.
{% highlight javascript %}
{
    port: 8126,
    backends: ['coscale-statsd-plugin'],
    flushInterval: 10000,

    coscaleApiHost: 'https://api.coscale.com',
    coscaleAppId: '[[app_id]]',
    coscaleAccessToken: '[[accessToken]]'
}
{% endhighlight %}

## Integrations

StatsD has many libraries available to push your own data right from application code. You can find a full list <a href="https://github.com/etsy/statsd/wiki" target="_BLANK">here</a>.
