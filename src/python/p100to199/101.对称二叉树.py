#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   101.对称二叉树.py
@Time    :   2020/08/14 23:55:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (52.68%)
# Likes:    961
# Dislikes: 0
# Total Accepted:    191.7K
# Total Submissions: 363.9K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# 进阶：
#
# 你可以运用递归和迭代两种方法解决这个问题吗？
#
#

# @lc code=start
from collections import deque
"""
首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。初始化时我们把
根节点入队两次。每次提取两个结点并比较它们的值（队列中每两个连续的结点应该是
相等的，而且它们的子树互为镜像），然后将两个结点的左右子结点按相反的顺序插入
队列中。当队列为空时，或者我们检测到树不对称（即从队列中取出两个不相等的连续
结点）时，该算法结束。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        que = deque()
        que.append(root)
        que.append(root)

        while que:
            r1 = que.popleft()
            r2 = que.popleft()

            if not r1 and not r2:
                continue

            if not r1 or not r2 or (r1.val != r2.val):
                return False

            que.append(r1.left)
            que.append(r2.right)

            que.append(r1.right)
            que.append(r2.left)

        return True


# @lc code=end

# 递归
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         return self.isSym(root, root)

#     def isSym(self, r1: TreeNode, r2: TreeNode) -> bool:
#         if not r1 and not r2:
#             return True

#         if not r1 or not r2:
#             return False

#         return (r1.val == r2.val and self.isSym(r1.left, r2.right)
#                 and self.isSym(r1.right, r2.left))
