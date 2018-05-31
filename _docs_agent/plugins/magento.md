---
layout: page
title: Monitoring and collecting data from Magento
description: Information on how to install the Magento plugin and the metrics collected by the CoScale Magento plugin.
---

>  Magento is the eCommerce software and platform trusted by the world's leading brands. Recognized as the leading eCommerce platform to the 2015 Internet Retailer Top 1000, B2B 300 and Hot 100 lists, Magento Commerce works hand in hand with retailers, brands and branded manufacturers across B2C and B2B industries to successfully integrate digital and physical shopping experiences. In addition to its flagship open source eCommerce platform, Magento Commerce boasts a strong portfolio of cloud-based omnichannel solutions including in-store, retail associate and order management technologies. Magento Commerce is supported by a vast global network of 300+ solution and technology partners and by a highly active global community of more than 66,000 developers as well as the largest eCommerce marketplace for extensions available for download on the Magento Marketplace.

More information on: [http://www.magento.com/](http://www.magento.com/)

## How it works

This plugin connects to the [CoScale Magento extension](https://www.magentocommerce.com/magento-connect/coscale-performance-business-monitoring.html) to gather important metrics and events from Magento.

The metrics contain business metrics, such as the number of products, orders, abondoned carts, but also technical metrics such as Magento caching metrics. The events contain Magento admin actions such as page cache flushes, reindexing, etc.

**The CoScale Magento plugin supports: 1.6.2.0, 1.7, 1.8, 1.8.1, 1.9, 1.9.1, 1.9.2**

### Installation

The CoScale Magento integration requires an extension in order to expose metrics to the CoScale platform. This extension can be added through Magento Connect.

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



<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/magento.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
