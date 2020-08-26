#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   673.最长递增子序列的个数.py
@Time    :   2020/08/26 17:44:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (35.74%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 31.8K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未排序的整数数组，找到最长递增子序列的个数。
#
# 示例 1:
#
#
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
#
#
# 示例 2:
#
#
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#
#
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
#
#
from typing import List
"""
Dynamic Programming

State:
  dp[i]: 表示以 nums[i] 为结尾的最长递增子序列的长度
  cnts[i]: 表示以 nums[i] 为结尾且长度为 dp[i] 的递增子序列的个数
"""


# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n, m = len(nums), 1
        dp, cnts = [1] * n, [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        cnts[i] = cnts[j]
                    elif dp[j] + 1 == dp[i]:
                        cnts[i] += cnts[j]

                    dp[i] = max(dp[i], dp[j] + 1)

            m = max(m, dp[i])

        return sum(cnts[i] for i, v in enumerate(dp) if v == m)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
    print(solu.findNumberOfLIS([1, 3, 5, 4, 7]))
    print(solu.findNumberOfLIS([2, 2, 2, 2, 2]))
    print(solu.findNumberOfLIS([1]))
