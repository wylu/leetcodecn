#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   28.对称的二叉树.py
@Time    :   2020/08/30 10:18:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(r1: TreeNode, r2: TreeNode) -> bool:
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val != r2.val:
                return False
            return dfs(r1.left, r2.right) and dfs(r1.right, r2.left)

        return dfs(root, root)
