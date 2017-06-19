---
layout: page
title: Log plugin
description: Information on the log plugin.
---

## How it works

The log plugin can collect data from any logs on your server. It uses regular expressions to parse information from a log file. It can count the number of lines that match the expression and get a value from within that line.

## Configuration

When configuring the log plugin you will have to specify the following attributes:

<table>
    <thead>
        <tr>
        <th>
            <!-- I gave it a width so the parameters names do not get broken -->
            <div style="width:150px;">Parameter</div>
        </th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>File path</code></td>
            <td>The full file path for the log file that you need to collect data from.</td>
        </tr>
        <tr>
            <td><code>Data type</code></td>
            <td>
                The possible values of this field are:

                <ul>
                    <li><strong>Count</strong>: For calculating the count of the matched entries in the log file.</li>
                    <li><strong>Average</strong>: For calculating the average values of the matched entries in the log file.</li>
                    <li><strong>Histogram</strong>: For calculating the histogram values of the matched entries in the log file.</li>
                    <li><strong>Minimum</strong>: For calculating the minimum values of the matched entries in the log file.</li>
                    <li><strong>Maximum</strong>: For calculating the maximum values of the matched entries in the log file.</li>
                </ul>
            </td>
        </tr>

        <tr>
            <td><code>Metric name</code></td>
            <td>The metric name that will be used to store the data.</td>
        </tr>
        <tr>
            <td><code>Regex</code></td>
            <td>
                The regex that will be used to match against each entry in the log file. <br/>
                The regex can be in two formats:

                <ul>
                    <li><strong>Normal regex ( pcre compliant )</strong></li>
                    <li>
                        <strong><a href="https://github.com/logstash-plugins/logstash-patterns-core/blob/master/patterns/grok-patterns" target="_blank">A set of predefined grok patterns</a></strong>
                        (<a href="https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html#_regular_expressions" target="_blank">More info about grok patterns here.</a>)
                    </li>
                </ul>

                <p>It is advisable to test the regex on a line before you use it. <a href="http://regexr.com/" target="_blank">regexr</a> is a good online tool for testing regexes.</p>

                {% include alert.html type="info" text="The regex will match against every log entry separately" %}
            </td>
        </tr>
        <tr>
            <td><code>Regex group name</code></td>
            <td>This field is required in case that the chosen data type is average, histogram, minimum or maximum. This is required to know which part of the matched regex we should use to calculate the average, histogram, minimum or maximum.</td>
        </tr>
        <tr>
            <td><code>Unit</code></td>
            <td>The unit for the calculated data. We ask for this for cosmetic purposes so when the numbers are displayed on any widgets the unit will appear next to it.</td>
        </tr>
    </tbody>
</table>

## Use-cases and examples

### Web server logs

We have a log file for a web server with these kind of logs:

    coscale.com GET /index.html 15824 43

The number 15824 represents the response size. If we wanted to calculate the average response size per second we can:

* Use your own regex:
    * `\.\*? \.\*? \.\*? (?<responseSize>[0-9]+) [0-9]+`

* Use a regex defined using grok patterns:
    * `%{IP} %{WORD} %{URIPATHPARAM} %{NUMBER:responseSize} %{NUMBER}`

Now if you configure your plugin like this:

<img alt="Log plugin configuration screenshot" src="{{ site.baseurl }}/gfx/agent/plugins/log/example-log-plugin-configuration.png" />

the log plugin will read the average response size from your logs and insert the data into CoScale to the metric __Response size per second__.

### Errors count
You can use the log plugin to get the count of errors logged in the log file. For example if the error log entry looks like this `2016-01-11 15:48:33,327 - [error] The error description`, your configuration will be as follows:

* DataType: Count
* Regex: `.*[error].*`

### Latency for 3rd party calls
You can use the log plugin to store the latency histogram data of a 3rd party call. For example if the log entry looks like this `CALL LAT 100 ms`, your configuration will be as follows:

* DataType: Histogram
* Regex: `CALL LAT (?<latency>\d+) ms`
* Regex group name: `latency`
