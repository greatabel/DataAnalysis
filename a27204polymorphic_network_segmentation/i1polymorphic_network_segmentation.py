import numpy as np
import networkx as nx
import time

'''

1.多态网络表示： 使用 PolymorphicNetwork 类来表示多态网络。这个类接受一个邻接矩阵作为输入，然后将其转换为 NetworkX 图形。

2.
深度优先搜索（DFS）： 实现了一个 depth_first_search 函数，该函数在给定的残余网络中找到一条从源到汇点的路径。这是求解最大流问题的关键部分。

3.
Ford-Fulkerson 算法： 使用 ford_fulkerson 函数实现了该算法，该算法计算给定图形中的最大流。该函数接受一个 NetworkX 图形，源节点和汇节点作为输入，并返回最大流量值。

4.
计算可靠性： 实现了一个 calculate_reliability 函数，该函数计算给定多态网络的可靠性。它使用 Ford-Fulkerson 算法计算最小割，并使用该值计算可靠性。

4.
测试和性能测量： 使用一个示例邻接矩阵创建了一个多态网络(我们自己生成出2个多态网络），
并测试了可靠性计算的性能。同时记录了算法的运行时间

'''
class PolymorphicNetwork:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.networkx_graph = nx.from_numpy_array(adjacency_matrix)


def depth_first_search(residual_network, source, sink):
    visited = set()
    stack = [(source, float('inf'), [])]

    while stack:
        current_node, current_flow, current_path = stack.pop()

        if current_node == sink:
            return current_path + [sink], current_flow

        visited.add(current_node)

        for neighbor, capacity in enumerate(residual_network[current_node]):
            if neighbor not in visited and capacity > 0:
                next_flow = min(current_flow, capacity)
                stack.append((neighbor, next_flow, current_path + [current_node]))

    return None, 0


# original
def ford_fulkerson(graph, source, sink):
    print('#ford_fulkerson#')
    # 初始化残余网络
    residual_network = graph.copy()
    
    # 初始化最大流量
    max_flow = 0
    
    # 循环直到不存在可行路径
    while True:
        # 使用深度优先搜索找到一条路径
        path, flow = depth_first_search(residual_network, source, sink)
        
        # 如果找不到路径，跳出循环
        if not path:
            break
        
        # 更新残余网络
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            residual_network[u][v] -= flow
            residual_network[v][u] += flow
        
        # 更新最大流量
        max_flow += flow
    
    return max_flow

# with cache version(imporove)
def ford_fulkerson(graph, source, sink, cache=None):
    print('#ford_fulkerson improved with cache #')

    if cache is None:
        cache = {}

    graph_key = tuple(sorted(graph.edges())) # Creates an immutable key

    if graph_key in cache:
        return cache[graph_key]

    # 初始化残余网络
    residual_network = graph.copy()

    # 初始化最大流量
    max_flow = 0

    # 循环直到不存在可行路径
    while True:
        # 使用深度优先搜索找到一条路径
        path, flow = depth_first_search(residual_network, source, sink)

        # 如果找不到路径，跳出循环
        if not path:
            break

        # 更新残余网络
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            residual_network[u][v] -= flow
            residual_network[v][u] += flow

        # 更新最大流量
        max_flow += flow

    cache[graph_key] = max_flow
    return max_flow



def calculate_reliability(network, source, sink):

    cache = {}
    min_cut = ford_fulkerson(network.networkx_graph, source, sink, cache)
    return 1 - min_cut / (min_cut + 1)




# 创建测试数据
adjacency_matrix_1 = np.array([
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1, 0]
])

adjacency_matrix_2 = np.array([
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0]
])

adjacency_matrices = [adjacency_matrix_1, adjacency_matrix_2]

# 测试算法性能
source, sink = 0, 5

for i, adjacency_matrix in enumerate(adjacency_matrices):
    print(f'adjacency_matrix_{i+1}', '=' * 10)
    print(adjacency_matrix)

    # 初始化多态网络
    network = PolymorphicNetwork(adjacency_matrix)

    start_time = time.time()
    reliability = calculate_reliability(network, source, sink)
    elapsed_time = time.time() - start_time

    print("Reliability:", reliability)
    print("Elapsed time:", elapsed_time)
