#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   103.二叉树的锯齿形层序遍历.py
@Time    :   2020/12/22 16:10:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (55.46%)
# Likes:    341
# Dislikes: 0
# Total Accepted:    97.5K
# Total Submissions: 172.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回锯齿形层序遍历如下：
#
#
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
#
#
#
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans, level = [], []
        que, flag = deque([root]), True

        while que:
            for _ in range(len(que)):
                root = que.popleft()
                level.append(root.val)

                if root.left:
                    que.append(root.left)
                if root.right:
                    que.append(root.right)

            if not flag:
                level.reverse()
            ans.append(level)
            level, flag = [], not flag

        return ans


# @lc code=end
