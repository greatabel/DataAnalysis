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
