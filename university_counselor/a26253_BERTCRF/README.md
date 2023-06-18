1.
安装python3.6 以上版本

2. 
安装pip3 
（如果网速慢 可以pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package  把some-package替换成自己的慢的包 )

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
模拟运行在:
python3 i2wsgi.py

开另外一个命令行，输入：
jupyter notebook i1mytransformaer.ipynb


6.
浏览器访问：
http://localhost:5000/mysimulation

首页在：
http://localhost:5000/home


已经注册好的管理员账号 可以直接登录：
管理员1
username: greatabel1@126.com
password: abel
你也可以自己注册和登录


-------------------
一般用户测试账号:(geust_test)
username:test@126.com
password: test

7.
个人主页： http://localhost:5000/profile









# ------------------------------ 总需求 ------------------------------------

1.
从知识库中提取实体描述。挖掘知识库中实体的描述文本，将实体名字转换为向量表示。

2.
利用名称字典兀配技术，在短文本中识别出候选实体。结合实体描述向量和BERT模型（如bert-base-chinese），完成实体识别任务。

3.
使用BERT-ENE模型与BERT-CRF模型相融合的方法。针对实体消歧子任务，将其视为二分类问题。通过基于BERT的二分类模型对候选实体进行预测，然后对预测的概率进行排序，进而完成消歧任务。

4.

数据集我估计不下载，是从哈工大随便找个实体抽取的数据集挑选一部分先用一下

5.
知识图谱并不需要用neo4j，可视化知识图谱我打算基于numpy+json+d3自己撸一个，更快速，
我们的数据量不需要上neo4j

6.
（可选）
基于transformers实现，但是因为我们用到了transformers，那么需要网络流场，
最好有代理你需要，链接Hugging Face去下载模型，至少1G+吧。
部署方案和部署脚本我会提前写给你，但是如果不行，建议你直接购买包远程部署的服务，我去到时候给你用付费代理下安装）

部署方案是买家提前自己在windows上用wsl2 （ubuntu18.04）或者买家有自己的macbook也可以

7.
那你增加一个功能7
把算法系统化：
1. 账号系统
2. web平台把算法做的过程通过ipynb之类合成进来
3. 把算法分析的结果通过知识图谱可视化出来
4. 把要分析的短文本管理起来


# ------------------------------ end 总需求 ------------------------------------





