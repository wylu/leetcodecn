#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   257.二叉树的所有路径.py
@Time    :   2020/09/04 00:07:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (64.95%)
# Likes:    314
# Dislikes: 0
# Total Accepted:    52.7K
# Total Submissions: 81.1K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 输入:
#
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
#
# 输出: ["1->2->5", "1->3"]
#
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        def dfs(root: TreeNode) -> None:
            if not root.left and not root.right:
                ans.append('->'.join(stack[:] + [str(root.val)]))
                return
            stack.append(str(root.val))
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            stack.pop()

        ans, stack = [], []
        dfs(root)
        return ans


# @lc code=end
