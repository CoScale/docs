---
layout: page
title: Generic script plugin
description: Information on how to use the CoScale generic script plugin.
---
## Description
Once you have an [agent]({{ site.baseurl }}/agent/index) running on your server, you can add the generic script plugin to gather custom metrics and events. The plugin executes a script once every minute to gather data from it and sends it to CoScale.

The generic script plugin has **2** modes: **configuration** mode and **data retrieval** mode. Our plugin will first run in configuration mode to get the metrics that should be created. Afterwards, it will run every minute in data retrieval mode to get the data.

{% include alert.html type="warning" text="Scripts have a maximum runtime of 5 seconds." %}

## Prerequisite
* [CoScale Agent installed]({{ site.baseurl }}/agent/index)

## Examples
Sample scripts for the generic script plugin can be found in this GitHub repository:

<a href="https://github.com/CoScale/coscale-generic-scripts" target="_blank" class="btn btn-large btn-info"><i class="fa fa-3x fa-fw fa-github-square"></i> GitHub repository</a>

## Details

To get the agent to execute your generic script, you will need to add the path of your script in the configuration of the plugin. The simplest way to do this is via the "Agents" page in your application.

Each configuration line added in the configuration dialog will be executed asynchronously. Here are some configuration samples:

- `/home/coscale/scripts/bash-script.sh`
- `python /srv/scripts/pythonScript.py`
- `powershell.exe C:\scripts\powershell-script.ps1`

### Configuration mode

Every time the agent is restarted, it will execute `<script> -c` to get the configuration of your script. This will determine what metrics will be created in your app when data is retrieved.

**Note:** The `<script> -c` should return within 1 second, otherwise it will be killed.

**Note:** The script should return exit code 0. Otherwise, the output will not be parsed and a failure entry will be logged.

This is an **example** output of a script in **configuration mode**:

{% highlight json %}
{
    "maxruntime": 1000,
    "period": 60,
    "metrics": [{
        "id": 1,
        "datatype": "DOUBLE",
        "name": "First metric",
        "description": "Description for first metric",
        "groups": "MyMetrics/Category1",
        "unit": "Bytes",
        "tags": "MYTAG1,MYTAG2",
        "calctype": "Difference",
        "dimensions": [
            {"id": 1, "name":"dimension1"},
            {"id": 2, "name":"dimension2"},
            {"id": 3, "name":"dimension3"}
        ]
    }, {
        "id": 2,
        "datatype": "DOUBLE",
        "name": "Second metric",
        "description": "Description for second metric",
        "groups": "MyMetrics/Category1",
        "unit": "",
        "tags": "MYTAG1,MYTAG2",
        "calctype": "Instant",
        "dimensions": [
            {"id": 4, "name":"dimension4"},
            {"id": 5, "name":"dimension5"}
        ]
    }],
    "events": [{
        "id": 1,
        "name": "First event",
        "description": "Description for first event",
        "attributeDescriptions": [
            {"name":"firstAttribute", "type":"integer", "unit":"#"}
        ]
    }]
}
{% endhighlight %}

#### Parameters

| Parameter               | Description                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                    | ID of the metric / event, this should be the same as when the script is run in **data retrieval** mode. These IDs are local to the script and unrelated to the IDs given by the API.                                                  |
| `calctype`              | There are currently 3 available options for the `calctype`:                                                                                          |
|                         |     - Difference: Metric result will be the difference between value from a minute ago and the current value.                                        |
|                         |     - Instant: Metric result will be a new value every minute.                                                                                       |
|                         |     - Average: Metric result will be average over time.                                                                                              |
| `maxruntime`            | Maximum amount of time in milliseconds the script is allowed to run in data retrieval mode. If runtime exceeds this value the script will be stopped.|
| `period`                | Time interval in miliseconds where the agent polls the script for data.                                                                                  |
|                         | The maximum value for this is 5000. Your script can only take 5 seconds to run or it will be killed by the agent.                                    |
| `datatype`              | The data type of the created metric. Only `"DOUBLE"` is supported at this moment                                                                     |
| `groups`                | The metric group that this metric should be added to. Groups inside other groups need to be separated by a `/`                                       |
| `tags`                  | You can add a tag to add extra meaning to a metric (i.e. CPU_LOAD). Set as empty string to ignore this.
| `attributeDescriptions` | The [attribute descriptions]({{ site.baseurl }}/events/custom-attributes/) of the event.                                                              |
| `dimensions`            | The dimensions related to the given metric.                                                                                                          |

### Data retrieval mode
Once the agent has been started, the Generic Script plugin will gather data once every minute by calling `<script> -d`.

**Note:** The `<script> -d` should return within 5 seconds, otherwise it will be killed.

Given the above configuration, the following output is an example of the script running in **data retrieval mode**:

{% highlight bash %}
M1 "1:dimension1_value1,2:dimension2_value1,3:dimension3_value1" 8.5
M2 "4:dimension4_value1,5:dimension5_value1" 12345.6
E1 -300 0 "65.5" "{"firstAttribute":66}"
{% endhighlight %}

#### Parameters for metrics

| Parameter                   | Description                                                |
|-----------------------------|------------------------------------------------------------|
| `M1`                        | 'M' + the id of the metric as defined in configuration. |
| `"4:dimension4_value1,5:dimension5_value1"`                        | A comma separated list of dimension ids, colon and name of the dimension value. The outer quotes are required. |
| `8.5`                       | The value of the metric at the current time.                   |

#### Parameters for events

| Parameter                   | Description                                                                    |
|-----------------------------|--------------------------------------------------------------------------------|
| `E1`                        | 'E' + the id of the event as defined in configuration.                         |
| `-300`                      | The event start time. This can be the relative time in seconds or a unix timestamp. |
| `0`                         | The event end time. This can be the relative time in seconds or a unix timestamp.   |
| `"65.5"`                    | The message/content of the eventData. The quotes are required.             |
| `"{"firstAttribute":66}"` | All [attributes]({{ site.baseurl }}/events/custom-attributes/) for this event. The outer quotes are required.             |
