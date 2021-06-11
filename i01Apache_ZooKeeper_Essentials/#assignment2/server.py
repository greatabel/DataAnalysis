import multiprocessing
import os
import argparse
from kazoo.client import KazooClient
import time
import uuid
import logging


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
my_id = uuid.uuid4()

print("current pid：",os.getpid())


def parse_args():
    parser = argparse.ArgumentParser(description='Please input parameter')
    parser.add_argument('-host', type=str, default='localhost',

                        help="host")
    parser.add_argument('-port', type=int, default=2181,
                        help='port')
    parser.add_argument('-zookeeper', type=str, default='localhost',
                        help='zookeeper ip')

    parser.add_argument('-zookeeper_port', type=int, default=2181,
                        help='zookeeper port')
    
    args = parser.parse_args()
    return args

def read(key):
    # # 获取某个节点下所有子节点
    # node = zk.get_children('/my_key_value')
    # 获取某个节点对应的值
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()
    value = zk.get(key)
    print(value, '@'*5)
    zk.stop()


def add_and_update(key, value):
    print(key, value, '#'*20)
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()
    # children = zk.get_children('/')


    # 创建节点：makepath 设置为 True ，父节点不存在则创建，其他参数不填均为默认
    # zk.create('/zookeeper/goodboy')
    # 操作完后，别忘了关闭zk连接

    # zk.stop()
    print('#'*20)
    data, stat = zk.get(key)
    print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
    if zk.exists(key):
        zk.set(key, value)
        print('@'*10, 'setting')
    else:
        zk.create(key, value, makepath=True)
    # zk.create(key)


    # print(value, type(value),'#'*10)
    # if value != b"":
    #     zk.set(key, value)
    zk.stop()


def leader_func():
    print("I am the leader {}".format(str(my_id)))

    # while True:
    #     print("{} is working! ".format(str(my_id) ))
    #     time.sleep(1)

# 定义一个函数，准备作为新进程的 target 参数

def action(args, *add):
    print(args)
    for arc in add:
        print("port %s --当前进程%d" % (arc,os.getpid()))

    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()
    election = zk.Election("/electionpath")
    election.run(leader_func)
    zk.stop()
    add_and_update('/zookeeper/mykey', b'this is my value!')
    read('/zookeeper/mykey')

    add_and_update('/zookeeper/mykey', b'this is my setting value!')

if __name__=='__main__':
    # python3 server.py -host localhost -port 2181 -zookeeper localhost -zookeeper_port 2181
    args = parse_args()
    print('args=', args)
    #定义为进程方法传入的参数
    my_tuple = (2181, 2182, 2183)
    #设置进程启动方式
    multiprocessing.set_start_method('spawn')
   
    #创建子进程，执行 action() 函数
    my_process = multiprocessing.Process(target = action, args = (args,*my_tuple))
    #启动子进程
    my_process.start()