不同区域的划分划分成不同的元胞区域大小，还是可以这样做：映射不同区域的元胞到多车道 x 线段的，2D矩阵上：
   比如3车道区域在工业区，商业区，居民区可以映射为
   [
    [1,block01],[1,block01]..... [1, block0i],[1, block11],.....[1, block1j]...
    [2,block01],[2,block01]..... [2, block0i],[2, block11],.....[2, block1j]...
    [3,block01],[3,block01]..... [3, block0i],[3, block11],.....[3, block1j]...
   ]
        根据居民区、工作区、商业区实际大小采用不同元胞划分，然后模拟车辆（传统汽油车、电动车【电动车加速更快，加速情况更多】）
可以模拟电动车占比分布，在不同区域元胞不同，在模拟上其实表现的出啦的是：电动车经过不同block时候，
元胞尺寸变化（大小不同，为了方便处理，比如元胞邻居从Moore型，变化为扩展Moore型 在不同街区），
在不同的元胞类型中对于车辆而言：
车速不同，
变道概率不同

然后我们把区域的网络结构图分成若干条经过不同区域的多车道主线路：
比如图中例子整个交通网切割为：崇明岛和地点主干线，环线
然后交界点出可以设定：变道离开车道的概率更大，车速更慢等设定

最终我们模拟的是：
车辆在这些元胞自动机模型模拟在2D环境（多车道，多类型小区，不同长度线）上行驶的状况
在