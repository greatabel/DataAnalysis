
------------java 版本  ----------

------------使用MultipleInput实现 reduce端联结  ----------
创建文件夹
hadoop fs -mkdir /sales


#查看文件
hdfs dfs -ls /sales

hadoop fs -put sales.txt /sales/sales.txt

hadoop fs -mkdir /accounts

hadoop fs -put accounts.txt /accounts/accounts.txt



javac ReduceJoin.java  -cp $(hadoop classpath)

jar cvf join.jar  *.class
------------
hadoop jar join.jar ReduceJoin /sales /accounts /output30
------------
hadoop fs -cat /output30/part-r-00000
------------
hadoop fs -get /output30/part-r-00000 result.txt
------------
#



------------使用图算法  ----------
hadoop  fs -mkdir /graphin
hadoop fs -put graph.txt /graphin/graph.txt

编译成为jar:
javac GraphPath.java  -cp $(hadoop classpath)
jar -cvf graph.jar *.class
执行mapreduce作业:
hadoop jar graph.jar GraphPath /graphin  /output40
hadoop fs -get /output40/part-r-00000 graph_result.txt