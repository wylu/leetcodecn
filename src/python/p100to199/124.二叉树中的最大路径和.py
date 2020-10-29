#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   124.二叉树中的最大路径和.py
@Time    :   2020/09/26 18:41:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (43.16%)
# Likes:    720
# Dislikes: 0
# Total Accepted:    77.1K
# Total Submissions: 178.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#
#
#
# 示例 1：
#
# 输入：[1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# 输出：6
#
#
# 示例 2：
#
# 输入：[-10,9,20,null,null,15,7]
#
#  -10
#  / \
# 9  20
#   /  \
#  15   7
#
# 输出：42
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
    def maxPathSum(self, root: TreeNode) -> int:
        ans = -0x80000000

        def dfs(root: TreeNode) -> int:
            nonlocal ans
            if not root:
                return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            ans = max(ans, root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return ans


# @lc code=end
