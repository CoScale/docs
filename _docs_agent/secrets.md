---
layout: page
title: Using secrets in configuration
description: Configure the CoScale agent and plugins using secrets.
---

When creating your Docker image you can add a label to tell the CoScale agent how to monitor this image when it's detected. To make this work in an environment where you sensitive data is stored in a secret. You can also tell the agent to read usernames and passwords from a secrets file/mount.

In this example we have created an image with RabbitMQ running on it, we added a Docker label to automatically run the RabbitMQ plugin on the container once it starts. We tell the agent to get the password from a secret on the filesystem located at `/run/secrets/rabbitmq_password` by defining `$/run/secrets/rabbitmq_password` in the Docker LABEL.

{% highlight bash %}
FROM rabbitmq:3.6

RUN rabbitmq-plugins enable rabbitmq_management

LABEL com.coscale.monitoring='[{"PluginType":"RABBITMQ","Configuration":{"HOSTNAME":["localhost"],"PORT":["15672"],"USERNAME":["$/run/secrets/rabbitmq_username"],"PASSWORD":["$/run/secrets/rabbitmq_password"]}}]'
{% endhighlight %}
