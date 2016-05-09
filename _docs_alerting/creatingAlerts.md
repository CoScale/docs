---
layout: page
title: Adding alerts to a notification scheme
description: Steps on how to add alerts to a notification scheme.
---
<ol>
    <li>
        <p>
            Go to your desired notification block and click the 'add alert' button to add a new alert to that group.
        </p>

        <p>
            <img src="{{ site.baseurl }}/gfx/alerting/createAlert/addAlert.png"/>
        </p>
    </li>

    <li>
        <p>
            The alert dialog will appear and you can start configuring the details for the alert.
        </p>

        <ul>
            <li>
                <strong>Name:</strong> The name for the alert.
            </li>

            <li>
                <strong>Description:</strong> A description for the alert.
            </li>

            <li>
                <strong>Datatype:</strong> Which datatype do you want to monitor?
            </li>

            <li>
                <strong>Use forecast data?:</strong> Do you wish to include fore-casted data in the alert so you can preemptively be alerted?
            </li>

            <li>
                <strong>Subject:</strong> The level on which the alert should monitor. If you choose server you will also be able to specify a specific server or servergroup.
            </li>

            <li>
                <strong>Alert rule:</strong> You have several different inputs that together will define the exact rule for the alert.
            </li>

            <li>
                <strong>Automatically resolve alert?:</strong> If you wish for CoScale to automatically resolve emails for you after a specific period then leave this turned on. (Our recommendation is to keep it turned on)
            </li>

            <li>
                <strong>Automatically resolve after:</strong> The time after which the alert will get auto resolved.
            </li>
        </ul>

        <p>
            The widget with the red line is a visual representation of when the alert should be triggered. 
        </p>

        <p>
            <img src="{{ site.baseurl }}/gfx/alerting/createAlert/alertDialog.png"/>
        </p>
    </li>

    <li>
        <p>
            Once you are finished configured all the parameters click save in the dialog and you will see the alert appear in the list in the notification scheme block.
        </p>

        <p>
            <img src="{{ site.baseurl }}/gfx/alerting/createAlert/alertCreated.png"/>
        </p>
    </li>

    <li>
        <p>
            When hovering over a row you will see the 'edit' and 'delete' buttons appear if you wish to change your alert.
        </p>

        <p>
            <img src="{{ site.baseurl }}/gfx/alerting/createAlert/editAlert.png"/>
        </p>
    </li>

</ol>
