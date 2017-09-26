---
layout: page
title: Pushing data with CLI
description: Information on how to use the CoScale CLI to push and get custom data.
---

## Prerequisite
* [CoScale Command line tool]({{ site.baseurl }}/tools/cli/installation)

## Simple insert example

In this example we create a metric, and then push a single data point to it. 

Create an application metric: 
`./coscale-cli metric new --name "Transaction value" --dataType "DOUBLE" --subject "APPLICATION" --unit "$"`

This returns the metric object (we will need the id for inserting data)

{% highlight json %}
{
 "id": 675,
 "version": 1,
 "state": "ENABLED",
 "name": "Transaction value",
 "description": "",
 "unit": "$",
 "period": 60,
 "source": "cli",
 "dataType": "DOUBLE",
 "subject": "APPLICATION"
}
{% endhighlight %}

Push data for the application metric. In this example we will push data for the 'Transaction value' metric (id 675) at timestamp 1495108650 with value 1.23:

`coscale-cli data insert --data="M675:A:1495108650:1.23"`

You can also use timestamp value 0 to use the current timestamp.

## Complex insert example

In this example we will be using the CoScale dimension system while pushing data using the CoScale CLI. In the example below we are pushing a datapoint for Queue `q1` and Cluster `cli1`. 

`./coscale-cli data insert --data="M1:A:1456409700:1.2:{"Queue":"q1","Cluster":"cl1"};M2:A:1456409700:3.14"`

Explanation for the command:

* metric id: 1
* subject: A
    * value: 1.2
    * timestamp: 1456409700 = Feb 25 2016, 9:15:00 AM EST
    * a JSON object with the names of the dimension and the name of the dimensionvalue. In this example, we're pushing data for Queue "q1" on Cluster "cl1".
* metric id: 2
* subject: A
    * value: 3.14
    * timestamp: 1456409700 = Feb 25 2016, 9:15:00 AM EST

You can get more help about the options running the command `./coscale-cli data insert --data`. This will give you more information about the parameters and possibilities.

    Mandatory:
        --data
            To send data for the DOUBLE metric data type, use the following format:
                "M<metric id>:S<subject Id>:<time>:<value/s>"
                eg:    --data="M1:S100:1454580954:1.2"

            To send data for the HISTOGRAM metric data type, use the following format:
                "M<metric id>:S<subject Id>:<seconds ago>:[<no of samples>,<percentile width>,[<percentile data>]]"
                eg: --data="M1:S1:-60:[100,50,[1,2,3,4,5,6]]"

            Sending multiple data entries is possible by using semicolon as separator:
                eg: --data="M1:S100:-60:1.2;M1:S100:0:2"

            The time is formatted as follows:
                Positive numbers are interpreted as unix timestamps in seconds.
                Zero is interpreted as the current time.
                Negative numbers are interpreted as a seconds ago from the current time.

## A retrieval example
`./coscale-cli data get --start=1474632472 --stop=1475062253 --aggregator=AVG --subjects=AVG(s1,s2) --metricId=1 --dimensionsSpecs=[[1,"AVG(1,2)"],[2,"5,6"]]`

Will get all relevant data for:

* metric id 1
* subjects: The Average over Server 1 and Server 2.
* dimensionSpecs: One or more JSON arrays, each containing a dimension ID and a string to define the dimensionvalues. * is interpreted as "All dimensionvalues for the related dimension".
* between timestamp 1456228800 and 1456315200 (Tue, 23 Feb 2016 12:00:00 PM GMT and Wed, 24 Feb 2016 12:00:00 PM GMT)

The data will be split out per measurement. In case of the example, data will be returned for:

* The Average over Server 1 and Server 2, the Average over dimensionvalue 1 and 2, combined with dimensionvalue 5

* The Average over Server 1 and Server 2, the Average over dimensionvalue 1 and 2, combined with dimensionvalue 6

The Aggregators for the subjects and dimensionSpecs are optional and can be left out. Leaving them out will cause values to be returned for each individual server/dimensionvalue.
