#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   645.错误的集合.py
@Time    :   2021/07/04 09:24:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
# https://leetcode-cn.com/problems/set-mismatch/description/
#
# algorithms
# Easy (41.65%)
# Likes:    186
# Dislikes: 0
# Total Accepted:    41.7K
# Total Submissions: 98.2K
# Testcase Example:  '[1,2,2,4]'
#
# 集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且
# 有一个数字重复 。
#
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。
#
# 请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,2,4]
# 输出：[2,3]
#
#
# 示例 2：
#
#
# 输入：nums = [1,1]
# 输出：[1,2]
#
#
#
#
# 提示：
#
#
# 2 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup_total = sum(nums)
        uni_total = sum(set(nums))
        duplicate = dup_total - uni_total
        not_found = (1 + len(nums)) * len(nums) // 2 - uni_total
        return [duplicate, not_found]


# @lc code=end

# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         cnt = [0] * n
#         for num in nums:
#             cnt[num - 1] += 1

#         not_found = duplicate = 0
#         for i in range(n):
#             if cnt[i] == 0:
#                 not_found = i + 1
#             elif cnt[i] > 1:
#                 duplicate = i + 1

#         return [duplicate, not_found]

if __name__ == '__main__':
    solu = Solution()
    print(solu.findErrorNums(nums=[1, 2, 2, 4]))
    print(solu.findErrorNums(nums=[1, 1]))
    print(solu.findErrorNums(nums=[3, 2, 3, 4, 6, 5]))
