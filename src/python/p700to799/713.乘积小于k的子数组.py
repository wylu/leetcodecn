#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   713.乘积小于k的子数组.py
@Time    :   2020/09/22 09:10:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#
# https://leetcode-cn.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (36.61%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    9.3K
# Total Submissions: 25.3K
# Testcase Example:  '[10,5,2,6]\n100'
#
# 给定一个正整数数组 nums。
#
# 找出该数组内乘积小于 k 的连续的子数组的个数。
#
# 示例 1:
#
#
# 输入: nums = [10,5,2,6], k = 100
# 输出: 8
# 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
#
#
# 说明:
#
#
# 0 < nums.length <= 50000
# 0 < nums[i] < 1000
# 0 <= k < 10^6
#
#
#
import math

from typing import List
"""
方法一：二分查找

分析

我们可以使用二分查找解决这道题目，即对于固定的 i，二分查找出最大的 j 满足
nums[i] 到 nums[j] 的乘积小于 k。但由于乘积可能会非常大（在最坏情况下会
达到 1000^50000，会导致数值溢出，因此我们需要对 nums 数组取对数，将乘法
转换为加法，即：

log(nums[i] * ... * nums[j]) = log(nums[i]) + ... + log(nums[j])

这样就不会出现数值溢出的问题了。

算法

对 nums 中的每个数取对数后，我们存储它的前缀和 prefix，即：

prefix[i+1] = nums[0] + ... + nums[i]

这样在二分查找时，对于 i 和 j，我们可以用 prefix[j+1] − prefix[i] 得到
nums[i] 到 nums[j] 的乘积的对数。对于固定的 i，当找到最大的满足条件的 j
后，它会包含 j−i+1 个乘积小于 k 的连续子数组。
"""


# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0

        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + math.log(nums[i - 1])

        ans = 0
        logk = math.log(k) - 1e-9
        for i in range(n):
            lo, hi = i + 1, n + 1
            while lo < hi:
                mid = (lo + hi) // 2
                if ps[mid] - ps[i] < logk:
                    lo = mid + 1
                else:
                    hi = mid
            ans += lo - i - 1

        return ans


# @lc code=end

# 超时
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         ans, n = 0, len(nums)
#         for i in range(n):
#             cur = 1
#             for j in range(i, -1, -1):
#                 cur *= nums[j]
#                 if cur >= k:
#                     break
#                 ans += 1

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
