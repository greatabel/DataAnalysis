from kazoo.client import KazooClient
from kazoo.exceptions import KazooException
import logging
from time import sleep


class Client(object):
    def __init__(self):
        logging.basicConfig()
        self.zk = KazooClient(hosts='127.0.0.1:2181')
        self.zk.start()


class Queue(object):
    def __init__(self, root, client=None):
        self.root = root
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
            print("Interrupted exception")

        self.name = ""


    def produce(self, number):
        """
        Add element to the queue.
        :param number:
        :return:
        """
        self.client.zk.create(self.root + "/element", number,  ephemeral=False, sequence=True)
        return True

    def consume(self):
        """
        Remove first element from the queue.
        :return: first element's value
        """
        while True:
            children = self.client.zk.get_children(self.root)
            if len(children) == 0:
                print("Going to wait")
                sleep(1)

            else:
                sequences = [element[7:] for element in children]
                min_number = min(sequences)
                print( "min node: " + self.root + "/element" + min_number)
                value, stat = self.client.zk.get(self.root + "/element" + min_number)
                self.client.zk.delete(self.root + "/element" + min_number)
                print(value)

if __name__ == '__main__':
    q = Queue('testQ')
    q.produce(b'10')
    q.produce(b'20')
    q.consume()
