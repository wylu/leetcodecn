#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   145.二叉树的后序遍历.py
@Time    :   2020/08/05 21:50:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (72.16%)
# Likes:    360
# Dislikes: 0
# Total Accepted:    104K
# Total Submissions: 144.1K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ans = []
        stack = [root]
        while stack:
            root = stack.pop()
            ans.append(root.val)

            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        ans.reverse()
        return ans


# @lc code=end
