#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   144.二叉树的前序遍历.py
@Time    :   2020/08/05 21:39:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (66.40%)
# Likes:    330
# Dislikes: 0
# Total Accepted:    145.2K
# Total Submissions: 218.6K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [1,2,3]
#
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []
        stack = [root]
        while stack:
            root = stack.pop()
            ans.append(root.val)

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return ans


# @lc code=end
