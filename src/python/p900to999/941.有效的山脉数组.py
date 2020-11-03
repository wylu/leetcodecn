#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   941.有效的山脉数组.py
@Time    :   2020/11/03 13:49:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#
# https://leetcode-cn.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (36.19%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 83.8K
# Testcase Example:  '[2,1]'
#
# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
#
# 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
#
#
# A.length >= 3
# 在 0 < i < A.length - 1 条件下，存在 i 使得：
#
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
#
#
# 示例 1：
#
# 输入：[2,1]
# 输出：false
#
#
# 示例 2：
#
# 输入：[3,5,5]
# 输出：false
#
#
# 示例 3：
#
# 输入：[0,3,2,1]
# 输出：true
#
#
# 提示：
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
#
from typing import List


# @lc code=start
class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        n = len(a)
        if n < 3:
            return False

        i = 1
        while i < n and a[i] > a[i - 1]:
            i += 1

        if i == 1 or i == n:
            return False

        while i < n and a[i] < a[i - 1]:
            i += 1

        return i == n


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.validMountainArray([0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 11]))
    print(solu.validMountainArray([0, 1]))
    print(solu.validMountainArray([0, 1, 2]))
    print(solu.validMountainArray([2, 1, 0]))
