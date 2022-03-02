#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   564.寻找最近的回文数.py
@Time    :   2022/03/02 19:48:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=564 lang=python3
#
# [564] 寻找最近的回文数
#
# https://leetcode-cn.com/problems/find-the-closest-palindrome/description/
#
# algorithms
# Hard (27.48%)
# Likes:    204
# Dislikes: 0
# Total Accepted:    15.9K
# Total Submissions: 57.8K
# Testcase Example:  '"123"'
#
# 给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
#
# “最近的”定义为两个整数差的绝对值最小。
#
#
#
# 示例 1:
#
#
# 输入: n = "123"
# 输出: "121"
#
#
# 示例 2:
#
#
# 输入: n = "1"
# 输出: "0"
# 解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。
#
#
#
#
# 提示:
#
#
# 1 <= n.length <= 18
# n 只由数字组成
# n 不含前导 0
# n 代表在 [1, 10^18 - 1] 范围内的整数
#
#
#
"""
方法一：模拟
思路和算法

构造回文整数有一个直观的方法：用原数的较高位的数字替换其对应的较低位。例如，
对于数 12345，我们可以用 1 替换 5，用 2 替换 4，这样原数即变为回文整数 12321。

在这种方案中，我们修改的都是较低位的数字，因此构造出的新的整数与原数较为接近。
大部分情况下，这种方案是最优解，但还有部分情况我们没有考虑到。

1.构造的回文整数大于原数时，我们可以减小该回文整数的中间部分来缩小回文整数和原数
的差距。例如，对于数 99321，我们将构造出回文整数 99399，实际上 99299 更接近原数。

当我们减小构造的回文整数时，可能导致回文整数的位数变化。例如，对于数 100，我们
将构造出回文整数 101，减小其中间部分将导致位数减少。得到的回文整数形如 999...999
（10^{len}-1）。

2.构造的回文整数小于原数时，我们可以增大该回文整数的中间部分来缩小回文整数和原数
的差距。例如，对于数 12399，我们将构造出回文整数 12321，实际上 12421 更接近原数。

当我们增大构造的回文整数时，可能导致回文整数的位数变化。例如，对于数 998，我们将
构造出回文整数 999，增大其中间部分将导致位数增加。得到的回文整数形如 100...001
（10^{len}+1）。

3.构造的回文整数等于原数时，由于题目约定，我们需要排除该回文整数，在其他的可能情况
中寻找最近的回文整数。

考虑到以上所有的可能，我们可以给出最终的方案：分别计算出以下每一种可能的方案对应的
回文整数，在其中找到与原数最近且不等于原数的数即为答案。

1.用原数的前半部分替换后半部分得到的回文整数。
2.用原数的前半部分加一后的结果替换后半部分得到的回文整数。
3.用原数的前半部分减一后的结果替换后半部分得到的回文整数。
4.为防止位数变化导致构造的回文整数错误，因此直接构造 999...999 和 100...001 作为
  备选答案。
"""


# @lc code=start
class Solution:

    def nearestPalindromic(self, n: str) -> str:
        m = len(n)
        candidates = [10**(m - 1) - 1, 10**m + 1]
        prefix = int(n[:(m + 1) // 2])
        for x in range(prefix - 1, prefix + 2):
            y = x if m % 2 == 0 else x // 10
            while y:
                x = x * 10 + y % 10
                y //= 10
            candidates.append(x)

        ans, num = -1, int(n)
        for cdd in candidates:
            if cdd == num:
                continue

            if (ans == -1 or abs(cdd - num) < abs(ans - num)
                    or abs(cdd - num) == abs(ans - num) and cdd < ans):
                ans = cdd

        return str(ans)


# @lc code=end

if __name__ == '__main__':
    solu = Solution()
    print(solu.nearestPalindromic("10001"))
    print(solu.nearestPalindromic("1001"))
