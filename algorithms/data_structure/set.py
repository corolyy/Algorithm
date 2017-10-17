# -*- coding: utf-8 -*-


set_0 = {3, 9, 7, 5 ,1}
set_1 = {1, 3, 5, 7, 9}
set_2 = {i for i in range(10)}

# &
print set_1 & set_2 # --> set([7, 1, 3, 5, 9])

# |
print set_1 | set_2 # --> set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# -
# result related with order
print set_1 - set_2 # --> set({})
print set_2 - set_1 # --> set{[0, 8, 2, 4, 6]}

# ==
print set_0 == set_1 # --> True