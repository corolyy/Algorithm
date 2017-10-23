# -*- coding: utf-8 -*-
from collections import deque

'''Find the seller'''
graph = {}  # 有向无环图
graph['you'] = ['alice', 'bob', 'claire']
graph['you'] = ['anuj', 'peggy']
graph['you'] = ['peggy']
graph['you'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

sellers = {'thom'}


def is_seller(name):
    return name in sellers


# 时间复杂度: O(V + E), V - vertice,顶点数, E - edge,边数
def find_seller(name):
    search_que = deque()
    search_que += graph[name]
    searched_set = set()
    while search_que:
        person = search_que.popleft()
        if is_seller(person):
            print '{} is seller'.format(person)
            return
        else:
            searched_set.add(person)
            added_persons = [p for p in graph[person] if p not in searched_set]
            search_que += added_persons
    print 'No seller'

find_seller('you')