---
layout: page
title: CLI Installation
---

To install the CoScale command line interface we provide two different methods. You can:

* [Download the binary](#download-binary) by using our install script. This method is advised as it requires no additional software installed.
* [Compile from scratch](#compile-yourself) with the <a href="https://golang.org/" target="_BLANK">golang</a> compiler.

{% include alert.html type="warning" text="You need root/sudo access to install the CoScale CLI." %}

## Prerequisite

* CoScale APP_ID and accessToken

## 1. Install

### Download binary

#### Linux

Use the following one-liner to install the CoScale CLI on Linux in /opt/coscale/cli.

`bash -c \"eval $(curl -L https://raw.githubusercontent.com/CoScale/coscale-cli/master/install.sh)\"`

You are now ready to use our CLI tool, try executing the command `coscale-cli`.

<small>The script should work on most UNIX based operating systems, if you experience any problems <a href="mailto:support@coscale.com" class="support">contact our support</a> and they will assist you further.</small>


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

# Create symlink
ln -v -s /opt/coscale/cli/coscale-cli /usr/bin/coscale-cli
{% endhighlight %}

## 2. Configure CLI
This will remove the need to pass along the app_id and accesstoken args everytime you can the `coscale-cli` command.

{% highlight bash %}
# Create config file, don't forget to replace [appId] and [accessToken] with your own
echo "{\"baseurl\":\"https://api.coscale.com\", \"appid\":\"[appId]\", \"accesstoken\":\"[accessToken]\"}" | gzip -c > /opt/coscale/cli/api.conf
{% endhighlight %}

## 3. Test if everything works

Run `coscale-cli event list`, it should return a json array. If it returns the CLI help, <a href="mailto:info@coscale.com" class="support">contact support</a>.
