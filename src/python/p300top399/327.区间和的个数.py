#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   327.区间和的个数.py
@Time    :   2020/11/07 22:19:11
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
# https://leetcode-cn.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (36.90%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 37.1K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# 给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
#
# 说明:
# 最直观的算法复杂度是 O(n^2) ，请在此基础上优化你的算法。
#
# 示例:
#
# 输入: nums = [-2,5,-1], lower = -2, upper = 2,
# 输出: 3
# 解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
#
#
#
from typing import List
"""
方法一：归并排序
思路与算法

设前缀和数组为 preSum，则问题等价于求所有的下标对 (i,j)，满足
preSum[j]−preSum[i] ∈ [lower,upper]

我们先考虑如下的问题：给定两个升序排列的数组 n1, n2，试找出所有的下标对
(i,j)，满足 n2[j]−n1[i] ∈ [lower,upper]。在已知两个数组均为升序的
情况下，这一问题是相对简单的：我们在 n2 中维护两个指针 l,r。起初，它们
都指向 n2 的起始位置。

随后，我们考察 n1 的第一个元素。首先，不断地将指针 l 向右移动，直到
n2[l] ≥ n1[0] + lower 为止，此时，l 及其右边的元素均大于或等于
n1[0] + lower；随后，再不断地将指针 r 向右移动，直到 n2[r] > n1[0]+upper
为止，则 r 左边的元素均小于或等于 n1[0]+upper。故区间 [l,r) 中的所有下标 j，
都满足 n2[j]−n1[0] ∈ [lower,upper]

接下来，我们考察 n1 的第二个元素。由于 n1 是递增的，不难发现 l,r 只可能向右
移动。因此，我们不断地进行上述过程，并对于 n1 中的每一个下标，都记录相应的区间
[l,r) 的大小。最终，我们就统计得到了满足条件的下标对 (i,j) 的数量。

在解决这一问题后，原问题就迎刃而解了：我们采用归并排序的方式，能够得到左右两个
数组排序后的形式，以及对应的下标对数量。对于原数组而言，若要找出全部的下标对
数量，只需要再额外找出左端点在左侧数组，同时右端点在右侧数组的下标对数量，
而这正是我们此前讨论的问题。
"""


# @lc code=start
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]

        def merge(left: int, mid: int, right: int) -> None:
            # 统计下标对的数量
            ans, i, lt, rt = 0, left, mid + 1, mid + 1
            while i <= mid:
                while lt <= right and ps[lt] - ps[i] < lower:
                    lt += 1
                while rt <= right and ps[rt] - ps[i] <= upper:
                    rt += 1
                ans += rt - lt
                i += 1

            assist = [0] * (right - left + 1)
            i, j, k = left, mid + 1, 0
            while i <= mid or j <= right:
                if i > mid:
                    assist[k] = ps[j]
                    j += 1
                elif j > right:
                    assist[k] = ps[i]
                    i += 1
                else:
                    if ps[i] <= ps[j]:
                        assist[k] = ps[i]
                        i += 1
                    else:
                        assist[k] = ps[j]
                        j += 1
                k += 1

            for i in range(k):
                ps[left + i] = assist[i]

            return ans

        def mergeSort(left: int, right: int) -> int:
            ans = 0
            if left < right:
                mid = (left + right) // 2
                ans += mergeSort(left, mid)
                ans += mergeSort(mid + 1, right)
                ans += merge(left, mid, right)
            return ans

        return mergeSort(0, n)


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.countRangeSum([-2, 5, -1], -2, 2))
