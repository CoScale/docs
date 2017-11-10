---
layout: page
title: Setting up a reverse proxy for RUM traffic
description: Setting up a reverse proxy for RUM traffic
---

This tutorial explains how to setup an Apache Reverse Proxy on a bastion host that only forwards RUM calls and forbids all other traffic to the CoScale on-premise installation.

## Docker configuration

CoScale provides a pre-configured Docker image to use in your public Docker environment. This can be deployed using the Docker Swarm services or Kubernetes ReplicationControllers. The image supports using a url as destination.

### Example

{% highlight bash %}
$ docker run -d \
    -p 0.0.0.0:8080:80 \
    -e "DESTINATION=http://coscale.company.com/" \
    --name rum-proxy coscale/rum-proxy:1.0
{% endhighlight %}

Exposes the RUM Service on port 8080 and proxies the requests to http://coscale.company.com

### Enable HTTPS

To enable HTTPS:
* Set ENABLE_HTTPS=1
* Mount a directory containing https.crt, https.crt to /data/ssl.

For example:

{% highlight bash %}
$ docker run -d \
    -p 0.0.0.0:8080:80 \
    -p 0.0.0.0:8443:443 \
    -v /home/cs/ssl:/data/ssl:ro \
    -e "ENABLE_HTTPS=1" \
    -e "DESTINATION=http://coscale.company.com/" \
    --name rum-proxy coscale/rum-proxy:1.0
{% endhighlight %}
  
### Running on Kubernetes

The following configuration can be used to create a service that runs the rum-proxy (without HTTPS):

{% highlight yaml %}
apiVersion: v1
kind: Service
metadata:
  name: coscale-rum-proxy
  labels:
    app: coscale-rum-proxy
spec:
  ports:
  - port: 80
    protocol: TCP
  selector:
    app: coscale-rum-proxy
---
apiVersion: v1
kind: ReplicationController
metadata:
  name: coscale-rum-proxy
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: coscale-rum-proxy
    spec:
      containers:
      - name: rum-proxy
        image: coscale/rum-proxy:1.0
        ports:
        - containerPort: 80
        env:
        - name: DESTINATION
          value: "http://coscale.company.com/"
{% endhighlight %}

## Manual configuration

### Install Apache2

We'll be using a Debian based Linux installation in this example, but most commands are applicable to all Linux environments.

`apt-install apache2`

### Enable required Apache2 modules

You might not include all the modules mentioned below. E.g.: if you're not going to use SSL or if you're just forwarding and not interested in blocking (rewrite) anything.

{% highlight bash %}
a2enmod xml2enc
a2enmod proxy
a2enmod proxy_http
a2enmod proxy_ajp
a2enmod rewrite
a2enmod deflate
a2enmod headers
a2enmod proxy_balancer
a2enmod proxy_connect
a2enmod proxy_html
a2enmod ssl
{% endhighlight %}

### Create a site config

`vim  /etc/apache2/sites-available/revproxy.conf`

Replace the servername `coscale.mycompany.com` with the hostname you want Apache to handle. This needs to be the same as the one configured in the CoScale environment config and the one mentioned in the CoScale RUM javascript snippet. If you put the incorrect one, Apache won't handle the requests.

Replace the destination IP (`10.99.5.27` in the example) with the IP where the bastion host can reach the CoScale environment.

Configure the SSL part correctly or leave it out if you're not using SSL.

[NC] means Not Case Sensitive
[F,L] means Forbidden (send 403 forbidden) and Last (end the rewriting here) if the condition matches.

{% highlight apache %}
<VirtualHost *:80>
  ServerName 'coscale.mycompany.com'
  ProxyPreserveHost On
  ProxyRequests Off
  ProxyPass / 'http://10.99.5.27/'
  ProxyPassReverse / 'http://10.99.5.27/'
  <Location />
  RewriteEngine On
  RewriteCond %{REQUEST_URI} !^/rum/ [NC]
  RewriteRule ^.*$ - [F,L]
  </Location>
</VirtualHost>

<VirtualHost *:443>
  ServerName 'coscale.mycompany.com'
  SSLProxyEngine on
  ProxyPreserveHost On
  ProxyRequests Off
  ProxyPass / 'https://10.99.5.27/'
  ProxyPassReverse / 'https://10.99.5.27/'
  SSLCertificateFile /data/websites/mycompany_ssl/mycompany.crt
  SSLCertificateKeyFile /data/websites/mycompany_ssl/myserver.key
  SSLCertificateChainFile /data/websites/mycompany_ssl/bundle.crt
  <Location />
  RewriteEngine On
  RewriteCond %{REQUEST_URI} !^/rum/ [NC]
  RewriteRule ^.*$ - [F,L]
  </Location>
</VirtualHost>
{% endhighlight %}

An example for the SSL part with letsencrypt certificate (replace the 3 lines):

{% highlight apache %}
SSLCertificateFile /etc/letsencrypt/live/coscale.mycompany.com/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/coscale.mycompany.com/privkey.pem
Include /etc/letsencrypt/options-ssl-apache.conf
{% endhighlight %}

### Enable the site and disable the default site

{% highlight bash %}
a2ensite revproxy
a2dissite 000-default
restart apache
service apache2 restart
{% endhighlight %}

### Point the resolving / DNS for the hostname to the bastion host

Make sure the requests cannot go directly to the CoScale environment (firewall /separated network / ...), but to the bastion host. Point the hostname to the IP of the bastion host, in DNS for everyone or in /etc/hosts, only for your host.
