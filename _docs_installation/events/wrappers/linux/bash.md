---
layout: page
title: Bash script wrapper
---

<a href="https://github.com/CoScale/coscale-commandwrapper-script" target="_blank" class="btn btn-large btn-info"><i class="fa fa-3x fa-fw fa-github-square"></i> Github repository</a>

## Prerequisite
* Configured CoScale CLI

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
`sh ./coscale-cron.sh --cli /opt/coscale/coscale-cli --category "System cron" --name "Cache clean-up" --live -- rm -rf /var/cache/website/*`

### Ping a production server 5 times
`sh ./coscale-cron.sh --cli /opt/coscale/coscale-cli --category "Monitoring" --name "Ping production" --live -- ping -n 5 \"http://production.com\"`
