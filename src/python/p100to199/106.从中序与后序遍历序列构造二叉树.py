#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   106.从中序与后序遍历序列构造二叉树.py
@Time    :   2020/08/15 18:32:16
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (69.27%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    47.1K
# Total Submissions: 67.9K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder or len(inorder) != len(postorder):
            return

        indices = {v: i for i, v in enumerate(inorder)}
        return self.build(0, postorder, 0, len(postorder) - 1, indices)

    def build(self, si: int, post: List[int], sp: int, ep: int,
              indices: dict) -> TreeNode:
        if sp > ep:
            return

        root = TreeNode(post[ep])
        idx = indices[root.val]
        llen = idx - si

        root.left = self.build(si, post, sp, sp + llen - 1, indices)
        root.right = self.build(idx + 1, post, sp + llen, ep - 1, indices)

        return root


# @lc code=end
