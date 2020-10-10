# http://gsy.github.io/2016/04/17/python-zookeeper.html

# encoding: utf-8
__author__ = 'guang'

import unittest
# from barrier import Barrier
import threading
import time
# encoding: utf-8
__author__ = 'guang'
from kazoo.client import KazooClient
from kazoo.exceptions import KazooException
import logging


class Client(object):
    def __init__(self):
        logging.basicConfig()
        self.zk = KazooClient(hosts='127.0.0.1:2181')
        self.zk.start()

class Barrier(object):
    def __init__(self, root, size, client=None):
        """
        :param root: 父节点目录
        :param size: Barrier等待的操作的数目
        :param client: zookeeper客户端
        :return:
        """
        self.root = root
        self.size = size
        if client is None:
            self.client = Client()
        else:
            self.client = client

        try:
            stat = self.client.zk.exists(self.root, watch=False)
            if stat is None:
                self.client.zk.create(self.root, value=b"", acl=None, ephemeral=False)
        except KazooException as e:
            print("Keeper exception when instantiating queue: " + e)
        except KeyboardInterrupt:
            print( "Interrupted exception")

        self.name = ""

    def join(self, name):
        self.client.zk.create(self.root + '/' + name, value=b'', acl=None, ephemeral=True, sequence=False)
        while True:
            children = self.client.zk.get_children(self.root)
            if len(children) >= self.size:
                return True

    def leave(self, name):
        self.client.zk.delete(self.root + '/' + name)
        while True:
            children = self.client.zk.get_children(self.root)
            if len(children) <= 0:
                return True




class CarDriveTest(unittest.TestCase):

    def test_drive_independent(self):

        def drive_to_seattle(name, time_to_gas_station):
            print("{0} Leaving House".format(name))

            time.sleep(time_to_gas_station)

            print("{0} Arrived at Gas Station".format(name) )

            print( "{0} Leaving for Seattle".format(name) )

        charlie = threading.Thread(group=None, target=drive_to_seattle, name="charlie", args=("charlie", 1), kwargs={})
        charlie.run()

        mac = threading.Thread(group=None, target=drive_to_seattle, name="mac", args=("mac", 2), kwargs={})
        mac.run()

        dennis = threading.Thread(group=None, target=drive_to_seattle, name="dennis", args=("dennis", 3), kwargs={})
        dennis.run()

    def test_drive_together(self):

        def drive_to_seattle(name, time_to_gas_station):
            b.join(name)
            print("{0} Leaving House".format(name))

            time.sleep(time_to_gas_station)

            print( "{0} Arrived at Gas Station".format(name) )
            b.leave(name)

            print( "{0} Leaving for Seattle".format(name) )

        b = Barrier("drive_to_seattle", 2)

        charlie = threading.Thread(group=None, target=drive_to_seattle, name="charlie", args=("charlie", 1), kwargs={})
        charlie.start()

        mac = threading.Thread(group=None, target=drive_to_seattle, name="mac", args=("mac", 2), kwargs={})
        mac.start()

        dennis = threading.Thread(group=None, target=drive_to_seattle, name="dennis", args=("dennis", 3), kwargs={})
        dennis.run()




if __name__ == '__main__':
    unittest.main()