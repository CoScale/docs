---
layout: page
title: Magento plugin
description: Information on how to install the Magento plugin and the metrics collected by the CoScale Magento plugin.
---

>  Magento is the eCommerce software and platform trusted by the world's leading brands. Recognized as the leading eCommerce platform to the 2015 Internet Retailer Top 1000, B2B 300 and Hot 100 lists, Magento Commerce works hand in hand with retailers, brands and branded manufacturers across B2C and B2B industries to successfully integrate digital and physical shopping experiences. In addition to its flagship open source eCommerce platform, Magento Commerce boasts a strong portfolio of cloud-based omnichannel solutions including in-store, retail associate and order management technologies. Magento Commerce is supported by a vast global network of 300+ solution and technology partners and by a highly active global community of more than 66,000 developers as well as the largest eCommerce marketplace for extensions available for download on the Magento Marketplace. 

More information on: [http://www.magento.com/](http://www.magento.com/)

## How it works
This plugin connects to the [CoScale Magento extension](https://www.magentocommerce.com/magento-connect/coscale-performance-business-monitoring.html) to gather important metrics and events from Magento.

The metrics contain business metrics, such as the number of products, orders, abondoned carts, but also technical metrics such as Magento caching metrics. The events contain Magento admin actions such as page cache flushes, reindexing, etc.

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

| Metric name                                                                     | Metric unit |
|---------------------------------------------------------------------------------|-------------|
| Magento %s The total number of customers in the system                          | customers   |
| Magento %s Abandonned carts                                                     | cart        |
| Magento %s Avg time to pick/pack an order                                       | s           |
| Magento %s New customers today                                                  |             |
| Magento %s The average amount of an order in the system for this store          | #           |
| Magento %s The average amount of orders since last collect for this store       | #           |
| Magento %s The average size of an order in the system for this store            | items       |
| Magento %s The average size of orders since last collect for this store         | items       |
| Magento %s The qty of orders picked                                             |             |
| Magento %s The total amount of an order in the system for this store            | #           |
| Magento %s The total amount of orders since last collect for this store         | #           |
| Magento %s The total number of orders in canceled state                         | orders      |
| Magento %s The total number of orders in completed pick/pack state              | orders      |
| Magento %s The total number of orders in completed state                        | orders      |
| Magento %s The total number of orders in completed state                        |             |
| Magento %s The total number of orders in new state                              | orders      |
| Magento %s The total number of orders in new state                              |             |
| Magento %s The total number of orders in pick/pack state                        |             |
| Magento %s The total number of orders in processing state                       | orders      |
| Magento %s The total number of orders in processing state                       |             |
| Magento %s The total number of orders in the system for this store              | orders      |
| Magento %s The total number of orders in the system for this store              |             |
| Magento %s The total number of orders in waiting for pick/pack state            | orders      |
| Magento %s The total number of orders since last collect for this store         | orders      |
| Magento %s The total number of orders today                                     |             |
| Magento %s The total number of pageviews for this store                         |             |
| Magento %s The total size of all order in the system for this store             | items       |
| Magento %s The total size of orders since last collect for this store           | items       |
| Magento %s The total time needed to pick/pack current orders in pick/pack state |             |
| Magento %s The total time needed to pick/pack new orders                        |             |
| Magento %s Total time to pick/pack                                              |             |
| Magento %s Total value of abandoned carts                                       |             |
| Magento %s URL Rewrites                                                         | rewrites    |
| Magento Amount of messages in the e-mail queue                                  | messages    |
| Magento Files in var/report/                                                    | files       |
| Magento Logfile var/log/%s                                                      | b           |
| Magento The total number of categories created today                            | cat         |
| Magento The total number of categories in the system                            | cat         |
| Magento The total number of products created today                              | prods       |
| Magento The total number of products in the system                              | prods       |
