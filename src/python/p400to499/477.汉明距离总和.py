#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   477.汉明距离总和.py
@Time    :   2020/08/09 23:40:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#
# https://leetcode-cn.com/problems/total-hamming-distance/description/
#
# algorithms
# Medium (50.91%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 13.4K
# Testcase Example:  '[4,14,2]'
#
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
#
# 计算一个数组中，任意两个数之间汉明距离的总和。
#
# 示例:
#
#
# 输入: 4, 14, 2
#
# 输出: 6
#
# 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
# 2 + 2 = 6.
#
#
# 注意:
#
#
# 数组中元素的范围为从 0到 10^9。
# 数组的长度不超过 10^4。
#
#
#
from typing import List
"""
考虑二进制中的每一位

汉明距离等于两个数二进制表示中对应位置不同的数量。假设数组中的每个数都表示为 k 位
的二进制数（高位补 0），那么我们可以发现，要计算数组中任意两个数的汉明距离的总和，
可以先算出数组中任意两个数二进制第 i 位的汉明距离的总和，在将所有的 k 位之和相加。

也就是说，二进制中的每一位都是可以独立计算的。因此，我们考虑数组中每个数二进制的
第 i 位，假设一共有 t 个 0 和 n - t 个 1，那么显然在第 i 位的汉明距离的总和为
t * (n - t)。

由于所有的数都在 [0, 10^9] 的范围内，因此 k 最大为 31。我们只要计算出每一位上
的汉明距离的总和，再相加即可。
"""


# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        cnt = [0] * 32
        for num in nums:
            i = 0
            while num:
                cnt[i] += (num & 1)
                num >>= 1
                i += 1

        ans = 0
        for t in cnt:
            ans += t * (n - t)

        return ans


# @lc code=end
