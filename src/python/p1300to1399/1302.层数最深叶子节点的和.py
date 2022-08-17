#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1302.层数最深叶子节点的和.py
@Time    :   2022/08/17 21:50:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#
# https://leetcode.cn/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (85.68%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    51.9K
# Total Submissions: 60.6K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# 给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# 输出：15
#
#
# 示例 2：
#
#
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：19
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 10^4] 之间。
# 1 <= Node.val <= 100
#
#
#
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ans = max_depth = 0

        def dfs(root: TreeNode, depth: int):
            if not root:
                return

            nonlocal ans, max_depth
            if depth == max_depth:
                ans += root.val
            elif depth > max_depth:
                ans, max_depth = root.val, depth

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return ans


# @lc code=end
