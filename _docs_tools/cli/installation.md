---
layout: page
title: CLI Installation
description: Instructions on how to install the CoScale command line interface.
---

To install the CoScale command line interface we provide three different methods. You can:

* [Install the agent]({{ site.baseurl}}/agent/install) which will download the CLI tool automatically
* [Download the binary](#download-binary) by using our install script. This method is advised as it requires no additional software installed.
* [Use Docker image](#docker-container) that is available on Docker Hub.
* [Compile from scratch](#compile-yourself) with the <a href="https://golang.org/" target="_BLANK">golang</a> compiler.

## Docker Container

We have a Docker image available with the CoScale-CLI. You can find it on [Docker Hub](https://hub.docker.com/r/coscale/cli/).

To use, run `docker run coscale/cli [your command] --app-id=[application_id] --access-token=[accesstoken]`. 

Make sure to replace `[your command]`, `[application_id]` and `[accesstoken]` with the required values. You can find the application id and the access token in your CoScale dashboard. For the command you can leave it empty and you will get a description of all the possible options.

Example:  
`docker run coscale/cli server list --app-id=000abcde-3e82-43ab-8456-3e269492a7a2 --access-token=d9aff8be-201a-4907-a9a4-aa712358406f`


## Host installation

{% include alert.html type="warning" text="You need root/sudo access to install the CoScale CLI." %}

### Download binary

#### Linux

Use the following one-liner to install the CoScale CLI on Linux in /opt/coscale/cli.

`bash -c "eval $(curl -L https://raw.githubusercontent.com/CoScale/coscale-cli/master/install.sh)"`

You are now ready to use our CLI tool, try executing the command `coscale-cli`.

<small>The script should work on most UNIX based operating systems, if you experience any problems <a href="mailto:support@coscale.com" class="js-support">contact our support</a> and they will assist you further.</small>


#### Windows

Visit the CoScale Cli github [latest release](https://github.com/CoScale/coscale-cli/releases/latest) and download the attached `coscale-cli.exe` binary.

Once downloaded you can use our CLI tool by executing `coscale-cli` in the same folder as the download.  
Add the location of our CLI tool to your PATH variable to run it from anywhere.


#### Mac OS X

Mac OS X is currently not supported, please contact our support for more information.

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

Run `coscale-cli event list`, it should return a json array. If it returns the CLI help, <a href="mailto:info@coscale.com" class="js-support">contact support</a>.
