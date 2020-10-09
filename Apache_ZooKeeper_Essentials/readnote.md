docker pull zookeeper

docker run --name my-zookeeper --restart always -d zookeeper

 Follower port::2888
 Election port::3888
 AdminServer port::8080

 When a server is on, you can connect via commands：
docker run -it --rm --link my-zookeeper:zookeeper zookeeper zkCli.sh -server zookeeper