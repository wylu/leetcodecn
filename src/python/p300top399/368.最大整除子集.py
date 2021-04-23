#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   368.最大整除子集.py
@Time    :   2021/04/23 22:24:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
# https://leetcode-cn.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (44.49%)
# Likes:    313
# Dislikes: 0
# Total Accepted:    31.5K
# Total Submissions: 70.9K
# Testcase Example:  '[1,2,3]'
#
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i],
# answer[j]) 都应当满足：
#
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
#
#
# 如果存在多个有效解子集，返回其中任何一个均可。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# nums 中的所有整数 互不相同
#
#
#
from typing import List
"""
前言
首先需要理解什么叫「整除子集」。根据题目的描述，如果一个所有元素互不相同
的集合中的任意元素存在整除关系，就称为整除子集。为了得到「最大整除子集」，
我们需要考虑如何从一个小的整除子集扩充成为更大的整除子集。

根据整除关系具有传递性，即如果 a|b，并且 b|c，那么 a|c，可知：

  - 如果整数 a 是整除子集 S1 的最小整数 b 的约数（即 a|b），那么可以将
    a 添加到 S1 中得到一个更大的整除子集；
  - 如果整数 c 是整除子集 S2 的最大整数 d 的倍数（即 d|c），那么可以将
    c 添加到 S2 中得到一个更大的整除子集。

这两点揭示了当前问题状态转移的特点，因此可以使用动态规划的方法求解。题目
只要求我们得到多个目标子集的其中一个，根据求解动态规划问题的经验，我们需
要将子集的大小定义为状态，然后根据结果倒推得到一个目标子集。事实上，当前
问题和使用动态规划解决的经典问题「300. 最长递增子序列」有相似之处。

方法一：动态规划
根据前言的分析，我们需要将输入数组 nums 按照升序排序，以便获得一个子集的
最小整数或者最大整数。又根据动态规划的「无后效性」状态设计准则，我们需要
将状态定义成「某个元素必须选择」。

状态定义：dp[i] 表示在输入数组 nums 升序排列的前提下，以 nums[i] 为最大
整数的「整除子集」的大小（在这种定义下 nums[i] 必须被选择）。

状态转移方程：枚举 j = 0 ... i-1 的所有整数 nums[j]，如果 nums[j] 能
整除 nums[i]，说明 nums[i] 可以扩充在以 nums[j] 为最大整数的整除子集里
成为一个更大的整除子集。

初始化：由于 nums[i] 必须被选择，因此对于任意 i = 0 ... n-1，初始的时候
dp[i] = 1，这里 n 是输入数组的长度。

输出：同时由于我们需要输出具体方案，需要额外使用 rec 数组来记录每个状态
是由哪个状态转移而来。定义 rec[i] 为记录 dp[i] 是由哪个下标的状态转移而来，
如果 dp[i] = dp[j] + 1, 则有 rec[i] = j。

对于求方案数的题目，多开一个数组来记录状态从何转移而来是最常见的手段。
当我们求得所有的状态值之后，可以对 dp 数组进行遍历，取得具体的最长
「整除子集」长度和对应下标，然后使用 rec 数组进行回溯，取得答案。
"""


# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        f = [1] * n
        g = list(range(n))

        size = 1
        nums.sort()
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and f[j] + 1 > f[i]:
                    f[i] = f[j] + 1
                    g[i] = j
                    size = max(size, f[i])

        idx = -1
        for i in range(n - 1, -1, -1):
            if f[i] == size:
                idx = i
                break

        ans = []
        while size:
            ans.append(nums[idx])
            idx = g[idx]
            size -= 1

        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.largestDivisibleSubset(nums=[1, 2, 3]))
    print(solu.largestDivisibleSubset(nums=[1, 2, 4, 8]))
