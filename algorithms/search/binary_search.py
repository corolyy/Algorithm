# -*- coding: utf-8 -*-


def binary_search(list, item):
    '''find index of item in list, O(n) =  log(n)

    O(n): int(log(n)) + 1 --> 100: 7, 128: 8
    :param list: a sorted list, order: small to big
    :param item:
    :return: index of item, None if not found
    '''
    l, r = 0, len(list)
    '''why using l <= r not l < r
    
    if using l < r, (l + r)/2 will always smaller than r, 
    then the right edge won't be found.
    '''
    while l <= r:
        mid = (l + r) / 2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            l = mid + 1
        else:
            r = mid - 1
    return None

if __name__=="__main__":
    lst = [1, 2, 3, 4, 5]
    print binary_search(lst, 3) # 2
    print binary_search(lst, 5) # 4
