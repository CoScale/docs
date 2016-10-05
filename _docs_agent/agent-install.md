---
layout: page
title: Agent install
description: Installing the CoScale agent on Linux.
---

To install the CoScale agent on your system, download the agent and run the following commands.

## Unix

* Debian, Ubuntu: `sudo dpkg -i coscale-agent.deb`
* RedHat, CentOS: `sudo rpm -iUvh coscale-agent.rpm`

## Microsoft Windows

To install this agent, download the agent to your server and double click on the installer. Follow the instructions.

## Kubernetes

We support installing the CoScale agent through a DaemonSet configuration. You can find an example of this below. Make sure to replace the values for APP_ID, ACCESS_TOKEN, TEMPLATE_ID and CERTIFICATE. You can find these after creating an agent with a Kubernetes plugin.

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
      - image: coscale/coscale-agent
        imagePullPolicy: Always
        name: coscale-agent
        env:
        - name: APP_ID
          value: "replace_this_with_your_app_id"
        - name: BASE_URL
          value: "https://api.coscale.com"
        - name: ACCESS_TOKEN
          value: "replace_this_with_your_access_token"
        - name: TEMPLATE_ID
          value: "replace_this_with_your_template_id"
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
