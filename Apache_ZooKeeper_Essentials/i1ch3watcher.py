import logging
import signal
from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch
from time import sleep


# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


zoo_path = '/MyPath'
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
zk.ensure_path(zoo_path)

@zk.ChildrenWatch(zoo_path)
def child_watch_func(children):
    print("List of Children %s" % children)

while True:
    signal.pause()
