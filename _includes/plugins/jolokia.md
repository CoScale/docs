## Metrics

### Jolokia 

| Name | Unit | Dimensions |
|------|------|------------|
| Jolokia active check latency | s |  |
| Jolokia active check uptime | % |  |
| Jolokia Uptime | ms | Endpoint |

### Jolokia / Buffer Pool 

| Name | Unit | Dimensions |
|------|------|------------|
| Jolokia BufferPool Count |  | Endpoint, BufferPool |
| Jolokia BufferPool Memory Used | b | Endpoint, BufferPool |

### Jolokia / Classes 

| Name | Unit | Dimensions |
|------|------|------------|
| Jolokia Loaded Class Count |  | Endpoint |
| Jolokia Unloaded Class Count |  | Endpoint |

### Jolokia / CPU 

| Name | Unit | Dimensions |
|------|------|------------|
| Jolokia Compilation Time | ms | Endpoint |
| Jolokia Process CPU time | ms | Endpoint |

### Jolokia / Garbage Collection 

| Name | Unit | Dimensions |
|------|------|------------|
| Jolokia Garbage Collections |  | Endpoint, Collector |
| Jolokia GC Collection Time | ms | Endpoint, Collector |

### Jolokia / Memory 

| Name | Unit | Dimensions |
|------|------|------------|
| Jolokia Memory Usage Committed | b | Endpoint, MemoryPool |
| Jolokia Memory Usage Init | b | Endpoint, MemoryPool |
| Jolokia Memory Usage Max | b | Endpoint, MemoryPool |
| Jolokia Memory Usage Used | b | Endpoint, MemoryPool |

### Jolokia / Open files 

| Name | Unit | Dimensions |
|------|------|------------|
| Jolokia Max File Descriptor Count |  | Endpoint |
| Jolokia Open File Descriptor Count |  | Endpoint |

### Jolokia / Threads 

| Name | Unit | Dimensions |
|------|------|------------|
| Jolokia Daemon Thread Count |  | Endpoint |
| Jolokia Started Threads |  | Endpoint |
| Jolokia Thread Count |  | Endpoint |
| Jolokia Thread CPU Time | % | Endpoint |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| JOLOKIA service state watcher | State watcher | status |

