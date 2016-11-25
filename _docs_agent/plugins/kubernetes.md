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

## Installation GCE

Google Container Engine requires a special setup for Kubernetes monitoring. We will create two agents, 1 for monitoring all minions and 1 for retrieving data from the Kubernetes master. We do this because GCE does not allow us to ssh into the Kubernetes master node.

### 1. Create an agent for your Kubernetes master. 

This agent will be configured to monitor the Kubernetes master. It should only contain the Kubernetes plugin configured with "Connect without authentication" and as a hostname the Kubernetes Master IP. 

The Master IP you can find on your local machine or the Kubernetes minions. `~/.kube/config | grep server` will return the IP address of the server. 

Finish the agent configuration and deploy it using the following Kubernetes config. Don't forget to replace `$APP_ID`, `$ACCESS_TOKEN` and `$TEMPLATE_ID` with the ones you find in the container deployment command.

{% highlight yaml %}
apiVersion: extensions/v1beta1
kind: ReplicaSet
metadata:
  labels:
    name: coscale-agent-kubernetes-master
  name: coscale-agent-kubernetes-master
spec:
  replicas: 1
  template:
    metadata:
      labels:
        name: coscale-agent-kubernetes-master
    spec:
      containers:
      - image: coscale/coscale-agent:latest
        imagePullPolicy: Always
        name: coscale-agent
        env:
        - name: APP_ID
          value: "$APP_ID"
        - name: ACCESS_TOKEN
          value: "$ACCESS_TOKEN"
        - name: TEMPLATE_ID
          value: "$TEMPLATE_ID"
        - name: COSCALE_KUBE_MON_MASTER
          value: "true"
        volumeMounts:
        - name: dockersocket
          mountPath: /var/run/docker.sock
        - name: hostroot
          mountPath: /host
          readOnly: true
      volumes:
      - hostPath:
          path: /var/run/docker.sock
        name: dockersocket
      - hostPath:
          path: /
        name: hostroot
{% endhighlight %}

### 2. Create an agent to monitor your Kubernets minions

This agent will be configured for deployment on all the minion machines. It should also contain the Kubernets plugin, configured in the same way as the agent for Master, but it also can contain any plugin you need to monitor the services on the minion machines. To start with, let's add the 'Resource plugin' and 'Docker plugin'. 

Finish the agent configuration and deploy it using the following Kubernetes config. Don't forget to replace `$APP_ID`, `$ACCESS_TOKEN` and `$TEMPLATE_ID` with the ones you find in the container deployment command.

{% highlight yaml %}
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  labels:
    name: coscale-agent
  name: coscale-agent
spec:
  template:
    metadata:
      labels:
        name: coscale-agent
    spec:
      hostNetwork: true    
      containers:
      - image: coscale/coscale-agent:latest
        imagePullPolicy: Always
        name: coscale-agent
        env:
        - name: APP_ID
          value: "$APP_ID"
        - name: ACCESS_TOKEN
          value: "$ACCESS_TOKEN"
        - name: TEMPLATE_ID
          value: "$TEMPLATE_ID"
        volumeMounts:
        - name: dockersocket
          mountPath: /var/run/docker.sock
        - name: hostroot
          mountPath: /host
          readOnly: true
      volumes:
      - hostPath:
          path: /var/run/docker.sock
        name: dockersocket
      - hostPath:
          path: /
        name: hostroot
{% endhighlight %}