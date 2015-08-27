---
layout: page
title: Bash script wrapper
---

<a href="https://github.com/CoScale/coscale-commandwrapper-script" target="_blank" class="btn btn-large btn-info"><i class="fa fa-3x fa-fw fa-github-square"></i> Github repository</a>

## Prerequisite
* [CoScale Command line tool]({{ site.baseurl }}/installation/cli/installation)

## Install

Get the <a target="_blank" href="https://github.com/CoScale/coscale-commandwrapper-script" class="js-github-release">latest release</a> and unzip.

or

Git clone repository:
`git clone https://github.com/CoScale/coscale-commandwrapper-script.git`.

## How to use

In this example we will use a script that pings our server 5 times.

1. Create a script for your job and add the commands you want to run

    `touch /root/cron/test-website.sh`

    `echo "ping -n 5 google.com" > /root/cron/test-website.sh`

2. Add to command to your cron service and put the CoScale cron wrapper in front of it. Don't forget to replace `[[category]]` and `[[name]]` with your own.

    `*/5 * * * * /root/coscale-commandwrapper-script/cron.sh --category "[[category]]" --name "[[name]]" --live -- /root/cron/test-website.sh`

## Arguments

argument | explanation
-------- | -----------
`--app_id` *optional*       | CoScale application id
`--app_token` *optional*    | CoScale token
`--cli`                     | CoScale CLI tool directory
`--name`                    | Name of the event
`--category`                | Category of the event
`--live`                    | Live switch, only use when you want to run command and send events, disable for testing
`--`                        | Everything after this argument will be read as the command you want to execute. Make sure you escape " and '.

## Notes
* Make sure to escape ' and " characters as they may cause problems.
* The command is always executed, even when CoScale services are having difficulties.
* Exit code from the script is the same as your command

## Examples

### Clean cache directory
`/root/coscale-commandwrapper-script/cron.sh --category "System cron" --name "Cache clean-up" --live -- rm -rf /var/cache/website/*`

### Ping a production server 5 times
`/root/coscale-commandwrapper-script/cron.sh --category "Monitoring" --name "Ping production" --live -- ping -n 5 google.com`
