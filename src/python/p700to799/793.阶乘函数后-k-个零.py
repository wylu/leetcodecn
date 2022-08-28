#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   793.阶乘函数后-k-个零.py
@Time    :   2022/08/28 17:49:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#
# https://leetcode.cn/problems/preimage-size-of-factorial-zeroes-function/description/
#
# algorithms
# Hard (46.57%)
# Likes:    158
# Dislikes: 0
# Total Accepted:    18.4K
# Total Submissions: 39.5K
# Testcase Example:  '0'
#
#  f(x) 是 x! 末尾是 0 的数量。回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 。
#
#
# 例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。
#
#
# 给定 k，找出返回能满足 f(x) = k 的非负整数 x 的数量。
#
#
#
# 示例 1：
#
#
# 输入：k = 0
# 输出：5
# 解释：0!, 1!, 2!, 3!, 和 4! 均符合 k = 0 的条件。
#
#
# 示例 2：
#
#
# 输入：k = 5
# 输出：0
# 解释：没有匹配到这样的 x!，符合 k = 5 的条件。
#
# 示例 3:
#
#
# 输入: k = 3
# 输出: 5
#
#
#
#
# 提示:
#
#
# 0 <= k <= 10^9
#
#
#

# @lc code=start
from functools import lru_cache


class Solution:

    def preimageSizeFZF(self, k: int) -> int:

        @lru_cache(None)
        def count(x: int) -> int:
            res = 0
            while x:
                x //= 5
                res += x
            return res

        i, right = 0, 0x7FFFFFFFFF
        while i < right:
            x = (i + right + 1) // 2
            if count(x) <= k:
                i = x
            else:
                right = x - 1

        left, j = 0, 0x7FFFFFFFFF
        while left < j:
            x = (left + j) // 2
            if count(x) < k:
                left = x + 1
            else:
                j = x

        return max(0, right - left + 1)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.preimageSizeFZF(0))
    print(solu.preimageSizeFZF(5))
    print(solu.preimageSizeFZF(3))
    print(solu.preimageSizeFZF(1000000000))
