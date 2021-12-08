#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   689.三个无重叠子数组的最大和.py
@Time    :   2021/12/08 09:15:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=689 lang=python3
#
# [689] 三个无重叠子数组的最大和
#
# https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
#
# algorithms
# Hard (52.57%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 9.4K
# Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，找出三个长度为 k 、互不重叠、且 3 * k 项的和最大的子数组，并返回这三个子数组。
#
# 以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 0 开始）。如果有多个结果，返回字典序最小的一个。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,1,2,6,7,5,1], k = 2
# 输出：[0,3,5]
# 解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
# 也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
# 输出：[0,2,4]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] < 2^16
# 1 <= k <= floor(nums.length / 3)
#
#
#
from collections import defaultdict
from itertools import accumulate
from typing import List
"""
动态规划

思路：

用 dp[i][j]​ 表示到数组第 j 个元素为止，前 i​ 个互不重叠的子数组的最大值。
对于当前第 j​ 个元素所对应的值，我们有不取和取两种选择，选择不取该元素，
则值为到 j-1 个元素时前 i 个互不重叠的子数组的最大值，即 dp[i][j-1]​，
选择取该元素，则值为到 j-k​ 个元素时前 i-1​ 个互不重叠的子数组的最大值
dp[i-1][j-k]​ 加上最后一段子数组的和，我们选择这两种情况下较大值即可，
可以得到如下状态转移方程：

dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + sum[j] - sum[j-k])

其中，sum 为前缀和数组。
"""


# @lc code=start
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ps = list(accumulate(nums))
        n = len(nums)
        f = [[0] * n for _ in range(4)]

        indices = defaultdict(list)
        for i in range(1, 4):
            f[i][i * k - 1] = ps[i * k - 1]
            indices[(i, i * k - 1)].extend(j * k for j in range(i))

        for i in range(1, 4):
            for j in range(i * k, n):
                if f[i][j - 1] >= f[i - 1][j - k] + ps[j] - ps[j - k]:
                    f[i][j] = f[i][j - 1]
                    indices[(i, j)] = indices[(i, j - 1)]
                else:
                    f[i][j] = f[i - 1][j - k] + ps[j] - ps[j - k]
                    indices[(i, j)] = indices[(i - 1, j - k)] + [j - k + 1]

        return indices[(3, n - 1)]


# @lc code=end

# class Solution:
#     def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
#         ans = []
#         sum1, max_sum1, max_sum1_idx = 0, 0, 0
#         sum2, max_sum12, max_sum12_idx = 0, 0, ()
#         sum3, max_sum123 = 0, 0

#         for i in range(k * 2, len(nums)):
#             sum1 += nums[i - k * 2]
#             sum2 += nums[i - k]
#             sum3 += nums[i]

#             if i >= k * 3 - 1:
#                 if sum1 > max_sum1:
#                     max_sum1 = sum1
#                     max_sum1_idx = i - k * 3 + 1
#                 if max_sum1 + sum2 > max_sum12:
#                     max_sum12 = max_sum1 + sum2
#                     max_sum12_idx = (max_sum1_idx, i - k * 2 + 1)
#                 if max_sum12 + sum3 > max_sum123:
#                     max_sum123 = max_sum12 + sum3
#                     ans = [*max_sum12_idx, i - k + 1]

#                 sum1 -= nums[i - k * 3 + 1]
#                 sum2 -= nums[i - k * 2 + 1]
#                 sum3 -= nums[i - k + 1]

#         return ans

if __name__ == '__main__':
    solu = Solution()
    nums = [1, 2, 1, 2, 6, 7, 5, 1]
    print(solu.maxSumOfThreeSubarrays(nums=nums, k=2))
