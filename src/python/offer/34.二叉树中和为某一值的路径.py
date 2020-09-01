#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   34.二叉树中和为某一值的路径.py
@Time    :   2020/09/02 00:00:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        def dfs(root: TreeNode, target: int) -> None:
            if not root.left and not root.right:
                if root.val == target:
                    ans.append(stack[:] + [target])
                return

            stack.append(root.val)
            if root.left:
                dfs(root.left, target - root.val)
            if root.right:
                dfs(root.right, target - root.val)
            stack.pop()

        ans, stack = [], []
        dfs(root, sum)
        return ans
