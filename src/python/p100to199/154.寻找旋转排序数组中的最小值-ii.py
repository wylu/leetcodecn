#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   154.寻找旋转排序数组中的最小值-ii.py
@Time    :   2020/10/05 00:43:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (50.32%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    38.2K
# Total Submissions: 76K
# Testcase Example:  '[1,3,5]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 注意数组中可能存在重复的元素。
#
# 示例 1：
#
# 输入: [1,3,5]
# 输出: 1
#
# 示例 2：
#
# 输入: [2,2,2,0,1]
# 输出: 0
#
# 说明：
#
#
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findMin([1, 3, 5]))
    print(solu.findMin([2, 2, 2, 0, 1]))
    print(solu.findMin([3, 1, 3]))
