---
layout: page
title: Custom Attributes
---
CoScale allows you to push custom attributes together with your events. When defining an event category you can configure these parameters so that every event added after will be required to set them. These extra parameters are then shown in our event flags and can be used to color the event in our 'Event overview' widget. This gives meaning to your events and allows you to quickly see if one is not performing as expected.

<img src="{{ site.baseurl}}/gfx/installation/events/custom-attributes/automation_job_overview.png" alt="Event overview" class="img-responsive" />

## Creating the category
When creating a category through the [API]({{ site.baseurl }}/api/) or with our [CLI]({{ site.baseurl }}/installation/cli/index) you can add an extra optional parameter called `attributeDescriptions`. This parameter should contain a JSON array with information on which extra attributes the events should set.

### Parameters

#### Name
Name of the attribute your want to track

#### Type
Type of parameter you want to push to our system. `integer` types can be used to color the events on the 'Event overview' widget, as seen in the example above.

* string
* integer

#### Unit
The unit of the value that is added to the event. This is a string value that is used in our dashboard and is not used for processing.

### Example
{% highlight javascript %}
[
    {
        "name":"exitCode",
        "type":"integer"
    },
    {
        "name":"executionTime",
        "type":"integer",
        "unit":"s"
    },
    {
        "name":"extraData",
        "type":"string"
    }
]
{% endhighlight %}

## Pushing an event
After a category is created with custom attributes you need to send your events with an extra 'attribute' parameter containing the custom attributes described in `attributeDescriptions`. The parameter is a JSON object containing the names (key) available in `attributeDescriptions` with a metric value compatible with the type.

### Example
Example for the `attributeDescriptions` defined in the example above.
{% highlight javascript %}
{
    "exitCode":1,
    "executionTime":123,
    "extraData":"Disk full"
}
{% endhighlight %}
