---
layout: page
title: Kubernetes plugin
description: Information on the metrics collected by the CoScale Kubernetes plugin.
---

> Kubernetes is an open-source system for automating deployment, scaling, and management of containerized applications.

More information on: [http://kubernetes.io/](http://kubernetes.io/)

## Events

* Container ready: Events generated when containers change their readiness status
* Container running: Events generated when containers start
* Deployment:	Events generated when a deployment is started
* Kubernetes event:	Internal Kubernetes events
* Node draining:	Events generated when a node is draining
* Node ready:	Events generated when nodes change their readiness status
* Replica set scaling:	Events generated when replica sets change their desired replicas count
* Replication controller scaling	Events generated when replication controllers change their desired replicas count
* Too few replicas:	Events generated when a replication controller/replica set doesn't have enough actual replicas

## Metrics

### Containers

| Metric name                                                 | Metric unit |
|-------------------------------------------------------      |-------------|
| Kubernetes container cpu system time                        | %           |
| Kubernetes container cpu time                               | %           |
| Kubernetes container cpu user time                          | %           |
| Kubernetes container logs storage usage                     | b           |
| Kubernetes container memory usage bytes                     | b           |
| Kubernetes container memory working set bytes               | b           |
| Kubernetes container network receive errors total           | #           |
| Kubernetes container network receive packets dropped total  | #           |
| Kubernetes container network receive packets total          | #           |
| Kubernetes container network receive rate                   | b/s         |
| Kubernetes container network transmit errors total          | #           |
| Kubernetes container network transmit packets dropped total | #           |
| Kubernetes container network transmit packets total         | #           |
| Kubernetes container pgfault memory failures total          | #           |
| Kubernetes container pgmajfault memory failures total       | #           |
| Kubernetes container rootfs usage                           | b           |
| Kubernetes restart count for container                      | #           |
| Kubernetes run time for container                           | s           |

### Master

| Metric name                                                                       | Metric unit |
|-----------------------------------------------------------------------------------|-------------|
| Kubernetes number of containers                                                   | #           |
| Kubernetes number of sets                                                         | #           |
| Kubernetes number of jobs                                                         | #           |
| Kubernetes number of nodes                                                        | #           |
| Kubernetes number of podTemplates                                                 | #           |
| Kubernetes number of pods                                                         | #           |
| Kubernetes number of ready containers                                             | #           |
| Kubernetes number of ready nodes                                                  | #           |
| Kubernetes number of replica sets                                                 | #           |
| Kubernetes number of replication controllers                                      | #           |
| Kubernetes number of running containers                                           | #           |
| Kubernetes number of running jobs                                                 | #           |
| Kubernetes number of running pods                                                 | #           |
| Kubernetes number of running services                                             | #           |
| Kubernetes number of successful jobs                                              | #           |
| Persistent volume claims: Kubernetes number of bound persistent volumes claims    | #           |
| Persistent volume claims: Kubernetes number of pending persistent volumes claims  | #           |
| Persistent volume claims: Kubernetes number of persistent volumes claims          | #           |
| Persistent volumes: Kubernetes number of bound persistent volumes                 | #           |
| Persistent volumes: Kubernetes number of failed persistent volumes                | #           |
| Persistent volumes: Kubernetes number of persistent volumes                       | #           |
| Persistent volumes: Kubernetes number of released persistent volumes              | #           |
| Pods                                                                              | #           |
| Kubernetes number of containers in default namespace                              | #           |
| Kubernetes number of daemon sets in default namespace                             | #           |
| Kubernetes number of pods in default namespace                                    | #           |
| Kubernetes number of pods templates in default namespace                          | #           |
| Kubernetes number of ready containers in default namespace                        | #           |
| Kubernetes number of replica sets in default namespace                            | #           |
| Kubernetes number of replication controllers in default namespace                 | #           |
| Kubernetes number of running containers in default namespace                      | #           |
| Kubernetes number of services in default namespace                                | #           |
| kube-system: Kubernetes number of containers in kube-system namespace             | #           |
| kube-system: Kubernetes number of daemon sets in kube-system namespace            | #           |
| kube-system: Kubernetes number of pods in kube-system namespace                   | #           |
| kube-system: Kubernetes number of pods templates in kube-system namespace         | #           |
| kube-system: Kubernetes number of ready containers in kube-system namespace       | #           |
| kube-system: Kubernetes number of replica sets in kube-system namespace           | #           |
| kube-system: Kubernetes number of replication controllers in kube-system namespace| #           |
| kube-system: Kubernetes number of running containers in kube-system namespace     | #           |
| kube-system: Kubernetes number of services in kube-system namespace               | #           |
| kube-system: Replica sets                                                         | #           |
| kube-system: Replication controllers                                              | #           |
| kube-system: Services                                                             | #           |


### Node

| Metric name                                                            | Metric unit |
|------------------------------------------------------------------------|-------------|
| Kubernetes node create pod operation count                             | #           |
| Kubernetes node create pod operation latency sum                       | s           |
| Kubernetes node docker create container operation count                | #           |
| Kubernetes node docker create container operation latency sum          | s           |
| Kubernetes node docker info operation count                            | #           |
| Kubernetes node docker info operation latency sum                      | s           |
| Kubernetes node docker inspect container operation count               | #           |
| Kubernetes node docker inspect container operation latency sum         | s           |
| Kubernetes node docker inspect image operation count                   | #           |
| Kubernetes node docker inspect image operation latency sum             | s           |
| Kubernetes node docker list containers operation count                 | #           |
| Kubernetes node docker list containers operation latency sum           | s           |
| Kubernetes node docker list images operation count                     | #           |
| Kubernetes node docker list images operation latency sum               | s           |
| Kubernetes node docker pull image operation count                      | #           |
| Kubernetes node docker pull image operation latency sum                | s           |
| Kubernetes node docker remove container operation count                | #           |
| Kubernetes node docker remove container operation latency sum          | s           |
| Kubernetes node docker start container operation count                 | #           |
| Kubernetes node docker start container operation latency sum           | s           |
| Kubernetes node docker stop container operation count                  | #           |
| Kubernetes node docker stop container operation latency sum            | s           |
| Kubernetes node number of pods                                         | #           |
| Kubernetes node number of running containers                           | #           |
| Kubernetes node sync pod operation count                               | #           |
| Kubernetes node sync pod operation latency sum                         | s           |


You can find an example for installing CoScale agent with Kubernetes Daemon Set here: [https://gist.github.com/kidk/53798512dc67c6c85534496ca3e708dc](https://gist.github.com/kidk/53798512dc67c6c85534496ca3e708dc)
