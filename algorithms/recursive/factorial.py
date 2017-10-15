# -*- coding: utf-8 -*-
'''Recursive is more space-consuming because of '''
''' call stack of Recursive
{5 * Recursive(4)}
{5 * {4 * Recursive(3)}}
{5 * {4 * {3 * Recursive(2)}}}
{5 * {4 * {3 * {2 * Recursive(1)}}}}
{5 * {4 * {3 * {2 * 1}}}}
{5 * {4 * {3 * 2}}}
{5 * {4 * 6}}
{5 * 24}
120
'''
def recursive(n):
    if n <= 1: # base case
        return 1 if n in {0, 1} else 0
    else: # recursive case
        return n * recursive(n - 1)

''' call stack of TailRecursive
tail_recursive(4, 5)
tail_recursive(3, 5 * 4)
tail_recursive(2， 5 * 4 * 3)
tail_recursive(1， 5 * 4 * 3 * 2)
120
'''
def tail_recursive(n, a=1):
    if n <= 1: # base case
        return 0 if n < 0 else a
    else: # recursive case
        return tail_recursive(n - 1, n * a)

if __name__=="__main__":
    print recursive(5)
    print tail_recursive(5)