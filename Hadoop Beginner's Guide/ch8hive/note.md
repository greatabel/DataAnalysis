
# - 可以解决红线问题
-

MapReduce是一个功能强大的数据处理范式，能从复杂处理过程中凝练宝贵结论。
借助建立在hadoop基础上的产品，用户能从更高或更熟悉的角度理解存储在HDFS上的数据。


Hive3.1安装
https://blog.csdn.net/aguang_vip/article/details/81583661


# 向Hive导入新数据过程分为3个阶段：
1）定义表各个字段，该表讲用于导入数据
2）把数据导入已创建的表中
3） 针对上表执行HiveQL查询


1）
DROP TABLE ufodata ;
CREATE TABLE ufodata(sighted string, reported string, sighting_location string,
shape string, duration string, description string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t' ;


hadoop 已经存在了：
/data/hadoop-ufo-60000.tsv

2）
LOAD DATA INPATH '/data/hadoop-ufo-60000.tsv' OVERWRITE INTO TABLE ufodata ;

3）
执行查询（不需要进入hive terminal）
hive -e "select count(*) from ufodata;"
-
hive -e "select sighted from ufodata limit 5;"


# hive表是一个逻辑概念
表的创建和数据导入并没有真正引起MapReduce作业的执行

crreate table 和 load data 语句都不会创建实际的表数据，只是生成一些元数据
当Hive使用HiveQL转换成MapReduce作业访问概念上存储在表中的数据时，将会用到这些元数据

------------------------------------------------------------------------------



1)
创建 i2states.hql

DROP TABLE states ;
CREATE EXTERNAL TABLE states(abbreviation string, full_name string)
ROW FORMAT delimited
FIELDS TERMINATED BY '\t'
LOCATION '/tmp/states' ;

2)
先保证：相关数据集已经存在hadoop中:

确保hdfs上文件夹存在
hdfs dfs -mkdir /tmp/states

拷贝到文件夹底下
hdfs dfs -copyFromLocal states.txt /tmp/states/

查询确认
hdfs dfs -ls /tmp/states

3)
执行
hive -f i2states.hql

4)
对刚创建的表进行查询
hive -e "select full_name from states where abbreviation like 'CA' "

应该看到结果：
Logging initialized using configuration in file:/opt/hive-3.1.2/conf/hive-log4j2.properties Async: true
Loading class `com.mysql.jdbc.Driver'. This is deprecated. The new driver class is `com.mysql.cj.jdbc.Driver'. The driver is automatically registered via the SPI and manual loading of the driver class is generally unnecessary.
Hive Session ID = 4a7e8c47-1252-4f11-91fb-4b5994cd4271
OK
California
Time taken: 2.165 seconds, Fetched: 1 row(s)




