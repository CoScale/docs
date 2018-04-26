---
layout: page
title: CouchDB plugin
description: Information on the metrics collected by the CoScale CouchDB plugin.
---

> Apache CouchDB is open source database software that focuses on ease of use and having an architecture that "completely embraces the Web". It has a document-oriented NoSQL database architecture and is implemented in the concurrency-oriented language Erlang; it uses JSON to store data, JavaScript as its query language using MapReduce, and HTTP for an API.

More information on: [http://couchdb.apache.org/](http://couchdb.apache.org/)

## How it works

CouchDB CoScale plugin lets you inspect how CouchDB performs. The plugin collects metrics like requests per second, request sizes, http requests methods, CouchDB database reads/writes and a multitude of other useful metrics. This plugins uses the CouchDB API, which is exposed by default and no additional configuration is required.

**The minimal supported version of CouchDB is 1.5**

## Installation

{% include_relative _installation.md orchestrator="false" service="CouchDB" %}

## Configuration

### Active checks

This plugin can be configured to query a view on your CouchDb. This active monitoring allows us to calculate the uptime of the service and the response time of the query.

A database, username, password, design id and view id should be provided.

## Events

* Service state

## Metrics

| Metric name                                                 | Metric unit |
|-------------------------------------------------------------|-------------|
| CouchDb number of HTTP GET requests                         | req/s       |
| CouchDb length of a request inside CouchDB without MochiWeb | s           |
| CouchDb number of authentication cache hits                 | hits/s      |
| CouchDb number of authentication cache misses               | misses/s    |
| CouchDb number of bulk requests                             | req/s       |
| CouchDb number of clients for continuous _changes           | req/s       |
| CouchDb number of file descriptors CouchDB has open         | files/s     |
| CouchDb number of HTTP 200 OK responses                     | req/s       |
| CouchDb number of HTTP 201 Created responses                | req/s       |
| CouchDb number of HTTP 202 Accepted responses               | req/s       |
| CouchDb number of HTTP 301 Moved Permanently responses      | req/s       |
| CouchDb number of HTTP 304 Not Modified responses           | req/s       |
| CouchDb number of HTTP 400 Bad Request responses            | req/s       |
| CouchDb number of HTTP 401 Unauthorized responses           | req/s       |
| CouchDb number of HTTP 403 Forbidden responses              | req/s       |
| CouchDb number of HTTP 404 Not Found responses              | req/s       |
| CouchDb number of HTTP 405 Method Not Allowed responses     | req/s       |
| CouchDb number of HTTP 409 Conflict responses               | req/s       |
| CouchDb number of HTTP 412 Precondition Failed responses    | req/s       |
| CouchDb number of HTTP 500 Internal Server Error responses  | req/s       |
| CouchDb number of HTTP COPY requests                        | req/s       |
| CouchDb number of HTTP DELETE requests                      | req/s       |
| CouchDb number of HTTP HEAD requests                        | req/s       |
| CouchDb number of HTTP POST requests                        | req/s       |
| CouchDb number of HTTP PUT requests                         | req/s       |
| CouchDb number of HTTP requests                             | req/s       |
| CouchDb number of open databases                            | conn/s      |
| CouchDb number of temporary view reads                      | req/s       |
| CouchDb number of times a database was changed              | writes/s    |
| CouchDb number of times a document was read from a database | reads/s     |
| CouchDb number of view reads                                | req/s       |
