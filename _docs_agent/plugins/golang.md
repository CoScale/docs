---
layout: page
title: Golang support
description: Information on the metrics collected by CoScale for Golang.
---

> Golang is a programming language created at Google. It is a compiled, statically typed language in the tradition of Algol and C, with garbage collection, limited structural typing, memory safety features and CSP-style concurrent programming features added. The compiler and other language tools originally developed by Google are all free and open source.

More information on: [https://golang.org/](https://golang.org/)

## How it works

Because Golang has no default logging or metrics endpoint we need to include one in our application. We will use the [Golang prometheus library](https://github.com/prometheus/client_golang) together with the CoScale Prometheus endpoint parser to retrieve metrics from the standard Golang runtime as well as provide a possibility to extend it with custom metrics.

## Configuration

### Configure your Golang application to provide a Prometheus endpoint

Add [client_golang](https://github.com/prometheus/client_golang) to your application using the built in golang import system. You can find an example of the integration below:

{% highlight golang %}
// Copyright 2015 The Prometheus Authors
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// A minimal example of how to include Prometheus instrumentation.
package main

import (
	"flag"
	"log"
	"net/http"

	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var addr = flag.String("listen-address", ":8080", "The address to listen on for HTTP requests.")

func main() {
	flag.Parse()
	http.Handle("/metrics", promhttp.Handler())
	log.Fatal(http.ListenAndServe(*addr, nil))
}
{% endhighlight %}

It is now possible to also add custom metrics, more information can be found on the [client_golang docs](https://godoc.org/github.com/prometheus/client_golang/prometheus). Custom metrics will be automatically detected and pushed by the CoScale agent.

### Configure the CoScale Prometheus plugin to parse the information from the endpoint

CoScale uses the Prometheus plugin to parse the information from the Golang Prometheus endpoint, go to Agent configuration and enable the CoScale Prometheus plugin for your environment. Depending on the setup you will need to add the plugin to an agent or setup the CoScale in-container monitoring for a certain image.

The endpoint configured above is available on port 8080 with endpoint `/metrics`:

`http://localhost:8080/metrics`

You can also add a Docker Label to your `Dockerfile` so that the agent will automatically pick up the Prometheus endpoint when it detects a new container:

`LABEL com.coscale.monitoring='[{"PluginType":"PROMETHEUS","Configuration":{"STATS URL":["http://127.0.0.1:8080/metrics"]}}]'`
