---
layout: page
title: Bash script wrapper
---

## Prerequisite
* [Command line tool]({{ site.baseurl }}/installation/cli/installation)

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

2. Add to command to your cron service and put the CoScale cron wrapper in front of it. Don't forget to replace `[[category]]` and `[[name]]` with your own.

    `*/5 * * * * sudo -u testuser /opt/coscale/cron.sh --category "[[category]]" --name "[[name]]" --live -- /home/testuser/test-website.sh`

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
`sudo -u testuser /opt/coscale/cron.sh --category "Monitoring" --name "Ping production" --live -- ping -c 5 google.com`

### Clean cache directory
`sudo -u testuser /opt/coscale/cron.sh --category "System cron" --name "Cache clean-up" --live -- rm -rf /tmp/cache/website/*`
