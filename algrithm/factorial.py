# -*- coding:utf-8 -*-
"""阶乘递归调用"""


def factorial(n):
    # base condition
    if n == 1:
        return 1
    else:
        # recursion condition
        return n * factorial(n-1)


def countdown(i):
    print i
    # base condition
    if i <= 1:
        return
    else:
        # recursion condition
        countdown(i - 1)


if __name__ == '__main__':
    print factorial(3)
    print '-'*10
    countdown(3)