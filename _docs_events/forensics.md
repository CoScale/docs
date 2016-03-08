---
layout: page
title: Forensics
description: Information on what forensics are and where you can view them.
---

Forensics are special events inserted by our agents. You can easly recognize them by their looking glass (<i class="fa fa-fw fa-search"></i>) icon on your charts. They can help you identify problems on your server as they can display additional data about the moment they occured.

## Enabling forensics

Forensics are enabled by default for most linechart widgets. You can disable forensics by toggling the switchbutton at the bottom of the Events step in a widget configuration dialog.

<img src="{{ site.baseurl}}/gfx/events/forensics/include_forensics.png" alt="Event step with forensics switchbutton" class="img-responsive" />

Forensics are available for specific metrics. If you selected such a metric, forensics will now be displayed on your linechart. You can view the details of the forensic event by clicking it and then clicking `show details` in the context menu. This will pin the time so you can freely move your cursor to the right where the forensic details will be shown. You can click on the chart to view details about the clicked point or press tab to unpin the time again.

<img src="{{ site.baseurl}}/gfx/events/forensics/forensic_processes.png" alt="process forensics" class="img-responsive" />

## Forensic types

### Processes

Process forensics will display a list of up to 10 processes and how much resources they were using at that moment. 

There are multiple types of process forensics:

* **CPU forensics:** For Linux this metric is called `Total CPU Usage` and for Windows this metric is called `Total Percent Processor Time`. These list the top 10 processes and how much processor time they use in %.

* **Disk forensics:** For Linux these metrics are called `All disks write bytes per second` and `All disks read bytes per second`, for Windows these metrics are called `Total Write Bytes Per Sec` and `Total Bytes Received Per Sec`. These list processes currently using the disk in b/s.

* **Memory forensics:** For Linux this metric is called `Used memory` and for Windows this metric is called `Used Physical Memory`. These list the top 10 processes and how much memory they use in %.

* **Network forensics:** For Linux these metrics are called `Outgoing traffic on all interfaces` and `Incoming traffic on all interfaces`, for Windows these metrics are called `Total Bytes Sent Per Sec` and `Total Bytes Received Per Sec`. These list processes currently sending or receiving network traffic in b/s.

{% include alert.html type="info" text="Take a look at your &quot;Server Metrics&quot; dashboard, we configured all process forensics for you there." %}

### Http requests

There are also 2 flavors of http forensics:

* **Latency forensics:** These forensics will only show up in the "Web request latency" widget and will show you the slowest pages and the latency for a couple of samples. Each sample also contains the complete logline of your webserver.

* **Error forensics:** These forensics will only show up in the "web request error" widget and will show you the pages with the most errors and which error code it returned. Only 5xx status codes are considered errors.

{% include alert.html type="info" text="Take a look at your &quot;HTTP Backend&quot; dashboard, we configured all HTTP forensics for you there." %}