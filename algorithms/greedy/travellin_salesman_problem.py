# -*- coding: utf-8 -*-
from random import randint
import sys

'''旅行商问题: 最优方案需O(N!)

求N个城市之间的最短路线，不定起点
'''
MARLIN, BERKELEY, SAN_FRANCISCO, FREMONT, PALO_ALTO = ('Marlin', 'Berkeley',
                                                       'SanFrancisco',
                                                       'Fremont', 'PaloAlto')
Marlin = {BERKELEY: 17, SAN_FRANCISCO: 10, FREMONT: 32, PALO_ALTO: 36}
Berkeley = {MARLIN: 17, SAN_FRANCISCO: 14, FREMONT: 31, PALO_ALTO: 48}
SanFrancisco = {MARLIN: 10, BERKELEY: 14, FREMONT: 30, PALO_ALTO: 31}
Fremont = {MARLIN: 32, SAN_FRANCISCO: 30, BERKELEY: 32, PALO_ALTO: 16}
PaloAlto = {MARLIN: 36, SAN_FRANCISCO: 31, FREMONT: 16, BERKELEY: 48}
city_dict = {MARLIN: Marlin, BERKELEY: Berkeley,
             FREMONT: Fremont, PALO_ALTO: PaloAlto,
             SAN_FRANCISCO: SanFrancisco}


# 1. 随机选择一个城市作为起点
# 2. 选择还没到过的最近的城市
# 3. 循环第二步
def select_nearest(city_map, city_unreached):
    nearest_city, nearest_distance = None, sys.maxint
    for city, distance in city_map.items():
        if city in city_unreached and distance < nearest_distance:
            nearest_city, nearest_distance = city, distance
    return nearest_city, nearest_distance


city_list = [key for key in city_dict.keys()]

# - 随机选择城市
curr_city = city_list[randint(0, len(city_list) - 1)]
travel_order = [curr_city]
travel_distance = 0
city_unreached = {key for key in city_dict.keys()} - {curr_city}
# - 选择还没到过的城市，直到全部去过
while city_unreached:
    curr_city, distance = select_nearest(city_dict.get(curr_city),
                                         city_unreached)
    city_unreached -= {curr_city}
    travel_order.append(curr_city)
    travel_distance += distance

print travel_order, travel_distance
print ('TravelOrder: {0}. \nTravelDistance: {1}'
       .format(' --> '.join(travel_order), travel_distance))
