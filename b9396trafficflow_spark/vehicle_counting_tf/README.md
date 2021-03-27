检测部分推荐部署ubuntu或者其他linux，
其他代码可以部署到其他操作系统平台

1.
安装python3.6 以上版本

2. 
安装pip3 

3.
可选（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
根据机器是否有cuda的英伟达显卡，分别安装：
$ pip3 install tensorflow     # Python 3.n; CPU support (no GPU support)

$ pip3 install tensorflow-gpu # Python 3.n; GPU support

检测算法在ubuntu上运行的时候，最好装上python3-dev（不是必须的）
sudo apt-get install python3-pip python3-dev # for Python 3.n

4.2
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip3 install --upgrade -r requirements.txt


5.
terminal 里面cd 到 new_version文件夹

then enter virtual environment:
Windows run:
movie-env\Scripts\activate.bat

Unix/MacOS run:
source movie-env/bin/activate

6.
Ubuntu 18.04 安装 RabbitMQ 和配置：
https://wangxin1248.github.io/linux/2020/03/ubuntu-install-rabbitmq.html
根据博客链接完成第六步的rabgitMQ server运行起来

7.

7.1
开2个命令行窗口 ,分别执行：
python3 i0vehicle_detection_main.py imshow --input_video=input_video1.mp4

python3 i0vehicle_detection_main.py imshow --input_video=input_video.mp4

模拟多路口数据输入和检测

7.2
模拟接收的机器（可以2台）每一台上运行：
python3 i4msg_receiver.py 
python3 i5spark_anlysis.py --placeid=0
和
python3 i4msg_receiver.py 
python3 i5spark_anlysis.py --placeid=1

8.
因为我们没有时序数据，所以我根据traffic_measurement.csv混淆生成了一批带时序的历史数据
保存在i8predict_flow/history_traffic_measurement
（8.1～8.2非必须的步骤，我预测训练和使用的是默认已经从云端下载到本地的数据）

假设本地hadoop已经配置，服务已经运行起来，可以执行：
8.1
上传历史数据岛hadoop, 可以运行 i6put_to_hdfs.py

8.2
从hadoop 下载数据到本地，可以运行 i7get_from_hdfs.py

9.
9.1
如果你想要自己训练，可以运行 i8predict_flow/preduct_train.py（非必须）

我已经给你保存了训练好的模型： finalized_model.sav / myencoders.pkl
可以直接使用.

9.2
新开一个命令行，进入虚拟环境，进入i8predict_flow 下，运行
python3 app.py







