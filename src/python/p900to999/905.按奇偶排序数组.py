#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   905.按奇偶排序数组.py
@Time    :   2020/11/12 11:08:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#
# https://leetcode-cn.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (69.44%)
# Likes:    176
# Dislikes: 0
# Total Accepted:    44.5K
# Total Submissions: 64.1K
# Testcase Example:  '[3,1,2,4]'
#
# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
#
# 你可以返回满足此条件的任何数组作为答案。
#
#
#
# 示例：
#
# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
#
#
#
from typing import List


# @lc code=start
class Solution:
    def sortArrayByParity(self, a: List[int]) -> List[int]:
        i, j = 0, len(a) - 1
        while i < j:
            while i < j and a[i] % 2 == 0:
                i += 1
            while i < j and a[j] % 2 == 1:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
        return a


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.sortArrayByParity([3, 1, 2, 4]))
    print(solu.sortArrayByParity([1, 2]))
