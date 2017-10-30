# -*- coding:utf-8 -*-
"""合并二叉树"""


class BiTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = BiTree(data)
                else:
                    self.left.insert(data)
            elif data >= self.data:
                if self.right is None:
                    self.right = BiTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def traverse_preorder(self):
        if self.data is not None:
            print self.data
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()


def mergeTrees(t1, t2):
    """
    :type t1: BiTree
    :type t2: BiTree
    """
    if t1 is not None and t2 is not None:
        t1.data += t2.data
        t1.left = mergeTrees(t1.left, t2.left)
        t1.right = mergeTrees(t1.right, t2.right)

    elif t1 is None and t2 is not None:
        t1 = t2

    return t1


if __name__ == '__main__':
    tree1 = BiTree(10)
    tree1.insert(3)
    tree1.insert(2)
    tree1.insert(11)
    tree1.traverse_preorder()
    print '-'*60
    tree2 = BiTree(6)
    tree2.insert(3)
    tree2.insert(4)
    tree2.insert(8)
    tree2.traverse_preorder()

    print '-'*60
    mergeTrees(tree1, tree2)
    tree1.traverse_preorder()
