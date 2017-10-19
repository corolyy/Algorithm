# -*- coding: utf-8 -*-


org_list = [3, 8, 11, 5, 7, 1, 8, 5]

for i in range(1, len(org_list)):
    for j in range(len(org_list) - i):
        if org_list[j] > org_list[j + 1]:
            org_list[j], org_list[j + 1] = org_list[j + 1], org_list[j]

print org_list # --> [1, 3, 5, 5, 7, 8, 8, 11]