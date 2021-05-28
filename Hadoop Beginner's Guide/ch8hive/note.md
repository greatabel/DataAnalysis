
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
CREATE TABLE ufodata(sighted string, reported string, sighting_location string,
shape string, duration string, description string);

hadoop 已经存在了：
/data/hadoop-ufo-60000.tsv

2）
LOAD DATA INPATH '/data/hadoop-ufo-60000.tsv' OVERWRITE INTO TABLE ufodata ;

3）
执行查询（不需要进入hive terminal）
hive -e "select count(*) from ufodata;"
-
hive -e "select sighted from ufodata limit 5;"


