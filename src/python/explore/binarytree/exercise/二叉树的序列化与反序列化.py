#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   二叉树的序列化与反序列化.py
@Time    :   2020/08/15 22:34:49
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


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
        res = []
        self._serial(root, res)
        return ','.join(res)

    def _serial(self, root: TreeNode, res: List[str]) -> None:
        if not root:
            res.append('#')
            return

        res.append(str(root.val))
        self._serial(root.left, res)
        self._serial(root.right, res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        Args:
            data (str): a serial str of binary tree

        Returns:
            TreeNode: the root of tree
        """
        data = data.split(',')
        data.reverse()
        return self._deserial(data)

    def _deserial(self, data: List[str]) -> TreeNode:
        val = data.pop()
        if val == '#':
            return

        root = TreeNode(int(val))
        root.left = self._deserial(data)
        root.right = self._deserial(data)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
