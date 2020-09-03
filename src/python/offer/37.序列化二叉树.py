#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   37.序列化二叉树.py
@Time    :   2020/09/03 19:41:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        Args:
            root (TreeNode): the root of tree

        Returns:
            str: a serial str of binary tree
        """
        def dfs(root: TreeNode) -> None:
            if not root:
                data.append('#')
                return
            data.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        data = []
        dfs(root)
        return ','.join(data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        Args:
            data (str): a serial str of binary tree

        Returns:
            TreeNode: the root of tree
        """
        def dfs() -> TreeNode:
            val = data.pop()
            if val == '#':
                return
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            return root

        data = data.split(',')
        data.reverse()
        return dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left, tree.right = TreeNode(2), TreeNode(3)
    tree.right.left, tree.right.right = TreeNode(4), TreeNode(5)

    codec = Codec()
    res = codec.serialize(tree)
    print(res)
    tree = codec.deserialize(res)
    res = codec.serialize(tree)
    print(res)
