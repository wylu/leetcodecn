#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   94.二叉树的中序遍历.py
@Time    :   2020/08/05 21:44:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (72.36%)
# Likes:    608
# Dislikes: 0
# Total Accepted:    207.6K
# Total Submissions: 286.9K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            ans.append(root.val)
            root = root.right

        return ans


# @lc code=end
