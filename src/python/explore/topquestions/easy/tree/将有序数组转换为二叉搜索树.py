#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   将有序数组转换为二叉搜索树.py
@Time    :   2020/08/02 00:05:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], left: int, right: int) -> TreeNode:
        if left > right:
            return

        mid = (left + right + 1) // 2
        root = TreeNode(nums[mid])
        root.left = self.build(nums, left, mid - 1)
        root.right = self.build(nums, mid + 1, right)

        return root
