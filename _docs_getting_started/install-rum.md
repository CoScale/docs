---
layout: page
title: Integrate Real User Monitoring (RUM)
---

The CoScale Real User Monitoring service or RUM is a Javascript snippet that provides insight into the performance on the user’s device. It tells you what is happening on your website after a webpage has left your infrastructure. We monitor all API calls, resources like Javascript and CSS, and external services. We measure how long they take to load en the impact on the overall performance of your website.

{% include alert.html type="info" text="The snippet will have little to no impact on webpage performance, it uses the browser API to retrieve data and will run after the page is loaded." %}

To install we need to add the javascript snippet just before the `</head>` tag on your website. It is best to add it the general template, so you can get a complete oversight of your application.

To find our snippet, go to 'Metrics' > 'Real user monitoring' in our sidebar, you can now follow the instructions on the screen, it will direct you to the RUM component installation page containing the instructions to integrate with your website. After installing the script our service should detect incoming traffic within minutes, but it does depend on the amount of traffic the website receives.

<p class="text-center"><img class="" src="{{ site.baseurl }}/gfx/getting-started/install-rum/rum_install.png" alt="CoScale RUM installation instructions" /></p>

## Now we wait
It can take up to 24 hours before all pages our detected and added to our dashboard. We will send you an e-mail when we detect new pages inside your application. While we wait let us get on with the next step of installing our agent to provide infrastructure insights and server performance metrics.

<a href="{{ site.baseurl }}/getting-started/install-agent" class="btn btn-primary btn-lg btn-block spacing-top">Step 3: Installing the agent</a>
