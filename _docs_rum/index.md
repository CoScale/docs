---
layout: page
title: Real user monitoring
description: Overview of information on how to configure, maintain the CoScale real user monitoring component.
---

## Installation

### [Installing Real User Monitoring in your code]({{ site.baseurl }}/rum/install)
A quick how to guide on installing and configuring the CoScale Real user monitoring component for monitoring your front-end performance.

### [Integrating Real User Monitoring with Google Tag Manager]({{ site.baseurl }}/rum/google-tag-manager)
Step by step instructions on how to add the RUM component javascript to <a href="https://www.google.com/tagmanager/" target="_BLANK">Google Tag manager</a>.

## Advanced

### [Tags]({{ site.baseurl }}/rum/tags)
Group pages with tags to measure the performance of similar pages.

### [Markers]({{ site.baseurl }}/rum/markers)
Measure the performance of certain parts of your front-end application.

### [Metrics]({{ site.baseurl }}/rum/metrics)
What RUM metrics we collect and how they are measured

## Information

### Browser support

Our snippet is fully supported by 66,31% and partially 81,43% supported on all popular browsers. (<a href="http://caniuse.com/" target="_BLANK">source sep 2015</a>)

<table class="table table-hover table-browsers">
    <thead>
        <tr>
            <th>IE</th>
            <th>Edge</th>
            <th>Firefox</th>
            <th>Chrome</th>
            <th>Safari</th>
            <th>Opera</th>
            <th>iOS Safari</th>
            <th>Opera Mini</th>
            <th>Android Browser</th>
            <th>Chrome for Android</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="danger">8</td>
            <td class=""></td>
            <td class=""></td>
            <td class="success">31</td>
            <td class=""></td>
            <td class=""></td>
            <td class="danger">7.1</td>
            <td class=""></td>
            <td class="warning">4.1</td>
            <td class=""></td>
        </tr>
        <tr>
            <td class="warning">9</td>
            <td class=""></td>
            <td class="success">38</td>
            <td class="success">43</td>
            <td class=""></td>
            <td class=""></td>
            <td class="danger">8.4</td>
            <td class=""></td>
            <td class="warning">4.3</td>
            <td class=""></td>
        </tr>
        <tr>
            <td class="success">10</td>
            <td class=""></td>
            <td class="success">39</td>
            <td class="success">44</td>
            <td class="warning">9</td>
            <td class="success">31</td>
            <td class="warning">9</td>
            <td class=""></td>
            <td class="success">4.4.4</td>
            <td class=""></td>
        </tr>
        <tr>
            <td class="success">11</td>
            <td class="success">12</td>
            <td class="success">40</td>
            <td class="success">45</td>
            <td class="warning">10</td>
            <td class="success">32</td>
            <td class="warning">10</td>
            <td class="danger">8</td>
            <td class="success">44</td>
            <td class="success">44</td>
        </tr>
        <tr>
            <td class=""></td>
            <td class="success">13</td>
            <td class="success">41</td>
            <td class="success">46</td>
            <td class="success">11</td>
            <td class="success">33</td>
            <td class="success">11</td>
            <td class=""></td>
            <td class=""></td>
            <td class=""></td>
        </tr>
        <tr>
            <td class=""></td>
            <td class=""></td>
            <td class="success">42</td>
            <td class="success">47</td>
            <td class=""></td>
            <td class="success">34</td>
            <td class=""></td>
            <td class=""></td>
            <td class=""></td>
            <td class=""></td>
        </tr>
        <tr>
            <td class=""></td>
            <td class=""></td>
            <td class="success">43</td>
            <td class="success">48</td>
            <td class=""></td>
            <td class=""></td>
            <td class=""></td>
            <td class=""></td>
            <td class=""></td>
            <td class=""></td>
        </tr>
    </tbody>
</table>
<span class="text-success">Green version are fully supported</span>, <span class="text-warning">yellow may lack some required features</span> and <span class="text-danger">red is not supported</span>.

### iOS & Android Support for Navigation and Resource Timing

<table class="table table-hover table-browsers">
    <thead>
        <tr>
            <th>&nbsp;</th>
            <th>iOS 7 UIWebView</th>
            <th>iOS 8 WKWebView</th>
            <th>Android 4.3 Webkit Webview</th>
            <th>Android 4.4 Chromium Webview</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="">Navigation Timing</td>
            <td class="danger">No</td>
            <td class="success">Yes</td>
            <td class="success">Yes</td>
            <td class="success">Yes</td>
        </tr>
        <tr>
            <td class="">Resource Timing</td>
            <td class="danger">No</td>
            <td class="danger">No</td>
            <td class="danger">No</td>
            <td class="success">Yes</td>
        </tr>
    </tbody>
</table>


<span>**Navigation Timing** is an API that measures client performance and gives access to the full timing information related to the page, from when the browser opened the connection to when it resolved the DNS name to when it finished loading the page.</span>.

<span>The **Resource Timing** API allows you to collect complete timing information related to resources in a document. It enables you to measure user latency, which is crucial to benchmark web pages. Using the Resource Timing API allows us to retrieve and analyze a detailed profile of all the network timing data for every resource on the page.</span>
