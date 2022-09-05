#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   652.寻找重复的子树.py
@Time    :   2022/09/05 21:45:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#
# https://leetcode.cn/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (60.54%)
# Likes:    594
# Dislikes: 0
# Total Accepted:    78.1K
# Total Submissions: 129K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# 给定一棵二叉树 root，返回所有重复的子树。
#
# 对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
#
# 如果两棵树具有相同的结构和相同的结点值，则它们是重复的。
#
#
#
# 示例 1：
#
#
#
#
# 输入：root = [1,2,3,4,null,2,4,null,null,4]
# 输出：[[2,4],[4]]
#
# 示例 2：
#
#
#
#
# 输入：root = [2,1,1]
# 输出：[[1]]
#
# 示例 3：
#
#
#
#
# 输入：root = [2,2,2,3,null,3,null]
# 输出：[[2,3],[3]]
#
#
#
# 提示：
#
#
# 树中的结点数在[1,10^4]范围内。
# -200 <= Node.val <= 200
#
#
#
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:

    def findDuplicateSubtrees(
            self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        idx, seen, repeat = 0, {}, set()

        def dfs(root: Optional[TreeNode]) -> str:
            if not root:
                return 0

            atree = (root.val, dfs(root.left), dfs(root.right))
            if atree in seen:
                btree, index = seen[atree]
                repeat.add(btree)
                return index

            nonlocal idx
            idx += 1
            seen[atree] = (root, idx)
            return idx

        dfs(root)
        return list(repeat)


# @lc code=end

# class Solution:

#     def findDuplicateSubtrees(
#             self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
#         seen, repeat = {}, set()

#         def dfs(root: Optional[TreeNode]) -> str:
#             if not root:
#                 return ''

#             serial = ''.join([
#                 str(root.val), '(',
#                 dfs(root.left), ')(',
#                 dfs(root.right), ')'
#             ])
#             if serial in seen:
#                 repeat.add(seen[serial])
#             else:
#                 seen[serial] = root

#             return serial

#         dfs(root)
#         return list(repeat)
