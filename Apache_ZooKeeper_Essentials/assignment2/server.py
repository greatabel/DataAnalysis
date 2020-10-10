import multiprocessing
import os
import argparse

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


print("current process ID：",os.getpid())
# 定义一个函数，准备作为新进程的 target 参数

def action(name, *add):
    print(name)
    for arc in add:
        print("%s --当前进程%d" % (arc,os.getpid()))


if __name__=='__main__':
    # python3 server.py -host localhost -port 2181 -zookeeper localhost -zookeeper_port 2181
    args = parse_args()
    print('args=', args)
    #定义为进程方法传入的参数
    my_tuple = ("http://c.biancheng.net/python/",\
                "http://c.biancheng.net/shell/",\
                "http://c.biancheng.net/java/")
    #设置进程启动方式
    multiprocessing.set_start_method('spawn')
   
    #创建子进程，执行 action() 函数
    my_process = multiprocessing.Process(target = action, args = ("my_process进程",*my_tuple))
    #启动子进程
    my_process.start()