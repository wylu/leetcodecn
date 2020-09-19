#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   494.目标和.py
@Time    :   2020/09/19 18:07:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (44.43%)
# Likes:    401
# Dislikes: 0
# Total Accepted:    45.8K
# Total Submissions: 103.2K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或
# -中选择一个符号添加在前面。
#
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
#
#
#
# 示例：
#
# 输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 一共有5种方法让最终目标和为3。
#
#
#
#
# 提示：
#
#
# 数组非空，且长度不会超过 20 。
# 初始的数组的和不会超过 1000 。
# 保证返回的最终结果能被 32 位整数存下。
#
#
#
# from functools import lru_cache
from typing import List
"""
方法一：DFS 枚举

方法二：动态规划

这道题也是一个常见的背包问题，我们可以用类似求解背包问题的方法来求出可能的方法数。

我们用 dp[i][j] 表示用数组中的前 i 个元素，组成和为 j 的方案数。考虑第 i 个数
nums[i]，它可以被添加 + 或 -，因此状态转移方程如下：

    dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]

也可以写成递推的形式：

    dp[i][j + nums[i]] += dp[i - 1][j]
    dp[i][j - nums[i]] += dp[i - 1][j]

由于数组中所有数的和不超过 1000，那么 j 的最小值可以达到 -1000。在很多语言中，
是不允许数组的下标为负数的，因此我们需要给 dp[i][j] 的第二维预先增加 1000，即：

    dp[i][j + nums[i] + 1000] += dp[i - 1][j + 1000]
    dp[i][j - nums[i] + 1000] += dp[i - 1][j + 1000]
"""


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        dp = [[0] * 2001 for _ in range(n)]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1
        for i in range(1, n):
            for j in range(-1000, 1001):
                if dp[i - 1][j + 1000] > 0:
                    dp[i][j + nums[i] + 1000] += dp[i - 1][j + 1000]
                    dp[i][j - nums[i] + 1000] += dp[i - 1][j + 1000]

        return 0 if S > 1000 else dp[n - 1][S + 1000]


# @lc code=end

# 方法一
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         n = len(nums)

#         @lru_cache(None)
#         def dfs(c: int, target: int) -> int:
#             if c == n:
#                 return int(target == S)
#             return dfs(c + 1, target + nums[c]) + dfs(c + 1, target - nums[c])

#         return dfs(0, 0)

if __name__ == '__main__':
    solu = Solution()
    print(solu.findTargetSumWays([1, 1, 1], 2))
    print(solu.findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(
        solu.findTargetSumWays([
            40, 2, 49, 50, 46, 6, 5, 23, 38, 45, 45, 17, 4, 26, 40, 33, 14, 9,
            37, 24
        ], 7))
