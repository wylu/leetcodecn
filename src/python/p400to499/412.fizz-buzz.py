#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   412.fizz-buzz.py
@Time    :   2020/08/02 22:37:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""

#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode-cn.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (64.06%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    40.3K
# Total Submissions: 62.8K
# Testcase Example:  '1'
#
# 写一个程序，输出从 1 到 n 数字的字符串表示。
#
# 1. 如果 n 是3的倍数，输出“Fizz”；
#
# 2. 如果 n 是5的倍数，输出“Buzz”；
#
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
#
# 示例：
#
# n = 15,
#
# 返回:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
#
#
#
from typing import List


# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n <= 0:
            return []

        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))

        return ans


# @lc code=end
