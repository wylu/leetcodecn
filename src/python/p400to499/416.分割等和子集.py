#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   416.分割等和子集.py
@Time    :   2020/10/11 21:55:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (49.51%)
# Likes:    533
# Dislikes: 0
# Total Accepted:    75.4K
# Total Submissions: 155K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意:
#
#
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
#
#
# 示例 1:
#
# 输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#
#
#
#
# 示例 2:
#
# 输入: [1, 2, 3, 5]
#
# 输出: false
#
# 解释: 数组不能分割成两个元素和相等的子集.
#
#
#
#
#
from typing import List
"""
dp[i][j]: 是否能 nums[0,...,i] 中取若干个元素使得其总和为 j
"""


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, tot = len(nums), sum(nums)
        if n < 2 or tot % 2 != 0:
            return False

        tot //= 2
        dp = [True] + [False] * tot

        for i in range(n):
            for j in range(tot, nums[i] - 1, -1):
                dp[j] |= dp[j - nums[i]]

        return dp[tot]


# @lc code=end

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         n, tot = len(nums), sum(nums)
#         if n < 2 or tot % 2 != 0:
#             return False

#         tot //= 2
#         dp = [[False] * (tot + 1) for _ in range(n)]

#         for i in range(n - 1):
#             dp[i][0] = True
#             if nums[i] <= tot:
#                 dp[i][nums[i]] = True

#             for j in range(1, tot + 1):
#                 if dp[i][j]:
#                     dp[i + 1][j] = True
#                     if j + nums[i + 1] <= tot:
#                         dp[i + 1][j + nums[i + 1]] = True

#         return dp[n - 1][tot]

if __name__ == "__main__":
    solu = Solution()
    print(solu.canPartition([1, 5, 11, 5]))
    print(solu.canPartition([1, 2, 3, 5]))
    print(solu.canPartition([100]))
