from kazoo.client import KazooClient
from time import sleep

def my_leader_function(name):
    print('#'*10, name)
    sleep(1)

zk = KazooClient()
zk.start()
election = zk.Election("/electionpath", "my-identifier")

# blocks until the election is won, then calls
# my_leader_function()
print('*'*5, election.contenders())
election.run(my_leader_function, 'test')
print('*'*5, election.contenders())