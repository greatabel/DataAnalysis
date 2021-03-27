'''
# python代码是直接调用hdfs接口，如果代码因为未知原因不work时候，
# 还可以使用hdfs的命令，直接处理，具体如下:

# 以 100w条数据的 traffic_measurement.csv 为例子，
直接hdfs的bash 命令的方式， 步骤如下：

# 关闭只读模式 
hdfs dfsadmin -safemode leave

# 删除旧的同名数据
hdfs dfs -rm -r traffic_measurement.csv

# 在hdfs上创建data目录
hdfs dfs -mkdir /data

# 上传100w记录的csv
hdfs dfs -copyFromLocal traffic_measurement.csv data

#查看文件
hdfs dfs -ls /data



'''



'''
 -------------
 
 https://crs4.github.io/pydoop/api_docs/hdfs_api.html#module-pydoop.hdfs
'''

import pydoop.hdfs as hdfs



b = hdfs.path.isdir('/data')


if b==True :
	hdfs_client = hdfs.hdfs()
	data_list = hdfs_client.list_directory('/data')
	print(data_list)

	for item in data_list:
	    print(item['name'])
	    if 'traffic_measurement.csv' in item['name']:
	        print('rm -->', item['name'])
	        hdfs.rm(item['name'], recursive=True, user=None)

	print('---after rm ---')
	data_list = hdfs_client.list_directory('/data')
	print(data_list)



	hdfs.put('traffic_measurement.csv', '/data')
	print('---after put ---')
	data_list = hdfs_client.list_directory('/data')
	print(data_list)


