#终端中启动: 
hbase shell

#hbase shell中展示table:
list

#创建表
create 'mytable', 'cf'
#在'mytable'表的'first'行中的'cf:message'列对应的数据单元中插入字节数组'hello HBase
put 'mytable','first', 'cf:message', 'hello HBase'
put 'mytable','second', 'cf:foo', 0x0
put 'mytable','third','cf:bar',3.14159

get 'mytable', 'first'
scan 'mytable'

#  ------------------------ end of ch1 ------------------------





























