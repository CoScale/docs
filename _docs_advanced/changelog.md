---
layout: page
title: Changelog
description: A changelog of the most recent changes and additions to the CoScale platform.
---

## Release 3.13.0 (25 September 2017)

* Kibana integration
    * You can now interactively link your Kibana instance with CoScale
* Agent plugins
    * New plugin: Calico
    * Jolokia plugin:
        * Added native support for Openshift Jolokia
    * Kubernetes plugin: 
        * Time in state metrics converted to an event, significant performance improvements as a result.
    * Docker plugin:
        * New metric: Total number of containers
        * Docker plugin publically available for Microsoft Windows 2016
* Frontend
    * Better warning and error messages when using docker labels
    * When disconnecting a dimension from the global selector your selection is no longer lost
    * Servers page: Page should load a lot faster now
* CoScale CLI now available for Mac OS X

## Release 3.12.0 (12 September 2017)

* Alert page improvements
    * Many improvements including: Clone alert triggers, create dashboard from alert
* UX improvements & Small css improvements
    * Consistency in the plugin dialogs
    * Improvements to the flow for SSO users
    * Users can change their application name
    * Agent page: Always show configure and install instructions buttons
    * Widgets / Topology: Show the server the container is running on in the tooltip
* Agents
    * New plugins: Apache Solr, Jolokia plugin
    * Optimize sending data when agent has been offline for a while
    * Resources plugin: added more metrics
    * JMX plugin
        * Ability to add multiple endpoints
        * Support authentication
    * Docker/Kubernetes plugin
        * Too few replica events for DaemonSets and StatefulSets
        * CoScale Docker images are now certified for Red Hat
        * "Docker total host cpu usage" metrics added
        * Change 'groups' in security context constraint so that only 'system:cluster-admins' are allowed to use it.
        * Moved POD system containers to another server group

## Release 3.11.0 (30 June 2017)

* Frontend improvements
    * Allow enterprise users to login to CoScale with their Single-Sign-On (SSO) platform
    * [Public dashboard] Add subtile CoScale branding on public dashboard
    * Improve user experience for selecting metrics and events in the wizard.
    * Added support for COUNT/COUNTER metrics
* Agent improvements
    * Monitor internal kubernetes services (etcd, kubeapi)
    * [Postgresql] Add support to gather query performance data from pg_stats
* Anomaly detection
    * Improve anomaly detection for thread based metrics
    * Reduce sensitivity for RUM

## Release 3.10.0 (17 May 2017)

* Alerts through webhooks. 
    * Allows integration with many new alert providers (PagerDuty, OpsGenie, Nagios)
* Agent improvements
    * Docker image detection now supports more flexible regex's
    * Improved UI to provide detected images during the configuration
    * Docker plugin startup and image detection got some significant performance improvements
    * The agent now skips duplicate UPDATE_CONFIG agent actions
    * Improved logging in the agent, now includes containerid for easier debugging
* Alerts
    * Default alerts for CPU is now average over all cores, not for separate cores
* Switched over from Intercom to ZenDesk to provide support
* OnPrem
    * Update script (apicall) now correctly resets the api configuration after completion.
    * Pre-allocator no longer runs on 2 containers preventing duplicate column family ID's in cassandra

## Release 3.9.0 (25 April 2017)

* New default dashboards for the Docker & container orchestrators
    * Technology pane now has a click through
    * Topology widget now has a click through
    * Default dashboards for Docker added
* Improvements in the Agents
    * Agent now gathers more detailed metrics about deployments in Kubernetes & OpenShift environments
    * Plugin configurations can be added to your Docker images as labels and will now be picked up by the agent
* Improvements to the anomaly detection
    * Widgets on the dashboards will now show related anomalies
    * Anomaly emails are now more informative and can be further explored with a link to the app
    * Loadbalanced anomalies now also work on latencies
* General improvements to the frontend
    * Dashboard topbar was redesigned to be more responsive and have reduced clutter
    * EventList is now has a search field and received many small style improvements 
    * List of dashboards is now autorefreshed.
* Performance improvements to speed up the api
    * Alerts should no longer trigger on disabled servers
* Alerts can now be set on the messages of events 
* Billing page now allows for a registration key to be set

## Release 3.8.0 (10 March 2017)

* Inline configuration on the agents page & new configuration for custom agents
* Anomalies show on all widgets
* New collector: Azure

## Release 3.7.0 (27 February 2017)

* Using Kubernetes Watcher api to reduce Kubernetes plugin overhead
* Collect container metrics on hosts instead of Kubernetes api to improve scalability
* Support for ReplicaSets and StatefulSets
* Various fixes to plugins and bar charts

## Release 3.6.0 (20 February 2017)

* New and improved flow to create widgets
* HTTPS support for on-prem installations

## Release 3.5.0 (23 January 2016)

* A new plugin for Couchbase
* Monitoring /dev/stdout and /dev/stderr from Docker plugin
* Monitoring Kubernetes Cron jobs

## Release 3.4.0 (12 January 2016)

* New plugin: ActiveMQ
* General usability improvements throughout the frontend
    * Dashboard dropdown can now be navigated via keyboard navigation.
    * Usability improvements for the event list widget
    * Improved error pages
* Alerts email now support dimensions 
* OpenShift plugin now has new authentication options
* Zooming on charts should no longer break

## Release 3.3.0 (15 December 2016)

* A user-friendly agent installation flow for docker environments
* Dimension selector for Requests and RUM pages
* Custom visualisation for anomalies on load-balanced services
* Alerting page that allows the user to resolve multiple alerts at once
* Separate plugin for OpenShift
* Improved functionality on JMX plugin
* Lots of small improvements and bugfixes

## Release 3.2.0 (23 November 2016)

* Active checks in all our plugins: this allows you to check whether a service is up and how fast it is responding to your health check request
* Improved docker monitoring by introducing a table view on the containers that are consuming the most resources
* New metrics to find containers that are hanging in a pending or creating state
* Support for Google Container Engine
* Support for multiple memcached services on 1 server
* Lots of small improvements and bugfixes

## Release 3.1.0 (20 October 2016)

* Improved the dynamic behaviour of server and server groups : we leverage the start and stop times on the containers to keep the number of containers fetched and displayed by the frontend as low as possible. We also added a start and stop time to server group, so that for example old Kubernetes services don't stay around forever,
* Added support for multiple Redis servers in 1 agent,
* Further improved the resource usage of the CoScale Agent.
* Lots of small improvements and bugfixes
