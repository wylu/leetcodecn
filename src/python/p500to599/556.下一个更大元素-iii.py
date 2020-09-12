#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   556.下一个更大元素-iii.py
@Time    :   2020/09/12 11:04:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#
# https://leetcode-cn.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (31.42%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 20.6K
# Testcase Example:  '12'
#
# 给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
#
# 示例 1:
#
#
# 输入: 12
# 输出: 21
#
#
# 示例 2:
#
#
# 输入: 21
# 输出: -1
#
#
#


# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def reverse(s: int, e: int) -> None:
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        nums = list(str(n))
        m = len(nums)
        i = m - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1

        if i == 0:
            return -1

        i, j = i - 1, i - 1
        while i < m - 1 and nums[i + 1] > nums[j]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
        reverse(j + 1, m - 1)

        ans = int(''.join(nums))
        return -1 if ans > 0x7FFFFFFF else ans


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.nextGreaterElement(12))
    print(solu.nextGreaterElement(21))
    print(solu.nextGreaterElement(123000))
    print(solu.nextGreaterElement(100000))
    print(solu.nextGreaterElement(12543))
    print(solu.nextGreaterElement(120321))
    print(solu.nextGreaterElement(0))
    print(solu.nextGreaterElement(1999999999))
