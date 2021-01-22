#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   989.数组形式的整数加法.py
@Time    :   2020/08/04 18:02:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#
# https://leetcode-cn.com/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (44.16%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    14.7K
# Total Submissions: 33.2K
# Testcase Example:  '[1,2,0,0]\n34'
#
# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
#
# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
#
#
#
#
#
#
# 示例 1：
#
# 输入：A = [1,2,0,0], K = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234
#
#
# 示例 2：
#
# 输入：A = [2,7,4], K = 181
# 输出：[4,5,5]
# 解释：274 + 181 = 455
#
#
# 示例 3：
#
# 输入：A = [2,1,5], K = 806
# 输出：[1,0,2,1]
# 解释：215 + 806 = 1021
#
#
# 示例 4：
#
# 输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
# 输出：[1,0,0,0,0,0,0,0,0,0,0]
# 解释：9999999999 + 1 = 10000000000
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# 如果 A.length > 1，那么 A[0] != 0
#
#
#
from typing import List


# @lc code=start
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        i, carry = len(A) - 1, K
        ans = []
        while i >= 0 or carry:
            if i >= 0:
                carry += A[i]
                i -= 1
            ans.append(carry % 10)
            carry //= 10
        ans.reverse()
        return ans


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.addToArrayForm(A=[1, 2, 0, 0], K=34))
    print(solu.addToArrayForm(A=[2, 7, 4], K=181))
    print(solu.addToArrayForm(A=[2, 1, 5], K=806))
    print(solu.addToArrayForm(A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1))
