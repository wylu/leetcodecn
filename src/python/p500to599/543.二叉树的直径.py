#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   543.二叉树的直径.py
@Time    :   2020/09/26 14:06:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (51.64%)
# Likes:    489
# Dislikes: 0
# Total Accepted:    72.7K
# Total Submissions: 140.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
# 示例 :
# 给定二叉树
#
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \
# ⁠     4   5
#
#
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
#
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0

        def dfs(root: TreeNode) -> int:
            nonlocal ans
            left = 1 + dfs(root.left) if root.left else 0
            right = 1 + dfs(root.right) if root.right else 0
            ans = max(ans, left + right)
            return max(left, right)

        dfs(root)
        return ans


# @lc code=end
