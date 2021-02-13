#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   448.找到所有数组中消失的数字.py
@Time    :   2021/02/13 14:03:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (62.60%)
# Likes:    605
# Dislikes: 0
# Total Accepted:    81.9K
# Total Submissions: 130.8K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
#
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
#
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
#
# 示例:
#
#
# 输入:
# [4,3,2,7,8,2,3,1]
#
# 输出:
# [5,6]
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            nums[(num - 1) % n] += n
        return [i + 1 for i, num in enumerate(nums) if num <= n]


# @lc code=end

# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
#                 idx = nums[i] - 1
#                 nums[i], nums[idx] = nums[idx], nums[i]
#         return [i + 1 for i, num in enumerate(nums) if i + 1 != num]

if __name__ == "__main__":
    solu = Solution()
    print(solu.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
