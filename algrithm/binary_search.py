# -*- coding:utf-8 -*-
"""
二分法查找（有序序列）
O(logn)
"""


def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == target:
            return mid
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

if __name__ == '__main__':
    alist = [1, 3, 5, 7, 9, 11]
    print binary_search(alist, 7)
    print binary_search(alist, 6)
    print binary_search(alist, 11)