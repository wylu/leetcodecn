#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   410.分割数组的最大值.py
@Time    :   2020/07/25 21:15:02
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
Dynamic Programming
「将数组分割为 m 段，求...」是动态规划题目常见的问法。

State:
  f[i][j]: 表示将数组的前 i 个数分割为 j 段所能得到的最大连续子数组和的最小值。

Initial State:
  f[0][0] = 0

State Transition:
  在进行状态转移时，考虑第 j 段的具体范围：我们可以枚举 k，其中前 k 个数被分割为
  j−1 段，而第 k+1 到第 i 个数为第 j 段。此时，这 j 段子数组中和的最大值，就等于
  f[k][j−1] 与 sub(k+1,i) 中的较大值，其中 sub(i,j) 表示数组 nums 中下标落在
  区间 [i,j] 内的数的和。

  由于我们要使得子数组中和的最大值最小，因此可以列出如下的状态转移方程：
      f[i][j] = min{max(f[k][j−1], sub(k+1,i))}, 0 <= k <= i-1

  对于状态 f[i][j]，由于我们不能分出空的子数组，因此合法的状态必须有 i >= j。
  对于不合法（i < j）的状态，由于我们的目标是求出最小值，因此可以将这些状态全部
  初始化为一个很大的数。

  在上述的状态转移方程中，一旦我们尝试从不合法的状态 f[k][j−1] 进行转移，那么
  max(...) 将会是一个很大的数，就不会对最外层的 min{...} 产生任何影响。

  此外，我们还需要将 f[0][0] 的值初始化为 0。在上述的状态转移方程中，当 j=1 时，
  唯一的可能性就是前 i 个数被分成了一段。如果枚举的 k=0，那么就代表着这种情况；
  如果 k != 0，对应的状态 f[k][0] 是一个不合法的状态，无法进行转移。
  因此我们需要令 f[0][0] = 0。
"""

#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
# https://leetcode-cn.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (44.03%)
# Likes:    266
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 34.2K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。
# 设计一个算法使得这 m 个子数组各自和的最大值最小。
#
# 注意:
# 数组长度 n 满足以下条件:
#
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
#
#
# 示例:
#
#
# 输入:
# nums = [7,2,5,10,8]
# m = 2
#
# 输出:
# 18
#
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
#
#
#

from typing import List


# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[1 << 32 - 1] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for e in nums:
            sub.append(sub[-1] + e)

        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))

        return f[n][m]


# @lc code=end
