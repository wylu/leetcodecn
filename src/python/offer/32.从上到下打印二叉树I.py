#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   32.从上到下打印二叉树I.py
@Time    :   2020/09/02 00:35:08
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
    def levelOrder(self, root: TreeNode) -> List[int]:
        def bfs(root: TreeNode) -> None:
            if not root:
                return
            q = deque()
            q.append(root)
            while q:
                node = q.popleft()
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        ans = []
        bfs(root)
        return ans
