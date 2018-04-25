---
layout: page
title: Nodejs support
description: Information on the metrics collected by CoScale for NodeJS.
---

> Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine. Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient.

More information on: [https://nodejs.org/en/](https://nodejs.org/en/)

## How it works

Because NodeJS has no logging or status page by default we need to include one in our application. The configuration and setup depends on the framework being used. At the moment CoScale supports [express.js](http://expressjs.com/) together with [prom-client](https://github.com/siimon/prom-client) to retrieve performance and request data.

## Installation

{% include_relative _installation.md orchestrator="false" service="Nodejs" %}

## Configuration

### Configure your NodeJS application to expose a prometheus endpoint

Add [prom-client](https://github.com/siimon/prom-client) to your application using [npm](https://www.npmjs.com/). The first section of code needs to be added to the top part of your main javascript file, perferablly below the `var app = express();` line.


{% highlight javascript %}
// Initiate prometheus client and metrics
const promClient = require('prom-client');

// Gather default metrics from V8 engine
const collectDefaultMetrics = promClient.collectDefaultMetrics;
collectDefaultMetrics({ timeout: 1000 })

// Prepare two custom metrics to measure latency and request rate
const promLatency = new promClient.Histogram({
  name: 'http_request_duration_ms',
  help: 'Duration of HTTP requests in ms',
  labelNames: ['method', 'route', 'code'],
  // buckets for response time from 0.1ms to 500ms
  buckets: [0.10, 5, 15, 50, 100, 200, 300, 400, 500]
})
const promRate = new promClient.Counter({
  name: 'http_request_count',
  help: 'Number of HTTP requests',
  labelNames: ['method', 'route', 'code']
})

// Register start time for each request
app.use((req, res, next) => {
  res.locals.startEpoch = Date.now()
  next()
})
{% endhighlight %}

The next code to add is to expose the Prometheus endpoint, it should be add just above the `app.listen` code line.

{% highlight javascript %}
// Provide prometheus endpoint to collect data
app.get('/metrics', (req, res) => {
  // Deny connections from outside the container
  var remote = req.ip || req.connection.remoteAddress
  if ((remote !== '::1') && (remote !== 'localhost') && (remote !== '::ffff:127.0.0.1')) {
    return res.status(401).send();
  }

  // Return prometheus metrics
  res.set('Content-Type', promClient.register.contentType)
  res.end(promClient.register.metrics())
})

// Register stop time for each request and pass to prometheus
app.use((req, res, next) => {
  const responseTimeInMs = Date.now() - res.locals.startEpoch

  promLatency
    .labels(req.method, req.route.path, res.statusCode)
    .observe(responseTimeInMs)
  promRate
    .labels(req.method, req.route.path, res.statusCode)
    .inc()

  next()
})
{% endhighlight %}

### Configure the CoScale Prometheus plugin to parse the information from the endpoint

CoScale uses the Prometheus plugin to parse the information from the NodeJS Prometheus endpoint, go to Agent configuration and enable the CoScale Prometheus plugin for your environment. Depending on the setup you will need to add the plugin to an agent or setup the CoScale in-container monitoring for a certain image.

The endpoint configured above is available on the default nodejs port (80) with endpoint `metrics`:

`http://localhost:80/metrics`

You can also add a Docker Label to your `Dockerfile` so that the agent will automatically pick up the Prometheus endpoint when it detects a new container:

`LABEL com.coscale.monitoring='[{"PluginType":"PROMETHEUS","Configuration":{"STATS URL":["http://127.0.0.1/metrics"]}},{"PluginType":"ENDPOINTCHECKER","Configuration":{"ENDPOINT":["http://127.0.0.1/"]}}]'`
