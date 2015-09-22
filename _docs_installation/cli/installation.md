---
layout: page
title: CLI Installation
---

To install the CoScale command line interface we provide two different methods. The first method is to [download a binary](#download-binary) provided by CoScale and copy it to the right location. This method is advised as it requires no additional software installed. The other method is to [compile the tool](#compile-yourself) yourself. To complete the installation, you can [create a config file](#configure-cli) that will remove the need to enter app_id and accessToken every time you use the tool.

{% include alert.html type="warning" text="You need root/sudo access." %}

## Prerequisite

* CoScale APP_ID and accessToken

## 1. Install

### Download binary

#### Linux

Follow this guide to install the CoScale CLI on Linux. It should work on most operating systems, if you experience any problems contact our support and they will assist you further.


{% highlight bash %}
# Create CoScale CLI dir
mkdir -p /opt/coscale/cli

# Download CLI into dir
cd /opt/coscale/cli
curl -L https://github.com/CoScale/coscale-cli/releases/download/0.1/coscale-cli-linux > coscale-cli
chmod +x coscale-cli

# Add dir to $PATH
echo "export PATH=\"${PATH}:/opt/coscale/cli\"" >> /root/.bashrc
source /root/.bashrc

{% endhighlight %}

#### Windows / Mac OS X

These are currently not supported, please contact our support for more information.

### Compile yourself

#### Linux / Mac OS X

Follow this guide to compile the CoScale cli on your system.

{% highlight bash %}
# Get latest sourcecode (you need to have git installed)
git clone https://github.com/CoScale/coscale-cli.git

# Make sure you have Golang installed. https://golang.org/doc/install
go version

# Go to dir
cd coscale-cli

# Build
sh build.sh

# Create CoScale CLI dir
mkdir -p /opt/coscale/cli

# Copy CLI into dir
cp bin/coscale-cli /opt/coscale/cli

# Add dir to $PATH
echo "export PATH=\"${PATH}:/opt/coscale/cli\"" >> /root/.bashrc
{% endhighlight %}

## 2. Configure CLI
This will remove the need to pass along the app_id and accesstoken args everytime you can the `coscale-cli` command.

{% highlight bash %}
# Create config file, don't forget to replace [appId] and [accessToken] with your own
echo "{\"baseurl\":\"https://api.coscale.com\", \"appid\":\"[appId]\", \"accesstoken\":\"[accessToken]\"}" | gzip -c > /opt/coscale/cli/api.conf
{% endhighlight %}

## 3. Test if everything works

Run `coscale-cli event list`, it should return a json array. If it returns the CLI help, <a href="#" class="support">contact support</a>.
