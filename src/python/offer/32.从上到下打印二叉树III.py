#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   32.从上到下打印二叉树III.py
@Time    :   2020/09/02 23:08:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        ans, level = [], []
        cur_last, next_last, flag = root, None, True

        while q:
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
                next_last = node.left

            if node.right:
                q.append(node.right)
                next_last = node.right

            if node == cur_last:
                cur_last = next_last
                ans.append(level if flag else level[::-1])
                flag = not flag
                level = []

        return ans
