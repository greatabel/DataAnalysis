import logging
from kazoo.client import KazooClient
from kazoo.client import KazooState
from time import sleep


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()


# def my_listener(state):
#     if state == KazooState.LOST:
#         # Register somewhere that the session was lost
#         print('#lost')
#     elif state == KazooState.SUSPENDED:
#         # Handle being disconnected from Zookeeper
#         print('#being disconnected from Zookeeper')
#     else:
#         # Handle being connected/reconnected to Zookeeper
#         print('#being connected/reconnected to Zookeeper')

# zk.add_listener(my_listener)

def children_callback(children):
    print('****' , children)

children = zk.get_children('/zookeeper', children_callback)

# zk.create('/zookeeper/goodboy')
zk.create('/zookeeper/mykey')
# zk.delete('/zookeeper/mykey')
# zk.delete('/zookeeper/goodboy')

while True: 
    sleep(1)