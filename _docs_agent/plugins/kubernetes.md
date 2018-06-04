---
layout: page
title: Monitoring and collecting data from Kubernetes
description: Information on the metrics collected by the CoScale Kubernetes plugin.
---

> Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.

More information on: [http://kubernetes.io/](http://kubernetes.io/)

## How it works

This plugin monitors your Kubernetes cluster.

It can give you information about your Kubernetes nodes status, services, containers, events and replication controllers.

## Installation

{% include_relative _installation.md orchestrator="true" service="Kubernetes" %}

## Configuration

Kubernetes provides multiple ways of connecting and retrieving metrics.

* Connect without authentication
* Connect using credentials (username, password)
* Connect using a token
* Connect with client certificate (administration certificate and key)

Kubernetes is configured by default without authentication. When additional credentials are required you can connect with username/password, token or client (X509) certificate. For more information about authentication you can go to [the Kubernetes docs](https://kubernetes.io/docs/admin/authentication/).


<!-- Auto generated metrics view -->
<div class="metrics">
{% capture my_include %}{% include plugins/kubernetes.md %}{% endcapture %}
{{ my_include | markdownify }}
</div>
