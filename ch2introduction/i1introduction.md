@spark的结构如下 ==>
spark SQL   Spark Streaming  MLib   GraphX

        Spark Core
独立调度器   Yarn        Mesos
----------------------------

@Hadoop并非 Spark 的必要条件，Spark 支持任何实现了 Hadoop 接口的存储系统

@
从上层看，每个spark应用都是由一个驱动器程序(drive program)来发起集群上的各种
并行操作。
drive progam包含应用的main函数，定义集群上的分布式数据集，还对这些分布式数据
集应用来相关操作.

drive program 通过一个sparkcontext访问spark，这个对象代表对计算集群的一个连接。


