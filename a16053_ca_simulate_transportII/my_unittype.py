unit_types = []
inners = []
parkings = []

'''
1 代表不可达到的区域或者障碍、封锁的区域
0 2 3 4 分别表示不同类型的街区 可以当作居民区，商业区，公共企业商业区，交通枢纽区
'''

# type0 可以当作一个时期的西安街区模拟，具体可以根据实际情况自己修改下面的矩阵
# 目前只是大致的划分，你可以细化
type_0 = [
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 0, 1, 0, 0, 3, 3, 1],
        [1, 2, 2, 0, 1, 0, 0, 0, 3, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 2, 2],
        [1, 0, 0, 0, 0, 0, 0, 2, 1, 2],
		[1, 1, 1, 0, 1, 0, 2, 2, 2, 2],
		[1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 0, 0, 1, 4, 4, 1],
		[1, 0, 1, 0, 0, 0, 1, 4, 4, 1],
		[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

# type0 可以当作一个时期的城市的模拟（或者西安没有大规模基建前的区域），具体可以根据实际情况自己修改下面的矩阵
# 目前只是大致的划分，你可以细化
type_1 = [
        [1, 1, 1, 2, 2, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 3, 3, 3],
        [1, 0, 0, 0, 1, 0, 0, 0, 3, 3],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 2, 1, 1],
		[1, 1, 1, 0, 1, 0, 2, 2, 2, 1],
		[1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
		[0, 0, 1, 0, 0, 0, 1, 0, 0, 3],
		[2, 0, 1, 0, 0, 0, 1, 3, 3, 3],
		[2, 0, 1, 0, 0, 0, 1, 3, 3, 1],
		[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    ]



unit_types.append(type_0)
unit_types.append(type_1)

# 内部封闭区域的入口（比如进入汉阳要上的收费口）的模拟
inners.append([13, 7])
inners.append([13, 8])
# 停车场模拟，车去那边概率会增加
parkings.append([4, 7])
parkings.append([4, 8])

