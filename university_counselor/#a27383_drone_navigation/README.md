0.



numpy 1.21.2 文档：https://numpy.org/doc/stable/

matplotlib 3.4.3 文档：https://matplotlib.org/stable/contents.html


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
python3 i0drone_navigation.py






# ---- start of requirement -----


我看啦数据和论文这些后，尽量机遇现有的数据和论文，
我们模拟实验主要是py3+numpy+matplot+geopy等库，py的技术栈哈：

1.
主要利用“导航台位置坐标和无人机经过主要点坐标.xlsx”，
建立无人机航点和DME导航台数据模型：根据实际应用场景，建立航点（无人机飞行任务的途经点）和DME导航台的地理位置数据模型。
这些数据可以以经纬度坐标的形式表示，并存储在NumPy里面，也许会增加写塔台，感觉有点过于集中啦

2.
实现DME距离测量和DME/DME定位算法：
根据DME原理，实现无人机与DME导航台之间的距离测量。
基于多个DME导航台的距离测量结果，实现DME/DME定位算法来计算无人机的位置。

3.
模拟无人机沿航点飞行过程：通过将无人机的实际位置与DME/DME定位算法估算的位置进行对比，
模拟无人机在各个航点之间飞行的过程。此过程可以分为多个步骤，模拟无人机在不同航点之间的飞行轨迹。

4.
性能分析与优化：通过可视化实际轨迹与估计轨迹的对比，对DME/DME导航系统的性能进行分析。
为了优化性能，可以尝试增加DME导航台数量、调整导航台布局、提高DME信号精度

# ----   end of requirement -----