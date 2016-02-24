---
layout: page
title: Internet Information Services plugin
description: Information on the metrics collected by the CoScale IIS plugin.
---

## Installation

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

|                    Metric name                  |           Metric unit            |
|-------------------------------------------------|----------------------------------|
| IIS current Anonymous Users                     | Amount of users                  |
| IIS anonymous Users/sec                         | Amount of users per second       |
| IIS total Anonymous Users                       | Amount of users                  |
| IIS maximum Anonymous Users                     | Amount of users                  |
| IIS current NonAnonymous Users                  | Amount of users                  |
| IIS nonAnonymous Users/sec                      | Amount of users per second       |
| IIS total NonAnonymous Users                    | Amount of users                  |
| IIS maximum NonAnonymous Users                  | Amount of users                  |
| IIS connection Attempts/sec                     | Amount of connections per second |
| IIS total Connection Attempts (all instances)   | Amount of connections            |
| IIS current Connections                         | Amount of connections            |
| IIS maximum Connections                         | Amount of connections            |
| IIS lock Requests/sec                           | Amount of requests per second    |
| IIS total Lock Requests                         | Amount of requests               |
| IIS unlock Requests/sec                         | Amount of requests per second    |
| IIS total Unlock Requests                       | Amount of requests               |
| IIS files Sent/sec                              | Amount of files per second       |
| IIS total Files Sent                            | Amount of files                  |
| IIS logon Attempts/sec                          |                                  |
| IIS total Logon Attempts                        |                                  |
| IIS files Received/sec                          | Amount of files per second       |
| IIS total Files Received                        | Amount of files                  |
| IIS post Requests/sec                           | Amount of requests per second    |
| IIS total Post Requests                         | Amount of requests               |
| IIS head Requests/sec                           | Amount of requests per second    |
| IIS total Head Requests                         | Amount of requests               |
| IIS delete Requests/sec                         | Amount of requests per second    |
| IIS total Delete Requests                       | Amount of requests               |
| IIS copy Requests/sec                           | Amount of requests per second    |
| IIS total Copy Requests                         | Amount of requests               |
| IIS trace Requests/sec                          | Amount of requests per second    |
| IIS total Trace Requests                        | Amount of requests               |
| IIS mkcol Requests/sec                          | Amount of requests per second    |
| IIS total Mkcol Requests                        | Amount of requests               |
| IIS proppatch Requests/sec                      | Amount of requests per second    |
| IIS total Proppatch Requests                    | Amount of requests               |
| IIS search Requests/sec                         | Amount of requests per second    |
| IIS total Search Requests                       | Amount of requests               |
| IIS move Requests/sec                           | Amount of requests per second    |
| IIS total Move Requests                         | Amount of requests               |
| IIS total Method Requests/sec                   | Amount of requests per second    |
| IIS total Method Requests                       | Amount of requests               |
| IIS put Requests/sec                            | Amount of requests per second    |
| IIS total Put Requests                          | Amount of requests               |
| IIS propfind Requests/sec                       | Amount of requests per second    |
| IIS total Propfind Requests                     | Amount of requests               |
| IIS options Requests/sec                        | Amount of requests per second    |
| IIS total Options Requests                      | Amount of requests               |
| IIS other Request Methods/sec                   | Amount of requests per second    |
| IIS total Other Request Methods                 | Amount of requests               |
| IIS bytes Received/sec                          | Amount of bytes per second       |
| IIS total Bytes Received                        | Amount of bytes                  |
| IIS bytes Sent/sec                              | Amount of bytes                  |
| IIS total Bytes Sent                            | Amount of bytes                  |
| IIS bytes Total/sec                             | Amount of bytes per second       |
| IIS locked Errors/sec                           | Amount of errors per second      |
| IIS total Locked Errors                         | Amount of errors                 |
| IIS total Files Transferred                     | Amount of files                  |
| Files/sec                                       | Amount of files per second       |
| IIS set Requests/sec                            | Amount of requests per second    |
| IIS total Get Requests                          | Amount of requests               |
| IIS current CGI Requests                        | Amount of requests               |
| IIS CGI Requests/sec                            | Amount of requests per second    |
| IIS total CGI Requests                          | Amount of requests               |
| IIS maximum CGI Requests                        | Amount of requests               |
| IIS service Uptime                              | Amount of seconds                |
| IIS total Bytes Transferred                     | Amount of bytes                  |
| IIS not Found Errors/sec                        | Amount of errors per second      |
| IIS total Not Found Errors                      | Amount of errors                 |
| IIS current blocked bandwidth bytes.            | Amount of bytes                  |
| IIS total blocked bandwidth bytes.              | Amount of bytes                  |
| IIS measured Async I/O Bandwidth Usage          |                                  |
| IIS total Allowed Async I/O Requests            | Amount of requests               |
| IIS current Blocked Async I/O Requests          | Amount of requests               |
| IIS total Blocked Async I/O Requests            | Amount of requests               |
| IIS total Rejected Async I/O Requests           | Amount of requests               |
| IIS current ISAPI Extension Requests            | Amount of requests               |
| IIS ISAPI Extension Requests/sec                | Amount of requests per second    |
| IIS total ISAPI Extension Requests              | Amount of requests               |
| IIS maximum ISAPI Extension Requests            | Amount of requests               |
