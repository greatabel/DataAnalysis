import numpy as np
import networkx as nx
from random import random
import matplotlib.pyplot as plt
import time


class PolymorphicNetwork:
    def __init__(
        self,
        adjacency_matrix,
        node_types=[],
        type_failure_probabilities={},
    ):
        print("node_types", "=" * 20, node_types)  # debug statement
        self.adjacency_matrix = adjacency_matrix
        print("adjacency_matrix=", adjacency_matrix)  # debug statement
        # Move these lines up
        self.networkx_graph = nx.from_numpy_array(
            adjacency_matrix, create_using=nx.DiGraph()
        )
        print(self.networkx_graph.nodes(data=True))  # debug statement
        print("1-" * 10)
        self.networkx_graph = nx.relabel_nodes(
            self.networkx_graph, {i: str(i) for i in range(adjacency_matrix.shape[0])}
        )

        self.node_types = node_types or [0] * adjacency_matrix.shape[0]
        self.type_failure_probabilities = type_failure_probabilities or {}

        # Calculate node failure probabilities based on node types
        node_failure_probabilities = {
            str(i): self.type_failure_probabilities[node_type]
            for i, node_type in enumerate(self.node_types)
        }
        print("@" * 20)
        print(self.node_types)  # debug statement
        print("#" * 10)
        print(
            "node_failure_probabilities==>", node_failure_probabilities
        )  # debug statement

        # Set node attributes: node types and failure probabilities
        nx.set_node_attributes(
            self.networkx_graph,
            dict(enumerate(self.node_types)),
            "node_type",
        )

        nx.set_node_attributes(
            self.networkx_graph,
            {str(i): node_type for i, node_type in enumerate(self.node_types)},
            "node_type",
        )

        nx.set_node_attributes(
            self.networkx_graph,
            node_failure_probabilities,
            "node_failure_probability",
        )


def calculate_edge_reliability(weight):
    return 1 - 1 / (weight + 1)


def depth_first_search(residual_network, source, sink):
    # 创建一个集合以存储访问过的节点
    visited = set()
    # 初始化栈，包含源节点、当前流量和当前路径
    stack = [(source, float("inf"), [])]

    # 当栈不为空时继续搜索
    while stack:
        # 弹出当前节点、当前流量和当前路径
        current_node, current_flow, current_path = stack.pop()

        # 如果当前节点是汇点，返回当前路径和当前流量
        if current_node == sink:
            return current_path + [sink], current_flow

        # 将当前节点添加到访问过的节点集合中
        visited.add(current_node)

        # 遍历当前节点的邻居节点
        # 请注意，我们现在使用了 residual_network.adj[current_node]
        for neighbor, capacity in residual_network.adj[current_node].items():
            # 如果邻居节点没有被访问过且容量大于0，将其添加到栈中
            if neighbor not in visited and capacity["weight"] > 0:
                next_flow = min(current_flow, capacity["weight"])
                stack.append((neighbor, next_flow, current_path + [current_node]))

    # 如果没有找到从源到汇的路径，返回 None 和 0
    return None, 0


def min_cut(graph, source, residual_network):
    # 使用深度优先搜索找到所有可以从源点开始通过有正容量的边到达的节点
    visited = set()
    dfs(residual_network, source, visited)

    # 最小割就是所有从访问过的节点指向未访问过的节点的边
    min_cut_edges = []
    for u in visited:
        for v in set(graph.networkx_graph.nodes()) - visited:
            if graph.networkx_graph.has_edge(u, v):
                min_cut_edges.append((u, v))

    return min_cut_edges


def dfs(graph, node, visited):
    visited.add(node)
    for neighbor, attrs in graph[node].items():
        if attrs["weight"] > 0 and neighbor not in visited:
            dfs(graph, neighbor, visited)


# original
def original_ford_fulkerson(graph, source, sink):
    print("#original_ford_fulkerson#")

    # 使用 graph.networkx_graph.copy() 初始化残余网络
    residual_network = graph.networkx_graph.copy()

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
            residual_network[u][v]["weight"] -= flow
            residual_network[v][u]["weight"] += flow

        # 更新最大流量
        max_flow += flow

    # 使用最后的残余网络找到最小割
    min_cut_edges = min_cut(graph, source, residual_network)
    print('\nmin_cut_edges 最小割s====>', min_cut_edges)
    return max_flow


def ford_fulkerson(graph, source, sink, cache=None):
    print("#ford_fulkerson improved with cache #")

    if cache is None:
        cache = {}

    graph_key = tuple(sorted(graph.networkx_graph.edges()))  # Creates an immutable key

    if graph_key in cache:
        return cache[graph_key]

    # 使用 graph.networkx_graph.copy() 初始化残余网络
    residual_network = graph.networkx_graph.copy()

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
            residual_network[u][v]["weight"] -= flow
            residual_network[v][u]["weight"] += flow

        # 更新最大流量
        max_flow += flow

    cache[graph_key] = max_flow
    # 使用最后的残余网络找到最小割
    min_cut_edges = min_cut(graph, source, residual_network)
    print('\nmin_cut_edge 最小割 s====>', min_cut_edges)
    return max_flow



def monte_carlo_simulation(network, n_runs=1000):
    node_failure_probabilities = nx.get_node_attributes(
        network.networkx_graph, "node_failure_probability"
    )
    print(
        "monte_carlo_simulation node_failure_probabilities==>",
        node_failure_probabilities,
    )

    success_count = 0
    for _ in range(n_runs):
        working_network = nx.Graph()
        working_network.add_node(str(source))
        working_network.add_node(str(sink))
        working_edges = []
        for u, v, data in network.networkx_graph.edges(data=True):
            u_failure = random() > node_failure_probabilities[str(u)]
            v_failure = random() > node_failure_probabilities[str(v)]

            if u_failure and v_failure:
                working_edges.append((str(u), str(v), data))
        working_network.add_edges_from(working_edges)
        if nx.has_path(working_network, str(source), str(sink)):
            success_count += 1
    return success_count / n_runs




def compare_ford_fulkerson(network, source, sink):
    # 计时并运行原始的Ford Fulkerson函数
    start_time = time.time()
    min_cut_original = original_ford_fulkerson(network, source, sink)
    end_time = time.time()
    original_time = (end_time - start_time) * 1000
    print(f"Original Ford Fulkerson took {original_time:.2f} milliseconds.")

    # 计时并运行改进的Ford Fulkerson函数
    start_time = time.time()
    min_cut_improved = ford_fulkerson(network, source, sink)
    end_time = time.time()
    improved_time = (end_time - start_time) * 1000
    print(f"Improved Ford Fulkerson took {improved_time:.2f} milliseconds.")

    # 使用matplotlib进行可视化
    methods = ["Original", "Improved"]
    times = [original_time, improved_time]
    plt.bar(methods, times, color=['blue', 'green'])
    plt.xlabel('Method')
    plt.ylabel('Time (ms)')
    plt.title('Comparison of Ford Fulkerson methods')
    plt.show()





def calculate_node_reliability(network, source, sink):
    node_failure_probabilities = nx.get_node_attributes(
        network.networkx_graph, "node_failure_probability"
    )

    # 调用比较函数
    compare_ford_fulkerson(network, source, sink)

    edge_reliabilities = {
        (u, v): calculate_edge_reliability(data["weight"])
        for u, v, data in network.networkx_graph.edges(data=True)
    }
    nx.set_edge_attributes(network.networkx_graph, edge_reliabilities, "reliability")

    reliability_estimate = monte_carlo_simulation(network)
    return reliability_estimate



adjacency_matrix_1 = np.array(
    [
        [0, 12, 15, 0, 0, 0],
        [13, 0, 0, 12, 0, 0],
        [15, 0, 0, 8, 25, 0],
        [0, 12, 8, 0, 0, 20],
        [0, 0, 25, 0, 0, 5],
        [0, 0, 0, 20, 5, 0],
    ]
)

source, sink = "0", "5"

node_failure_probabilities = [0.1, 0.2, 0.3, 0.1, 0.05, 0.15]
node_types1 = [0, 1, 0, 1, 1, 2]
type_failure_probabilities = {0: 0.1, 1: 0.2, 2: 0.3}

network_1 = PolymorphicNetwork(
    adjacency_matrix_1,
    node_types=node_types1,
    type_failure_probabilities=type_failure_probabilities,
)

node_colors = {0: "r", 1: "g", 2: "b", 3: "y"}  


# ---可视化---
# 可视化多态网络

node_types_list = []
for _, data in network_1.networkx_graph.nodes(data=True):
    print("#" * 20)
    print(data)  # debug statement
    print(data.keys())  # debug statement
    node_types_list.append(data["node_type"])

# 为每个节点分配颜色
node_color_list = [node_colors[node_type] for node_type in node_types_list]

# 可视化多态网络
pos = nx.spring_layout(network_1.networkx_graph)
nx.draw_networkx_nodes(network_1.networkx_graph, pos, node_color=node_color_list)
nx.draw_networkx_edges(network_1.networkx_graph, pos)
nx.draw_networkx_labels(network_1.networkx_graph, pos)
edge_labels = nx.get_edge_attributes(network_1.networkx_graph, "weight")
nx.draw_networkx_edge_labels(network_1.networkx_graph, pos, edge_labels=edge_labels)
plt.show()


reliability_estimate = calculate_node_reliability(network_1, source, sink)
print("Reliability estimate:", reliability_estimate)
