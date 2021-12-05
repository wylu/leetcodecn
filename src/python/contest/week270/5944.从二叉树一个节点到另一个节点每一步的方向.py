#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5944.从二叉树一个节点到另一个节点每一步的方向.py
@Time    :   2021/12/05 10:42:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int,
                      destValue: int) -> str:
        def find_ancestor(root: TreeNode, p: int, q: int) -> TreeNode:
            if not root or root.val == p or root.val == q:
                return root

            left = find_ancestor(root.left, p, q)
            right = find_ancestor(root.right, p, q)

            if left and right:
                return root

            return left or right

        start_path = []
        dest_path = []

        def find_start(root: TreeNode) -> bool:
            if not root:
                return False

            if root.val == startValue:
                return True

            start_path.append('U')
            if find_start(root.left) or find_start(root.right):
                return True
            start_path.pop()

            return False

        def find_dest(root: TreeNode) -> bool:
            if not root:
                return False

            if root.val == destValue:
                return True

            dest_path.append('L')
            if find_dest(root.left):
                return True
            dest_path.pop()

            dest_path.append('R')
            if find_dest(root.right):
                return True
            dest_path.pop()

            return False

        root = find_ancestor(root, startValue, destValue)
        find_start(root)
        find_dest(root)
        return ''.join(start_path) + ''.join(dest_path)
