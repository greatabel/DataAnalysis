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
ubuntu上：
sudo apt-get update
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev


4.2
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt

5.
模拟运行在:
python3 i2wsgi.py





6.
浏览器访问：

http://localhost:5000/home

已经注册好的管理员账号 可以直接登录：
管理员1
username: greatabel1@126.com
password: abel

管理员2
admin@126.com   
ps：admin

你也可以自己注册和登录




-------------------
一般用户测试账号:(geust_test)
username:test@126.com
password: test

7.
个人主页： http://localhost:5000/profile









# ------------------------------ 总需求 ------------------------------------

1.、建立云加密理论模型，对模型的可行性进行分析验证
2、选定加密方案并设计基于云计算下加密技术
3、实现从第三方向云端上传文件，（功能1）
并对文件基于关键字进行正确搜索（功能2）（这里文件内容和文件名都是需要加密的）
4、对不同的用户设置不同的搜索权限（比如文件A只需1班的人搜索，2班的人就不能对A文件进行搜索，即使输入了相同的关键字）（功能3）
4、尝试提高搜索算法性能，在大量云端数据中对信息进行搜索
5、尝试从系统模型、效率与安全性方面对算法性能进行探索和改进
6、交互界面功能齐全，美观
——————————
方案：
a.通过设计一套flask api，做加解密，然后云端的服务商不持有密钥就行
这样就算sony一样被hacker了，黑客也无法加解密文件
b. flask网站设计上传功能需要上传带上密钥，然后利用flask api加密密码
c. 用户可以设置服务器防止密钥在内存中的时间和对其他用户的权限
d. 这样根据内存中会过期的密钥副本实现对3，4的控制和搜索功能（搜索的时候会对用户同意的用户临时使用下内存中的密钥授权下关键词搜索）


# ------------------------------ end 总需求 ------------------------------------





