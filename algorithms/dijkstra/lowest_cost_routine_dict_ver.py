# -*- coding: utf-8 -*-
''' 曲别针换钢琴(使用dict实现)



'''
CLIP, POSTER, CD, GUITAR, DRUM, PIANO = ('clip', 'poster', 'cd', 'guitar',
                                         'drum', 'piano')

infinity = float('inf')
graph = {CLIP: {POSTER: 0, CD: 5},
         POSTER: {GUITAR: 30, DRUM: 35},
         CD: {GUITAR: 15, DRUM: 20},
         GUITAR: {PIANO: 20},
         DRUM: {PIANO: 10},
         PIANO: {}}

start, end = CLIP, PIANO
father_nodes = {POSTER: None, CD: None, GUITAR: None, DRUM: None, PIANO: None}
costs = {POSTER: infinity, CD: infinity, GUITAR: infinity, DRUM: infinity,
         PIANO: infinity}
# 由于起点已知，可根据起点进行初始化
father_nodes[POSTER], costs[POSTER] = CLIP, 0
father_nodes[CD], costs[CD] = CLIP, 5
candidates = {POSTER, CD, GUITAR, DRUM}
# - 寻找价值最小的节点
def find_lowest(candidates):
    candidates_dict = {k: v for k, v in costs.items() if k in candidates}
    candidates_costs = candidates_dict.values()
    candidates_costs.sort()
    print candidates_costs
    lowest = candidates_costs[0]
    for k, v in candidates_dict.items():
        if v == lowest:
            print k, v
            return k


# - 判断该节点的临界点是否要刷新
def refresh(lowest, candidates):
    neighbors = graph[lowest].keys()
    for neighbor in neighbors:
        if costs[neighbor] > costs[lowest] + graph[lowest][neighbor]:
            costs[neighbor] = costs[lowest] + graph[lowest][neighbor]
            father_nodes[neighbor] = lowest

while candidates:
    lowest = find_lowest(candidates)
    candidates.remove(lowest)
    refresh(lowest, candidates)

# 最低开销：
print costs[PIANO]
# 构建整条路径：
routine = [end]
while routine[0] != start:
    routine.insert(0, father_nodes[routine[0]])
print ' --> '.join(routine)
