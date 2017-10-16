# -*- coding: utf-8 -*-
from random import randint


def partition(list):
    if not list or len(list) < 2:
        raise ValueError("")
    l, r = [], []
    pivot = randint(0, len(list) - 1)
    for i in range(len(list)):
        if i == pivot:
            continue
        pivot_val = list[pivot]
        curr_val = list[i]
        if curr_val <= pivot_val:
            l.append(curr_val)
        else:
            r.append(curr_val)
    return l, pivot, r


def quick_sort(list):
    if len(list) < 2: # base case
        return list if len(list) == 1 else []
    else: # recursive case
        left_list, pivot, right_list = partition(list)
        return quick_sort(left_list) + [list[pivot]] + quick_sort(right_list)


print quick_sort([2, 2, -1, 3, 8, -2])
