---
layout: page
title: Datasource overview
description: An overview of all CoScale datasources.
---

<style>
    .datasources > div {
    	min-width: 850px;
        text-align: center;
    }

    .datasources .technology {
        position: relative;
        padding-bottom: 20px;
        display: inline-block;
        width: 120px;
        margin: 10px 0;
    }
    .datasources .technology > img,
    .datasources .technology > i {
        width: 50px;
        height: 50px;
        font-size: 50px;
        margin: 0 auto;
        display: block;
    }
    .datasources .technology > span {
        color: #333;
        position: absolute;
        bottom: 0;
        left: 0;
        text-align: center;
        right: 0;
        font-size: 0.8em;
    }

    .datasources .technology > a {
        position: absolute;
        bottom: 0;
        left: 0;
        text-align: center;
        right: 0;
        font-size: 0.8em;
    }

    .datasources fieldset {
    	border: 1px solid black;
        display: inline-block;
        position: relative;
        padding: 20px 10px 10px 10px;
    }
    .datasources fieldset.inner {
        display: block;
        margin-top: 15px;
    }
    .datasources fieldset.light {
        background: #f9f9f9;
        border-color: #f8f8f8;
    }
    .datasources fieldset.dotted {
        border-style: dotted;
        border-color: #000;
        background: #f2f2f2;
    }

    .datasources legend {
    	border: none;
    	margin: 0;
    	padding: 0 5px;
    	width: auto;
    }

    .datasources .error {
        color: #f00;
    }

    .datasources .mute {
        color: #999;
        font-size: 0.8em;
    }
    .datasources fieldset > .mute {
        position: absolute;
        margin: -15px 15px;
        left: 0px;
    }

    .datasources h2,
    .datasources h3,
    .datasources h4 {
    	margin: 0;
    	padding: 0;
    }
    .datasources h4 {
        font-weight: normal;
    }

    .marginT {
        margin-top: 20px;
    }


    .divider {
        font-size: 30px;
    }

    .legend {
        float: right;
        margin: 10px 0;
    }
</style>

<p>Below you can find an overview of what CoScale can monitor on your environment. When available, you can click the name of the components to get documentation on how to integrate with a certain service or application. If you have any questions or remarks, please don't hesitate to <a href="mailto:support@coscale.com" class="js-support">contact us</a>.</p>

<div class="datasources">
    <div>
        <fieldset>
            <legend align="center"><h2>Business</h2></legend>
            <span class="mute">Data collection of your business metrics and business indicators.</span>

            <div class="technology">
                <img alt="Google Analytics icon" src="{{ site.baseurl}}/gfx/agent/google-analytics.png"/>
                <a href="{{ site.baseurl }}/agent/plugins/googleanalytics"><span>Google Analytics</span></a>
            </div>

            <div class="technology">
                <img alt="Aweber icon" src="{{ site.baseurl}}/gfx/agent/aweber.png"/>
                <a href="{{ site.baseurl }}/agent/plugins/aweber"><span>Aweber</span></a>
            </div>

            <div class="technology">
                <img alt="Campaign monitor icon" src="{{ site.baseurl}}/gfx/agent/campaign-monitor.png"/>
                <a href="{{site.baseurl}}/agent/plugins/campaignmonitor"><span>Campaign Monitor</span></a>
            </div>

            <div class="technology">
                <img alt="Constant contact icon" src="{{ site.baseurl}}/gfx/agent/constant-contact.png"/>
                <a href="{{site.baseurl}}/agent/plugins/constantcontact"><span>Constant Contact</span></a>
            </div>

            <div class="technology">
                <img alt="Google Analytics icon" src="{{ site.baseurl}}/gfx/agent/google-analytics.png"/>
                <span>Google Analytics</span>
            </div>

            <div class="technology">
                <img alt="Mailchimp icon" src="{{ site.baseurl}}/gfx/agent/mailchimp.png"/>
                <a href="{{site.baseurl}}/agent/plugins/mailchimp"><span>Mailchimp</span></a>
            </div>

        </fieldset>
    </div>

    <div class="divider">
        <i class="fa fa-caret-up"></i>
    </div>

    <div>
        <fieldset>
            <legend align="center"><a href="{{site.baseurl}}/rum/install"><h2>Users (RUM)</h2></a></legend>
            <span class="mute">Data collection of your visitors' experience including pageload time, resources API calls, backend and frontend.</span>

            <div class="technology">
                <i class="fa fa-internet-explorer"></i>
                <span>Internet explorer 10</span>
            </div>

            <div class="technology">
                <i class="fa fa-edge"></i>
                <span>Edge</span>
            </div>

            <div class="technology">
                <i class="fa fa-firefox"></i>
                <span>Firefox 38</span>
            </div>

            <div class="technology">
                <i class="fa fa-chrome"></i>
                <span>Chrome 31</span>
            </div>

            <div class="technology">
                <i class="fa fa-opera"></i>
                <span>Opera 30</span>
            </div>
        </fieldset>
    </div>

    <div class="divider">
        <i class="fa fa-caret-up"></i>
    </div>

    <div>
        <fieldset>
            <legend align="center"><h2>Servers</h2></legend>
            <span class="mute">Data collection from your servers.</span>

            <fieldset class="dotted">
                <legend align="center"><a href="{{site.baseurl}}/agent/install"><h3>CoScale agent</h3></a></legend>
                <span class="mute">Data collection from many services running on your machine.</span>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>Container monitoring</h4></legend>
                        <span class="mute">Plugins for container monitoring.</span>

                        <div class="technology">
                            <img alt="Kubernetes icon" src="{{ site.baseurl}}/gfx/agent/kubernetes.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/kubernetes"><span>Kubernetes</span></a>
                        </div>

                        <div class="technology">
                            <img alt="Docker Swarm icon" src="{{ site.baseurl}}/gfx/agent/dockerswarm.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/docker-enterprise"><span>Docker Swarm</span></a>
                        </div>

                        <div class="technology">
                            <img alt="Docker icon" src="{{ site.baseurl}}/gfx/agent/docker.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/docker"><span>Docker</span></a>
                        </div>

                        <div class="technology">
                            <img alt="OpenShift icon" src="{{ site.baseurl}}/gfx/agent/openshift.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/openshift"><span>OpenShift</span></a>
                        </div>
                    </fieldset>
                </div>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>Generic monitoring</h4></legend>
                        <span class="mute">Plugins for generic monitoring.</span>

                        <div class="technology">
                            <img alt="CoScale resources icon" src="{{ site.baseurl}}/gfx/agent/coscale.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/resources"><span>CoScale Resources</span></a>
                            <div class="mute" style="position: absolute; top: 70px; left: -15px; width: 125%">CPU, Disk, Memory, Network</div>
                        </div>

                        <div class="technology">
                            <img alt="CollectD icon" src="{{ site.baseurl}}/gfx/agent/collectd.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/collectd"><span>
                                CollectD
                                <i class="fa fa-linux error"></i>
                            </span></a>
                        </div>

                        <div class="technology">
                            <img alt="Generic script icon" src="{{ site.baseurl}}/gfx/agent/genericscript.png"/>
                            <a href="{{ site.baseurl }}/custom-metrics/generic-script/index/"><span>Generic Script</span></a>
                        </div>

                        <div class="technology">
                            <img alt="JMX icon" src="{{ site.baseurl}}/gfx/agent/jmx.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/jmx"><span>JMX</span></a>
                        </div>

                        <div class="technology">
                            <img alt="Log plugin icon" src="{{ site.baseurl}}/gfx/agent/log_plugin.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/log"><span>
                                Log Plugin
                                <i class="fa fa-linux error"></i>
                            </span></a>
                        </div>
                    </fieldset>
                </div>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>HTTP</h4></legend>
                        <span class="mute">Plugins for web services.</span>

                        <div class="technology">
                            <img alt="Apache icon" src="{{ site.baseurl}}/gfx/agent/apache.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/apache"><span>Apache</span></a>
                        </div>

                        <div class="technology">
                            <img alt="HAProxy icon" src="{{ site.baseurl}}/gfx/agent/haproxy.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/haproxy"><span>HaProxy</span></a>
                        </div>

                        <div class="technology">
                            <img alt="IIS icon" src="{{ site.baseurl}}/gfx/agent/iis.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/iis"><span>
                                IIS
                                <i class="fa fa-windows error"></i>
                            </span></a>
                        </div>

                        <div class="technology">
                            <img alt="JBoss icon" src="{{ site.baseurl}}/gfx/agent/jboss.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/jboss"><span>JBoss</span></a>
                        </div>

                        <div class="technology">
                            <img alt="Varnish icon" src="{{ site.baseurl}}/gfx/agent/varnish.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/varnish"><span>
                                Varnish
                                <i class="fa fa-linux error"></i>
                            </span></a>
                        </div>
                    </fieldset>
                </div>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>Database</h4></legend>
                        <span class="mute">Plugins for relational databases.</span>

                        <div class="technology">
                            <img alt="MySQL icon" src="{{ site.baseurl}}/gfx/agent/mysql.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/mysql"><span>MySQL</span></a>
                        </div>

                        <div class="technology">
                            <img alt="MsSQL icon" src="{{ site.baseurl}}/gfx/agent/mssql.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/mssql"><span>
                                MSSQL
                                <i class="fa fa-windows error"></i>
                            </span></a>
                        </div>

                        <div class="technology">
                            <img alt="Oracle icon" src="{{ site.baseurl}}/gfx/agent/oracle.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/oracle"><span>
                                Oracle
                                <i class="fa fa-linux error"></i>
                            </span></a>
                        </div>

                        <div class="technology">
                            <img alt="PostgreSQL icon" src="{{ site.baseurl}}/gfx/agent/postgresql.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/postgresql"><span>PostgreSQL</span></a>
                        </div>
                    </fieldset>
                </div>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>NoSQL</h4></legend>
                        <span class="mute">Plugins for NoSQL databases.</span>

                        <div class="technology">
                            <img alt="Riak icon" src="{{ site.baseurl}}/gfx/agent/riak.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/riak"><span>
                                Riak
                                <i class="fa fa-linux error"></i>
                            </span></a>
                        </div>

                        <div class="technology">
                           <img alt="Couchbase icon" src="{{ site.baseurl}}/gfx/agent/couchbase.png"/>
                           <a href="{{ site.baseurl }}/agent/plugins/couchbase"><span>
                               Couchbase
                           </span></a>
                       </div>

                       <div class="technology">
                          <img alt="CouchDb icon" src="{{ site.baseurl}}/gfx/agent/couchdb.png"/>
                          <a href="{{ site.baseurl }}/agent/plugins/couchdb"><span>
                              CouchDb
                              <i class="fa fa-linux error"></i>
                          </span></a>
                      </div>

                      <div class="technology">
                          <img alt="Redis icon" src="{{ site.baseurl}}/gfx/agent/redis.png"/>
                          <a href="{{ site.baseurl }}/agent/plugins/redis"><span>
                              Redis
                              <i class="fa fa-linux error"></i>
                          </span></a>
                      </div>

                      <div class="technology">
                          <img alt="MongoDB icon" src="{{ site.baseurl}}/gfx/agent/mongodb.png"/>
                          <a href="{{ site.baseurl }}/agent/plugins/mongodb">
                            <span>MongoDB</span>
                            </a>
                      </div>
                      <div class="technology">
                         <img alt="Elasticsearch icon" src="{{ site.baseurl}}/gfx/agent/elasticsearch.png"/>
                         <a href="{{ site.baseurl }}/agent/plugins/elasticsearch"><span>Elasticsearch</span></a>
                     </div>

                         <div class="technology">
                            <img alt="Cassandra icon" src="{{ site.baseurl}}/gfx/agent/cassandra.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/cassandra"><span>Cassandra</span></a>
                        </div>
                    </fieldset>
                </div>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>Other</h4></legend>
                        <span class="mute">Plugins for additional services.</span>

                        <div class="technology">
                           <img alt="Magento icon" src="{{ site.baseurl}}/gfx/agent/magento.png"/>
                           <a href="{{ site.baseurl }}/agent/plugins/magento"><span>Magento</span></a>
                       </div>

                        <div class="technology">
                           <img alt="Kafka icon" src="{{ site.baseurl}}/gfx/agent/kafka.png"/>
                           <a href="{{ site.baseurl }}/agent/plugins/kafka"><span>Kafka</span></a>
                       </div>

                       <div class="technology">
                          <img alt="ActiveMQ icon" src="{{ site.baseurl}}/gfx/agent/activemq.png"/>
                          <a href="{{ site.baseurl }}/agent/plugins/activemq"><span>ActiveMQ</span></a>
                      </div>

                         <div class="technology">
                            <img alt="Memcached icon" src="{{ site.baseurl}}/gfx/agent/memcached.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/memcached"><span>Memcached</span></a>
                        </div>

                         <div class="technology">
                            <img alt="RabbitMQ icon" src="{{ site.baseurl}}/gfx/agent/rabbitmq.png"/>
                            <a href="{{ site.baseurl }}/agent/plugins/rabbitmq"><span>RabbitMQ</span></a>
                        </div>
                    </fieldset>
                </div>
            </fieldset>

            <div>
                <fieldset class="inner marginT dotted">
                    <legend align="center"><h3>Thirdparty resources</h3></legend>
                    <span class="mute">Data collection from thirdparty resources.</span>

                    <div class="technology">
                        <img alt="AWS icon" src="{{ site.baseurl}}/gfx/agent/amazon-aws.png"/>
                        <a href="{{site.baseurl}}/agent/plugins/amazoncloudwatch"><span>Amazon CloudWatch</span></a>
                    </div>

                    <div class="technology">
                        <img alt="Pingdom icon" src="{{ site.baseurl}}/gfx/agent/pingdom.png"/>
                        <a href="{{site.baseurl}}/agent/plugins/pingdom"><span>Pingdom</span></a>
                    </div>

                    <div class="technology">
                        <img alt="Rollbar icon" src="{{ site.baseurl}}/gfx/agent/rollbar.png"/>
                        <a href="{{site.baseurl}}/agent/plugins/rollbar"><span>Rollbar</span></a>
                    </div>

                    <div class="technology">
                        <img alt="Sentry icon" src="{{ site.baseurl}}/gfx/agent/sentry.png"/>
                        <a href="{{ site.baseurl }}/agent/plugins/sentry"><span>Sentry</span></a>
                    </div>
                </fieldset>
            </div>

            <div>
                <fieldset class="inner marginT dotted">
                    <legend align="center"><h3>Integrations</h3></legend>
                    <span class="mute">Data collection from automated jobs.</span>

                    <div class="technology">
                        <img alt="Puppet icon" src="{{ site.baseurl}}/gfx/agent/PUPPET.png"/>
                        <a href="{{ site.baseurl }}/events/automation/puppet"><span>Puppet</span></a>
                    </div>

                    <div class="technology">
                        <img alt="Chef icon" src="{{ site.baseurl}}/gfx/agent/CHEF.png"/>
                        <a href="{{ site.baseurl }}/events/automation/chef"><span>Chef</span></a>
                    </div>

                    <div class="technology">
                        <img alt="Salt icon" src="{{ site.baseurl}}/gfx/agent/SALT.png"/>
                        <a href="{{ site.baseurl }}/events/automation/salt"><span>Salt</span></a>
                    </div>

                    <div class="technology">
                        <img alt="Ansible icon" src="{{ site.baseurl}}/gfx/agent/ansible.png"/>
                        <a href="{{ site.baseurl }}/events/automation/ansible"><span>Ansible</span></a>
                    </div>

                    <div class="technology">
                        <img alt="Cron icon" src="{{ site.baseurl}}/gfx/agent/CRON.png"/>
                        <a href="{{ site.baseurl }}/events/wrappers/linux/index/"><span>Cron jobs</span></a>
                    </div>

                    <div class="technology">
                        <img alt="CLI icon" src="{{ site.baseurl}}/gfx/agent/CLI.png"/>
                        <a href="{{ site.baseurl }}/tools/cli/index/"><span>Coscale CLI</span></a>
                    </div>
                </fieldset>
            </div>
        </fieldset>
    </div>

    <section class="legend">
        <div>
            <i class="fa fa-linux error"></i>
            = Only supported by Linux agents.
        </div>
        <div>
            <i class="fa fa-windows error"></i>
            = Only supported by Windows agents.
        </div>
    </section>
</div>
