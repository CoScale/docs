---
layout: page
title: HAProxy plugin metrics
description: Information on the metrics collected by the CoScale HAProxy plugin.
---

The CoScale HAProxy plugin collects the following metrics:


|                                    Metric name                                        |       Metric unit       |
|---------------------------------------------------------------------------------------|-------------------------|
| HAProxy total number of HTTP requests received (req_tot) on %s                        |                         |
| HAProxy number of HTTP responses with 1xx code (hrsp_1xx) on %s                       |                         |
| HAProxy number of HTTP responses with 2xx code (hrsp_2xx) on %s                       |                         |
| HAProxy number of HTTP responses with 3xx code (hrsp_3xx) on %s                       |                         |
| HAProxy number of HTTP responses with 4xx code (hrsp_4xx) on %s                       |                         |
| HAProxy number of HTTP responses with 5xx code (hrsp_5xx) on %s                       |                         |
| HAProxy number of HTTP responses with other codes (protocol error) (hrsp_other) on %s |                         |
| HAProxy response errors (eresp) on %s                                                 |                         |
| HAProxy denied responses (dresp) on %s                                                |                         |
| HAProxy request errors (ereq) on %s                                                   |                         |
| HAProxy denied requests (dreq) on %s                                                  |                         |
| HAProxy connection errors (econ) on %s                                                |                         |
| HAProxy total downtime (downtime) on %s                                               | Amount of seconds       |
| HAProxy current sessions (scur) on %s                                                 |                         |
| HAProxy total sessions (stot) on %s                                                   |                         |
| HAProxy sessions limit (slim) on %s                                                   |                         |
| HAProxy max sessions (smax) on %s                                                     |                         |
| HAProxy warm up status (throttle) on %s                                               |                         |
| HAProxy (comp_out) on %s                                                              |                         |
| HAProxy (rtime) on %s                                                                 |                         |
| HAProxy (ctime) on %s                                                                 |                         |
| HAProxy (qtime) on %s                                                                 |                         |
| HAProxy (ttime) on %s                                                                 |                         |
| HAProxy (hanafail) on %s                                                              |                         |
| HAProxy (lastsess) on %s                                                              |                         |
| HAProxy bytes out (IEEE 1541-2002) (bout) on %s                                       |                         |
| HAProxy (srv_abrt) on %s                                                              |                         |
| HAProxy (last_agt) on %s                                                              |                         |
| HAProxy (cli_abrt) on %s                                                              |                         |
| HAProxy (comp_in) on %s                                                               |                         |
| HAProxy (comp_byp) on %s                                                              |                         |
| HAProxy current queued requests (qcur) on %s                                          |                         |
| HAProxy max queued requests (qmax) on %s                                              |                         |
| HAProxy queue limit (qlimit) on %s                                                    |                         |
| HAProxy server is active (server), number of active servers (backend) (act) on %s     |                         |
| HAProxy server is backup (server), number of backup servers (backend) (bck) on %s     |                         |
| HAProxy (check_duration) on %s                                                        |                         |
| HAProxy (last_chk) on %s                                                              |                         |
| HAProxy number of failed checks (chkfail) on %s                                       |                         |
| HAProxy number of UP->DOWN transitions (chkdown) on %s                                |                         |
| HAProxy last status change (in seconds) (lastchg) on %s                               |                         |
| HAProxy redispatches (warning) (wredis) on %s                                         |                         |
| HAProxy bytes in (IEEE 1541-2002) (bin) on %s                                         |                         |
| HAProxy total number of times a server was selected (lbtot) on %s                     |                         |
| HAProxy (comp_rsp) on %s                                                              |                         |
| HAProxy HTTP requests per second over last elapsed second (req_rate) on %s            |                         |
| HAProxy max number of HTTP requests per second observed (req_rate_max) on %s          |                         |
| HAProxy number of sessions per second over last elapsed second (rate) on %s           |                         |
| HAProxy max number of new sessions per second (rate_max) on %s                        |                         |
