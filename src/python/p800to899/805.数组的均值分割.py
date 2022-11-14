#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   805.数组的均值分割.py
@Time    :   2022/11/14 19:25:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#
# https://leetcode.cn/problems/split-array-with-same-average/description/
#
# algorithms
# Hard (30.25%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    14K
# Total Submissions: 34.7K
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# 给定你一个整数数组 nums
#
# 我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) ==
# average(B) 。
#
# 如果可以完成则返回true ， 否则返回 false  。
#
# 注意：对于数组 arr ,  average(arr) 是 arr 的所有元素的和除以 arr 长度。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,2,3,4,5,6,7,8]
# 输出: true
# 解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
#
#
# 示例 2:
#
#
# 输入: nums = [3,1]
# 输出: false
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 30
# 0 <= nums[i] <= 10^4
#
#
#
from typing import List


# @lc code=start
class Solution:

    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        s = sum(nums)
        for i in range(n):
            nums[i] = nums[i] * n - s

        m = n // 2
        left = set()
        for i in range(1, 1 << m):
            tot = sum(x for j, x in enumerate(nums[:m]) if i >> j & 1)
            if tot == 0:
                return True
            left.add(tot)

        rsum = sum(nums[m:])
        for i in range(1, 1 << (n - m)):
            tot = sum(x for j, x in enumerate(nums[m:]) if i >> j & 1)
            if tot == 0 or rsum != tot and -tot in left:
                return True

        return False


# @lc code=end
