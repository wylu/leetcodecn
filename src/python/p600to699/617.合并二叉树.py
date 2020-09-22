#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   617.合并二叉树.py
@Time    :   2020/09/23 00:12:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#
# https://leetcode-cn.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (77.26%)
# Likes:    477
# Dislikes: 0
# Total Accepted:    72.9K
# Total Submissions: 94.3K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL
# 的节点将直接作为新二叉树的节点。
#
# 示例 1:
#
#
# 输入:
# Tree 1                     Tree 2
# ⁠         1                         2
# ⁠        / \                       / \
# ⁠       3   2                     1   3
# ⁠      /                           \   \
# ⁠     5                             4   7
# 输出:
# 合并后的树:
# 3
# / \
# 4   5
# / \   \
# 5   4   7
#
#
# 注意: 合并必须从两个树的根节点开始。
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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def merge(t1: TreeNode, t2: TreeNode) -> TreeNode:
            if not t1:
                return t2
            if not t2:
                return t1
            root = TreeNode(t1.val + t2.val)
            root.left = merge(t1.left, t2.left)
            root.right = merge(t1.right, t2.right)
            return root

        return merge(t1, t2)


# @lc code=end
