#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   538.把二叉搜索树转换为累加树.py
@Time    :   2020/09/21 09:06:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#
# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (63.59%)
# Likes:    339
# Dislikes: 0
# Total Accepted:    41.5K
# Total Submissions: 65.4K
# Testcase Example:  '[5,2,13]'
#
# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater
# Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
#
#
#
# 例如：
#
# 输入: 原始二叉搜索树:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
#
# 输出: 转换为累加树:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
#
#
#
#
# 注意：本题和 1038:
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
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
    def convertBST(self, root: TreeNode) -> TreeNode:
        tot = 0

        def dfs(root: TreeNode) -> None:
            nonlocal tot
            if not root:
                return
            dfs(root.right)
            root.val += tot
            tot = root.val
            dfs(root.left)

        dfs(root)
        return root


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    tree = TreeNode(2)
    tree.left, tree.right = TreeNode(0), TreeNode(3)
    tree.left.left, tree.left.right = TreeNode(-4), TreeNode(1)
    solu.convertBST(tree)
