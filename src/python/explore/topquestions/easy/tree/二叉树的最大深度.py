#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   二叉树的最大深度.py
@Time    :   2020/08/01 22:48:17
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
    def maxDepth(self, root: TreeNode) -> int:
        # 自下而上 DFS
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
