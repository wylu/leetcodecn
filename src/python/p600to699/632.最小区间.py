#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   632.最小区间.py
@Time    :   2020/08/01 21:06:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#
# https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (38.93%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 18.4K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# 你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
#
# 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
#
# 示例 1:
#
#
# 输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出: [20,24]
# 解释:
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
#
#
# 注意:
#
#
# 给定的列表可能包含重复元素，所以在这里升序表示 >= 。
# 1 <= k <= 3500
# -10^5 <= 元素的值 <= 10^5
# 对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。
#
#
#

import heapq

from typing import List
"""
给定 k 个列表，需要找到最小区间，使得每个列表都至少有一个数在该区间中。该问题可以
转化为，从 k 个列表中各取一个数，使得这 k 个数中的最大值与最小值的差最小。

假设这 k 个数中的最小值是第 i 个列表中的 x，对于任意 j != i，设第 j 个列表中
被选为 k 个数之一的数是 y，则为了找到最小区间，y 应该取第 j 个列表中大于等于 x
的最小的数。

简单证明如下：假设 z 也是第 j 个列表中的数，且 z>y，则有 z-x > y-x，同时包含
x 和 z 的区间一定不会小于同时包含 x 和 y 的区间。因此，其余 k−1 个列表中应该
取大于等于 x 的最小的数。

由于 k 个列表都是升序排列的，因此对每个列表维护一个指针，通过指针得到列表中的
元素，指针右移之后指向的元素一定大于或等于之前的元素。

使用最小堆维护 k 个指针指向的元素中的最小值，同时维护堆中元素的最大值。初始时，
k 个指针都指向下标 0，最大元素即为所有列表的下标 0 位置的元素中的最大值。每次
从堆中取出最小值，根据最大值和最小值计算当前区间，如果当前区间小于最小区间则用
当前区间更新最小区间，然后将对应列表的指针右移，将新元素加入堆中，并更新堆中元
素的最大值。

如果一个列表的指针超出该列表的下标范围，则说明该列表中的所有元素都被遍历过，堆
中不会再有该列表中的元素，因此退出循环。
"""


# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        lo, hi = -10**6, 10**6
        maxVal = max(arr[0] for arr in nums)
        pq = [(arr[0], i, 0) for i, arr in enumerate(nums)]
        heapq.heapify(pq)

        while pq:
            minVal, row, idx = heapq.heappop(pq)
            if maxVal - minVal < hi - lo:
                lo, hi = minVal, maxVal

            if idx == len(nums[row]) - 1:
                break

            maxVal = max(maxVal, nums[row][idx + 1])
            heapq.heappush(pq, (nums[row][idx + 1], row, idx + 1))

        return [lo, hi]


# @lc code=end
