---
layout: page
title: CLI (command line interface)
description: Information on the CoScale command line interface with instructions for installation.
---

The CoScale command line interface is an interface to the CoScale API.

It provides easy to use methods for:

* Managing servers and server groups.
* Push metric groups, metrics and data.
* Register events and event categories.
* List, acknowledge and resolve your alerts.

## [Installation and Configuration]({{ site.baseurl }}/tools/cli/installation/)

## Usage
    coscale-cli a tool for CoScale Api.

    Usage:
    ./coscale-cli <object> <action> [--<field>='<data>']

    Actions for command "./coscale-cli":

    event
            event <action> [--<field>='<data>']
    server
            server <action> [--<field>='<data>']
    servergroup
            servergroup <action> [--<field>='<data>']
    metric
            metric <action> [--<field>='<data>']
    metricgroup
            metricgroup <action> [--<field>='<data>']
    data
            data <action> [--<field>='<data>']
    alert
            alert <action> [--<field>='<data>']
    check-config
            check-config is used to check to api configuration file


    The json objects are returned formatted by default, but can be returned on 1 line by using:
    --rawOutput

    By default the CoScale api credentials (authentication) will be taken from api.conf
    located in the same directory as the coscale-cli binary. If the file does not exist,
    the credentials can also be provided on the command line using:
    --api-url
        Base url for the api (optional, default = "https://api.coscale.com/").
    --app-id
        The application id.
    --access-token
        A valid access token for the given application.

    Use "coscale-cli [object] <help>" for more information about a command.

## Examples

#### Working with [events]({{ site.baseurl }}/events/index/)
Creating a basic CoScale event category called "Releases":

    ./coscale-cli event new --name "Releases"


Adding a CoScale event about to the "Releases" event category:

    ./coscale-cli event newdata --name "Releases" --message "V2.3.4" --subject "a"


Adding the current time as stoptime to the V2.3.4 release event. The dataid is the id that we got from newdata command.

    ./coscale-cli event updatedata --name "Releases" --dataid "4674066" --stopTime 0


Adding a second event about release V2.3.3 that happened on February first 2016.

    ./coscale-cli event newdata --name "Releases" --message "V2.3.3" --subject "a" --timestamp "1454328000" --stopTime "1454328000"


Creating a more advanced CoScale event category called "Daily backups". Each event we add will have extra attributes describing the size of the backup and the exitcode of our backup tool.

    ./coscale-cli event new --name "Daily backups" --description "All info about our daily backups" --attributeDescriptions '[{"name":"backup size","type":"integer","unit":"b"},{"name":"exitcode","type":"integer"}]'

Adding a backup event that started 1 hour ago, on server with id 4821, that was about 1 GB big and finished successfully. 

    ./coscale-cli event newdata --name "Daily backups" --message "backup on 1 Feb 2016" --subject "s4821" --timestamp -7200 --stopTime 0 --attribute '{"backup size":1000000000,"exitcode":0}'


#### Working with servers
Adding a server that will not run a CoScale agent, but can be used to attach events to.

    ./coscale-cli server new --name "cron server" --description "Server that that runs cron jobs"


#### Working with alerts
Viewing all unresolved alerts.

    ./coscale-cli alert list --filter unresolved

Resolving an alert from the list. The id is the id of an alert we got from the list command.

    ./coscale-cli alert resolve --id 347482

