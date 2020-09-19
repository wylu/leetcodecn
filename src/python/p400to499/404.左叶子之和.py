#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   404.左叶子之和.py
@Time    :   2020/09/19 10:39:12
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (56.02%)
# Likes:    199
# Dislikes: 0
# Total Accepted:    41.6K
# Total Submissions: 74.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#
#
#
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, isLeft: bool) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if isLeft else 0
            return dfs(root.left, True) + dfs(root.right, False)

        return dfs(root, False)


# @lc code=end
