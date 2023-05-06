import numpy as np
import networkx as nx
from random import random
import matplotlib.pyplot as plt


class PolymorphicNetwork:
    def __init__(self, adjacency_matrix, node_failure_probabilities=None):
        self.adjacency_matrix = adjacency_matrix
        self.node_failure_probabilities = (
            node_failure_probabilities or [0.0] * adjacency_matrix.shape[0]
        )
        self.networkx_graph = nx.from_numpy_array(
            adjacency_matrix, create_using=nx.DiGraph()
        )
        self.networkx_graph = nx.relabel_nodes(
            self.networkx_graph, {i: str(i) for i in range(adjacency_matrix.shape[0])}
        )
        nx.set_node_attributes(
            self.networkx_graph,
            dict(enumerate(self.node_failure_probabilities)),
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
    return max_flow


def monte_carlo_simulation(network, node_failure_probabilities, n_runs=1000):
    success_count = 0
    for _ in range(n_runs):
        working_network = nx.Graph()
        working_network.add_node(str(source))
        working_network.add_node(str(sink))
        working_edges = []
        for u, v, data in network.networkx_graph.edges(data=True):
            u_failure = random() > node_failure_probabilities[int(u)]
            v_failure = random() > node_failure_probabilities[int(v)]
            if u_failure and v_failure:
                working_edges.append((str(u), str(v), data))
        working_network.add_edges_from(working_edges)
        if nx.has_path(working_network, str(source), str(sink)):
            success_count += 1
    return success_count / n_runs


def calculate_node_reliability(network, source, sink, node_failure_probabilities):
    min_cut = ford_fulkerson(network, source, sink)
    edge_reliabilities = {
        (u, v): calculate_edge_reliability(data["weight"])
        for u, v, data in network.networkx_graph.edges(data=True)
    }
    nx.set_edge_attributes(network.networkx_graph, edge_reliabilities, "reliability")

    reliability_estimate = monte_carlo_simulation(network, node_failure_probabilities)
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

network_1 = PolymorphicNetwork(
    adjacency_matrix_1,
)


# ---可视化---
# 可视化多态网络
pos = nx.spring_layout(network_1.networkx_graph)
nx.draw_networkx_nodes(network_1.networkx_graph, pos, node_color="b")
nx.draw_networkx_edges(network_1.networkx_graph, pos)
nx.draw_networkx_labels(network_1.networkx_graph, pos)
edge_labels = nx.get_edge_attributes(network_1.networkx_graph, "weight")
nx.draw_networkx_edge_labels(network_1.networkx_graph, pos, edge_labels=edge_labels)
plt.show()
# ---end ----

reliability_estimate = calculate_node_reliability(
    network_1, source, sink, node_failure_probabilities
)
print("Reliability estimate:", reliability_estimate)
