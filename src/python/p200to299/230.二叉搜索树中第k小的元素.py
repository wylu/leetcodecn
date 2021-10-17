#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   230.二叉搜索树中第k小的元素.py
@Time    :   2021/10/17 14:58:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (74.78%)
# Likes:    494
# Dislikes: 0
# Total Accepted:    150.7K
# Total Submissions: 201.5K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#
#
# 示例 2：
#
#
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#
#
#
#
#
#
# 提示：
#
#
# 树中的节点数为 n 。
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
#
#
#
#
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1

        def pre_order(root: Optional[TreeNode]) -> None:
            nonlocal ans, k
            if not root or k == 0:
                return

            pre_order(root.left)
            if k:
                ans = root.val
                k -= 1
            if k:
                pre_order(root.right)

        pre_order(root)
        return ans


# @lc code=end
