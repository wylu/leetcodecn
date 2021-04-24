#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   897.递增顺序搜索树.py
@Time    :   2021/04/25 00:19:39
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#
# https://leetcode-cn.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (72.61%)
# Likes:    148
# Dislikes: 0
# Total Accepted:    28.1K
# Total Submissions: 38.7K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# 给你一棵二叉搜索树，请你 按中序遍历
# 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#
# 示例 2：
#
#
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#
#
#
#
# 提示：
#
#
# 树中节点数的取值范围是 [1, 100]
# 0 <= Node.val <= 1000
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        cur = dummy

        def inorder(root: TreeNode) -> None:
            nonlocal cur
            if not root:
                return

            inorder(root.left)
            cur.right = root
            root.left = None
            cur = cur.right
            inorder(root.right)

        inorder(root)
        return dummy.right


# @lc code=end
