---
layout: page
title: Docker Swarm plugin
description: Information on the metrics collected by the CoScale Docker Swarm plugin.
---

> Docker Swarm is native clustering for Docker. It turns a pool of Docker hosts into a single, virtual Docker host. Because Docker Swarm serves the standard Docker API, any tool that already communicates with a Docker daemon can use Swarm to transparently scale to multiple hosts.

More information on: [https://docs.docker.com/swarm/overview/](https://docs.docker.com/swarm/overview/)

## How it works

This plugin retrieves data from the Docker Swarm API on the distribution of containers, active services, node status, and failed tasks. The Docker API is exposed by default and no additional configuration is required.

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
