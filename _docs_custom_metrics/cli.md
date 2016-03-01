---
layout: page
title: Pushing data with CLI
description: Information on how to use the CoScale CLI to push custom data.
---

## Prerequisite
* [CoScale Command line tool]({{ site.baseurl }}/tools/cli/installation)

## An example
`./coscale-cli data insert --data="M1:A:1456409700:1.2;M2:A:1456409700:3.14"`

will store a datapoint for
- metric id 1 with value 1.2 at timestamp 1456409700 = Feb 25 2016, 9:15:00 AM EST
- metric id 2 with value 3.14 at the same timestamp 1456409700 = Feb 25 2016, 9:15:00 AM EST

You can get some more help about the options running the command, for example:
`./coscale-cli data insert --data`

This will give you some more information about the possibilities.

```
Mandatory:
    --data
        To send data for DOUBLE metric data typ use the following format:
            "M<metric id>:S<subject Id>:<time>:<value/s>"
            eg:    --data="M1:S100:1454580954:1.2

        To send data for HISTOGRAM metric data type use the following format:
            "M<metric id>:S<subject Id>:<seconds ago>:[<no of samples>,<percentile width>,[<percentile data>]]"
            eg: --data="M1:S1:-60:[100,50,[1,2,3,4,5,6]]"

        Sending multiple data entries is possible by using semicolon as separator.
            eg: --data="M1:S100:-60:1.2;M1:S100:0:2"

        The time is formatted as follows:
            Positive numbers are interpreted as unix timestamps in seconds.
            Zero is interpreted as the current time.
            Negative numbers are interpreted as a seconds ago from the current time.
```
