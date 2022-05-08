#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6057.统计值等于子树平均值的节点数.py
@Time    :   2022/05/08 10:33:44
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

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root: TreeNode):
            nonlocal ans

            if not root:
                return 0, 0

            lt, lc = dfs(root.left)
            rt, rc = dfs(root.right)

            total, count = lt + rt + root.val, lc + rc + 1
            if total // count == root.val:
                ans += 1

            return total, count

        dfs(root)
        return ans
