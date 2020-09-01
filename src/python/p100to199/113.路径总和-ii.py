#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   113.路径总和-ii.py
@Time    :   2020/09/01 23:51:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (60.91%)
# Likes:    306
# Dislikes: 0
# Total Accepted:    70.1K
# Total Submissions: 115K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
#
#
# 返回:
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
#
#
#
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        def dfs(root: TreeNode, target: int) -> None:
            if not root.left and not root.right:
                if root.val == target:
                    ans.append(stack[:] + [target])
                    return

            stack.append(root.val)
            if root.left:
                dfs(root.left, target - root.val)
            if root.right:
                dfs(root.right, target - root.val)
            stack.pop()

        ans, stack = [], []
        dfs(root, sum)
        return ans


# @lc code=end
