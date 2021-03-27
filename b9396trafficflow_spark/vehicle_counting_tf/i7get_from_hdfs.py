import pydoop.hdfs as hdfs
import csv


b = hdfs.path.isdir('/data')


if b==True :	
	print('---get test ---')
	lines = []
	with hdfs.open('hdfs://127.0.0.1:9000/data/traffic_measurement.csv') as f:
		for line in f:
			# print(line, type(line))
			l = line.decode('utf-8')
			if l is not None and l !='':
				lines.append(l)
	print(lines)
	print('---end get----')
	

	with open("traffic_measurement.csv", 'wb') as myfile:
	    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	    wr.writerow(lines)