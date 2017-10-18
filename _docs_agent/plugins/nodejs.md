---
layout: page
title: Nodejs support
description: Information on the metrics collected by CoScale for NodeJS.
---

> Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine. Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient. 

More information on: [https://nodejs.org/en/](https://nodejs.org/en/)

## How it works

Because NodeJS has no logging or status page by default we need to include one in our application. The configuration and setup depends on the framework being used. At the moment CoScale supports [express.js](http://expressjs.com/) together with [morgan](https://github.com/expressjs/morgan) to generate a request log.  

## Configuration

### Configure your NodeJS application to generate a request log

Add [morgan](https://github.com/expressjs/morgan) to your application using [npm](https://www.npmjs.com/) and enable it in your application. 

{% highlight javascript %}
var morgan = require('morgan')
{% endhighlight %}

Next we enable morgan and set a custom log format.

{% highlight javascript %}
morgan('nodejs ":method :url HTTP/:http-version" :response-time :status') 
{% endhighlight %}

The log format has been adapted to work with the [CoScale Apache plugin]({{ site.baseurl }}/agent/plugins/apache). 

### Configure the CoScale Apache plugin to parse the requests

CoScale uses the Apache plugin to parse the information from the NodeJS request log, go to agent configuration and enable the Apache plugin for your environment. Depending on the setup you will need to add the plugin to an agent or setup the CoScale in-container monitoring for a certain image.

#### Global statistics

The NodeJS configuration we've setup does not support an active status page, so you can disable this functionality. 

#### Log configuration

The default log format in the Apache plugin will work with the configuration that we enabled for NodeJS with morgan. So you just need to point the plugin to the right logfile on your filesystem or use `/dev/stdout` if you're using Docker logs.

### Active checks

The Apache plugin can be configured to perform a HTTP GET on your NodeJS. This active monitoring allows us to calculate the uptime of the service and the response time of the provided URL.

A full URL (eg. `http://localhost/test_page.php`) should be provided.
