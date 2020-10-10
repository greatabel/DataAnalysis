from kazoo.client import KazooClient
from time import sleep

zk = KazooClient()
zk.start()
lock = zk.Lock("/lockpath", "my-identifier")
with lock:  # blocks waiting for lock acquisition
    # do something with the lock
    print('get lock')
    sleep(2)

lock = zk.ReadLock("/lockpath", "my-identifier")
with lock:  # blocks waiting for outstanding writers
    # do something with the lock
    print('read lock')