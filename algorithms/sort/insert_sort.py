# -*- coding: utf-8 -*-


def find_smallest_index(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if smallest > list[i]:
            # using >= or > in this implementation won't
            # cause different result
            smallest = list[i]
            smallest_index = i
    return smallest_index


def insert_sort(list):
    '''sort the list from small to big; O(n^2)'''
    sorted_list = []
    for i in range(len(list)):
        smallest_index = find_smallest_index(list)
        sorted_list.append(list.pop(smallest_index))
    return sorted_list


if __name__=="__main__":
    print insert_sort([5, 7, 9, 9, 1, 1, 3])
