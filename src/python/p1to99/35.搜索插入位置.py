#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   35.搜索插入位置.py
@Time    :   2020/09/25 23:31:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (46.70%)
# Likes:    694
# Dislikes: 0
# Total Accepted:    253.3K
# Total Submissions: 542.4K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
#
#
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
#
#
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
#
#
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0
#
#
#
from typing import List


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.searchInsert([1, 3, 5, 6], 5))
    print(solu.searchInsert([1, 3, 5, 6], 2))
    print(solu.searchInsert([1, 3, 5, 6], 7))
    print(solu.searchInsert([1, 3, 5, 6], 0))
