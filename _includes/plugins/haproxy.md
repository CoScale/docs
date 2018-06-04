## Metrics

### HAProxy 

| Name | Unit | Dimensions |
|------|------|------------|
| HAProxy (check_duration) | ms | HaProxy backend server |
| HAProxy (cli_abrt) | trans | HaProxy backend server |
| HAProxy (comp_byp) | b | HaProxy backend server |
| HAProxy (comp_in) |  | HaProxy backend server |
| HAProxy (comp_out) |  | HaProxy backend server |
| HAProxy (comp_rsp) | b | HaProxy backend server |
| HAProxy (ctime) | ms/rec | HaProxy backend server |
| HAProxy (hanafail) | # | HaProxy backend server |
| HAProxy (last_agt) |  | HaProxy backend server |
| HAProxy (lastsess) | s | HaProxy backend server |
| HAProxy (qtime) | ms/rec | HaProxy backend server |
| HAProxy (rtime) | ms/rec | HaProxy backend server |
| HAProxy (srv_abrt) | trans | HaProxy backend server |
| HAProxy (ttime) | ms/rec | HaProxy backend server |
| HAProxy active check latency | s |  |
| HAProxy active check uptime | % |  |
| HAProxy bytes in (IEEE 1541-2002) (bin) | b | HaProxy backend server |
| HAProxy bytes out (IEEE 1541-2002) (bout) | b | HaProxy backend server |
| HAProxy connection errors (econ) | conn | HaProxy backend server |
| HAProxy current queued requests (qcur) | req | HaProxy backend server |
| HAProxy current sessions (scur) | session | HaProxy backend server |
| HAProxy denied requests (dreq) | req | HaProxy backend server |
| HAProxy denied responses (dresp) | resp | HaProxy backend server |
| HAProxy HTTP requests per second over last elapsed second (req_rate) | req/s | HaProxy backend server |
| HAProxy last status change (in seconds) (lastchg) | change | HaProxy backend server |
| HAProxy max number of HTTP requests per second observed (req_rate_max) | req/s | HaProxy backend server |
| HAProxy max number of new sessions per second (rate_max) | session | HaProxy backend server |
| HAProxy max queued requests (qmax) | req | HaProxy backend server |
| HAProxy max sessions (smax) | session | HaProxy backend server |
| HAProxy number of failed checks (chkfail) | checks | HaProxy backend server |
| HAProxy number of HTTP responses with 1xx code (hrsp_1xx) | session | HaProxy backend server |
| HAProxy number of HTTP responses with 2xx code (hrsp_2xx) | session | HaProxy backend server |
| HAProxy number of HTTP responses with 3xx code (hrsp_3xx) | session | HaProxy backend server |
| HAProxy number of HTTP responses with 4xx code (hrsp_4xx) | session | HaProxy backend server |
| HAProxy number of HTTP responses with 5xx code (hrsp_5xx) | session | HaProxy backend server |
| HAProxy number of HTTP responses with other codes (protocol error) (hrsp_other) | session | HaProxy backend server |
| HAProxy number of sessions per second over last elapsed second (rate) | session | HaProxy backend server |
| HAProxy number of UP->DOWN transitions (chkdown) | change | HaProxy backend server |
| HAProxy queue limit (qlimit) | msg | HaProxy backend server |
| HAProxy redispatches (warning) (wredis) | redis | HaProxy backend server |
| HAProxy request errors (ereq) | req | HaProxy backend server |
| HAProxy response errors (eresp) | resp | HaProxy backend server |
| HAProxy server is active (server), number of active servers (backend) (act) | # | HaProxy backend server |
| HAProxy server is backup (server), number of backup servers (backend) (bck) | # | HaProxy backend server |
| HAProxy server status | % | HaProxy backend server |
| HAProxy sessions limit (slim) | session | HaProxy backend server |
| HAProxy total downtime (downtime) | s | HaProxy backend server |
| HAProxy total number of HTTP requests received (req_tot) | req | HaProxy backend server |
| HAProxy total number of times a server was selected (lbtot) | # | HaProxy backend server |
| HAProxy total sessions (stot) | session | HaProxy backend server |
| HAProxy warm up status (throttle) | % | HaProxy backend server |

### HAProxy / Total 

| Name | Unit | Dimensions |
|------|------|------------|
| HAProxy server is active (server), total number of active servers (backend) (act) (over all backends) |  |  |
| HAProxy server is backup (server), total number of backup servers (backend) (bck) (over all backends) |  |  |
| HAProxy total (check_duration) (over all backends) |  |  |
| HAProxy total downtime (downtime) (over all backends) | s |  |
| HAProxy total max number of HTTP requests per second observed (req_rate_max) (over all backends) |  |  |
| HAProxy total max number of new sessions per second (rate_max) (over all backends) |  |  |
| HAProxy total number of (cli_abrt) (over all backends) |  |  |
| HAProxy total number of (comp_byp) (over all backends) |  |  |
| HAProxy total number of (comp_in) (over all backends) |  |  |
| HAProxy total number of (comp_out) (over all backends) |  |  |
| HAProxy total number of (comp_rsp) (over all backends) |  |  |
| HAProxy total number of (ctime) (over all backends) |  |  |
| HAProxy total number of (hanafail) (over all backends) |  |  |
| HAProxy total number of (last_agt) (over all backends) |  |  |
| HAProxy total number of (lastsess) (over all backends) |  |  |
| HAProxy total number of (qtime) (over all backends) |  |  |
| HAProxy total number of (rtime) (over all backends) |  |  |
| HAProxy total number of (srv_abrt) (over all backends) |  |  |
| HAProxy total number of (ttime) (over all backends) |  |  |
| HAProxy total number of bytes in (IEEE 1541-2002) (bin) (over all backends) | b |  |
| HAProxy total number of bytes out (IEEE 1541-2002) (bout) (over all backends) | b |  |
| HAProxy total number of connection errors (econ) (over all backends) |  |  |
| HAProxy total number of current queued requests (qcur) (over all backends) |  |  |
| HAProxy total number of current sessions (scur) (over all backends) |  |  |
| HAProxy total number of denied requests (dreq) (over all backends) | req |  |
| HAProxy total number of denied responses (dresp) (over all backends) |  |  |
| HAProxy total number of failed checks (chkfail) (over all backends) |  |  |
| HAProxy total number of HTTP requests per second over last elapsed second (req_rate) (over all backends) |  |  |
| HAProxy total number of HTTP requests received (req_tot) (over all backends) |  |  |
| HAProxy total number of HTTP responses with 1xx code (hrsp_1xx) (over all backends) |  |  |
| HAProxy total number of HTTP responses with 2xx code (hrsp_2xx) (over all backends) |  |  |
| HAProxy total number of HTTP responses with 3xx code (hrsp_3xx) (over all backends) |  |  |
| HAProxy total number of HTTP responses with 4xx code (hrsp_4xx) (over all backends) |  |  |
| HAProxy total number of HTTP responses with 5xx code (hrsp_5xx) (over all backends) |  |  |
| HAProxy total number of HTTP responses with other codes (protocol error) (hrsp_other) (over all backends) |  |  |
| HAProxy total number of max queued requests (qmax) (over all backends) |  |  |
| HAProxy total number of max sessions (smax) (over all backends) |  |  |
| HAProxy total number of redispatches (warning) (wredis) (over all backends) |  |  |
| HAProxy total number of request errors (ereq) (over all backends) | req |  |
| HAProxy total number of response errors (eresp) (over all backends) |  |  |
| HAProxy total number of seconds from last status change (lastchg) (over all backends) | s |  |
| HAProxy total number of sessions (stot) (over all backends) |  |  |
| HAProxy total number of sessions limit (slim) (over all backends) |  |  |
| HAProxy total number of sessions per second over last elapsed second (rate) (over all backends) | conn/s |  |
| HAProxy total number of times a server was selected (lbtot) (over all backends) |  |  |
| HAProxy total number of UP->DOWN transitions (chkdown) (over all backends) |  |  |
| HAProxy total queue limit (qlimit) (over all backends) |  |  |
| HAProxy warm up status (throttle) (over all backends) |  |  |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| HAPROXY service state watcher | State watcher | status |

