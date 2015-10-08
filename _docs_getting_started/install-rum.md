---
layout: page
title: Integrate Real User Monitoring (RUM)
description: Instructions on how to install and configure the CoScale Real User Monitoring component inside your application.
---

The CoScale Real User Monitoring service, or RUM for short, is a Javascript snippet that provides insight into the performance on the users computer and devices. It tells you what is happening with your application after the webpage has left your infrastructure. We monitor API calls, static resources like Javascript and CSS, and external services like Google Analytics and Facebook. We measure how long they take to load and the impact on the pageload time of your website.

{% include alert.html type="info" text="The snippet will have little to no impact on webpage performance, it uses the browser API to retrieve data and will run after the page is loaded." %}

To install the RUM service we need to add a javascript snippet just before the `</head>` tag on your website. It is best to add it the default template, so you can get a complete oversight of your application. In doubt, <a href="mailto:info@coscale.com" class="support">contact our support</a> so they can assist you in choosing the best location for the snippet.

To find our snippet, go to 'Datasources' > 'Real user monitoring' in our sidebar, you can now follow the instructions on the screen, it will direct you to the RUM component installation page containing the instructions to integrate with your website. After installing the script our service should detect incoming traffic within minutes, but it does depend on the amount of traffic the website receives.

<p class="text-center"><img class="" src="{{ site.baseurl }}/gfx/getting-started/install-rum/rum_install.png" alt="CoScale RUM installation instructions" /></p>

## Now we wait
It can take up to 24 hours before all pages our detected and added to our dashboard. While we wait let us get on with the next step of installing our agent as it will provide infrastructure insights and server performance metrics.

<a href="{{ site.baseurl }}/getting-started/install-agent" class="btn btn-primary btn-lg btn-block spacing-top">Step 3: Installing the agent</a>
