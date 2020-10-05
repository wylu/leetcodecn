#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   287.寻找重复数.py
@Time    :   2020/10/05 11:50:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (65.90%)
# Likes:    888
# Dislikes: 0
# Total Accepted:    100.2K
# Total Submissions: 152.1K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和
# n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1:
#
# 输入: [1,3,4,2,2]
# 输出: 2
#
#
# 示例 2:
#
# 输入: [3,1,3,4,2]
# 输出: 3
#
#
# 说明：
#
#
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n^2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。
#
#
#
from typing import List
"""
方法一：二分查找

方法二：快慢指针
"""


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# @lc code=end

# 方法一：二分查找
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         left, right = 1, len(nums) - 1
#         while left < right:
#             mid = (left + right) // 2
#             cnt = sum(1 for num in nums if num <= mid)
#             if cnt <= mid:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left

if __name__ == "__main__":
    solu = Solution()
    print(solu.findDuplicate([1, 3, 4, 2, 2]))
    print(solu.findDuplicate([3, 1, 3, 4, 2]))
