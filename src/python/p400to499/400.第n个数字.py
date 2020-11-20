#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   400.第n个数字.py
@Time    :   2020/11/20 22:07:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#
# https://leetcode-cn.com/problems/nth-digit/description/
#
# algorithms
# Medium (38.56%)
# Likes:    133
# Dislikes: 0
# Total Accepted:    11.9K
# Total Submissions: 30.9K
# Testcase Example:  '3'
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
#
# 注意:
# n 是正数且在32位整数范围内 ( n < 2^31)。
#
# 示例 1:
#
# 输入:
# 3
#
# 输出:
# 3
#
#
# 示例 2:
#
# 输入:
# 11
#
# 输出:
# 0
#
# 说明:
# 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
#
#
#
"""
解题思路
[1,9]：包含 9 个正整数，每个正整数包含一个数字，共 9*1 个数字
[10,99]：包含 90 个正整数，每个正整数包含两个数字，共 90*2 个数字
[100,999]：包含 900 个正整数，每个正整数包含三个数字，共 900*3 个数字

获取第 n 位所在区间。比如 n=200，通过计算可知，200-9*1-90*2=11，
即包含第 n 个数字的正整数在 100~999 这个区间，且在 100,101,102,103
中的第11位。

计算目标数。100~999 区间每个正整数由三个数字构成，由于 100 相当于
从 0 开始，计算下标为 (11-1)//3 = 3，则目标数 target = 100+3 = 103

计算答案在目标数的第几位。index = 11%3 = 2，即 103 中的第二位为 0。
由于数组中下标从 0 开始，则 index = (11-1)%3 = 1，str(target)[index]
即为所求。
"""


# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        i, cur = 1, 9
        while n > cur * i:
            n -= cur * i
            cur *= 10
            i += 1

        a, b = divmod(n - 1, i)
        return int(str(cur // 9 + a)[b])


# @lc code=end

if __name__ == "__main__":
    solu = Solution()
    print(solu.findNthDigit(10))
    print(solu.findNthDigit(3))
    print(solu.findNthDigit(11))
    print(solu.findNthDigit(0))
