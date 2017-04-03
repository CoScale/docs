---
layout: page
title: Docker plugin
description: Information on how to install the docker plugin and configure your container monitoring
---

> Docker is the world’s leading software containerization platform. Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications, whether on laptops, data center VMs, or the cloud. Docker containers wrap a piece of software in a complete filesystem that contains everything needed to run: code, runtime, system tools, system libraries – anything that can be installed on a server. This guarantees that the software will always run the same, regardless of its environment.

More information on: [https://www.docker.com/](https://www.docker.com/)

## Events

* Events reported by Docker
    * Container created
    * Container started
    * Container stopped
    * Container died
    * Container destroyed
    * Container killed
    * Container attach
* Events generated when 'docker exec' is called
    * Creating a plugin inside a container
    * Starting a plugin inside a container
    * Command was ran inside a container
* Docker service state watcher

## Metrics

| Metric name                                                                                               | Metric unit |
|-----------------------------------------------------------------------------------------------------------|-------------|
| Docker container total cpu usage                                                                          | %           |
| Docker container block IO read rate                                                                       | b/s         |
| Docker container block IO write rate                                                                      | b/s         |
| Docker container free memory bytes                                                                        | b           |
| Docker container free memory percentage                                                                   | %           |
| Docker container kernel mode cpu usage                                                                    | %           |
| Docker container memory limit                                                                             | b           |
| Docker container memory usage bytes                                                                       | b           |
| Docker container memory usage percentage                                                                  | %           |
| Docker container network receive errors total                                                             | #           |
| Docker container network receive packets dropped total                                                    | #           |
| Docker container network receive rate                                                                     | b/s         |
| Docker container network transmit errors total                                                            | #           |
| Docker container network transmit packets dropped total                                                   | #           |
| Docker container network transmit rate                                                                    | b/s         |
| Docker container number of CLOSE_WAIT connections                                                         | #           |
| Docker container number of CLOSING connections                                                            | #           |
| Docker container number of ESTABLISHED connections                                                        | #           |
| Docker container number of FIN_WAIT1 connections                                                          | #           |
| Docker container number of FIN_WAIT2 connections                                                          | #           |
| Docker container number of LAST_ACK connections                                                           | #           |
| Docker container number of LISTEN connections                                                             | #           |
| Docker container number of SYN_RECV connections                                                           | #           |
| Docker container number of SYN_SENT connections                                                           | #           |
| Docker container number of TIME_WAIT connections                                                          | #           |
| Docker container pgfault memory failures total                                                            | #           |
| Docker container pgmajfault memory failures total                                                         | #           |
| Docker container shm memory free bytes                                                                    | b           |
| Docker container shm memory free percent                                                                  | %           |
| Docker container shm memory limit                                                                         | b           |
| Docker container shm memory used bytes                                                                    | b           |
| Docker container user mode cpu usage                                                                      | %           |
| Docker running                                                                                            | %           |
| Number of bytes of page cache memory                                                                      | b           |
| The amount of anonymous and swap cache memory(includes transparent hugepages)                             | b           |
| The amount of swap currently used                                                                         | b           |
| The amount of working set memory, this includes recently accessed memory, dirty memory, and kernel memory | b           |


## How it works
The CoScale agent detects running containers on your system. With minimal configuration, it will start the required plugins whenever a running container is detected. These plugins will start within the same namespace as the container, so there is no need to forward ports or mount logfiles to your local filesystem. When a container disappears, the plugin will also automatically stop. Our plugins will do all their work from inside the container and send the data to our agent that will send it through to our platform.

## Installation

### Configure the CoScale agent with the Docker plugin

Choose the Docker plugin from our plugin list. Next, for each Docker image that you would like to monitor, you need to add a set of plugins to be installed when the image is run. Version is the same as the docker tag, so you can use `latest` or any custom tags you prefer. After adding a plugin, you will receive instructions on how to setup your Docker container so that our agent can monitor it.

<img src="{{ site.baseurl}}/gfx/agent/plugins/docker/configuration.png" alt="Screenshot of Docker configuration" class="img-responsive" />

#### Configurations

CoScale provides some custom images for the services that require configuration. Some of our plugins will work outside of the box without any configuration.

<table>
    <tr>
        <th>No configuration required</th>
        <th>Some setup required (custom image available*)</th>
        <th>Custom image coming soon</th>
    </tr>
    <tr>
        <td>
            <ul>
                <li>Redis</li>
                <li>MongoDB</li>
                <li>Memcached</li>
            </ul>
        </td>
        <td>
            <ul>
                <li>Nginx</li>
                <li>RabbitMQ</li>
                <li>MySQL</li>
            </ul>
        </td>
        <td>
            <ul>
                <li>Postgres</li>
                <li>Elasticsearch</li>
                <li>Tomcat</li>
                <li>Haproxy</li>
                <li>MariaDB</li>
                <li>Cassandra</li>
                <li>Sentry</li>
            </ul>
        </td>
    </tr>
</table>

*You can find a list of custom Docker images on [Docker Hub](https://hub.docker.com/u/coscale/).


### Install the CoScale agent on your machine running the Docker containers.

Follow the instructions in our application to install the CoScale agent on your Docker host. Our agent will then start the necessary plugins for the containers running on the Docker host. There is no need to restart or reconfigure the agent when containers are removed or restarted. Our agent will handle the plugins for monitoring the containers without manual intervention.

### Our agent will now collect data

Inside your dashboard under `Servers` you will now get a list of your running containers. All other metrics will be available under the usual metric groups.

### Monitor based on Docker labels

The agent will automatically start to monitor all Docker containers which have a label that starts with `com.coscale.monitoring` and contains a list of plugins and their configuration. These labels can be generated by clicking on the `Docker labels` button under the configuration pane. You can mark an image to be monitored by placing the generated label in your Dockerfile:

```
LABEL com.coscale.monitoring='[{"PluginType":"GENERICSCRIPT","Configuration":{"SCRIPT":["/script.sh"]}}]'
```

For already existing images the label can also be specified when creating containers, in the `docker run` command via the `--label` or `--label-file` options:

```
docker run -d --label com.coscale.monitoring='[{"PluginType":"CASSANDRA","Configuration":{"JMX HOSTNAME":["localhost"],"JMX PORT":["7199"]}}]' cassandra
```

Note that if the container's base image already has the 'com.coscale.monitoring' label, adding it again on `docker run` will overwrite the configuration in the base image. If instead want to extend the list of plugins defined in the base image, you can use a different label name in the `docker run` command, for example `com.coscale.monitoring.extra`.
