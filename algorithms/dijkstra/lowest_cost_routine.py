# -*- coding: utf-8 -*-
''' 曲别针换钢琴(使用Node对象实现)



'''
infinity = float('inf')

class Node(object):
    def __init__(self, name, parent=None, cost=infinity, neighbors=None):
        self.name = name
        self.parent = None
        self.cost = infinity
        self.neighbors = neighbors or {}

# 初始化各个节点
clip_node = Node(name='clip')
poster_node = Node(name='poster')
cd_node = Node(name='cd')
guitar_node = Node(name='guitar')
drum_node = Node(name='drum')
piano_node = Node(name='piano')
# 添加边与权重
clip_node.neighbors[poster_node] = 0
clip_node.neighbors[cd_node] = 5
poster_node.neighbors[guitar_node] = 30
poster_node.neighbors[drum_node] = 35
cd_node.neighbors[guitar_node] = 15
cd_node.neighbors[drum_node] = 20
guitar_node.neighbors[piano_node] = 20
drum_node.neighbors[piano_node] = 10
'''注意存在负权边时，已经遍历过的节点状态可能还会刷新，此时dijkstra算法不再适用，可选择Bellman-Ford算法'''
all_nodes = {clip_node, poster_node, cd_node, guitar_node, drum_node, piano_node}
def find_lowest_cost_routine(start=clip_node, end=piano_node):
    def find_and_remove_lowest_node(candidate_nodes):
        print [node.name for node in candidate_nodes]
        node_list = list(candidate_nodes)
        node_list.sort(key=lambda x: x.cost)
        lowest_node = node_list[0]
        assert isinstance(lowest_node, Node)
        for node in lowest_node.neighbors:
            # 计算是否需要刷新最低开销节点的邻居节点的信息：
            # - 若最低开销 + 距邻居开销 < 邻居本身开销 -> 更新邻居本身开销，及其上级节点
            l_to_n_cost = lowest_node.cost + lowest_node.neighbors.get(node, infinity)
            if l_to_n_cost < node.cost:
                node.cost = l_to_n_cost
                node.parent = lowest_node
        print lowest_node.name
        candidate_nodes.remove(lowest_node)

    # 初始化待考察节点
    candidate_nodes = all_nodes.copy()
    candidate_nodes.remove(start)
    candidate_nodes.remove(end)
    for node in start.neighbors:
        node.cost = start.neighbors.get(node, infinity)
        node.parent = start

    # - 找出当前最便宜的节点
    # - 对于该节点的邻居，检查是否有更短路径，有则刷新其开销
    while candidate_nodes:
        find_and_remove_lowest_node(candidate_nodes)

    # 打印路径
    node = end
    routine = [end]
    while node != start:
        routine.insert(0, node.parent)
        node = node.parent
    routine = [x.name for x in routine]
    print routine
    print 'Lowest cost: ', end.cost
    print 'Routine:', ' --> '.join(routine)


find_lowest_cost_routine()
