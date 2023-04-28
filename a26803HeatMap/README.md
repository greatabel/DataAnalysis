0.
操作系统/spark/算法/准备 论文相关素材：

KMeans文档介绍：https://spark.apache.org/docs/latest/ml-clustering.html#k-means
https://blog.csdn.net/chivalrousli/article/details/72639972

Windows上WSL2部署Ubuntu 18.04：
https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps
https://learn.microsoft.com/zh-cn/windows/wsl/install#manual-installation-steps

Ubuntu上Spark的配置文档：
https://spark.apache.org/docs/latest/configuration.html
https://blog.csdn.net/weixin_42001089/article/details/82346367



numpy 1.21.2 文档：https://numpy.org/doc/stable/

matplotlib 3.4.3 文档：https://matplotlib.org/stable/contents.html

pyspark 3.1.2 文档：https://spark.apache.org/docs/latest/api/python/index.html

folium 文档：https://python-visualization.github.io/folium/


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
jupyter notebook i0heatmap.ipynb





# ---- start of requirement -----

对于出租车载客热点区域分析，更适合使用Spark，hadoop可以作为hdfs的存储端（也用得上）：
为分析通常需要处理大量的数据，而Spark的内存计算能力可以很好地处理这些数据。
Spark有许多机器学习和图形分析算法，这些算法可以帮助您进行聚类、分类、回归等操作，
以识别和分析热点区域。map-reduce没法子搞区域和轨迹（不是不行，不适合


# ----   end of requirement -----