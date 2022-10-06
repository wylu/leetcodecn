#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   927.三等分.py
@Time    :   2022/10/06 19:53:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
#
# @lc app=leetcode.cn id=927 lang=python3
#
# [927] 三等分
#
# https://leetcode.cn/problems/three-equal-parts/description/
#
# algorithms
# Hard (35.24%)
# Likes:    165
# Dislikes: 0
# Total Accepted:    16.4K
# Total Submissions: 39.3K
# Testcase Example:  '[1,0,1,0,1]'
#
# 给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。
#
# 如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
#
#
# arr[0], arr[1], ..., arr[i] 为第一部分；
# arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
# arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
# 这三个部分所表示的二进制值相等。
#
#
# 如果无法做到，就返回 [-1, -1]。
#
# 注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以
# [0,1,1] 和 [1,1] 表示相同的值。
#
#
#
# 示例 1：
#
#
# 输入：arr = [1,0,1,0,1]
# 输出：[0,3]
#
#
# 示例 2：
#
#
# 输入：arr = [1,1,0,1,1]
# 输出：[-1,-1]
#
# 示例 3:
#
#
# 输入：arr = [1,1,0,0,1]
# 输出：[0,2]
#
#
#
#
# 提示：
#
#
#
# 3 <= arr.length <= 3 * 10^4
# arr[i] 是 0 或 1
#
#
#
from typing import List


# @lc code=start
class Solution:

    def threeEqualParts(self, arr: List[int]) -> List[int]:
        cnt = sum(arr)
        if cnt % 3 != 0:
            return [-1, -1]
        if cnt == 0:
            return [0, 2]

        ones = [i for i, num in enumerate(arr) if num]
        c0 = len(arr) - ones[-1] - 1
        c1 = cnt // 3

        a0 = ones[c1] - ones[c1 - 1] - 1
        if a0 < c0:
            return [-1, -1]

        b0 = ones[c1 * 2] - ones[c1 * 2 - 1] - 1
        if b0 < c0:
            return [-1, -1]

        s1 = arr[ones[0]:ones[c1 - 1] + 1]
        s2 = arr[ones[c1]:ones[c1 * 2 - 1] + 1]
        s3 = arr[ones[c1 * 2]:ones[-1] + 1]

        if s1 == s2 and s2 == s3:
            return [ones[c1 - 1] + c0, ones[c1 * 2 - 1] + c0 + 1]

        return [-1, -1]


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    arr = [1, 0, 1, 0, 1]
    print(solu.threeEqualParts(arr))

    arr = [1, 1, 0, 1, 1]
    print(solu.threeEqualParts(arr))

    arr = [1, 1, 0, 0, 1]
    print(solu.threeEqualParts(arr))
