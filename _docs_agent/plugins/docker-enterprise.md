---
layout: page
title: Docker Orchestration plugin
description: Information on the metrics collected by the CoScale Docker Swarm plugin.
---

> Docker Enterprise Edition (EE) 2.0 is the only enterprise-ready container platform that enables IT leaders to choose how to cost-effectively build and manage their entire application portfolio at their own pace, without fear of architecture and infrastructure lock-in. Docker’s container platform enables organizations to accelerate digital and multi-cloud initiatives by automating the delivery of legacy and modern applications using an agile operating model with integrated security. Because Docker EE includes services, support and training, organizations have a complete containerization strategy for supporting an ever-changing business environment.

More information on: [https://www.docker.com/enterprise-edition](https://www.docker.com/enterprise-edition). **This plugin also supports Docker Swarm.**

## How it works

This plugin retrieves data from the Docker Swarm API on the distribution of containers, active services, node status, and failed tasks. The Docker API is exposed by default and no additional configuration is required.

## Installation

{% include_relative _installation.md orchestrator="true" %}

## Events

* When node is draining
* When services change their desired replicas count
* When tasks start/stop
* When a service doesn't have enough actual replicas

## Metrics

| Metric name                                           | Metric unit |
|-------------------------------------------------------|-------------|
| Docker Swarm number of desired replicas for service X | #           |
| Docker Swarm number of failed nodes                   | #           |
| Docker Swarm number of failed tasks for service X     | #           |
| Docker Swarm number of nodes                          | #           |
| Docker Swarm number of running tasks for service X    | #           |
| Docker Swarm number of running tasks on node Y        | #           |
| Docker Swarm number of services                       | #           |
| Docker Swarm total number of failed tasks             | #           |
| Docker Swarm total number of running tasks            | #           |

**X** is replaced by service name

**Y** is replaced by node hostname
