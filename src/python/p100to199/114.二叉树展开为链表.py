#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   114.二叉树展开为链表.py
@Time    :   2020/08/02 20:04:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (69.61%)
# Likes:    478
# Dislikes: 0
# Total Accepted:    66.9K
# Total Submissions: 94.8K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为一个单链表。
#
#
#
# 例如，给定二叉树
#
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
#
# 将其展开为：
#
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # Morris Preorder Traversal
        pre, cur = None, root
        while cur:
            if not cur.left:
                cur = cur.right
                continue

            # 找出左子树的最右结点，也即找出当前结点的前驱
            pre = cur.left
            while pre.right:
                pre = pre.right

            pre.right = cur.right
            cur.right = cur.left
            cur.left = None

            cur = cur.right


# @lc code=end

# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if not root:
#             return

#         pre = None
#         stack = [root]
#         while stack:
#             cur = stack.pop()
#             if pre:
#                 pre.left = None
#                 pre.right = cur

#             if cur.right:
#                 stack.append(cur.right)

#             if cur.left:
#                 stack.append(cur.left)

#             pre = cur
