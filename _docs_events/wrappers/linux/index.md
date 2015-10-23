---
layout: page
title: Linux script wrapper
description: Information on how to install the CoScale cron wrapper to monitor the performance of your crons.
---

## Prerequisite
* [CoScale CLI installed]({{ site.baseurl }}/tools/cli/installation/)

    Note: The CoScale CLI is automatically installed by the agent

## Install

{% highlight bash %}
# You can always choose another directory, just make sure you enter the correct path in the examples
cd /opt/coscale/

# Download the latest version from Github
wget https://raw.githubusercontent.com/CoScale/coscale-commandwrapper-script/master/cron.sh

# Allow users to access the file
chmod +rwxrwxrwx /opt/coscale/cron.sh
{% endhighlight %}

## How to use

In this example we will use a script that pings our server 5 times.

1. Create a script for your job and add the commands you want to run

    `touch /home/testuser/test-website.sh`

    `echo "ping -n 5 google.com" > /home/testuser/test-website.sh`

    `chmod +x /home/testuser/test-website.sh`

2. Add to command to your crontab (`crontab -e`) and put the CoScale cron wrapper in front of it. Don't forget to replace `[[category]]` and `[[name]]` with your own.

    `*/5 * * * * /opt/coscale/cron.sh --category "[[category]]" --name "[[name]]" --live -- /home/testuser/test-website.sh`

Your crontab might look something like this:

{% highlight bash %}
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command

*/5 * * * * /opt/coscale/cron.sh --category "Monitoring website" --name "ping" --live -- /home/testuser/test-website.sh

# Other examples
*/5 * * * * /opt/coscale/cron.sh --category "Monitoring" --name "Ping production" --live -- ping -c 5 google.com  
*/5 * * * * /opt/coscale/cron.sh --category "Monitoring" --name "Ping production" --live -- /root/test-website-job.sh
*/5 * * * * /root/test-website.sh

*/5 * * * * /opt/coscale/cron.sh --category "Monitoring" --name "Ping production" --live -- ping -c 5 google.com  
*/5 * * * * /opt/coscale/cron.sh --category "Monitoring" --name "Ping production" --live -- /home/testuser/test-website-job2.sh
*/5 * * * * /home/testuser/test-website2.sh

{% endhighlight %}

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

### Ping a production server 5 times
`/opt/coscale/cron.sh --category "Monitoring" --name "Ping production" --live -- ping -c 5 google.com`

### Clean cache directory
`/opt/coscale/cron.sh --category "System cron" --name "Cache clean-up" --live -- rm -rf /tmp/cache/website/*`
