#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   04.06.后继者.py
@Time    :   2022/05/16 11:33:36
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
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans = None

        while root:
            if root.val > p.val:
                ans, root = root, root.left
            else:
                root = root.right

        return ans


# class Solution:
#     def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
#         stk, last = [], None

#         while stk or root:
#             while root:
#                 stk.append(root)
#                 root = root.left

#             root = stk.pop()
#             if last == p:
#                 return root

#             last = root
#             root = root.right
