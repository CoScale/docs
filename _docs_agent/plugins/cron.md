---
layout: page
title: Cron plugin
description: Information on how to install the cron plugin and the events collected by the CoScale Cron plugin.
---

## How it works
The cron plugin will parse your cron logs and insert them as [events]({{ site.baseurl }}/events/index/) into CoScale.
The event is called "Cron plugin event". For every cron job that runs on your server we log the following data:

 * Start time
 * Stop time
 * command executed
 * exit code
 * execution time
 * user
 * last 50 lines of output in case the exit code was not equal to 0.

There is also a [wrapper script]({{ site.baseurl }}/events/wrappers/linux/index/) available that gives more fine control over the event name and attributes, but misses the output functionality and requires some manual work to set up.

## Prerequisite
* [CoScale Agent installed]({{ site.baseurl }}/agent/index)

## Configuration

### Enabling cron logs
This is done by uncommenting the `cron.*` line in `/etc/rsyslog.d/50-default.conf`

	cron.*                         /var/log/cron.log

Restart the **rsyslog** service.

### Increasing the log level
By default only the start of a cron job is logged. The log level has to be increased for the plugin to work correctly.

| Level |                  Description                   |
|--------------------------------------------------------|
|   1   | The start time of all cron jobs is logged.     |
|   2   | The stop time of all cron  jobs is logged.     |
|   4   | Failed jobs (exit code != 0) are logged.       |
|   8   | The process number of all cron jobs is logged. |

Edit `/etc/init/cron.conf` and add the loglevel to the `exec cron` line.

	exec cron -L 15

Restart the **cron** service.

### Installing the plugin
The cron plugin only needs the path of your cron log. This is `/var/log/cron.log` by default.
