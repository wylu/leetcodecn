#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   二叉树的层序遍历.py
@Time    :   2020/08/14 23:16:43
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
        cur_tail, next_tail, level = root, None, []
        que = deque()
        que.append(root)

        while que:
            node = que.popleft()
            level.append(node.val)

            if node.left:
                next_tail = node.left
                que.append(node.left)

            if node.right:
                next_tail = node.right
                que.append(node.right)

            if node == cur_tail:
                cur_tail = next_tail
                ans.append(level)
                level = []

        return ans
