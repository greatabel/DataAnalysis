
# - 可以解决红线问题
-

6.1
在hadoop中，故障处理的位置靠前而且是一个核心问题。
Hadoop架构及设计的前提，就是作业执行过程会经常发生故障，并且故障在所难免。

我们通常故障分成5类：
节点故障，也就是DataNode/TaskTracker进程故障
集群主节点故障  NameNode/JobTracker进程故障
硬件故障
MapReduce作业中由软件错误引起个别任务故障
MapReduce作业中由数据问题引发的个别任务故障

-------------
hdfs dfsadmin 命令
hdfs dfsadmin -report

-------------
修改数据块大小从256M设置为4M为：

在hadoop3.14/etc/hadoop/hdfs-site.xml
中加上
    <property>
        <name>dfs.blocksize</name>
        <value>4194304</value>
    </property>


-------------
使用 jps 查看datanode进程id：
$ jps
6161 NameNode
7317 NodeManager
6390 DataNode
6934 ResourceManager
1114 Jps
6671 SecondaryNameNode

-------------
start-all.sh
重启所有节点










