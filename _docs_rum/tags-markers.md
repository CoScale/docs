---
layout: page
title: Google Tag Manager
description: Information on how to track groups of webpages and the performance of certain parts of your front-end application.
---

## Tags
By adding the following Javascript to a page with the RUM component installed you can group pages together. You can use this to monitor a certain group of pages to get an overall insight into the performance.

{% highlight javascript %}
// Add this anywhere on the page, if you have multiple on the same page the last one will be used
CoScale.Tag("Tag name");
{% endhighlight %}

## Markers
Measure parts of your Javascript application by placing start and stop markers inside your code. Our RUM component will measure the time difference between both calls and send it to the CoScale platform. You can have multiple markers running at the same time.

{% highlight javascript %}
// Start a marker
CoScale.MarkerStart("MARKER NAME");

// Stop an existing marker
CoScale.MarkerStop("MARKER NAME");
{% endhighlight %}
