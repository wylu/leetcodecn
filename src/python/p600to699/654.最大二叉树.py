#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   654.最大二叉树.py
@Time    :   2022/08/20 17:37:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
# https://leetcode.cn/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (81.52%)
# Likes:    518
# Dislikes: 0
# Total Accepted:    135.4K
# Total Submissions: 164K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:
#
#
# 创建一个根节点，其值为 nums 中的最大值。
# 递归地在最大值 左边 的 子数组前缀上 构建左子树。
# 递归地在最大值 右边 的 子数组后缀上 构建右子树。
#
#
# 返回 nums 构建的 最大二叉树 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,2,1,6,0,5]
# 输出：[6,3,5,null,2,0,null,null,1]
# 解释：递归调用如下所示：
# - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
# ⁠   - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
# ⁠       - 空数组，无子节点。
# ⁠       - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
# ⁠           - 空数组，无子节点。
# ⁠           - 只有一个元素，所以子节点是一个值为 1 的节点。
# ⁠   - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
# ⁠       - 只有一个元素，所以子节点是一个值为 0 的节点。
# ⁠       - 空数组，无子节点。
#
#
# 示例 2：
#
#
# 输入：nums = [3,2,1]
# 输出：[3,null,2,null,1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# nums 中的所有整数 互不相同
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

    def constructMaximumBinaryTree(self,
                                   nums: List[int]) -> Optional[TreeNode]:

        def dfs(s: int, e: int) -> Optional[TreeNode]:
            if s > e:
                return None

            if s == e:
                return TreeNode(nums[s])

            j = s
            for i in range(s + 1, e + 1):
                if nums[i] > nums[j]:
                    j = i

            return TreeNode(nums[j], dfs(s, j - 1), dfs(j + 1, e))

        return dfs(0, len(nums) - 1)


# @lc code=end
