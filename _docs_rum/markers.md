---
layout: page
title: Real User Monitoring Markers
description: Information on how to track the performance of certain parts of your front-end application.
---

## Markers
Measure parts of your Javascript application by placing start and stop markers inside your code. Our RUM component will measure the time difference between both calls and send it to the CoScale platform. You can have multiple markers running at the same time.

{% highlight javascript %}
// Start a marker
CoScale.MarkerStart("MARKER NAME");

// Stop an existing marker
CoScale.MarkerStop("MARKER NAME");
{% endhighlight %}
