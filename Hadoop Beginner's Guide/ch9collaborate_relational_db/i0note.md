
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

ubuntu 18.04 下面：
在'/etc/mysql/my.cnf' 
添加：
[mysqld]
secure-file-priv=""

----------------------- ----------------------- -----------------------

把数据导出到文件：
use hadooptest;

select first_name ,dept from employees INTO OUTFILE "/tmp/out.csv" FIELDS TERMINATED by ',' LINES TERMINATED BY '\n'; 

----------------------- ----------------------- -----------------------
Sqoop1.4.1之后，不会对Hadoop产生依赖关系

https://mirror-hk.koddos.net/apache/sqoop/1.4.7/
下载了：sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz

https://www.jianshu.com/p/44ffe378c69a
https://thecloudinternals.com/?p=1358


查询mysql数据库：
sqoop list-databases --connect jdbc:mysql://127.0.0.1:3306/hadooptest --username root --password abel1024  
结果如下：
I and manual loading of the driver class is generally unnecessary.
information_schema
hadooptest
hive
hx_vm
mysql
performance_schema
sys


先删除重复的hdfs：hdfs dfs -rm -r  /user/abel/employees

然后执行如下 导入mysql数据到hdfs：
sqoop import --connect jdbc:mysql://127.0.0.1:3306/hadooptest --username root --password abel1024  --table employees --bindir /opt/sqoop/

查询确认下：
hadoop fs -cat /user/abel/employees/part-m-00000

















