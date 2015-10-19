---
layout: page
title: StatsD installation
description: Installation of StatsD daemon.
---

This guide will help you install the StatsD daemon on a Debian based operating system. We start by generating a package for your operating system and then install the package.

## Installation

{% highlight bash %}
# Install required packages
sudo apt-get update
sudo apt-get install git nodejs devscripts debhelper npm

# Create directory for installation
mkdir ~/build
cd ~/build

# Clone StatsD github repository
git clone https://github.com/etsy/statsd.git
cd statsd

# Generate Debian package for installation
dpkg-buildpackage

# Install package
cd ..
sudo dpkg -i statsd*.deb

{% endhighlight %}

StatsD is now installed, you can now [install the CoScale StatsD plugin]({{ site.baseurl }}/custom-metrics/statsd/index) to push your metrics to our application.
