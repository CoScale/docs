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

<div class="datasources">
    <div>
        <fieldset>
            <legend align="center"><h2>Business</h2></legend>
            <span class="mute">Data collection of your business metrics and business indicators.</span>

            <div class="technology">
                <img src="{{ site.baseurl}}/gfx/agent/google-analytics.png"/>
                <span>Google Analytics</span>
            </div>

            <div class="technology">
                <img src="{{ site.baseurl}}/gfx/agent/aweber.png"/>
                <span>Aweber</span>
            </div>

            <div class="technology">
                <img src="{{ site.baseurl}}/gfx/agent/campaign-monitor.png"/>
                <span>Campaign Monitor</span>
            </div>

            <div class="technology">
                <img src="{{ site.baseurl}}/gfx/agent/constant-contact.png"/>
                <span>Constant Contact</span>
            </div>

            <div class="technology">
                <img src="{{ site.baseurl}}/gfx/agent/mailchimp.png"/>
                <span>Mailchimp</span>
            </div>
        </fieldset>
    </div>

    <div class="divider">
        <i class="fa fa-caret-up"></i>
    </div>

    <div>
        <fieldset>
            <legend align="center"><h2>Users (RUM)</h2></legend>
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
                <legend align="center"><h3>CoScale agent</h3></legend>
                <span class="mute">Data collection from many services running on your machine.</span>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>Generic monitoring</h4></legend>
                        <span class="mute">Plugins for generic monitoring.</span>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/coscale.png"/>
                            <span>CoScale Resources</span>
                            <div class="mute" style="position: absolute; top: 70px; left: -15px; width: 125%">CPU, Disk, Memory, Network</div>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/collectd.png"/>
                            <span>
                                CollectD
                                <i class="fa fa-linux error"></i>
                            </span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/genericscript.png"/>
                            <span>Generic Script</span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/jmx.png"/>
                            <span>JMX</span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/log_plugin.png"/>
                            <span>
                                Log Plugin
                                <i class="fa fa-linux error"></i>
                            </span>
                        </div>
                    </fieldset>
                </div>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>HTTP</h4></legend>
                        <span class="mute">Plugins for web services.</span>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/apache.png"/>
                            <span>Apache</span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/haproxy.png"/>
                            <span>HaProxy</span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/iis.png"/>
                            <span>
                                IIS
                                <i class="fa fa-windows error"></i>
                            </span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/jboss.png"/>
                            <span>JBoss</span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/varnish.png"/>
                            <span>
                                Varnish
                                <i class="fa fa-linux error"></i>
                            </span>
                        </div>
                    </fieldset>
                </div>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>Database</h4></legend>
                        <span class="mute">Plugins for relational databases.</span>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/mysql.png"/>
                            <span>MySql</span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/mssql.png"/>
                            <span>
                                MSSQL
                                <i class="fa fa-windows error"></i>
                            </span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/oracle.png"/>
                            <span>
                                Oracle
                                <i class="fa fa-linux error"></i>
                            </span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/postgresql.png"/>
                            <span>PostgreSQL</span>
                        </div>
                    </fieldset>
                </div>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>NoSQL</h4></legend>
                        <span class="mute">Plugins for NoSQL databases.</span>

                         <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/cassandra.png"/>
                            <span>Cassandra</span>
                        </div>

                         <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/couchdb.png"/>
                            <span>
                                CouchDb
                                <i class="fa fa-linux error"></i>
                            </span>
                        </div>

                         <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/elasticsearch.png"/>
                            <span>Elasticsearch</span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/mongodb.png"/>
                            <span>MongoDB</span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/redis.png"/>
                            <span>
                                Redis
                                <i class="fa fa-linux error"></i>
                            </span>
                        </div>

                        <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/riak.png"/>
                            <span>
                                Riak
                                <i class="fa fa-linux error"></i>
                            </span>
                        </div>
                    </fieldset>
                </div>

                <div>
                    <fieldset class="inner light">
                        <legend align="center"><h4>Other</h4></legend>
                        <span class="mute">Plugins for additional services.</span>

                         <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/magento.png"/>
                            <span>Magento</span>
                        </div>

                         <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/memcached.png"/>
                            <span>Memcached</span>
                        </div>

                         <div class="technology">
                            <img src="{{ site.baseurl}}/gfx/agent/rabbitmq.png"/>
                            <span>RabbitMQ</span>
                        </div>
                    </fieldset>
                </div>
            </fieldset>

            <div>
                <fieldset class="inner marginT dotted">
                    <legend align="center"><h3>Thirdparty resources</h3></legend>
                    <span class="mute">Data collection from thirdparty resources.</span>

                    <div class="technology">
                        <img src="{{ site.baseurl}}/gfx/agent/amazon-aws.png"/>
                        <span>Amazon</span>
                    </div>

                    <div class="technology">
                        <img src="{{ site.baseurl}}/gfx/agent/pingdom.png"/>
                        <span>Pingdom</span>
                    </div>

                    <div class="technology">
                        <img src="{{ site.baseurl}}/gfx/agent/rollbar.png"/>
                        <span>Rollbar</span>
                    </div>

                    <div class="technology">
                        <img src="{{ site.baseurl}}/gfx/agent/sentry.png"/>
                        <span>Sentry</span>
                    </div>
                </fieldset>
            </div>

            <div>
                <fieldset class="inner marginT dotted">
                    <legend align="center"><h3>Integrations</h3></legend>
                    <span class="mute">Data collection from automated jobs.</span>

                    <div class="technology">
                        <img src="{{ site.baseurl}}/gfx/agent/PUPPET.png"/>
                        <span>Puppet</span>
                    </div>

                    <div class="technology">
                        <img src="{{ site.baseurl}}/gfx/agent/CHEF.png"/>
                        <span>Chef</span>
                    </div>

                    <div class="technology">
                        <img src="{{ site.baseurl}}/gfx/agent/SALT.png"/>
                        <span>Salt</span>
                    </div>

                    <div class="technology">
                        <img src="{{ site.baseurl}}/gfx/agent/CRON.png"/>
                        <span>Cron jobs</span>
                    </div>

                    <div class="technology">
                        <img src="{{ site.baseurl}}/gfx/agent/CLI.png"/>
                        <span>Coscale CLI</span>
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