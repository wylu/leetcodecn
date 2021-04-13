#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   783.二叉搜索树节点最小距离.py
@Time    :   2020/08/18 14:08:08
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (53.62%)
# Likes:    71
# Dislikes: 0
# Total Accepted:    16.2K
# Total Submissions: 30.2K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# 给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。
#
#
#
# 示例：
#
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树节点对象(TreeNode object)，而不是数组。
#
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
#
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \
# ⁠   1   3
#
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
#
#
#
# 注意：
#
#
# 二叉树的大小范围在 2 到 100。
# 二叉树总是有效的，每个节点的值都是整数，且不重复。
# 本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# 相同
#
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
    def minDiffInBST(self, root: TreeNode) -> int:
        ans, pre = 0x7FFFFFFF, None

        def dfs(root: TreeNode) -> None:
            nonlocal ans, pre
            if not root:
                return
            dfs(root.left)
            if pre:
                ans = min(ans, root.val - pre.val)
            pre = root
            dfs(root.right)

        dfs(root)
        return ans


# @lc code=end

# class Solution:
#     def minDiffInBST(self, root: TreeNode) -> int:
#         ans, pre = 0x7FFFFFFF, None
#         stack = []
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root = root.left

#             root = stack.pop()
#             if pre:
#                 ans = min(ans, root.val - pre.val)
#             pre = root
#             root = root.right

#         return ans
