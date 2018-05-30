---
layout: page
title: Monitoring and collecting data from IIS - Internet Information Services
description: Information on the metrics collected by the CoScale IIS plugin.
---

> Internet Information Services (IIS) for Windows® Server is a flexible, secure and manageable Web server for hosting anything on the Web. From media streaming to web applications, IIS's scalable and open architecture is ready to handle the most demanding tasks.

More information on: [https://www.iis.net/](https://www.iis.net/)

## How it works

The plugin gathers global statistics using the performance counter client. No configuration is needed. It captures traffic rates, latencies and response codes of requests sent to the web server by parsing the IIS access log file. See next step for more information.

**The minimal supported version of IIS is 7.0.**

## Installation

{% include_relative _installation.md orchestrator="false" service="IIS" %}

## Configuration

1. Open "Internet Information Services (IIS) Manager"

2. Select the connection to your server.

3. Double click the Logging icon.
![Logging icon location]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/select_logging.png)

4. Select the W3C Format and click Select Fields

    ![W3C format selection]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/w3c_format.png)

5. Select the following fields:
    `cs-uri-stem cs-uri-query sc-status sc-bytes cs-bytes time-taken cs-host`
![W3C format fields]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/w3c_fields1.png)
![W3C format fields]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/w3c_fields2.png)

6. Apply the log format
![Apply format link]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/apply_format.png)

7. Go back to the Server view and restart the IIS service
![Restart server link]({{ site.baseurl}}/gfx/installation/agent/windows/plugin-iis-configuration/restart_server.png)


## Metrics

| Metric name                                                                                                                                                                                                                                         | Metric unit |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| The number of data bytes that have been sent by the Web service (since service startup).                                                                                                                                                            | b           |
| Current bytes temporarily blocked due to bandwidth throttling settings.                                                                                                                                                                             | b           |
| Current requests temporarily blocked due to bandwidth throttling settings.                                                                                                                                                                          | req         |
| IIS the rate files are transferred, that is, sent and received by the Web service.                                                                                                                                                                  | files/s     |
| Measured bandwidth of asynchronous I/O averaged over a minute.                                                                                                                                                                                      | b           |
| Number of data bytes that have been received by the Web service (since service startup).                                                                                                                                                            | b           |
| The current number of CGI requests being simultaneously processed by the Web service.                                                                                                                                                               | req         |
| The current number of connections established with the Web service.                                                                                                                                                                                 | conn        |
| The current number of ISAPI requests being simultaneously processed by the Web service.                                                                                                                                                             | req         |
| The length of time the Web Service has been running.                                                                                                                                                                                                | s           |
| The maximum number of CGI requests simultaneously processed by the Web service (since service startup).                                                                                                                                             | req         |
| The maximum number of concurrent connections established with the Web service (since service startup).                                                                                                                                              | conn        |
| The maximum number of concurrent non-anonymous connections to the Web service (since service startup).                                                                                                                                              | users       |
| The maximum number of ISAPI requests simultaneously processed by the Web service (since service startup).                                                                                                                                           | req         |
| The maximum number of users who established concurrent anonymous connections using the Web service (since service startup).                                                                                                                         | users       |
| The number of all HTTP requests (since service startup).                                                                                                                                                                                            | req         |
| The number of connections that have been attempted using the Web service (since service startup).  This counter is for all instances listed.                                                                                                        | conn        |
| The number of HTTP requests that are not OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, MOVE, COPY, MKCOL, PROPFIND, PROPPATCH, SEARCH, LOCK or UNLOCK methods (since service startup).                                                              | req         |
| The number of HTTP requests using the COPY method (since service startup).  Copy requests are used for copying files and directories.                                                                                                               | req         |
| The number of HTTP requests using the DELETE method (since service startup).  Delete requests are generally used for file removals.                                                                                                                 | req         |
| The number of HTTP requests using the GET method (since service startup).                                                                                                                                                                           | req         |
| The number of HTTP requests using the HEAD method (since service startup).  Head requests generally indicate a client is querying the state of a document they already have to see if it needs to be refreshed.                                     | req         |
| The number of HTTP requests using the LOCK method (since service startup).  Lock requests are used to lock a file for one user so that only that use can modify the file.                                                                           | req         |
| The number of HTTP requests using the MKCOL method (since service startup).  Mkcol requests are used to create directories on the server.                                                                                                           | req         |
| The number of HTTP requests using the MOVE method (since service startup).  Move requests are used for moving files and directories.                                                                                                                | req         |
| The number of HTTP requests using the OPTIONS method (since service startup).                                                                                                                                                                       | req         |
| The number of HTTP requests using the POST method (since service startup).                                                                                                                                                                          | req         |
| The number of HTTP requests using the PROPFIND method (since service startup).  Propfind requests retrieve property values on files and directories.                                                                                                | req         |
| The number of HTTP requests using the PROPPATCH method (since service startup).  Proppatch requests set property values on files and directories.                                                                                                   | req         |
| The number of HTTP requests using the PUT method (since service startup).                                                                                                                                                                           | req         |
| The number of HTTP requests using the SEARCH method (since service startup).  Search requests are used to query the server to find resources that match a set of conditions provided by the client.                                                 | req         |
| The number of HTTP requests using the UNLOCK method (since service startup).  Unlock requests are used to remove locks from files.                                                                                                                  | req         |
| The number of logons attempts to the Web Service (since service startup).                                                                                                                                                                           | #           |
| The number of requests that couldn't be satisfied by the server because the requested document could not be found (since service startup).  These are generally reported as an HTTP 404 error code to the client.                                   | errors      |
| The number of requests that couldn't be satisfied by the server because the requested was locked (since service startup).  These are generally reported as an HTTP 423 error code to the client.                                                    | errors      |
| The number of users who currently have a non-anonymous connection using the Web service.                                                                                                                                                            | users       |
| The number of users who currently have an anonymous connection using the Web service.                                                                                                                                                               | users       |
| The rate CGI requests are received by the Web service.                                                                                                                                                                                              | req/s       |
| The rate data bytes are being sent by the Web service.                                                                                                                                                                                              | b           |
| The rate files are received by the Web service.                                                                                                                                                                                                     | files/s     |
| The rate files are sent by the Web service.                                                                                                                                                                                                         | files/s     |
| The rate HTTP requests are made that do not use the OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, MOVE, COPY, MKCOL, PROPFIND, PROPPATCH, SEARCH, LOCK or UNLOCK methods.                                                                           | req/s       |
| The rate HTTP requests are received.                                                                                                                                                                                                                | req/s       |
| The rate HTTP requests using the COPY method are made.  Copy requests are used for copying files and directories.                                                                                                                                   | req/s       |
| The rate HTTP requests using the DELETE method are made.  Delete requests are generally used for file removals.                                                                                                                                     | req/s       |
| The rate HTTP requests using the GET method are made                                                                                                                                                                                                | req/s       |
| The rate HTTP requests using the HEAD method are made.  Head requests generally indicate a client is querying the state of a document they already have to see if it needs tobe refreshed.                                                          | req/s       |
| The rate HTTP requests using the LOCK method are made.  Lock requests are used to lock a file for one user so that only that user can modify the file.                                                                                              | req/s       |
| The rate HTTP requests using the MKCOL method are made.  Mkcol requests are used to create directories on the server.                                                                                                                               | req/s       |
| The rate HTTP requests using the MOVE method are made.  Move requests are used for moving files and directories.                                                                                                                                    | req/s       |
| The rate HTTP requests using the OPTIONS method are made.                                                                                                                                                                                           | req/s       |
| The rate HTTP requests using the POST method are made.                                                                                                                                                                                              | req/s       |
| The rate HTTP requests using the PROPFIND method are made.  Propfind requests retrieve property values on files and directories.                                                                                                                    | req/s       |
| The rate HTTP requests using the PROPPATCH method are made.  Proppatch requests set property values on files and directories.                                                                                                                       | req/s       |
| The rate HTTP requests using the PUT method are made.                                                                                                                                                                                               | req/s       |
| The rate HTTP requests using the SEARCH method are made.  Search requests are used to query the server to find resources that match a set of conditions provided by the client.                                                                     | req/s       |
| The rate HTTP requests using the TRACE method are made.  Trace requests allow the client to see what is being received at the end of the request chain and use the information for diagnostic purposes.                                             | req/s       |
| The rate HTTP requests using the UNLOCK method are made.  Unlock requests are used to remove locks from files.                                                                                                                                      | req/s       |
| The rate of errors due to requests that couldn't be satisfied by the server because the requested document could not be found.  These are generally reported as an HTTP 404 error code to the client.                                               | errors/s    |
| The rate of errors due to requests that couldn't be satisfied by the server because the requested document was locked.  These are generally reported as an HTTP 423 error code to the client.                                                       | errors/s    |
| The rate that connections to the Web service are being attempted.                                                                                                                                                                                   | conn/s      |
| The rate that data bytes are received by the Web service.                                                                                                                                                                                           | b/s         |
| The rate that ISAPI Extension requests are received by the Web service.                                                                                                                                                                             | req/s       |
| The rate that logons to the Web service are being attempted.                                                                                                                                                                                        | #/s         |
| The rate users are making anonymous connections to the Web service.                                                                                                                                                                                 | users/s     |
| The rate users are making non-anonymous connections to the Web service.                                                                                                                                                                             | users/s     |
| The sum of Bytes Sent/sec and Bytes Received/sec                                                                                                                                                                                                    | b/s         |
| The sum of Files Sent and Files Received (since service startup).                                                                                                                                                                                   | files       |
| The total number of files received by the Web service (since service startup).                                                                                                                                                                      | files       |
| The total number of files sent by the Web service (since service startup).                                                                                                                                                                          | files       |
| The total number of users who established a non-anonymous connection with the Web service (since service startup).                                                                                                                                  | users       |
| The total number of users who established an anonymous connection with the Web service (since service startup).                                                                                                                                     | users       |
| Total bytes blocked due to bandwidth throttling settings (since service startup).                                                                                                                                                                   | b           |
| Total bytes either received or sent by the Web service (since service startup).                                                                                                                                                                     | b           |
| Total ISAPI Extension Requests received (since service startup).                                                                                                                                                                                    | req         |
| Total number of CGI requests (since service startup).                                                                                                                                                                                               | req         |
| Total requests allowed by bandwidth throttling settings (since service startup).                                                                                                                                                                    | req         |
| Total requests rejected due to bandwidth throttling settings (since service startup).                                                                                                                                                               | req         |
| Total requests temporarily blocked due to bandwidth throttling settings (since service startup).                                                                                                                                                    | req         |
| Total Trace Requests is the number of HTTP requests using the TRACE method (since service startup).  Trace requests allow the client to see what is being received at the end of the request chain and use the information for diagnostic purposes. | req         |
