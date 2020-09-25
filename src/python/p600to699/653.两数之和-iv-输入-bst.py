#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   653.两数之和-iv-输入-bst.py
@Time    :   2020/09/25 17:27:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (56.63%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    21.5K
# Total Submissions: 38K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
#
# 案例 1:
#
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 9
#
# 输出: True
#
#
#
#
# 案例 2:
#
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 28
#
# 输出: False
#
#
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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()

        def dfs(root: TreeNode) -> bool:
            if not root:
                return False
            if k - root.val in seen:
                return True
            seen.add(root.val)
            return dfs(root.left) or dfs(root.right)

        return dfs(root)


# @lc code=end
