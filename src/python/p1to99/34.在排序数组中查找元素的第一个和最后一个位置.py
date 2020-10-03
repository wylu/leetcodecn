#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   34.在排序数组中查找元素的第一个和最后一个位置.py
@Time    :   2020/10/03 18:04:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (40.42%)
# Likes:    604
# Dislikes: 0
# Total Accepted:    137.1K
# Total Submissions: 339.2K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
#
from typing import List


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left

        start = search(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        end = search(target + 1)
        return [start, end - 1]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(solu.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(solu.searchRange([7, 7, 8, 8], 7))
    print(solu.searchRange([7, 7, 8, 8], 8))
