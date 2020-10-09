docker pull zookeeper

docker run --name my-zookeeper --restart always -d zookeeper

Follower port::2888
Election port::3888
AdminServer port::8080

When a server is on, you can connect via commands：
docker run -it --rm --link my-zookeeper:zookeeper zookeeper zkCli.sh -server zookeeper

docker container stop  my-zookeeper

docker swam run zookeeper
https://hub.docker.com/_/zookeeper

进入docker
docker exec -it zookeeper-xxx(比如 zookeeper_zoo1.1.5jfd3xx2go3ocfyibgs6x4ujb) bash
http://dubbo.apache.org/en-us/blog/dubbo-zk.html