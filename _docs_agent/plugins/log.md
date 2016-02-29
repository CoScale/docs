---
layout: page
title: Log plugin
description: Information on the log plugin.
---

The log plugin can collect data from any logs on your server.

## Configuration
When configuring the log plugin you will have to specify the following attributes:

* File path

    The full file path for the log file that you need to collect data from.

* Data type

    The possible values of this field are

    * Count: For calculating the count of the matched entries in the log file.
    * Average: For calculating the average values of the matched entries in the log file.
    * Histogram: For calculating the histogram values of the matched entries in the log file.
    * Minimum: For calculating the minimum values of the matched entries in the log file.
    * Maximum: For calculating the maximum values of the matched entries in the log file.

* Metric name

    The metric name that will be used to store the data.

* Regex

    The regex that will be used to match against each entry in the log file.
    {% include alert.html type="info" text="The regex will match against every log entry separately" %}

* Regex group name

    This field is required in case that the chosen data type is average, histogram, minimum or maximum. This is required to know which part of the matched regex we should use to calculate the average, histogram, minimum or maximum.

* Unit

    The unit for the calculated data, we ask for this for cosmetic purposes so when the numbers are displayed on any widgets the unit will appear next to it.

## Use-cases and examples

### Errors count
You can use the log plugin to get the count of errors logged in the log file. For example if the error log entry looks like this `2016-01-11 15:48:33,327 - [error] The error description`, your configuration will be as follows:

* DataType: Count
* Regex: `.*[error].*`

### Latency for 3rd party calls
You can use the log plugin to store the latency histogram data of a 3rd party call. For example if the log entry looks like this `CALL LAT 100 ms`, your configuration will be as follows:

* DataType: Histogram
* Regex: `CALL LAT (?'latency'\d+) ms`
* Regex group name: `latency`
