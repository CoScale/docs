## Metrics

### Google Cloud / App Engine 

| Name | Unit | Dimensions |
|------|------|------------|
| Google Cloud App Engine CPU utilization | # | project, resource |
| Google Cloud App Engine memory usage |  | project, resource |
| Google Cloud App Engine received bytes |  | project, resource, cached |
| Google Cloud App Engine Reserved cores | # | project, resource |
| Google Cloud App Engine Sent bytes |  | project, resource, cached |
| Google Cloud CPU megacycles | # | project, resource, source |
| Google Cloud Disk bytes read |  | project, resource |
| Google Cloud Disk bytes written |  | project, resource |
| Google Cloud Instance count | # | project, resource, state |
| Google Cloud Interception count | # | project, resource |
| Google Cloud Memcache operations | # | project, resource, command, status |
| Google Cloud Memcache received bytes |  | project, resource, status, command |
| Google Cloud Memcache sent bytes |  | project, resource, command |
| Google Cloud Memcache utilization | # | project, resource, command |
| Google Cloud Network bytes received. |  | project, resource |
| Google Cloud Network bytes sent. |  | project, resource |
| Google Cloud Quota denial count | # | project, resource |
| Google Cloud Response count | # | project, resource, loading, response_code |
| Google Cloud Response count by style | # | project, resource, dynamic, cached |
| Google Cloud Response latency | s | project, resource, loading, response_code |

### Google Cloud / Cloud SQL 

| Name | Unit | Dimensions |
|------|------|------------|
| Google Cloud Available for failover (Deprecated) | # | project, resource |
| Google Cloud Bytes used |  | project, resource |
| Google Cloud CPU reserved cores | # | project, resource |
| Google Cloud cumulative CPU usage | s | project, resource |
| Google Cloud Disk quota |  | project, resource |
| Google Cloud Disk read IO | # | project, resource |
| Google Cloud Disk utilization | # | project, resource |
| Google Cloud InnoDB dirty pages | # | project, resource |
| Google Cloud InnoDB free pages | # | project, resource |
| Google Cloud InnoDB fsync calls | # | project, resource |
| Google Cloud InnoDB log fsync calls | # | project, resource |
| Google Cloud InnoDB pages read | # | project, resource |
| Google Cloud InnoDB pages written | # | project, resource |
| Google Cloud InnoDB total pages | # | project, resource |
| Google Cloud Memory quota |  | project, resource |
| Google Cloud Memory utilization | # | project, resource |
| Google Cloud MySQL connections | # | project, resource |
| Google Cloud Queries | # | project, resource |
| Google Cloud Questions | # | project, resource |
| Google Cloud Replica lag | s | project, resource |
| Google Cloud Server up | # | project, resource |
| Google Cloud Slave I/O thread running |  | project, resource |
| Google Cloud Slave SQL thread running |  | project, resource |
| Google Cloud SQL CPU utilization | # | project, resource |
| Google Cloud SQL Memory usage |  | project, resource |
| Google Cloud SQL Sent bytes |  | project, resource, destination |
| Google Cloud SQL uptime | s | project, resource |
| Google Cloud State |  | project, resource |
| Google Cloud Write operations | # | project, resource |

### Google Cloud / Cloud Tasks 

| Name | Unit | Dimensions |
|------|------|------------|
| Google Cloud API requests | # | project, resource, api_method, response_code |
| Google Cloud Task attempt count | # | project, resource, response_code |
| Google Cloud Task attempt delays | s | project, resource |

### Google Cloud / Compute 

| Name | Unit | Dimensions |
|------|------|------------|
| Google Cloud Compute received bytes |  | project, resource, instance_name, loadbalanced |
| Google Cloud CPU usage | s | project, resource, instance_name |
| Google Cloud CPU utilization | # | project, resource, instance_name |
| Google Cloud Disk read bytes |  | project, resource, instance_name, device_name, storage_type, device_type |
| Google Cloud Disk read operations | # | project, resource, instance_name, device_name, storage_type, device_type |
| Google Cloud Disk write bytes |  | project, resource, instance_name, device_name, storage_type, device_type |
| Google Cloud Disk write operations | # | project, resource, instance_name, device_name, storage_type, device_type |
| Google Cloud Dropped bytes |  | project, resource, instance_name |
| Google Cloud Dropped packets | # | project, resource, instance_name |
| Google Cloud Received packets | # | project, resource, instance_name, loadbalanced |
| Google Cloud Sent bytes |  | project, resource, instance_name, loadbalanced |
| Google Cloud Sent packets | # | project, resource, instance_name, loadbalanced |
| Google Cloud SQL Reserved cores | # | project, resource, instance_name |
| Google Cloud Throttled read bytes |  | project, resource, instance_name, device_name, storage_type, device_type, throttle_reason |
| Google Cloud Throttled read operations | # | project, resource, instance_name, device_name, storage_type, device_type, throttle_reason |
| Google Cloud Throttled write bytes |  | project, resource, instance_name, device_name, storage_type, device_type, throttle_reason |
| Google Cloud Throttled write operations | # | project, resource, instance_name, device_name, storage_type, device_type, throttle_reason |
| Google Cloud Uptime | s | project, resource, instance_name |

### Google Cloud / Container 

| Name | Unit | Dimensions |
|------|------|------------|
| Google Cloud Container CPU usage | s | project, resource |
| Google Cloud Container CPU utilization | # | project, resource |
| Google Cloud Container uptime | s | project, resource |
| Google Cloud Disk capacity |  | project, resource, device_name |
| Google Cloud Disk usage |  | project, resource, device_name |
| Google Cloud Memory limit |  | project, resource |
| Google Cloud Memory usage |  | project, resource, memory_type |
| Google Cloud Page faults | # | project, resource, fault_type |
| Google Cloud Reserved cores | # | project, resource |

### Google Cloud / Interconnect 

| Name | Unit | Dimensions |
|------|------|------------|
| Google Cloud Circuit operational status |  | project, resource, link_id |
| Google Cloud Circuit receive power | # | project, resource, link_id |
| Google Cloud Circuit transmit power | # | project, resource, link_id |
| Google Cloud Egress bytes |  | project, resource |
| Google Cloud Egress errors | errors | project, resource |
| Google Cloud Egress packets | # | project, resource |
| Google Cloud Egress unicast packets | # | project, resource |
| Google Cloud Ingress bytes |  | project, resource |
| Google Cloud Ingress errors | errors | project, resource |
| Google Cloud Ingress packets | # | project, resource |
| Google Cloud Ingress unicast packets | # | project, resource |
| Google Cloud Interconnect dropped packets | # | project, resource |
| Google Cloud Interconnect Egress bytes |  | project, resource |
| Google Cloud Interconnect ingress bytes |  | project, resource |
| Google Cloud Network capacity | #/s | project, resource |
| Google Cloud Operational status |  | project, resource |

### Google Cloud / Loadbalancing 

| Name | Unit | Dimensions |
|------|------|------------|
| Google Cloud Backend latency | s | project, resource, protocol, response_code, response_code_class, proxy_continent, cache_result, client_country |
| Google Cloud Closed connections | # | project, resource, proxy_continent, client_country |
| Google Cloud Frontend RTT | s | project, resource, proxy_continent, client_country |
| Google Cloud Loadbalancing Egress bytes |  | project, resource, proxy_continent, client_country |
| Google Cloud Loadbalancing frontend RTT | s | project, resource, proxy_continent, client_country |
| Google Cloud Loadbalancing ingress bytes |  | project, resource, proxy_continent, client_country |
| Google Cloud New connections opened | # | project, resource, proxy_continent, client_country |
| Google Cloud Open connections | # | project, resource, proxy_continent, client_country |
| Google Cloud Request bytes |  | project, resource, protocol, response_code, response_code_class, proxy_continent, cache_result, client_country |
| Google Cloud Request count | # | project, resource, protocol, response_code, response_code_class, proxy_continent, cache_result, client_country |
| Google Cloud Response bytes |  | project, resource, protocol, response_code, response_code_class, proxy_continent, cache_result, client_country |
| Google Cloud Total latency | s | project, resource, protocol, response_code, response_code_class, proxy_continent, cache_result, client_country |

