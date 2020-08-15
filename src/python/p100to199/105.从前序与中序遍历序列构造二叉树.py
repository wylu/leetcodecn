#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   105.从前序与中序遍历序列构造二叉树.py
@Time    :   2020/08/15 18:44:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (67.74%)
# Likes:    620
# Dislikes: 0
# Total Accepted:    104.7K
# Total Submissions: 154.6K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
# 返回如下的二叉树：
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return

        indices = {v: i for i, v in enumerate(inorder)}
        return self.build(preorder, 0, len(preorder) - 1, 0, indices)

    def build(self, pre: List[int], sp: int, ep: int, si: int,
              indices: dict) -> TreeNode:
        if sp > ep:
            return

        root = TreeNode(pre[sp])
        idx = indices[root.val]
        llen = idx - si

        root.left = self.build(pre, sp + 1, sp + llen, si, indices)
        root.right = self.build(pre, sp + llen + 1, ep, idx + 1, indices)

        return root


# @lc code=end
