#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   938.二叉搜索树的范围和.py
@Time    :   2021/04/27 11:46:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#
# https://leetcode-cn.com/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (80.82%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    66K
# Total Submissions: 81.7K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
#
#
#
# 示例 1：
#
#
# 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
# 输出：32
#
#
# 示例 2：
#
#
# 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# 输出：23
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 2 * 10^4] 内
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# 所有 Node.val 互不相同
#
#
#


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0

        def dfs(root: TreeNode) -> None:
            nonlocal ans
            if not root:
                return

            dfs(root.left)
            if low <= root.val <= high:
                ans += root.val
            dfs(root.right)

        dfs(root)
        return ans


# @lc code=end
