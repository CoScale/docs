---
layout: page
title: Pushing events from command line interface
description: Information on how to push events with the CoScale command line interface tool.
---

## Prerequisites

* [CoScale Command line tool]({{ site.baseurl }}/installation/cli/installation)

## Quick tutorial

To get started we first need to create a event category.

`coscale-cli event new --name "Marketing" --description "Marketing campaigns and ads"`

After we can add events to it

`event data --name "Marketing" --message "Start campaign: Focus on other products" --subject a`

You can add as many categories and events as you'd like and you can also include variables to customize your events.
