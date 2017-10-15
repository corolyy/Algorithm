# -*- coding: utf-8 -*-


def array_sum(array, pre_sum=0):
    array = array or []
    length = len(array)
    if length < 2:
        sum = 0 if length < 1 else array[0]
        return pre_sum + sum
    else:
        pre_sum += array[0]
        return array_sum(array[1:], pre_sum)

print array_sum([9, 10 , 11, 20])
