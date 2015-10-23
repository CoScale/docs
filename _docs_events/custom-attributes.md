---
layout: page
title: Custom Attributes
description: Information on how to use the custom attributes together with the CoScale events.
---
CoScale allows you to push custom attributes together with your events. When defining an event category you can configure these parameters, so that every event added to this category will require them. The extra parameters are then shown on our event flags and can be used to color the events in our 'Event overview' widget. This means you can add extra information to your events and see if they are performing as expected.

<img src="{{ site.baseurl}}/gfx/installation/events/custom-attributes/automation_job_overview.png" alt="Event overview" class="img-responsive" />

## Creating the category
When creating a category through the [API]({{ site.baseurl }}/api/) or with our [CLI]({{ site.baseurl }}/tools/cli/index) you can add an extra optional parameter called `attributeDescriptions`. This parameter should contain a JSON array with information on which extra attributes the events should set. You can also use the dashboard to add the custom attributes to a category.

### Parameters
Every attribute inside the `attributeDescriptions` parameter requires 3 different elements.

* `name`: Name of the attribute your want to track



* `type` The type of parameter you want to push to our system.

    Attributes of type `integer` can be used to color the events on the 'Event overview' widget, as seen in the example above.

    * string
    * integer

* `unit`: The unit of the value that is added to the event.

    This is a string value that is used in our dashboard and is not used for processing. It can be left empty.

### Example `attributeDescriptions`
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
After a category is created with custom attributes you need to send your events with an extra 'attribute' parameter containing the custom attributes described in `attributeDescriptions`. The parameter is a JSON object containing the names (key) available in `attributeDescriptions` with a metric value compatible with the type used.

### Example
Example for the `attributeDescriptions` defined in the example above.
{% highlight javascript %}
{
    "exitCode":1,
    "executionTime":123,
    "extraData":"Disk full"
}
{% endhighlight %}
