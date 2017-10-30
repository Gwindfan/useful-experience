# -*- coding:utf-8 -*-
"""
数组求和（递归实现）

"""


def sum (arr):
    if arr == []:
        return 0
    else:
        return arr.pop(0) + sum(arr)


if __name__ == '__main__':
    array = [1, 2 ,3, 4]
    print sum(array)