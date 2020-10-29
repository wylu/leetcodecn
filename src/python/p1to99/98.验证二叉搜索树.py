#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   98.验证二叉搜索树.py
@Time    :   2020/09/24 09:34:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (32.43%)
# Likes:    777
# Dislikes: 0
# Total Accepted:    174K
# Total Submissions: 536.3K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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
    def isValidBST(self, root: TreeNode) -> bool:
        pre = -0x80000000 - 1
        while root:
            if not root.left:
                if root.val <= pre:
                    return False
                pre = root.val
                root = root.right
                continue

            precursor = root.left
            while precursor.right and precursor.right != root:
                precursor = precursor.right

            if not precursor.right:
                precursor.right = root
                root = root.left
            else:
                if root.val <= pre:
                    return False
                pre = root.val
                root = root.right
                precursor.right = None
        return True


# @lc code=end

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         pre = -0x80000000 - 1
#         stack = []
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             if root.val <= pre:
#                 return False
#             pre = root.val
#             root = root.right
#         return True
