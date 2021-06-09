
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


先删除重复的hdfs：
hdfs dfs -rm -r  /user/abel/employees

然后执行如下 导入mysql数据到hdfs：
sqoop import --connect jdbc:mysql://127.0.0.1:3306/hadooptest --username root --password abel1024  --table employees --bindir /opt/sqoop/  -m 1

查询确认下：
hadoop fs -cat /user/abel/employees/part-m-00000

----------------------- ----------------------- -----------------------

配置sqoop 和hive
https://blog.csdn.net/zhu_tianwei/article/details/49022749

hdfs dfs -rm -r  /user/abel/employees

hive -e "show tables like 'employees'"

然后执行如下 导入mysql数据到hdfs：
sqoop import --connect jdbc:mysql://127.0.0.1:3306/hadooptest --username root --password abel1024  --table employees --hive-import --hive-table employees  --bindir /opt/sqoop/  -m 1


检查hive的内容：
hive -e "select * from employees"

结果：
Hive Session ID = 76306faa-d883-4e19-8514-14d288fb418d
OK
Alice	Engineering	50000	2009-03-12
Bob	Sales	35000	2011-10-01
Camille	Marketing	40000	2003-04-20
David	Executive	75000	2001-03-20
Erica	Support	34000	2011-07-07
Time taken: 1.964 seconds, Fetched: 5 row(s)


检查Hive种已创建的数据表
hive -e "describe employees"

I and manual loading of the driver class is generally unnecessary.
Hive Session ID = 956152bc-fe81-45bb-b73a-2f14a21dd147
OK
first_name          	string              	                    
dept                	string              	                    
salary              	int                 	                    
start_date          	string              	                    
Time taken: 1.092 seconds, Fetched: 4 row(s)


#查看文件
hdfs dfs -ls /user/hive/warehouse/employees
hdfs dfs -rm -r  /user/hive/warehouse/employees

hive -e 'drop table employees'


sqoop import --connect jdbc:mysql://127.0.0.1:3306/hadooptest --username root --password abel1024 --target-dir /user/hive/warehouse/employees --query 'select first_name, dept, salary, timestamp(start_date) as start_date from employees where $CONDITIONS' --hive-import --hive-table employees --map-column-hive start_date=timestamp  --bindir /opt/sqoop/  -m 1


hive -e "describe employees"
结果：
Hive Session ID = 6bb6cf83-2663-4ff2-b192-dec53cd58602
OK
first_name          	string              	                    
dept                	string              	                    
salary              	int                 	                    
start_date          	timestamp           	                    
Time taken: 1.097 seconds, Fetched: 4 row(s)


hive -e "select * from employees"
结果：
Hive Session ID = 547b5298-0dcc-4b87-8df1-c5d0fd3800bc
OK
Alice	Engineering	50000	2009-03-12 00:00:00
Bob	Sales	35000	2011-10-01 00:00:00
Camille	Marketing	40000	2003-04-20 00:00:00
David	Executive	75000	2001-03-20 00:00:00
Erica	Support	34000	2011-07-07 00:00:00
Time taken: 1.93 seconds, Fetched: 5 row(s)


----------------------- ----------------------- -----------------------
先传本地文件到hadoop


# 关闭只读模式 
hdfs dfsadmin -safemode leave

# 删除旧的同名数据
hdfs dfs -rm -r /edata/newemployees.tsv

# 在hdfs上创建data目录
hdfs dfs -mkdir /edata

# 上传100w记录的csv
hdfs dfs -copyFromLocal newemployees.tsv /edata

#查看文件
hdfs dfs -ls /edata



#######从Hadoop导出数据

sqoop export --connect jdbc:mysql://127.0.0.1:3306/hadooptest --username root --password abel1024  --table employees --export-dir /edata --input-fields-terminated-by '\t'  --bindir /opt/sqoop/  -m 1

查看：
echo "select count(*) from employees" | mysql -u root -p hadooptest
输出：
Enter password: 
count(*)
5



----------------------- ----------------------- -----------------------
Sqoop导入和导出的区别

sqoop导入数据时，Sqoop对数据结构和数据类型了解更详细一些，
但是导出数据时，Sqoop只知道源文件位置以及字段和记录分隔符。

此外Sqoop导入数据可根据源数据表的名称和结构自动新建一个Hive数据表，
但只能把导出数据插入关系数据库已有数据表














































