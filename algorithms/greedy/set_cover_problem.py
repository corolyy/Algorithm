# -*- coding: utf-8 -*-

'''集合覆盖问题

假设你办了个广播节目, 需要覆盖全国所有的省份
不同的广播电台覆盖的省份各不相同, 如何选择最少的广播电台

若计算所有能覆盖全部省份的电台集合, 算法复杂度过高
使用贪心法, 快速求得近似解
'''

# provinces needed to be covered
provinces_needed = {'beijing', 'shanghai', 'tianjin', 'anhui', 'zhejiang',
                    'jiangsu', 'jiangxi', 'guangdong'}

# station - cover dict
stations = {}
stations['k1'] = {'anhui', 'zhejiang', 'jiangsu'}
stations['k2'] = {'shanghai', 'anhui', 'beijing'}
stations['k3'] = {'tianjin', 'jiangsu', 'jiangxi'}
stations['k4'] = {'zhejiang', 'jiangsu'}
stations['k5'] = {'jiangxi', 'guangdong'}

# - 选出覆盖了最多未覆盖省份的电台，即便这个电台覆盖已覆盖的州
# - 重复上一步，直到覆盖所有的州

def least_stations_cover_all_provinces(provinces_needed, stations_info):
    # ensure can cover all
    max_provinces = reduce(lambda x, y: x | y, stations_info.values())
    if provinces_needed - max_provinces:
        raise Exception('Mission impossible!')

    provinces_uncovered = provinces_needed
    final_stations = set()
    while provinces_uncovered:
        best_station, best_coverage = None, {}
        for station_name, station_coverage in stations_info.items():
            if len(provinces_uncovered &  station_coverage) > len(best_coverage):
                best_coverage = provinces_uncovered &  station_coverage
                best_station = station_name
        provinces_uncovered -= best_coverage
        final_stations.add(best_station)

    print final_stations

least_stations_cover_all_provinces(provinces_needed, stations)
