---
layout: page
title: Generic script plugin
description: Information on how to use the CoScale generic script plugin.
---
## Description
Once you have an [agent]({{ site.baseurl }}/agent/index) running on your server you can add the generic script plugin to gather custom metrics. The plugin executes a script once every minute to gather data from it and sends it to CoScale.

The generic script plugin has **2** modes: **configuration** mode and **data retrieval** mode. Our plugin will first run the configuration mode to get the metrics which should be created. Afterwards it will run every minute in data retrieval mode to get the data.

## Examples
A couple of examples of scripts for the generic script plugin can be found in this GitHub repository:

<a href="https://github.com/CoScale/coscale-generic-scripts" target="_blank" class="btn btn-large btn-info"><i class="fa fa-3x fa-fw fa-github-square"></i> Github repository</a>

## Details

To get the agent to execute your generic script you will need to add the path of your script in the configuration of the plugin. The simplest way to do this is via the "Agents" page in the application.

Each configuration line added in the configuration dialog will be executed asynchronously. Here are a couple of examples of configurations:

- `/home/coscale/scripts/bash-script.sh`
- `python /srv/scripts/pythonScript.py`
- `powershell.exe C:\scripts\powershell-script.ps1`

### Configuration mode
Every time the agent is restarted it will execute `<script> -c` to get the configuration of your script. This will determine what metrics that will be created for you for when your data is retrieved.

**Note:** The `<script> -c` should return within 1 second, otherwise it will be killed.

**Note:** The script should return exit code 0, otherwise the output is not be parsed and a failure log entry will be made.

This is an **example** output of a script in **configuration mode**:

{% highlight json %}
{
    "maxruntime": 1000,
    "metrics": [{
        "id": 1,
        "datatype": "DOUBLE",
        "name": "First metric",
        "description": "Description for first metric",
        "groups": "MyMetrics/Category1",
        "unit": "Bytes",
        "tags": "MYTAG1,MYTAG2",
        "calctype": "Difference"
    }, {
        "id": 2,
        "datatype": "DOUBLE",
        "name": "Second metric",
        "description": "Description for second metric",
        "groups": "MyMetrics/Category1",
        "unit": "",
        "tags": "MYTAG1,MYTAG2",
        "calctype": "Instant"
    }]
}
{% endhighlight %}

#### Parameters

| Parameter     | Description                                                                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`          | Id of the metric, this should be the same as when the script is run in **data retrieval** mode.                                                      |
| `calctype`    | There are currently 3 available options for the `calctype`:                                                                                          |
|               |     - Difference: Metric result will be the difference between value from a minute ago and the current value.                                        |
|               |     - Instant: Metric result will be a new value every minute.                                                                                       |
|               |     - Average: Metric result will be average over time.                                                                                              |
| `maxruntime`  | Maximum amount of time in milliseconds the script is allowed to run in data retrieval mode. If runtime exceeds this value the script will be stopped.|
|               | The maximum value for this is 5000. Your script can only take 5 seconds to run or it will be killed by the agent.                                    |
| `datatype`    | The data type of created metric. Only `"DOUBLE"` is supported at this moment                                                                         |
| `groups`      | The metric group that this metric should be added to. Groups inside other groups needs to be separated by a `/`                                      |
| `tags`        | You can add a tag to add extra meaning to a metric (i.e. CPU_LOAD). Set as empty string to ignore this.                                              |

### Data retrieval mode
Once the agent has been started, the Generic Script plugin will gather data once every minute by calling `<script> -d`.

**Note:** The `<script> -d` should return within 5 seconds, otherwise it will be killed.

Given the above configuration, the following output is an example of the script running in **data retrieval mode**:

{% highlight bash %}
M1 8.5
M2 12345.6
{% endhighlight %}
