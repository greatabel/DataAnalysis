hadoop-ufo-60000.tsv
这个UFO数据集是《Hadoop Beginner's Guide》书上使用的例子

如果hdfs故障
/home/abel/hadoop-3.1.4/sbin下执行: start-all.sh
然后访问：
http://localhost:9870 

上传ufo数据集到hdfs
在ch4文件夹中执行：
hdfs dfs -copyFromLocal hadoop-ufo-60000.tsv /data

查看hdfs的data文件夹: hdfs dfs -ls /data



mapred streaming -input /data/hadoop-ufo-60000.tsv -output /output10  -mapper "python3 wordcount_mapper.py" -reducer "python3 wordcount_reducer.py"



hadoop fs -cat output10/part-00000