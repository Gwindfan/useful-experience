# -*- coding:utf-8 -*-

"""选择排序 O(n^2)"""


def select_samllest(arr):
    smallest = arr[0]
    s_index = 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            s_index = i

    return s_index


def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest_index = select_samllest(arr)
        new_arr.append(arr.pop(smallest_index))

    return new_arr

if __name__ == '__main__':
    a = [11, 0, 1, 5, 6, 8]
    print selection_sort(a)