0.


# ---------


1.
安装python3.6 以上版本

2. 
安装pip3 
（如果网速慢 可以pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  把some-package替换成自己的慢的包 )

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.

terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
terminal底执行；
python3 i1polymorphic_network_segmentation.py






# ---- start of requirement -----

1.
多态网络表示： 使用 PolymorphicNetwork 类来表示多态网络。
实现接受一个邻接矩阵

2.
深度优先搜索（DFS）： 实现了一个 depth_first_search
求解最大流

3.
Ford-Fulkerson 算法： 
该算法计算给定图形中的最大流。并返回最大流量值。

4.
计算可靠性
它使用 Ford-Fulkerson 算法计算最小割，并使用该值计算可靠性

5.
测试和性能测量：
我们自己生成出3个多态网络
并测试了可靠性计算的性能。同时记录了算法的运行时间"
- - - - - - - - - - - - - - -
我对第三条进行改进：利用缓存字典进行减少查询或者其他一些裁剪




# ----   end of requirement -----