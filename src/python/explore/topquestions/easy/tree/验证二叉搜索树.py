#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   验证二叉搜索树.py
@Time    :   2020/08/01 22:51:35
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
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历二叉搜索树，结果序列单调递增
        if not root:
            return True

        preVal = -(1 << 31) - 1
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= preVal:
                return False
            preVal = root.val

            root = root.right

        return True
