
# - 可以解决红线问题
-

RDBMS用作数据库，会遇到数据规模和数据保留问题。
随着数据量增长，如何处理价值不太大的老旧数据？

最近出现新的解决方案，用关系数据库存储最新数据，同时使用Hadoop存储老数据
数据要么以文件形式存储在HDFS上，要么存储在Hive并保留RDBMS接口。

----------------------- ----------------------- -----------------------
创建数据表

create table employees(
first_name varchar(10) primary key, 
dept varchar(15), 
salary int,
start_date date
)

----------------------- ----------------------- -----------------------

把employees.tsv 文件导入数据表

mysql> use hadooptest;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> load data local infile "/home/abel/AbelProject/DataAnalysis/Hadoop Beginner's Guide/ch9collaborate_relational_db/employees.tsv"
    -> into table employees
    -> fields terminated by '\t' lines terminated by '\n';
Query OK, 5 rows affected (0.01 sec)
Records: 5  Deleted: 0  Skipped: 0  Warnings: 0

----------------------- ----------------------- -----------------------

