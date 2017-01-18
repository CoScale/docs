---
layout: page
title: Firewall / Proxy
description: Information about CoScale agent firewall settings and proxy configuration.
---

## Firewall
By default, all CoScale agents communicate with the CoScale platform over a secured SSL connection. The agent communicates with one host `api.coscale.com` on TCP port 443. No incoming connections are required.

## Proxy
The CoScale agent allows to send data using a proxy. This can be configured by setting an environment variable HTTPS_PROXY.

* For Linux systems this means adding an environment variable to `/etc/default/coscale-agent`

    `export https_proxy=http://[ip]:[port]/`

    After please [restart]({{ site.baseurl }}/agent/agent-restart) the agent.

* For Microsoft Windows a global environment variable HTTPS_PROXY must be set.

* For Docker agents add the https_proxy environment variable to the "docker run" command:  

      docker run -it --rm \  
      --privileged \  
      --net=host --pid=host \  
      --name coscale-agent \  
      -e APP_ID=“..." \  
      -e ACCESS_TOKEN=“..." \  
      -e TEMPLATE_ID=... \  
      -e https_proxy="http://<user>:<pass>@<proxy_host>:<port>/" \  
      -v /var/run/docker.sock:/var/run/docker.sock \  
      -v /:/host/:ro \  
      coscale/coscale-agent
    
* For Docker Swarm agents add the https_proxy environment variable to the "docker service” command:  

      docker service create \
      --mount type=bind,src=/proc/,dst=/host/proc \
      --mount type=bind,src=/,dst=/host \
      --mount type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock \
      --mode global \
      --env APP_ID="..." \
      --env ACCESS_TOKEN="..." \
      --env TEMPLATE_ID="..." \
      --env https_proxy="http://<user>:<pass>@<proxy_host>:<port>/" \
      --name coscale-agent \
      coscale/coscale-agent`

* For Kubernetes, OpenShift, Google Container Engine add the https_proxy environment variable to the DaemonSet configuration:  

      cat <<EOF | kubectl apply -f -
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
                value: "..."
              - name: ACCESS_TOKEN
                value: "..."
              - name: TEMPLATE_ID
                value: "..."
              - name: https_proxy
                value: "http://<user>:<pass>@<proxy_host>:<port>/"
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
      EOF


**Note** that this example applies directly to Kubernetes, for OpenShift and Google Container Engine the commands differ slightly. The easiest way to add the proxy is to copy the DaemonSet command from the CoScale UI and add the https_proxy environment variable under “spec > template > spec > containers > env” like in the example above.
