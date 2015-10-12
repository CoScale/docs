---
layout: page
title: Real User Monitoring Tags
description: Information on how to track groups of webpages.
---

## Tags
By adding the following Javascript to a page with the RUM component installed you can group pages together. You can use this to monitor a certain group of pages to get an overall insight into the performance.

{% highlight javascript %}
// Add this anywhere on the page, if you have multiple on the same page the last one will be used
CoScale.Tag("Tag name");
{% endhighlight %}
