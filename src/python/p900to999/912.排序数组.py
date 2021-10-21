#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   912.排序数组.py
@Time    :   2021/10/21 23:57:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (55.96%)
# Likes:    403
# Dislikes: 0
# Total Accepted:    235.3K
# Total Submissions: 420.4K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
# 示例 2：
#
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
#
#
#
import random
from typing import List


# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums: List[int], left: int, right: int) -> int:
            pivot = random.randint(left, right)
            nums[pivot], nums[right] = nums[right], nums[pivot]

            j = left - 1
            for i in range(left, right):
                if nums[i] < nums[right]:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]

            j += 1
            nums[j], nums[right] = nums[right], nums[j]
            return j

        def quickSort(nums: List[int], left: int, right: int) -> None:
            if left < right:
                idx = partition(nums, left, right)
                quickSort(nums, left, idx - 1)
                quickSort(nums, idx + 1, right)

        quickSort(nums, 0, len(nums) - 1)
        return nums


# @lc code=end

if __name__ == '__main__':
    import time
    solu = Solution()
    nums = list(range(1, 50000))
    start = time.monotonic()
    nums = solu.sortArray(nums)
    end = time.monotonic()

    print(f'Time Cost: {end - start:.3f}')
