#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   162.寻找峰值.py
@Time    :   2020/10/03 11:39:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
# https://leetcode-cn.com/problems/find-peak-element/description/
#
# algorithms
# Medium (47.55%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    60.7K
# Total Submissions: 127.6K
# Testcase Example:  '[1,2,3,1]'
#
# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
#
# 示例 2:
#
# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
# 或者返回索引 5， 其峰值元素为 6。
#
#
# 说明:
#
# 你的解法应该是 O(logN) 时间复杂度的。
#
#
from typing import List


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findPeakElement([1, 2, 3, 1]))
    print(solu.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
    print(solu.findPeakElement([1, 2, 3, 4, 5]))
    print(solu.findPeakElement([5, 4, 3, 2, 1]))
