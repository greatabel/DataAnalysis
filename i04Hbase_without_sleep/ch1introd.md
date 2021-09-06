#--------- CAP理论 --------- 
Consistency   一致性：数据一致更新，所有数据变动都是同步的
Availability  可用性：良好的响应性能
Partition tolerance 分区容错性: 可靠性

任何分布式系统只可同时满足2点，没法子3者兼顾

架构师不要将精力浪费在如何设计能满足3者的完美分布式系统，而是应该进行取舍

#---------  --------- 
HBase并不快，只是当数据量很大时候它慢得不明显


Base有两种服务器:Master服务器和RegionServer服务器

一般一个HBase集群有一个Master服务器和几个RegionServer服务 器。
Master服务器负责维护表结构信息，实际的数据都存储在 RegionServer服务器上

HBase有一点很特殊:客户端获取数据由客户端直连RegionServer 的，
所以你会发现Master挂掉之后你依然可以查询数据，但就是不能新 建表了。

#--------- Region --------- 
Region就是一段数据的集合。HBase中的表一般拥有一个到多个 Region。Region有以下特性:

Region不能跨服务器，一个RegionServer上有一个或者多个 Region。 

数据量小的时候，一个Region足以存储所有数据;但是，当数据量大的时候，HBase会拆分Region。 

当HBase在进行负载均衡的时候，也有可能会从一台 RegionServer上把Region移动到另一台RegionServer上。 Region是基于HDFS的，它的所有数据存取操作都是调用了HDFS的 客户端接口来实现的。



















