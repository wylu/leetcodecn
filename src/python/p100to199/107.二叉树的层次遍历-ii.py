#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   107.二叉树的层次遍历-ii.py
@Time    :   2020/09/06 21:36:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (66.43%)
# Likes:    320
# Dislikes: 0
# Total Accepted:    93.5K
# Total Submissions: 138.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其自底向上的层次遍历为：
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
#
#
#
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque()
        q.append(root)
        level, cur_last, next_last = [], root, None
        while q:
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
                next_last = node.left
            if node.right:
                q.append(node.right)
                next_last = node.right

            if node == cur_last:
                ans.append(level)
                cur_last = next_last
                level = []

        ans.reverse()
        return ans


# @lc code=end
