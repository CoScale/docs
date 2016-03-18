---
layout: page
title: Tutorial - Service availability check
description: Creating a service availability check using CoScale.
---

## Part 1: Creating a service availability script

We have already written service availability scripts to use with our [Generic Script plugin]({{ site.baseurl }}/custom-metrics/generic-script/index/). All you need to do is download the [Python](https://github.com/CoScale/coscale-generic-scripts/blob/master/uptime/service_check.py) or [Bash](https://github.com/CoScale/coscale-generic-scripts/blob/master/examples/bash-example.sh) version and edit a few small configuration settings within the script and everything should work out of the box.

We recommend using the [python version](https://github.com/CoScale/coscale-generic-scripts/blob/master/uptime/service_check.py) because python provides a better structure and is more readable.

If you are having problems with customizing the service availability script, or something is not clear, you can visit our [Generic Script plugin docs]({{ site.baseurl }}/custom-metrics/generic-script/index/) for more information. You can also contact us at support@coscale.com and we will try to address any problems you might have.

## Part 2: Creating an agent with a service availability script attached to it using the [Generic Script plugin]({{ site.baseurl }}/custom-metrics/generic-script/index/).

<ol>
    <!-- Go to page -->
    <li>
        <p>Go to <strong>Datasources</strong> > <strong>Agent</strong></p>
    </li>

    <!-- Create/edit agent -->
    <li>
        <p>
            <strong>Create a new agent</strong>, or you can also <strong>edit</strong> an existing one that you might have. The process is the same.
        </p>

        <img src="{{ site.baseurl }}/gfx/tutorials/service-availability-check/agent1.png " style="margin-bottom: 15px;"/>
    </li>

    <!-- Select Generic Script plugin -->
    <li>
        <p>
            We will only focus on configuring the necessary plugin for the agent. If you wish to read more extensive documentation on the whole process of configuring an agent please visit the <a target="_blank" href="{{ site.baseurl }}/agent/index">agent docs</a>. Generally the whole process should be straight-forward and self-explanatory.
        </p>


        <p>
            Now go to the <strong>Plugin step</strong> and add the <a target="_blank" href="{{ site.baseurl }}/custom-metrics/generic-script/index/">Generic script plugin</a>. A dialog will appear with the configuration steps for this plugin. What to fill in will be explained in the next step.
        </p>

        <img src="{{ site.baseurl }}/gfx/tutorials/service-availability-check/agent2.png " style="margin-bottom: 15px;"/>
    </li>

    <!-- Configuring Generic Script plugin -->
    <li>
        Configuring the Generic script plugin is very easy. You only have to provide the path to the script that will run the service availability check. The path is the location to the script on your server.

        <ul>
            <li>Go to the <strong>script step</strong>.</li>
            <li>Scroll down and click <strong>add another file</strong>.</li>
            <li>Fill in the <strong>path to the script</strong> in the input box that appears and click <strong>Finish</strong>.</li>
        </ul>

        <img src="{{ site.baseurl }}/gfx/tutorials/service-availability-check/agent3.png " style="margin-bottom: 15px;"/>
    </li>

    <!-- Finish agent configuration -->
    <li>
        <p>
            Continue through the steps and finish the agent configuration. Then download it and install it on your server(s).
        </p>

        <p>
            If you are editing an agent then the agent will update itself automatically after you finish the configuration. The auto-update procedure will require some minutes to complete so please be patient.
        </p>
    </li>

    <!-- Upload service script -->
    <li>
        <p>Don't forget to deploy the service availability script to your server to the same <strong>path</strong> as provided in the configuration of the Generic script plugin.</p>

        <p>
            Generally you should only have one server running the Generic script plugin with the service availability script. This does mean that if your server goes down, your availability check will also not work anymore, so you should have some backup system in place for these situations.
        </p>
    </li>
</ol>

## Part 3: Waiting for the first run of the service availability script.

<p>
    We have to wait until the script has been picked up by the agent and has run at least once. On the first run the agent will create the metrics in CoScale that have been defined in the service availability script.
</p>

<p>
    If the metrics have not been created in CoScale you cannot continue creating alerts for them since they will not be available.
</p>

## Part 4: Creating alerts for services that become unavailable.

<ol>
    <!-- Go to alerts,manage -->
    <li>
        <p>Go to <strong>Alerts</strong> > <strong>Manage</strong></p>
    </li>

    <!-- Create notification scheme -->
    <li>
        <p>Create a new <strong>notification scheme</strong></p>

        <img src="{{ site.baseurl }}/gfx/tutorials/service-availability-check/alerts1.png " style="margin-bottom: 15px;"/>
    </li>

    <!-- Notification settings -->
    <li>
        <p>Fill in the <strong>name</strong> & <strong>add the emails for the main recipients</strong>.</p>

        <p>The rest of the form is not required but it is worth considering if configuring the optional steps might be beneficial in your situation.</p>

        <img src="{{ site.baseurl }}/gfx/tutorials/service-availability-check/alerts2.png " style="margin-bottom: 15px;"/>
    </li>

    <!-- Alert block -->
    <li>
        <p>Now you will see a new alert block. Continue by clicking on the <strong>add new alert</strong> button.</p>

        <img src="{{ site.baseurl }}/gfx/tutorials/service-availability-check/alerts3.png " style="margin-bottom: 15px;"/>
    </li>

    <!-- Fill in the form -->
    <li>
        Fill in the alert form

        <ul>
            <li>Fill in the <strong>name</strong> for the alert</li>
            <li>Fill in the <strong>description</strong>. (optional)</li>
            <li><strong style="color: red;">!</strong> Leave the <strong>datatype</strong> on <strong>Server metric</strong> because the Generic Script plugin only pushes server metrics.</li>
            <li><strong style="color: red;">!</strong> Leave ‘<strong>use forecast data</strong>’ turned <strong>off</strong> because it does not apply in this case.</li>
            <li><strong>Subject</strong>: It is best to leave this set to <strong>all servers</strong> for complete coverage of the alert.</li>

            <li>
                <strong>Alert rule</strong>:
                <ul>
                    <li>Choose the correct metric in the first select box. Look for the same name as you provided in the script.</li>
                    <li>Set the value to <strong>not equal to 0</strong>. (<span style="color: green;">0 means service available</span>, <span style="color: red;">anything else means service not available</span>)</li>
                    <li>Set the <strong>period</strong> between <strong>120s</strong> and <strong>180s</strong> to avoid too many false positives.</li>
                </ul>
            </li>

            <li><strong>Auto resolving</strong> is turned on by default and we recommend to leave it on.</li>
        </ul>

        <img src="{{ site.baseurl }}/gfx/tutorials/service-availability-check/alerts4.png " style="margin-bottom: 15px;"/>
    </li>

    <!-- Repeat -->
    <li>
        <strong>Repeat</strong> the process of creating an alert for each service for which you wish to receive alerts when it becomes unavailable.
    </li>
</ol>

