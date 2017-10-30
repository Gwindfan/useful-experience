# -*-:coding:utf-8 -*-
"""
Djkstra 实现有向无环图（权重为正）
"""
# 记录已经处理节点
processed = []
inf = float('inf')


def find_lowest_cost_node(cost):
    lowest_cost = float('inf')
    the_node = None
    for n in cost.keys():
        if n not in processed:
            if cost[n] < lowest_cost:
                lowest_cost = cost[n]
                the_node = n
    return the_node


def djkstra(graph, cost, parent):
    node = find_lowest_cost_node(cost)
    while node:
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost[node] + neighbors[n]
            if new_cost < cost[n]:
                cost[n] = new_cost
                parent[n] = node
        processed.append(node)
        node = find_lowest_cost_node(cost)

    return parent


def traverse_path(m_parent):
    path = []
    key = 'finish'
    while key in m_parent:
        path.insert(0, key)
        key = m_parent[key]

    path.insert(0, 'start')
    return path


if __name__ == '__main__':
    # 图
    a_graph = dict(
        start=dict(
                a=6,
                b=2),
        a=dict(finish=1,),
        b=dict(
                a=3,
                finish=5),
        finish=dict()
    )
    # 从start 到节点的最少cost
    cost = dict(
        a=6,
        b=2,
        finish=float('inf')
    )
    # 节点的父节点
    parent = dict(
        a='start',
        b='start',
        finish=None
    )
    djkstra(a_graph, cost, parent)

    print traverse_path(parent)