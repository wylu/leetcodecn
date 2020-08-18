#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   530.二叉搜索树的最小绝对差.py
@Time    :   2020/08/18 15:56:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (57.80%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 33.4K
# Testcase Example:  '[1,null,3,2]'
#
# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
#
#
#
# 示例：
#
# 输入：
#
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
#
# 输出：
# 1
#
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
#
#
#
#
# 提示：
#
#
# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
# 相同
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
    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> None:
            nonlocal ans, pre
            if not root:
                return
            dfs(root.left)
            ans = min(ans, root.val - pre)
            pre = root.val
            dfs(root.right)

        ans, pre = 0x7FFFFFFF, -0x8FFFFFFF
        dfs(root)
        return ans


# @lc code=end
