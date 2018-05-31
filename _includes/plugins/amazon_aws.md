## Metrics

### Amazon / EC2 

| Name | Unit | Dimensions |
|------|------|------------|
| CPUCreditBalance | Count |  |
| CPUCreditUsage | Count |  |
| CPUSurplusCreditBalance | Count |  |
| CPUSurplusCreditsCharged | Count |  |
| CPUUtilization | Percent |  |
| DiskReadBytes | Bytes |  |
| DiskReadOps | Count |  |
| DiskWriteBytes | Bytes |  |
| DiskWriteOps | Count |  |
| NetworkIn | Bytes |  |
| NetworkOut | Bytes |  |
| NetworkPacketsIn | Count |  |
| NetworkPacketsOut | Count |  |
| StatusCheckFailed | Count |  |
| StatusCheckFailed_Instance | Count |  |
| StatusCheckFailed_System | Count |  |

### AWS / ApplicationELB 

| Name | Unit | Dimensions |
|------|------|------------|
| AWS/ApplicationELB:ActiveConnectionCount | Count | LoadBalancer |
| AWS/ApplicationELB:HealthyHostCount | Count | TargetGroup, LoadBalancer, AvailabilityZone |
| AWS/ApplicationELB:HTTPCode_Target_2XX_Count | Count | TargetGroup, LoadBalancer, AvailabilityZone |
| AWS/ApplicationELB:NewConnectionCount | Count | LoadBalancer |
| AWS/ApplicationELB:RequestCount | Count | TargetGroup, LoadBalancer, AvailabilityZone |
| AWS/ApplicationELB:RequestCountPerTarget | None | TargetGroup, LoadBalancer |
| AWS/ApplicationELB:TargetResponseTime | Seconds | TargetGroup, LoadBalancer, AvailabilityZone |
| AWS/ApplicationELB:UnHealthyHostCount | Count | TargetGroup, LoadBalancer, AvailabilityZone |

### AWS / DynamoDB 

| Name | Unit | Dimensions |
|------|------|------------|
| AWS/DynamoDB:ProvisionedReadCapacityUnits | Count | TableName |
| AWS/DynamoDB:ProvisionedWriteCapacityUnits | Count | TableName |

### AWS / EBS 

| Name | Unit | Dimensions |
|------|------|------------|
| AWS/EBS:BurstBalance | Percent | VolumeId |
| AWS/EBS:VolumeIdleTime | Seconds | VolumeId |
| AWS/EBS:VolumeQueueLength | Count | VolumeId |
| AWS/EBS:VolumeReadOps | Count | VolumeId |
| AWS/EBS:VolumeTotalWriteTime | Seconds | VolumeId |
| AWS/EBS:VolumeWriteBytes | Bytes | VolumeId |
| AWS/EBS:VolumeWriteOps | Count | VolumeId |

### AWS / ElastiCache 

| Name | Unit | Dimensions |
|------|------|------------|
| AWS/ElastiCache:BytesReadIntoMemcached | Bytes | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:BytesUsedForCacheItems | Bytes | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:BytesUsedForHash | Bytes | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:BytesWrittenOutFromMemcached | Bytes | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CasBadval | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CasHits | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CasMisses | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CmdConfigGet | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CmdConfigSet | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CmdFlush | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CmdGet | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CmdSet | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CmdTouch | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CPUUtilization | Percent | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CurrConfig | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CurrConnections | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:CurrItems | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:DecrHits | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:DecrMisses | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:DeleteHits | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:DeleteMisses | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:EvictedUnfetched | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:Evictions | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:ExpiredUnfetched | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:FreeableMemory | Bytes | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:GetHits | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:GetMisses | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:IncrHits | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:IncrMisses | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:NetworkBytesIn | Bytes | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:NetworkBytesOut | Bytes | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:NewConnections | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:NewItems | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:Reclaimed | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:SlabsMoved | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:SwapUsage | Bytes | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:TouchHits | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:TouchMisses | Count | CacheClusterId, CacheNodeId |
| AWS/ElastiCache:UnusedMemory | Bytes | CacheClusterId, CacheNodeId |

### AWS / ELB 

| Name | Unit | Dimensions |
|------|------|------------|
| AWS/ELB:EstimatedALBActiveConnectionCount | Count | LoadBalancerName |
| AWS/ELB:EstimatedALBConsumedLCUs | Count | LoadBalancerName |
| AWS/ELB:EstimatedALBNewConnectionCount | Count | LoadBalancerName |
| AWS/ELB:EstimatedProcessedBytes | Bytes | LoadBalancerName |
| AWS/ELB:HealthyHostCount | Count | AvailabilityZone, LoadBalancerName |
| AWS/ELB:Latency | Seconds | AvailabilityZone, LoadBalancerName |
| AWS/ELB:SurgeQueueLength | Count | AvailabilityZone, LoadBalancerName |
| AWS/ELB:UnHealthyHostCount | Count | AvailabilityZone, LoadBalancerName |

### AWS / Logs 

| Name | Unit | Dimensions |
|------|------|------------|
| AWS/Logs:IncomingBytes | Bytes | LogGroupName |

### AWS / NATGateway 

| Name | Unit | Dimensions |
|------|------|------------|
| AWS/NATGateway:ActiveConnectionCount | Count | NatGatewayId |
| AWS/NATGateway:BytesInFromDestination | Bytes | NatGatewayId |
| AWS/NATGateway:BytesInFromSource | Bytes | NatGatewayId |
| AWS/NATGateway:BytesOutToDestination | Bytes | NatGatewayId |
| AWS/NATGateway:BytesOutToSource | Bytes | NatGatewayId |
| AWS/NATGateway:ConnectionAttemptCount | Count | NatGatewayId |
| AWS/NATGateway:ConnectionEstablishedCount | Count | NatGatewayId |
| AWS/NATGateway:ErrorPortAllocation | Count | NatGatewayId |
| AWS/NATGateway:PacketsInFromSource | Count | NatGatewayId |
| AWS/NATGateway:PacketsOutToDestination | Count | NatGatewayId |

### AWS / RDS 

| Name | Unit | Dimensions |
|------|------|------------|
| AWS/RDS:BinLogDiskUsage by DatabaseClass | Bytes | DatabaseClass |
| AWS/RDS:BinLogDiskUsage by DBInstanceIdentifier | Bytes | DBInstanceIdentifier |
| AWS/RDS:BinLogDiskUsage by EngineName | Bytes | EngineName |
| AWS/RDS:BurstBalance by DatabaseClass | Percent | DatabaseClass |
| AWS/RDS:BurstBalance by DBInstanceIdentifier | Percent | DBInstanceIdentifier |
| AWS/RDS:BurstBalance by EngineName | Percent | EngineName |
| AWS/RDS:CPUCreditBalance | Count | DBInstanceIdentifier |
| AWS/RDS:CPUCreditUsage by DBInstanceIdentifier | Count | DBInstanceIdentifier |
| AWS/RDS:CPUCreditUsage by EngineName | Count | EngineName |
| AWS/RDS:CPUUtilization | Percent | DBInstanceIdentifier |
| AWS/RDS:CPUUtilization by DBInstanceIdentifier | Percent | DBInstanceIdentifier |
| AWS/RDS:DatabaseConnections by DatabaseClass | Count | DatabaseClass |
| AWS/RDS:DatabaseConnections by DBInstanceIdentifier | Count | DBInstanceIdentifier |
| AWS/RDS:DiskQueueDepth | Count | DBInstanceIdentifier |
| AWS/RDS:FreeableMemory by DBInstanceIdentifier | Bytes | DBInstanceIdentifier |
| AWS/RDS:FreeableMemory by EngineName | Bytes | EngineName |
| AWS/RDS:FreeStorageSpace by DatabaseClass | Bytes | DatabaseClass |
| AWS/RDS:FreeStorageSpace by DBInstanceIdentifier | Bytes | DBInstanceIdentifier |
| AWS/RDS:FreeStorageSpace by EngineName | Bytes | EngineName |
| AWS/RDS:NetworkReceiveThroughput | Bytes/Second | DBInstanceIdentifier |
| AWS/RDS:NetworkTransmitThroughput by DBInstanceIdentifier | Bytes/Second | DBInstanceIdentifier |
| AWS/RDS:NetworkTransmitThroughput by EngineName | Bytes/Second | EngineName |
| AWS/RDS:ReadIOPS | Count/Second | DBInstanceIdentifier |
| AWS/RDS:ReadLatency by DatabaseClass | Seconds | DatabaseClass |
| AWS/RDS:ReadLatency by DBInstanceIdentifier | Seconds | DBInstanceIdentifier |
| AWS/RDS:ReadLatency by EngineName | Seconds | EngineName |
| AWS/RDS:ReadThroughput by DatabaseClass | Bytes/Second | DatabaseClass |
| AWS/RDS:ReadThroughput by DBInstanceIdentifier | Bytes/Second | DBInstanceIdentifier |
| AWS/RDS:ReadThroughput by EngineName | Bytes/Second | EngineName |
| AWS/RDS:SwapUsage by DatabaseClass | Bytes | DatabaseClass |
| AWS/RDS:SwapUsage by DBInstanceIdentifier | Bytes | DBInstanceIdentifier |
| AWS/RDS:SwapUsage by EngineName | Bytes | EngineName |
| AWS/RDS:WriteIOPS by DatabaseClass | Count/Second | DatabaseClass |
| AWS/RDS:WriteIOPS by DBInstanceIdentifier | Count/Second | DBInstanceIdentifier |
| AWS/RDS:WriteIOPS by EngineName | Count/Second | EngineName |
| AWS/RDS:WriteLatency by DatabaseClass | Seconds | DatabaseClass |
| AWS/RDS:WriteLatency by DBInstanceIdentifier | Seconds | DBInstanceIdentifier |
| AWS/RDS:WriteLatency by EngineName | Seconds | EngineName |
| AWS/RDS:WriteThroughput by DatabaseClass | Bytes/Second | DatabaseClass |
| AWS/RDS:WriteThroughput by DBInstanceIdentifier | Bytes/Second | DBInstanceIdentifier |

### AWS / VPN 

| Name | Unit | Dimensions |
|------|------|------------|
| AWS/VPN:TunnelDataIn by TunnelIpAddress | Bytes | TunnelIpAddress |
| AWS/VPN:TunnelDataIn by VpnId | Bytes | VpnId |
| AWS/VPN:TunnelDataOut | Bytes | TunnelIpAddress |
| AWS/VPN:TunnelState | None | TunnelIpAddress |

