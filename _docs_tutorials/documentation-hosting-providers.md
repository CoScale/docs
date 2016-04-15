---
layout: page
title: How to introduce CoScale to your hosting provider
description: How to introduce CoScale to your hosting provider
---

### CUSTOMER

1. Create an account on our platform

    Visit [CoScale](http://www.coscale.com/) and choose “Free trial”. You will be redirected to a registration page where you’ll be asked to provide basic information: company name, company profile, email, password.

2. Invite your Hosting Provider to CoScale
    Click on Users -> Manage -> Invite user
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/CoScale-01-InviteUser.png"/>

3. Learn more about CoScale’s solution

    Visit [docs.coscale.com](http://docs.coscale.com/) to learn more about CoScale’s Full Stack Web Performance Monitoring solution. Send this URL to your hosting provider also.

### HOSTING PROVIDER

2. You will receive the invitation to use CoScale. After registering you will have access to the platform.

    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/01-Overview.png"/>

3. Create a new agent

    The CoScale lightweight agent is used to monitor server infrastructure and services, it uses log parsing and global status pages to gather its data and pushes the data to the CoScale platform through HTTPS calls.

    * Go to Datasources -> Agent. Click on “Create new CoScale agent”
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/02-NewAgent.png"/>

    * Select your operating system. We will use Ubuntu 14.04 in this tutorial.
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/03-OS.png"/>

    * Choose a plugin (e.g. Apache)
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/04-ApachePlugin.png"/>

    * Proceed with configuration, as described in every configuration step for the selected plugin
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/05-Apache-config-1.png"/>
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/06-Apache-config-2.png"/>
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/07-Apache-config-3.png"/>

    * After selecting and configuring all the plugins you need, proceed to “Next Step”. This will display a summary of the Agent and the selected plugins. Click on “Save agent”.
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/08-Summary.png"/>

    * Download the Agent on your server and install it
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/09-DownloadAgent.png"/>


        <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/10-InstallAgent.png"/>

    * You should see the Agent “Online” automatically
    <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/11-AgentOnline.png"/>

    * Click on Finish to close the Configuration section

    * If you wish to add another plugin, click on “Configure” for a specific Agent and follow the steps

        <img alt="New plugin" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/12-NewPlugin.png"/>

        For other platforms and plugins, please refer to the full documentation available here: [docs.coscale.com/agent]({{ site.baseurl }}/agent/index/)

    * __Real User Monitoring__

        The CoScale Real User Monitoring service, or RUM for short, is a Javascript snippet that provides insight into the performance on the user’s computer and devices. It tells you what is happening with your application after the webpage has left your infrastructure. We monitor API calls, static resources like Javascript and CSS, and external services like Google Analytics and Facebook. We measure how long they take to load and the impact on the page load time of your website.

        The snippet will have little to no impact on webpage performance, it uses the browser API to retrieve data and will run after the page is loaded.

        Go to Datasources -> Real user monitoring, copy and paste the snippet provided in the desired pages of your website, right before the </head> tag:

        <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/13-RUM-1.png"/>

        After adding the javascript snippet to your website, CoScale will automatically detect your web pages and list them in Metrics -> Real user monitoring.

        Initially, the page will look like this:

        <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/14-RUM-2.png"/>

        Then:

        <img alt="Invite user" src="{{ site.baseurl }}/gfx/tutorials/documentation-hosting-providers/15-RUM-3.png"/>

        And, after the mining process is finished, you should have access to Real User Monitoring data.
        For more details, please refer to the full documentation, available here: [docs.coscale.com/rum]({{ site.baseurl }}/rum/index/)

    If you have questions or remarks, please don't hesitate to contact us via

    * Email: [info@coscale.com](mailto:info@coscale.com)
    * Live chat: [CoScale.com](http://www.coscale.com)
