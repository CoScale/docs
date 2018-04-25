---
layout: page
title: Prometheus plugin
description: Information on the metrics collected by the CoScale Prometheus plugin.
---

> Prometheus implements a highly dimensional data model. Time series are identified by a metric name and a set of key-value pairs. By providing a Prometheus endpoint in your software CoScale can retrieve information, including the dimensions available.

More information on: [https://prometheus.io/](https://prometheus.io/)

## How it works

This plugin gathers metrics from a Prometheus endpoint. It parses the metrics and dimensions defined by the Prometheus endpoint and pushes them to CoScale.

## Installation

{% include_relative _installation.md orchestrator="false" service="Prometheus" %}

## Configuration

## Prometheus Connection

Provide one or multiple url's to the Prometheus endpoint available in your software. Prometheus has multiple [client libraries](https://prometheus.io/docs/instrumenting/clientlibs/) and [exporters/integrations](https://prometheus.io/docs/instrumenting/exporters/) to setup these endpoints.

## Metrics

The number and type of metrics depends on the definition on the Prometheus endpoint page.
