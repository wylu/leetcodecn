#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2035.将数组分成两个数组并最小化数组和的差.py
@Time    :   2021/10/13 17:18:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=2035 lang=python3
#
# [2035] 将数组分成两个数组并最小化数组和的差
#
# https://leetcode-cn.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/
#
# algorithms
# Hard (28.49%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 4.6K
# Testcase Example:  '[3,9,7,3]'
#
# 给你一个长度为 2 * n 的整数数组。你需要将 nums 分成 两个 长度为 n 的数组，分别求出两个数组的和，并 最小化 两个数组和之 差的绝对值
# 。nums 中每个元素都需要放入两个数组之一。
#
# 请你返回 最小 的数组和之差。
#
#
#
# 示例 1：
#
#
#
# 输入：nums = [3,9,7,3]
# 输出：2
# 解释：最优分组方案是分成 [3,9] 和 [7,3] 。
# 数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。
#
#
# 示例 2：
#
# 输入：nums = [-36,36]
# 输出：72
# 解释：最优分组方案是分成 [-36] 和 [36] 。
# 数组和之差的绝对值为 abs((-36) - (36)) = 72 。
#
#
# 示例 3：
#
#
#
# 输入：nums = [2,-1,0,4,-2,-9]
# 输出：0
# 解释：最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。
# 数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。
#
#
#
#
# 提示：
#
#
# 1 <= n <= 15
# nums.length == 2 * n
# -10^7 <= nums[i] <= 10^7
#
#
#
from typing import List
"""
方法一：Meet in the middle + 动态规划 + 双指针
要让两个数组和的差最小，就是要让其中一个数组的和尽可能接近 sum/2。

直接枚举，在 N=15 时需要考虑 C(30,15) 约等于 1.5 * 10^8 种情况
（这里还没有考虑每种情况需要求和），显然会超时。

因此，我们考虑使用 Meet in the middle 的方法，也即：分别求出前 N 个数中
取 i（0≤i≤N）个能够形成的和，以及后 N 个数中取 i（0≤i≤N）个能够形成的和，
最后枚举前 N 个数中选取的个数，来求取最后的答案。在折半之后，最多需要考虑
的情况只有 C(15,7) = 6435 种。

第一步是一个比较简单的动态规划，注意这里最好使用集合类型来存储中间结果，
以免出现大量重复。

第二步中，假设从前 N 个数中选 i 个，则应当从后 N 个数中选 N-i 个。
这时就变成了一个经典问题：从两个数组中各选择一个数，使得它们的和最接近
某一个给定的数。我们对两个数组分别排序后使用双指针求解即可。

在具体实现中，我们使用了一个小 trick，也即将原数组中所有数变为两倍。
这样可以保证我们的目标值 sum/2 是一个整数。
"""


# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] *= 2

        n = len(nums) // 2
        tot = sum(nums)

        ls = [set() for _ in range(n + 1)]
        rs = [set() for _ in range(n + 1)]
        ls[0].add(0)
        rs[0].add(0)

        for i in range(n):
            for j in range(i, -1, -1):
                for val in ls[j]:
                    ls[j + 1].add(val + nums[i])

        for i in range(n, n * 2):
            for j in range(i - n, -1, -1):
                for val in rs[j]:
                    rs[j + 1].add(val + nums[i])

        for i in range(n + 1):
            ls[i] = sorted(ls[i])
            rs[i] = sorted(rs[i])

        target = tot // 2
        dist = 0x7FFFFFFF
        for i in range(n + 1):
            llen, rlen = len(ls[i]), len(rs[n - i])
            pl, pr = 0, rlen - 1
            while pl < llen and pr >= 0:
                current = ls[i][pl] + rs[n - i][pr]
                dist = min(dist, abs(current - target))
                if current < target:
                    pl += 1
                else:
                    pr -= 1

        return dist


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumDifference(nums=[3, 9, 7, 3]))
    print(solu.minimumDifference(nums=[-36, 36]))
    print(solu.minimumDifference(nums=[2, -1, 0, 4, -2, -9]))
