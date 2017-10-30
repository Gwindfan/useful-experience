# -*- coding:utf-8 -*-

"""二叉树（左子树数值 < 右子数数值）"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data >= self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

    def traverse_preoder(self):
        if self.data is not None:
            print self.data
        if self.left:
            self.left.traverse_preoder()
        if self.right:
            self.right.traverse_preoder()
        return

    def traverse_inoder(self):
        if self.left:
            self.left.traverse_preoder()
        if self.data is not None:
            print self.data
        if self.right:
            self.right.traverse_preoder()
        return

    def traverse_postoder(self):
        if self.left:
            self.left.traverse_preoder()
        if self.right:
            self.right.traverse_preoder()
        if self.data is not None:
            print self.data
        return

if __name__ == '__main__':
    root = Node(8)
    root.insert_node(3)
    root.insert_node(10)
    root.insert_node(1)
    root.insert_node(0)
    print('前序遍历')
    root.traverse_preoder()
    print('中序遍历')
    root.traverse_inoder()
    print('后序遍历')
    root.traverse_inoder()
