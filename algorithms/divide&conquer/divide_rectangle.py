# -*- coding: utf-8 -*-


def divide_rectangle(length, width, pre_list):
    pre_list =  pre_list or []
    (length, width) = (width, length) if width > length else (length, width)
    pre_list.extend([width for i in range(length / width)])
    if length % width == 0: # base case
        return pre_list
    else: # recursive case
        return divide_rectangle(width, length % width, pre_list)

print divide_rectangle(640, 50, [])