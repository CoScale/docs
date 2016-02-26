---
layout: page
title: Magento plugin
description: Information on how to install the Magento plugin and the metrics collected by the CoScale Magento plugin.
---

## How it works.
This plugin connects to the [CoScale Magento extension](https://www.magentocommerce.com/magento-connect/coscale-performance-business-monitoring.html) to gather important metrics and events from Magento.

The metrics contain business metrics, such as the number of products, orders, abondoned carts, but also technical metrics such as Magento caching metrics. The events contain Magento admin actions such as page cache flushes, reindexing, etc.

{% include alert.html type="warning" text="The CoScale Magento extension is still in BETA and should be used with caution on production systems. <a href=\"mailto:info@coscale.com\" class=\"js-support\">contact support</a> for more information" %}

## Installing the Magento CoScale extension.
Magento requires an extension in order to expose metrics to the CoScale platform. This extension can be added through Magento Connect.

* Visit the [Coscale Magento Connect extension store page](https://www.magentocommerce.com/magento-connect/coscale-performance-business-monitoring.html) and click "Install Now" for the CoScale Performance & Business monitoring plugin. Read and agree to the extension lisence agreement and click the "Get Extension Key" button.

  <img src="/gfx/agent/plugins/magento/getExtensionKey.png" alt="Magento Connect link">

* Select and copy the key.

* Navigate to the Magento Connect Manager.

  <img src="/gfx/agent/plugins/magento/magentoConnect.png" alt="Magento Connect link">

* Paste the key you copied in the previous steps, click install and continue the installation. The Magento extension should now be installed.

* Continue to the "Configuration" page to setup the plugin.

  <img src="/gfx/agent/plugins/magento/configuration.jpg" alt="Magento configuration link">

* Click "system" in the sidebar on the left.

  <img src="/gfx/agent/plugins/magento/system.jpg" alt="Magento system link">

* In "CoScale monitoring" you can enable or disable the extension.

  <img src="/gfx/agent/plugins/magento/CoScaleMonitoring.jpg" alt="CoScale monitoring">

* Configure a CoScale agent with the Magento plugin and install it on your Magento servers.


## Collected metrics.

|                  Metric name                    |       Metric unit       |
|-------------------------------------------------|-------------------------|
| "Magento %s Customers"                          |  Customers              |
| Magento Files in var/report/                    | files                   |
| Magento Logfile var/log/%s                      |  b                      |
| Magento %s New Order size total                 |  items                  |
| Magento %s Order size average                   |  items                  |
| Magento %s New Order amount total               |  #                      |
| Magento %s Order amount average                 |  #                      |
| Magento %s Total New Orders                     |  orders                 |
| Magento %s Order size total                     |  items                  |
| Magento %s Order size total average             |  items                  |
| Magento %s Order amount total                   |  #                      |
| Magento %s Order amount total average           |  #                      |
| Magento %s Orders                               |  orders                 |
| Magento %s Orders new                           |  orders                 |
| Magento %s Orders processing                    |  orders                 |
| Magento %s Orders completed                     |  orders                 |
| Magento %s Abandonned carts                     |  cart                   |
| Magento Amount of messages in the e-mail queue  |  messages               |
| Magento Products                                |  orders                 |
| Magento New products today                      |  prods                  |
| Magento Categories                              |  cat                    |
| Magento New categories today                    |  cat                    |
| Magento %s URL Rewrites                         |  rewrites               |
| Magento %s Total value of abandoned carts       |  #                      |
| Magento %s Orders pending pick/pack             |  orders                 |
| Magento %s Orders pick/pac                      |  orders                 |
| Magento %s Orders completed pick/pack           |  orders                 |
| Magento %s Picked qty                           |  qty                    |
| Magento %s Picked time                          |  s                      |
| Magento %s Avg time pick/pack                   |   s                     |
| Magento %s Time pending pick/pack               |  s                      |
| Magento %s Time current pick/pack               |  s                      |
| Magento %s Total orders processing              |  orders                 |
| Magento %s Total orders completed               |  orders                 |
| Magento %s Total orders                         |  orders                 |
| agento %s Total orders new                      |  orders                 |
| Magento %s Total orders today                   |  orders                 |
| Magento %s New customers today                  |  customers              |
