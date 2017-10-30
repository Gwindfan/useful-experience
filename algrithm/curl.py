# -*- coding:utf-8 -*-
"""如果匹配则返回 True，类语法解析"""
mdict= {
    '(': ')',
    ')': '(',
    '[': ']',
    ']': '[',
    '{': '}',
    '}': '{',
}


def check(str):
    curls = list(str)
    stack = []
    # 异常处理
    if 1 == len(curls):
        return False

    for i in range(0, len(curls)):
        if 0 == len(stack):
            if curls[i] in [']', '}', ')']:
                return False
            else:
                stack.insert(0, curls[i])
        else:
            if mdict[stack[0]] == curls[i]:
                stack.pop(0)
            else:
                stack.insert(0, curls[i])

    return True if 0 == len(stack) else False

if __name__ == '__main__':
    str = '((()))([])[]{}'
    print check(str)