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

@ 有当你的整个数据集能在单台机器的内存中放得下时，才能使用 collect()
在大多数情况下，RDD 不能通过 collect() 收集到驱动器进程中，因为它们一般都很大。
此时，我们通常要把数据写到诸如 HDFS 或 Amazon S3 这样的分布式存储系统。
你可以使用 saveAsTextFile()、saveAsSequenceFile()，
或者任意的其他行动操作来把 RDD 的数据内容以各种自带的格式保存起来

@RDD 的转化操作都是惰性求值的。这意味着在被调用行动操作之前 Spark 不会开始计算。
这对新用户来说可能与直觉有些相违背之处，但是对于那些使用过诸如 Haskell 等函数式语言或者
类似 LINQ 这样的数据处理框架的人来说，会有些似曾相识。

@ Spark常见的数据源：
    文件格式和文件系统：Spark 可以访问很多种不同的文件格式，包括文本文件、JSON、SequenceFile，
以及 protocol buffer
    Spark SQL 它针对包括 JSON 和 Apache Hive 在内的结构化数据源，为我们提供了一套更加简洁高效的 API
    Spark 自带的库和一些第三方库，它们可以用来连接 Cassandra、HBase、Elasticsearch 以及 JDBC 源

@6.2 累加器 和 广播变量
通常在向 Spark 传递函数时，比如使用 map() 函数或者用 filter() 传条件时，
可以使用驱动器程序中定义的变量，但是集群中运行的每个任务都会得到这些变量的一份新的副本，
更新这些副本的值也不会影响驱动器中的对应变量。Spark的两个共享变量，“累加器与广播变量”
分别为结果聚合与广播这两种常见的通信模式突破了这一限制。

@7.1  park 集群采用的是主 / 从结构。在一个 Spark 集群中，
有一个节点负责中央协调，调度各个分布式工作节点。这个中央协调节点被称为驱动器（Driver）节点，
与之对应的工作节点被称为执行器（executor）节点。驱动器节点可以和大量的执行器节点进行通信，
它们也都作为独立的 Java 进程运行。驱动器节点和所有的执行器节点一起被称为一个 Spark 应用（application）。

Spark 应用通过一个叫作集群管理器（Cluster Manager）的外部服务在集群中的机器上启动。
Spark 自带的集群管理器被称为独立集群管理器。
Spark 也能运行在 Hadoop YARN 和 Apache Mesos 这两大开源集群管理器上


@






































