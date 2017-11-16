---
layout: page
title: Calico plugin
description: Information on the metrics collected by the CoScale Calico plugin.
---

> Free and open source, Project Calico is designed to simplify, scale, and secure cloud networks. Calico provides secure network connectivity for containers and virtual machine workloads. Calico creates and manages a flat layer 3 network, assigning each workload a fully routable IP address. Workloads can communicate without IP encapsulation or network address translation for bare metal performance, easier troubleshooting, and better interoperability. In environments that require an overlay, Calico uses IP-in-IP tunneling or can work with other overlay networking such as flannel.

More information on: [https://www.projectcalico.org](https://www.projectcalico.org)

## How it works

The core Calico component is Felix. Felix exposes metrics through a Prometheus endpoint. This plugin gathers Calico metrics from the Felix metrics endpoint, parses the metrics and pushes them to CoScale.

## Configuration

The list of endpoints exposing Calico metrics is required.

## Metrics

Depends on the exposed metrics.
