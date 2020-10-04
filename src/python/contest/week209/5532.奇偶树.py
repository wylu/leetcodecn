#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5532.奇偶树.py
@Time    :   2020/10/04 10:42:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :   BFS
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = deque()
        q.append(root)

        even = True
        while q:
            pre = -0x8FFFFFFF - 1 if even else 0x7FFFFFFF + 1

            for _ in range(len(q)):
                node = q.popleft()
                if even:
                    if node.val % 2 != 1 or node.val <= pre:
                        return False
                else:
                    if node.val % 2 != 0 or node.val >= pre:
                        return False

                pre = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            even ^= True

        return True
