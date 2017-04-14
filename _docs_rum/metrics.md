---
layout: page
title: Real User Monitoring Metrics
description: What RUM metrics we collect and how they are measured.
---

For the collection of RUM metrics we use the browser <a href="https://www.w3.org/TR/navigation-timing-2/">Navigation Timing API</a>

## Navigation Timing API Chart

To correctly understand what our measurements are based on you first need to look at the complete picture of the Navigation Timing:

<img alt="Navigation timing screenshot" src="{{ site.baseurl }}/gfx/rum/navigation-timing-api-chart.jpg" />

All of the metrics we collect are part of, or the sum of specific components in the Navigation Timing flow.

## List of metrics
<a href="#backend-time">Backend-time</a>

<a href="#connection-time">Connection time</a>

<a href="#download-time">Download time</a>

<a href="#first-byte-time">First byte time</a>

<a href="#load-event-start">Load event start</a>

<a href="#load-event-end">Load event end</a>

## Backend-time
Backend-time is the sum of specific components in the Navigation Timing API that do not rely on front-end processing.

The timing collected for the "resources" are also network timings.

The sum of all the network timings together make up the backend time.

<img alt="RUM back-end time screenshot" src="{{ site.baseurl }}/gfx/rum/rum-backend-time-metric.jpg" />

## Connection time

<img alt="RUM connection time screenshot" src="{{ site.baseurl }}/gfx/rum/rum-connection-time-metric.jpg" />

## Download time

<img alt="RUM download time screenshot" src="{{ site.baseurl }}/gfx/rum/rum-download-time-metric.jpg" />

## First byte time

<img alt="RUM first byte time screenshot" src="{{ site.baseurl }}/gfx/rum/rum-first-byte-time-metric.jpg" />

## Load event start

<img alt="RUM load event start screenshot" src="{{ site.baseurl }}/gfx/rum/rum-load-event-start-metric.jpg" />

## Load event end

<img alt="RUM load event end screenshot" src="{{ site.baseurl }}/gfx/rum/rum-load-event-end-metric.jpg" />
