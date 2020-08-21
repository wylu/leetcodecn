#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   111.二叉树的最小深度.py
@Time    :   2020/08/21 12:49:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (43.18%)
# Likes:    339
# Dislikes: 0
# Total Accepted:    116.4K
# Total Submissions: 265.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root: TreeNode, depth: int) -> None:
            nonlocal ans
            if not root.left and not root.right:
                ans = min(ans, depth + 1)
                return
            if root.left:
                dfs(root.left, depth + 1)
            if root.right:
                dfs(root.right, depth + 1)

        ans = 0x7FFFFFFF
        dfs(root, 0)
        return ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    print(solu.minDepth(tree))
