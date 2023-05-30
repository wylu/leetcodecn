#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   1110.删点成林.py
@Time    :   2023/05/30 23:46:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2023, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林
#
# https://leetcode.cn/problems/delete-nodes-and-return-forest/description/
#
# algorithms
# Medium (69.31%)
# Likes:    288
# Dislikes: 0
# Total Accepted:    33.8K
# Total Submissions: 48.8K
# Testcase Example:  '[1,2,3,4,5,6,7]\n[3,5]'
#
# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。
#
# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
#
# 返回森林中的每棵树。你可以按任意顺序组织答案。
#
#
#
# 示例 1：
#
#
#
#
# 输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
# 输出：[[1,2,null,4],[6],[7]]
#
#
# 示例 2：
#
#
# 输入：root = [1,2,4,null,3], to_delete = [3]
# 输出：[[1,2,4]]
#
#
#
#
# 提示：
#
#
# 树中的节点数最大为 1000。
# 每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
# to_delete.length <= 1000
# to_delete 包含一些从 1 到 1000、各不相同的值。
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

    def delNodes(self, root: Optional[TreeNode],
                 to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)

        def dfs(root: Optional[TreeNode], hasParent: bool) -> List[TreeNode]:
            if not root:
                return []

            if root.val in to_delete:
                return dfs(root.left, False) + dfs(root.right, False)

            res = [] if hasParent else [root]

            if root.left:
                res.extend(dfs(root.left, True))
                if root.left.val in to_delete:
                    root.left = None

            if root.right:
                res.extend(dfs(root.right, True))
                if root.right.val in to_delete:
                    root.right = None

            return res

        return dfs(root, False)


# @lc code=end
