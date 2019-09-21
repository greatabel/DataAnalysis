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


@Spark对数据的核心抽象-- 弹性分布式数据集
Resilient Distributed Dataset 简称RDD，RDD其实就是分布式的元素集合

在Spark中，对数据的操作不外乎是创建RDD 转化已有RDD 调用RDD操作求值

虽然你可以任何时候定义新的RDD，但spark只会惰性计算RDD

默认情况下Spark的RDD会在你每次进行行动操作重新计算，如果想要
多个行动中冲用RDD，可以使用RDD.persist()缓存。
默认不进行持久化，对于大规模数据集很有意义：如果不回冲用RDD，没必要
浪费存储空间，Spark直接遍历一边计算出结果。