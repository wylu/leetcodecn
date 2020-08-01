#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   二叉树的层序遍历.py
@Time    :   2020/08/01 23:37:37
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

        ans = []
        que = deque()
        que.append(root)
        curTail, nextTail, level = root, None, []
        while que:
            cur = que.popleft()
            level.append(cur.val)

            if cur.left:
                que.append(cur.left)
                nextTail = cur.left
            if cur.right:
                que.append(cur.right)
                nextTail = cur.right

            if cur == curTail:
                ans.append(level)
                level = []
                curTail = nextTail

        return ans
