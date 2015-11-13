---
layout: page
title: Integrate Real User Monitoring (RUM)
description: Instructions on how to install and configure the CoScale Real User Monitoring component inside your application.
---

The CoScale Real User Monitoring service, or RUM for short, is a Javascript snippet that provides insight into the performance on the users computer and devices. It tells you what is happening with your application after the webpage has left your infrastructure. We monitor API calls, static resources like Javascript and CSS, and external services like Google Analytics and Facebook. We measure how long they take to load and the impact on the pageload time of your website.

{% include alert.html type="info" text="The snippet will have little to no impact on webpage performance, it uses the browser API to retrieve data and will run after the page is loaded." %}

To install the RUM service we need to add a javascript snippet just before the `</head>` tag on your website. It is best to add it the default template of the website, this way you get a complete oversight of your application. If you are unsure where to place the snippet please <a href="mailto:info@coscale.com" class="js-support">contact our support</a> so they can assist you in choosing the best location for the snippet.

To find the CoScale RUM snippet, go to 'Datasources' > 'Real user monitoring' in our sidebar and follow the instructions on the screen. After installing the script our service will detect incoming traffic within minutes, but it does depend on the amount of traffic the website receives.

<p class="text-center"><img class="" src="{{ site.baseurl }}/gfx/getting-started/install-rum/rum_install.png" alt="CoScale RUM installation instructions" /></p>

That was it, now we wait as it can take up to 24 hours before all pages are detected and added to our dashboard.

## Extra
Increase the visibility of your front-end performance by using tags and markers.

### [Tags]({{ site.baseurl }}/rum/tags)
Tags allow you to group pages to get an overview on their overall performance.

### [Markers]({{ site.baseurl }}/rum/markers)
Markers show performance of front-end heavy applications by measuring the time between start and stop command.
