---
layout: page
title: Monitoring and collecting data from Azure
description: Information on the metrics collected by the CoScale Azureh plugin.
---

> Microsoft Azure is a growing collection of integrated cloud services that developers and IT professionals use to build, deploy, and manage applications through our global network of datacenters. With Azure, you get the freedom to build and deploy wherever you want, using the tools, applications, and frameworks of your choice. Azure supports a broad selection of operating systems, programming languages, frameworks, databases, and devices.

More information on: [https://azure.microsoft.com](https://azure.microsoft.com)

## Installation

{% include_relative _thirdparty.md %}


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/azure.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
