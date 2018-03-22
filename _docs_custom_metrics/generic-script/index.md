---
layout: page
title: Generic script plugin
description: Information on how to use the CoScale generic script plugin.
---
## Description
Once you have an [agent]({{ site.baseurl }}/agent/index) running on your server, you can add the generic script plugin to gather custom metrics and events. The plugin executes the scripts you provide once every minute to gather data from it and sends it to CoScale.

The scripts provided to the generic script plugin must have **2** modes: a **configuration** mode and a **data retrieval** mode. Our plugin will first run your scripts in configuration mode to get the metrics that should be created. Afterwards, it will run the scripts every minute in data retrieval mode to get the data.

## Prerequisite
* [CoScale Agent installed]({{ site.baseurl }}/agent/index)

## Examples
Sample scripts for the generic script plugin can be found in the GitHub repository below. The repository contains examples for filesystems, mailservers, uptime checking, certificate checking, etc.

<a href="https://github.com/CoScale/coscale-generic-scripts" target="_blank" class="btn btn-large btn-info"><i class="fa fa-3x fa-fw fa-github-square"></i> GitHub repository</a>

## Configuration

Adding custom metrics and events using the generic script plugin can be achieved by adding the generic script plugin to your agent. The simplest way to do so is via the "Agents" page in your application. During the configuration of the plugin you will have to provide the path to the scripts you wish to execute. All scripts provided in the configuration will be executed asynchronously.

The configuration can be a path to a script, for example:

- `/home/cs/scripts/bash-script.sh`

The configuration can also include parameters, this way you can also provide an interpreted script:

- `python /srv/scripts/pythonScript.py`
- `powershell.exe C:\scripts\powershell-script.ps1`


## Developing a script

In this section we will explain in detail how you can create a script to generate custom metrics and events. 

### Configuration mode

When the agent is started, it will execute `<script> -c` to retrieve the metric and events defined by the script. The output should be a json that contains the metrics and events.

{% include alert.html type="warning" text="`<script> -c` should return within 1 second, otherwise it will be killed. The script should return exit code 0. Otherwise, the output will not be parsed and an error will be logged." %}

This is an **example** output of a script in **configuration mode**:

{% highlight json %}
{
    "maxruntime": 5000,
    "period": 60,
    "metrics": [{
        "id": 1,
        "name": "Incoming traffic on interface",
        "description": "Incoming traffic in bytes on network interface",
        "groups": "Networking/Traffic",
        "unit": "b/s",
        "tags": "NETWORK",
        "datatype": "GUAGE",
        "calctype": "Instant",
        "dimensions": [
            {"id": 1, "name":"interface"}
        ]
    }, {
        "id": 2,
        "name": "Second metric",
        "description": "Description for second metric",
        "groups": "MyMetrics/Category2",
        "unit": "",
        "tags": "MYTAG1,MYTAG2",
        "datatype": "DOUBLE",
        "calctype": "Difference",
        "dimensions": [
            {"id": 2, "name":"dimension2"},
            {"id": 3, "name":"dimension3"}
        ]
    }],
    "events": [{
        "id": 1,
        "name": "My custom event",
        "description": "Description for my custom event",
        "attributeDescriptions": [
            {"name":"Exit code", "type":"integer", "unit":""}
        ]
    }]
}
{% endhighlight %}

#### maxruntime

The maximum amount of time (in milliseconds) the script is allowed to run in data retrieval mode, if the runtime exceeds this value the script will be stopped. The maximum value for maxruntime is 50000 (50 seconds).

#### period

Time interval (in seconds) between agent polls that retrieve the data. The minimum value for period is 60 (1 minute).


#### Metric fields

| Field                   | Description                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                    | ID of the metric.                                                                                                                                    |
|                         | This ID will be used to match the data in the **data retrieval** model with the metric from the **configuration** mode.                              |
|                         | IDs are local to the script and unrelated to the IDs given by the API.                                                                               |
| `name`                  | The name of the metric. (Note that this will be suffixed with '- Custom' to prevent collisions with other plugins.)                                  |
| `description`           | Description of the metric.                                                                                                                           |
| `groups`                | The metric groups that this metric should be added to (comma separated). Nested groups should be separated by a `/`.                                 |
| `unit`                  | The unit for the metric (shown on the Y-axis in the UI).                                                                                             |
| `tags`                  | You can add a tag to add extra meaning to a metric (i.e. NETWORK).                                                                                   |
| `datatype`              | The data type of the created metric. The following 3 options are available for the `datatype`:                                                       |
|                         |     - GAUGE: value at this point in time (eg. memory usage)                                                                                          |
|                         |     - COUNT: a number per a given interval (eg. number of log lines added)                                                                           |
|                         |     - COUNTER: keeps increasing over time (eg. total number of log lines). You can graph the diffs on the totals in the UI.                          |
|                         | More information about these datatypes can be found on [the metrics 2.0 website](http://metrics20.org/spec/).                                        |
| `calctype`              | The calculation performed on the data returned by the script. The following 3 options are available for the `calctype`:                              |
|                         |     - Instant: the metric data is the data returned by the script.                                                                                   |
|                         |     - Difference: the metric data is the difference between the last value returned by the script and the current value.                             |
| `dimensions`            | The dimensions for the metric. The dimension `id` will be used in the **data retreival** mode.                                                       |



#### Event fields

| Field                   | Description                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                    | ID of the event.                                                                                                                                     |
|                         | This ID will be used to match the data in the **data retrieval** model with the metric from the **configuration** mode.                              |
|                         | IDs are local to the script and unrelated to the IDs given by the API.                                                                               |
| `name`                  | The name of the event. (Note that this will be suffixed with '- Custom' to prevent collisions with other plugins.)                                   |
| `description`           | Description of the event.                                                                                                                            |
| `attributeDescriptions` | The [attribute descriptions]({{ site.baseurl }}/events/custom-attributes/) of the event.                                                             |


### Data retrieval mode

Once the agent has been started, the Generic Script plugin will gather data once every minute by calling `<script> -d`.

{% include alert.html type="warning" text="Scripts executed by the generic script plugin are automatically stopped after 1 minute." %}

Given the configuration above, the following output is an example of the script running in **data retrieval mode**:

{% highlight bash %}
M1 "1:eth0" 8.5
M2 "2:dimension2_value1,3:dimension3_value1" 12345.6
E1 -300 0 "The event triggered" "{"Exit code":137}" S
{% endhighlight %}

#### Metric format

{% highlight bash %}
M1 "1:eth0" 8.5
{% endhighlight %}

| Field                   | Description                                                                   |
|-------------------------|-------------------------------------------------------------------------------|
| `M1`                    | 'M' followed by the id of the metric as defined in **configuration** mode.    |
|                         | In this example M1 refers to "Incoming traffic on interface".                 |
| `"1:eth0"`              | A comma separated list of dimension ids and their value.                      |
|                         | `1:eth0` sets dimension with id 1 ("interface") to value "eth0".              |
|                         | **Important: the quotes are required.**                                       |
| `8.5`                   | The value of the metric at the current time.                                  |

#### Event format

{% highlight bash %}
E1 -300 0 "The event triggered" "{"Exit code":137}" S
{% endhighlight %}

| Field                       | Description                                                                              |
|-----------------------------|------------------------------------------------------------------------------------------|
| `E1`                        | 'E' followed by the id of the event as defined in **configuration** mode.                |
|                             | In this example E1 refers to "My custom event".                                          |
| `-300`                      | The start time for the event. 2 formats can be used here:                                |
|                             |   - Relative time: 0 for now, minus x for x seconds ago (eg. `-300` is 300 seconds ago). |
|                             |   - Absolute time: Unix timestamp in seconds (eg `1458345600` is March 19, 2016).        |
| `0`                         | The end time for the event. Same format as the start time applies.                       |
| `"The event triggered"`     | The message for the event (string). The quotes are required.                             |
| `"{"Exit code":137}"`       | All [attributes]({{ site.baseurl }}/events/custom-attributes/) for this event. The quotes are required. |
| `S`                         | Indicates that the event data should be attached to the current server/container.        |
|                             | Application-level events can be created by putting A instead of S.                       |
