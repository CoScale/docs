## Metrics

### GlusterFS 

| Name | Unit | Dimensions |
|------|------|------------|
| GlusterFS services uptime | s | Process |

### GlusterFS / Brick 

| Name | Unit | Dimensions |
|------|------|------------|
| GlusterFS bytes read by clients | b | Brick, Volume, Peer, Client |
| GlusterFS bytes written by clients | b | Brick, Volume, Peer, Client |
| GlusterFS free inodes per brick |  | Brick, Volume, Peer |
| GlusterFS free space per brick | b | Brick, Volume, Peer |
| GlusterFS inodes per brick |  | Brick, Volume, Peer |
| GlusterFS number of clients connected to volume |  | Brick, Volume, Peer |
| GlusterFS number of offline bricks |  | Peer |
| GlusterFS number of online bricks |  | Peer |
| GlusterFS total space per brick | b | Brick, Volume, Peer |
| GlusterFS used space per brick | b | Brick, Volume, Peer |

### GlusterFS / Memory 

| Name | Unit | Dimensions |
|------|------|------------|
| GlusterFS maximum total allocated memory (usmblks) | b | Brick, Volume, Peer |
| GlusterFS memory allocated in mmapped regions (hblkhd) | b | Brick, Volume, Peer |
| GlusterFS memory in freed fastbin blocks (fsmblks) | b | Brick, Volume, Peer |
| GlusterFS non-mmapped memory allocated (arena) | b | Brick, Volume, Peer |
| GlusterFS number of free chunks (ordblks) |  | Brick, Volume, Peer |
| GlusterFS number of free fastbin blocks (smblks) |  | Brick, Volume, Peer |
| GlusterFS number of mmapped regions (hblks) |  | Brick, Volume, Peer |
| GlusterFS top-most releasable memory (keepcost) | b | Brick, Volume, Peer |
| GlusterFS total allocated memory (uordblks) | b | Brick, Volume, Peer |
| GlusterFS total free memory (fordblks) | b | Brick, Volume, Peer |

### GlusterFS / Peer 

| Name | Unit | Dimensions |
|------|------|------------|
| GlusterFS number of bricks per peer |  | Peer |
| GlusterFS peer connected | % | Peer |

### GlusterFS / Volume 

| Name | Unit | Dimensions |
|------|------|------------|
| GlusterFS arbiter count per volume |  | Volume |
| GlusterFS disperse count per volume |  | Volume |
| GlusterFS number of bricks per volume |  | Volume |
| GlusterFS number of replicas per volume |  | Volume |
| GlusterFS number of snapshots per volume |  | Volume |
| GlusterFS number of volumes |  |  |
| GlusterFS number of volumes in status |  | Status |
| GlusterFS rebalance data size | b | Volume |
| GlusterFS rebalance failures count |  | Volume |
| GlusterFS rebalance files count |  | Volume |
| GlusterFS rebalance skipped count |  | Volume |
| GlusterFS redundancy count per volume |  | Volume |
| GlusterFS stripe count per volume |  | Volume |
| GlusterFS subvolume count per volume |  | Volume |

### GlusterFS / Volume / Profile 

| Name | Unit | Dimensions |
|------|------|------------|
| GlusterFS bytes read | b | Brick, Volume, Peer |
| GlusterFS bytes written | b | Brick, Volume, Peer |
| GlusterFS operation call count |  | Brick, Volume, Peer, Operation |
| GlusterFS operation latency | s | Brick, Volume, Peer, Operation |

## Events

| Name | Description | Attributes |
|------|-------------|------------|
| GLUSTERD service state watcher | State watcher | status |
| GLUSTERFS service state watcher | State watcher | status |
| GLUSTERFSD service state watcher | State watcher | status |

