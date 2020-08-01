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
from queue import SimpleQueue
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
        que = SimpleQueue()
        que.put(root)
        curTail, nextTail, level = root, None, []
        while not que.empty():
            cur = que.get()
            level.append(cur.val)

            if cur.left:
                que.put(cur.left)
                nextTail = cur.left
            if cur.right:
                que.put(cur.right)
                nextTail = cur.right

            if cur == curTail:
                ans.append(level)
                level = []
                curTail = nextTail

        return ans
