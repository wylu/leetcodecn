#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   199.二叉树的右视图.py
@Time    :   2021/05/04 18:15:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (64.91%)
# Likes:    453
# Dislikes: 0
# Total Accepted:    104.1K
# Total Submissions: 160.4K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []

        def dfs(root: TreeNode, level: int) -> None:
            if not root:
                return

            if level == len(ans):
                ans.append(root.val)
            else:
                ans[level] = root.val

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return ans


# @lc code=end
