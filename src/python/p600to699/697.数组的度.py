#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   697.数组的度.py
@Time    :   2021/02/20 09:31:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
# https://leetcode-cn.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (56.72%)
# Likes:    228
# Dislikes: 0
# Total Accepted:    33.7K
# Total Submissions: 59.4K
# Testcase Example:  '[1,2,2,3,1]'
#
# 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
#
# 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
#
#
# 示例 1：
#
#
# 输入：[1, 2, 2, 3, 1]
# 输出：2
# 解释：
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#
#
# 示例 2：
#
#
# 输入：[1,2,2,3,1,4,2]
# 输出：6
#
#
#
#
# 提示：
#
#
# nums.length 在1到 50,000 区间范围内。
# nums[i] 是一个在 0 到 49,999 范围内的整数。
#
#
#
from typing import List
"""
方法一：哈希表
思路及解法

记原数组中出现次数最多的数为 x，那么和原数组的度相同的最短连续子数组，
必然包含了原数组中的全部 x，且两端恰为 x 第一次出现和最后一次出现的位置。

因为符合条件的 x 可能有多个，即多个不同的数在原数组中出现次数相同。所以
为了找到这个子数组，我们需要统计每一个数出现的次数，同时还需要统计每一个
数第一次出现和最后一次出现的位置。

在实际代码中，我们使用哈希表实现该功能，每一个数映射到一个长度为 3 的
数组，数组中的三个元素分别代表这个数出现的次数、这个数在原数组中第一次
出现的位置和这个数在原数组中最后一次出现的位置。当我们记录完所有信息后，
我们需要遍历该哈希表，找到元素出现次数最多，且前后位置差最小的数。
"""


# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = dict()
        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]

        maxNum = minLen = 0
        for _, item in mp.items():
            cnt, first, last = item
            if cnt > maxNum:
                maxNum = cnt
                minLen = last - first + 1
            elif cnt == maxNum:
                minLen = min(minLen, last - first + 1)

        return minLen


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findShortestSubArray([1, 2, 2, 3, 1]))
    print(solu.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
