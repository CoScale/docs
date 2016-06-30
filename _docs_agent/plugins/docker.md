---
layout: page
title: Docker plugin
description: Information on how to install the docker plugin and configure your container monitoring
---

## How it works
The CoScale agent detects running containers on your system, with some configuration it will start the required plugins whenever a running container is detected. These plugins will start within the same namespace as the container, so there is no need to forward ports or mount logfiles to your local filesystem. When container disappear the plugin will also automatically stop. Our plugins will do all their work from inside the container and send the data to our agent that will send it through to our platform.

## Installation

### Configure the CoScale agent with the Docker plugin

Choose the Docker plugin from our plugin list. Next add all the containers you would like to monitor and the plugins that need to start to monitor the container. Version is the same as the docker tag, so you can use `latest` or any custom tags you prefer. After adding a plugin you will receive instructions on how to setup your Docker container so that our agent can monitor it.

<img src="{{ site.baseurl}}/gfx/agent/plugins/docker/configuration.png" alt="Screenshot of Docker configuration" class="img-responsive" />

#### Configurations

CoScale provides some custom images for the services that require configuration. Some of our plugins will work outside of the box without any configuration.

<table>
    <tr>
        <th>No configuration required</th>
        <th>Some setup required (custom image available*)</th>
        <th>Not tested yet</th>
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

    * You can find a list of custom Docker images on [Docker Hub](https://hub.docker.com/u/coscale/).


### Install the CoScale agent on your machine running the Docker containers.

Follow the instructions in our application to install the CoScale agent on your Docker host. Our agent will then start the necessary plugins for the containers running on the Docker host. There is no need to restart or reconfigure the agent when containers are removed or restarted. Our agent will handle the plugins for monitoring the containers without manual intervention.

### Our agent will now collect data

Inside your dashboard under `Servers` you will now get a list of your running containers. All other metrics will be available under the usual metric groups.
