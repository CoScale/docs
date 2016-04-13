---
layout: page
title: Tracking web requests by method
description: How to track web requests by HTTP method.
---

1. Navigate to your <a href="http://app.coscale.com" db-href="/metrics/requests/" class="js-dashboard-link">web requests</a> page. This page is available in the navigation menu: Metrics > Web.

2. Find the web request you would also like to track the method for. In this example we want to track post requests for "lifestyle.com/api/send_message".
<img src="{{ site.baseurl}}/gfx/agent/extra/requests-method/requestList.png" alt="Web requests list" class="img-responsive" />

3. Start by adding a child request by clicking the button on the right > "Add child request". Fill in the fields as follows:
 <img src="{{ site.baseurl}}/gfx/agent/extra/requests-method/addNewRequest.png" alt="The new web request dialog." class="img-responsive" />
* **Name**: The name of the child request, this can be the HTTP method you want to match.
* **Match type**: This should be set to `Method`.
* **Function**: This should be set to `Exact match`.
* **Value**: The method you want to match, eg: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS, CONNECT

4. After a couple minutes it should be possible to select and view data for the configured methods.