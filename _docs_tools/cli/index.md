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

## [Installation and Configuration]({{ site.baseurl }}/installation/cli/installation/)

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

Adding a CoScale event category with custom attributes exitCode and executionTime (in seconds).

`./coscale-cli event new --name "Example category" --attributeDescriptions "[{\"name\":\"exitCode\", \"type\":\"integer\"}, {\"name\":\"executionTime\", \"type\":\"integer\", \"unit\":\"s\"}]"`

Adding a CoScale event to "Example category" with name 'Event example', exitCode '0' and an executionTime of 10 seconds.

`./coscale-cli event data --name "Example category" --message "Event example" --subject "a" --attribute "{\"exitCode\":0, \"executionTime\":10}"`
