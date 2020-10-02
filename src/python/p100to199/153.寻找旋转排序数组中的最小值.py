#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   153.寻找旋转排序数组中的最小值.py
@Time    :   2020/10/02 22:26:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (51.70%)
# Likes:    262
# Dislikes: 0
# Total Accepted:    80.9K
# Total Submissions: 156.4K
# Testcase Example:  '[3,4,5,1,2]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
#
# 输入: [3,4,5,1,2]
# 输出: 1
#
# 示例 2:
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
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
            else:
                right = mid

        return nums[left]


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findMin([3, 4, 5, 1, 2]))
    print(solu.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(solu.findMin([1, 2, 3, 4, 5]))
