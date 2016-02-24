---
layout: page
title: Generic script
description: Information on how to use the CoScale generic script plugin.
---
## Description
The CoScale agent can poll a script or executable every minute to gather multiple custom metrics.
The generic script plugin enabled on the CoScale agent allows a customer to select scripts or executables that provides custom metrics to the CoScale agent. The CoScale agent will then push the data that was returned by the script to the CoScale API.

The generic script plugin has 2 modes: configuration mode and data retrieval mode. Our plugin will first run the configuration mode to get the metrics which should be created. Afterwards it will run every minute in data retrieval model to get the data.

{% include alert.html type="warning" text="Scripts have a maximum runtime of 5 seconds." %}

## Prerequisite
* [CoScale Agent installed]({{ site.baseurl }}/agent/index)

## Examples
<a href="https://github.com/CoScale/coscale-generic-scripts" target="_blank" class="btn btn-large btn-info"><i class="fa fa-3x fa-fw fa-github-square"></i> Github repository</a>

## Details

### Parameters

#### Datatypes

* DOUBLE

#### Calctypes

* Difference : metric result will be the difference between new and old
* Instant : metric result will be new value
* Average : metric result will be average over time

#### Maxruntime
Maximum amount of time in milliseconds the script is allowed to run in data retrieval mode. If runtime exceeds this value the script will be stopped.

### Requirements
* The script should return return exit code 0, otherwise the output is not be parsed and a failure log entry will be made.
* The script -c should return within 1 second, otherwise it will be killed.
* The script -d should return within the `maxruntime` defined in the configuration, otherwise it will be killed.

### Output examples

#### Configuration
{% highlight javascript %}
{
    "maxruntime":1000,
    "metrics":[
        {
            "id":1,
            "datatype":"DOUBLE",
            "name":"First metric",
            "description":"Description for first metric",
            "groups":"MyMetrics/Category1",
            "unit":"Bytes",
            "tags":"MYTAG1,MYTAG2",
            "calctype":"Difference"
        },
        {
            "id":2,
            "datatype":"DOUBLE",
            "name":"Second metric",
            "description":"Description for second metric",
            "groups":"MyMetrics/Category1",
            "unit":"",
            "tags":"MYTAG1,MYTAG2",
            "calctype":"Instant"
        },
        {
            ....
        }
    ]
}
{% endhighlight %}

#### Data retrieval
{% highlight bash %}
M1 8.5
M2 12345.6
....
{% endhighlight %}
