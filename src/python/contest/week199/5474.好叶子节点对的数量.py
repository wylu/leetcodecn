#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5474.好叶子节点对的数量.py
@Time    :   2020/07/26 11:22:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import itertools

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        self.dist = distance
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root: TreeNode, depth: int) -> List:
        if not root:
            return []

        if not root.left and not root.right:
            return [depth]

        lds = self.dfs(root.left, depth + 1)
        rds = self.dfs(root.right, depth + 1)

        for i in lds:
            if i - depth >= self.dist:
                continue
            for j in rds:
                if (i - depth) + (j - depth) <= self.dist:
                    self.ans += 1

        return [i for i in itertools.chain(lds, rds) if i - depth < self.dist]
