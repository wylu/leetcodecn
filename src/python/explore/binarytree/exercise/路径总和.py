#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   路径总和.py
@Time    :   2020/08/15 08:30:44
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        return (self.hasPathSum(root.left, sum - root.val)
                or self.hasPathSum(root.right, sum - root.val))
