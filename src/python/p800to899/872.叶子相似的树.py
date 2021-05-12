#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   872.叶子相似的树.py
@Time    :   2021/05/10 19:13:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#
# https://leetcode-cn.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (65.37%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    47.6K
# Total Submissions: 72.7K
# Testcase Example:
# '[3,5,1,6,2,9,8,null,null,7,4]\n' +
# '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
#
#
#
# 举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。
#
# 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
#
# 如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root1 = [1], root2 = [1]
# 输出：true
#
#
# 示例 3：
#
#
# 输入：root1 = [1], root2 = [2]
# 输出：false
#
#
# 示例 4：
#
#
# 输入：root1 = [1,2], root2 = [2,2]
# 输出：true
#
#
# 示例 5：
#
#
#
#
# 输入：root1 = [1,2,3], root2 = [1,3,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 给定的两棵树可能会有 1 到 200 个结点。
# 给定的两棵树上的值介于 0 到 200 之间。
#
#
#
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root: TreeNode, seq: List[int]) -> None:
            if not root:
                return
            if root.left:
                dfs(root.left, seq)
            if not root.left and not root.right:
                seq.append(root.val)
            if root.right:
                dfs(root.right, seq)

        seq1, seq2 = [], []
        dfs(root1, seq1)
        dfs(root2, seq2)
        return seq1 == seq2


# @lc code=end
