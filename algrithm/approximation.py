# -*- coding:utf-8 -*-
"""
近似算法解决"NP完全问题"
集合覆盖，找到电台最小集合覆盖预期州
"""

def get_state_set(stations, states_needed):
    the_set = set()
    best_station = None
    # 电台实际于需求的交集
    covered = set()
    while states_needed:
        for station, this_states_covered in stations.items():
            this_covered = this_states_covered & states_needed
            if len(covered) < len(this_covered):
                covered = this_covered
                best_station = station
        states_needed -= covered
        the_set.add(best_station)
        covered = set()

    return the_set


if __name__ == '__main__':
    # 需要覆盖州集合
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
    # 电台实际覆盖州集合
    stations = {}
    stations['kone'] = set(['id', 'nv', 'ut'])
    stations['ktwo'] = set(['wa', 'id', 'mt'])
    stations['kthree'] = set(['or', 'nv', 'ca'])
    stations['kfour'] = set(['nv', 'ut'])
    stations['kfive'] = set(['ca', 'az'])

    print get_state_set(stations ,states_needed)