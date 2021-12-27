unit_types = []
inners = []
parkings = []

'''
1 代表不可达到的区域或者障碍、封锁的区域
0 2 3 4 5 6 7 8分别表示不同类型的街区 可以当作无数据区，居民区，商业区，公共服务，公司企业，教育科研，休闲风景，交通枢纽区
'''


type_0 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 8, 2, 8, 8, 8, 3, 8, 5, 4, 5, 4, 8, 4, 8, 8, 8, 3, 3, 5, 3, 4, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 5, 1, 6, 1, 1, 0, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 4],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 4, 1, 3, 2, 1, 0, 1, 3, 4, 4, 3, 5, 7, 5, 7, 4, 1, 1, 1, 0, 1, 1, 4],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 3, 1, 6, 4, 4, 1, 1, 4, 1, 1, 1, 1, 0, 8, 8, 3, 8, 8, 5, 3],
        [1, 0, 8, 5, 4, 7, 0, 2, 5, 1, 8, 1, 1, 4, 1, 6, 1, 2, 1, 1, 4, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
	[1, 0, 1, 1, 4, 1, 1, 1, 1, 1, 3, 1, 1, 5, 1, 2, 1, 7, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
	[1, 0, 0, 0, 0, 5, 8, 2, 5, 5, 0, 8, 4, 3, 3, 3, 4, 7, 4, 3, 5, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 5],
	[1, 3, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 5, 1, 5, 1, 4, 1, 1, 4, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
	[4, 3, 8, 7, 4, 0, 8, 8, 4, 8, 8, 8, 4, 4, 5, 4, 5, 5, 4, 4, 0, 1, 1, 1, 1, 0, 3, 4, 4, 5, 3, 4, 5],
	[3, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 4, 1, 8, 1, 5, 1, 1, 6, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
	[5, 5, 8, 5, 8, 5, 8, 3, 5, 3, 8, 4, 3, 6, 4, 4, 8, 4, 4, 4, 4, 3, 8, 7, 8, 4, 1, 1, 1, 0, 1, 1, 8],
	[3, 1, 1, 1, 4, 1, 1, 1, 1, 1, 8, 1, 1, 6, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 5, 1, 1, 5],
	[3, 1, 1, 1, 5, 1, 1, 1, 1, 1, 5, 5, 8, 8, 7, 0, 8, 0, 7, 8, 3, 8, 8, 0, 7, 4, 3, 8, 3, 8, 3, 4, 4],
	[3, 1, 1, 1, 5, 1, 1, 1, 1, 1, 8, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 4, 1, 1, 3, 1, 1, 1, 6, 1, 1, 3],
	[3, 1, 1, 1, 5, 1, 1, 1, 1, 1, 3, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 0, 1, 1, 6],
	[3, 3, 5, 3, 3, 4, 5, 4, 3, 4, 3, 8, 4, 4, 4, 4, 4, 4, 3, 4, 4, 5, 4, 4, 3, 4, 7, 4, 4, 3, 4, 4, 8],
    	[3, 1, 1, 1, 1, 1, 8, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 6, 1, 4],
        [3, 1, 1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 7, 1, 3],
	[8, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 4, 3, 4, 3, 7, 4, 7, 3, 3, 3, 4, 4, 4, 4, 4, 1, 1, 1, 1, 2, 1, 6],
	[3, 1, 1, 4, 1, 1, 3, 1, 1, 1, 4, 1, 1, 3, 1, 4, 1, 3, 1, 3, 1, 1, 1, 1, 1, 4, 7, 3, 3, 3, 5, 3, 3],
	[6, 1, 1, 5, 1, 1, 3, 1, 1, 1, 4, 1, 1, 4, 1, 4, 1, 4, 1, 3, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 7, 1, 6],
	[6, 4, 4, 3, 3, 4, 8, 1, 1, 1, 8, 1, 1, 4, 1, 4, 1, 4, 1, 6, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 4],
	[3, 1, 1, 0, 1, 1, 4, 4, 7, 7, 3, 3, 6, 5, 4, 4, 3, 4, 8, 5, 4, 8, 4, 4, 8, 8, 4, 4, 3, 6, 8, 3, 3],
	[3, 3, 1, 4, 1, 1, 7, 1, 1, 1, 4, 1, 1, 3, 1, 4, 1, 3, 1, 4, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 6, 1, 3],
	[1, 2, 7, 4, 8, 1, 3, 1, 1, 1, 6, 1, 1, 4, 1, 4, 1, 4, 1, 4, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 4, 1, 0],
	[1, 1, 1, 1, 4, 3, 3, 3, 3, 3, 4, 4, 4, 4, 6, 4, 3, 7, 3, 4, 3, 3, 4, 3, 4, 4, 5, 8, 4, 6, 3, 6, 8],
	[1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 0, 1, 1, 4, 1, 0, 1, 3, 1, 1, 1, 1, 4, 1, 1, 0, 1, 5, 1, 6, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 3, 6, 5, 1, 2, 3, 3, 6, 1, 6, 1, 4, 1, 1, 1, 1, 3, 1, 1, 7, 1, 4, 4, 3, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 3, 1, 1, 4, 1, 5, 1, 3, 1, 1, 1, 1, 0, 1, 1, 3, 4, 4, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 4, 3, 4, 7, 3, 3, 6, 6, 6, 4, 0, 4, 1, 1, 1, 1, 1, 1, 1],
    ]


heats = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
# type_1 = [
#         [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#         [1, 2, 2, 0, 1, 0, 0, 3, 3, 1],
#         [1, 2, 2, 0, 1, 0, 0, 0, 3, 1],
#         [1, 0, 0, 0, 0, 0, 0, 1, 2, 2],
#         [1, 0, 0, 0, 0, 0, 0, 2, 1, 2],
# 	[1, 1, 1, 0, 1, 0, 2, 2, 2, 2],
# 	[1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
# 	[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
# 	[0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
# 	[1, 0, 1, 0, 0, 0, 1, 4, 4, 1],
# 	[1, 0, 1, 0, 0, 0, 1, 4, 4, 1],
# 	[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     ]



unit_types.append(type_0)
# unit_types.append(type_1)

# 内部封闭区域的入口（比如进入汉阳要上的收费口）的模拟
inners.append([13, 7])

# inners.append([13, 8])
# 停车场模拟，车去那边概率会增加
parkings.append([4, 7])

# parkings.append([4, 8])

