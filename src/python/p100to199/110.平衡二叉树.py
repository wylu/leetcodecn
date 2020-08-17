#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   110.平衡二叉树.py
@Time    :   2020/08/17 12:37:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (52.86%)
# Likes:    418
# Dislikes: 0
# Total Accepted:    111.8K
# Total Submissions: 207.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回 true 。
#
# 示例 2:
#
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# 返回 false 。
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
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root) != -1

    def dfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        ld = self.dfs(root.left)
        if ld == -1:
            return -1

        rd = self.dfs(root.right)
        if rd == -1 or abs(ld - rd) > 1:
            return -1

        return 1 + max(ld, rd)


# @lc code=end

# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:
#         return self.dfs(root) != -1

#     def dfs(self, root: TreeNode) -> int:
#         if not root:
#             return 0

#         if not root.left and not root.right:
#             return 1

#         ld = self.dfs(root.left)
#         rd = self.dfs(root.right)

#         if ld == -1 or rd == -1 or abs(ld - rd) > 1:
#             return -1
#         return 1 + max(ld, rd)
