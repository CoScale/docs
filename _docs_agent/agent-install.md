---
layout: page
title: Agent install
description: Installing the CoScale agent on Linux.
---

Installing the CoScale agent depends a lot on your environment and if it's a container or non-container environment. Below you can find several examples of the install commands. **It is advised to always copy the commands from your CoScale application interface!**

## Unix

* Debian, Ubuntu: `sudo dpkg -i coscale-agent.deb`
* RedHat, CentOS: `sudo rpm -iUvh coscale-agent.rpm`

## Microsoft Windows

To install this agent, download the agent to your server and double click on the installer. Follow the instructions.

## Kubernetes

Kubernetes monitoring is done through a DaemonSet and a ReplicaSet in a private `coscale` namespace. The right permissions need to be given to the CoScale agent in RBAC environments. The DaemonSet agent is responsible for container, application and node monitoring. The ReplicaSet retrieves orchestration data from the active Kubernetes master.

{% highlight bash %}
kubectl create namespace coscale
{% endhighlight %}

{% highlight yaml %}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: coscale-agent
  namespace: coscale
{% endhighlight %}

{% highlight yaml %}
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRole
metadata:
  annotations:
    rbac.authorization.kubernetes.io/autoupdate: "true"
  labels:
    kubernetes.io/bootstrapping: rbac-defaults
  name: coscale-cluster-role
rules:
- apiGroups:
  - '*'
  resources:
  - '*'
  verbs:
  - get
  - list
  - watch
- nonResourceURLs:
  - '*'
  verbs:
  - get
  - list
  - watch
{% endhighlight %}

{% highlight yaml %}
apiVersion: extensions/v1beta1
kind: ReplicaSet
metadata:
  labels:
    name: coscale-agent-kubernetes-master
  name: coscale-agent-kubernetes-master
  namespace: coscale
spec:
  replicas: 1
  template:
    metadata:
      labels:
        name: coscale-agent-kubernetes-master
    spec:
      serviceAccountName: coscale-agent
      tolerations:
        - operator: "Exists"
      containers:
      - image: coscale/coscale-agent:latest
        imagePullPolicy: Always
        name: coscale-agent
        env:
        - name: APP_ID
          value: "xxxx"
        - name: ACCESS_TOKEN
          value: "xxxx"
        - name: TEMPLATE_ID
          value: "xxxx"
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
---
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  labels:
    name: coscale-agent
  name: coscale-agent
  namespace: coscale
spec:
  template:
    metadata:
      labels:
        name: coscale-agent
    spec:
      hostNetwork: true
      serviceAccountName: coscale-agent
      tolerations:
        - operator: "Exists"
      containers:
      - image: coscale/coscale-agent
        securityContext:
          privileged: true
        imagePullPolicy: Always
        name: coscale-agent
        env:
        - name: APP_ID
          value: "xxxx"
        - name: ACCESS_TOKEN
          value: "xxxx"
        - name: TEMPLATE_ID
          value: "xxxx"
        - name: COSCALE_KUBE_NODE_ONLY
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

## Openshift

Openshift monitoring is done through a DaemonSet and a ReplicaSet in a private `coscale` namespace. The right permissions need to be given to the CoScale agent in Openshift environments using a SecurityContextConstraints, without this our agent cannot communicate with the Openshift platform. The DaemonSet agent is responsible for container, application and node monitoring. The ReplicaSet retrieves orchestration data from the active Openshift master.

{% highlight yaml %}
apiVersion: v1
kind: SecurityContextConstraints
allowHostDirVolumePlugin: true
allowHostIPC: false
allowHostNetwork: true
allowHostPID: false
allowHostPorts: false
allowPrivilegedContainer: true
allowedCapabilities: null
defaultAddCapabilities: null
fsGroup:
  type: MustRunAs
groups:
- system:cluster-admins
metadata:
  name: coscale-scc
priority: null
readOnlyRootFilesystem: false
requiredDropCapabilities: null
runAsUser:
  type: RunAsAny
seLinuxContext:
  type: RunAsAny
supplementalGroups:
  type: RunAsAny
volumes:
- '*'
{% endhighlight %}

{% highlight bash %}
oadm new-project coscale --node-selector=""
oc project coscale
oc create serviceaccount coscale
oadm policy add-cluster-role-to-user cluster-admin system:serviceaccount:coscale:coscale
oadm policy add-scc-to-user coscale-scc system:serviceaccount:coscale:coscale
{% endhighlight %}

{% highlight yaml %}
apiVersion: v1
kind: ReplicationController
metadata:
  labels:
    name: coscale-agent-kubernetes-master
  name: coscale-agent-kubernetes-master
  namespace: coscale
spec:
  replicas: 1
  template:
    metadata:
      labels:
        name: coscale-agent-kubernetes-master
    spec:
      serviceAccount: coscale
      containers:
      - image: coscale/coscale-agent:latest
        imagePullPolicy: Always
        name: coscale-agent
        env:
        - name: APP_ID
          value: "xxxx"
        - name: ACCESS_TOKEN
          value: "xxxx"
        - name: TEMPLATE_ID
          value: "xxxx"
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
---
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
      serviceAccount: coscale
      hostNetwork: true
      containers:
      - image: coscale/coscale-agent
        imagePullPolicy: Always
        name: coscale-agent
        securityContext:
          privileged: true
        env:
        - name: APP_ID
          value: "xxxx"
        - name: ACCESS_TOKEN
          value: "xxxx"
        - name: TEMPLATE_ID
          value: "xxxx"
        - name: COSCALE_KUBE_NODE_ONLY
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
