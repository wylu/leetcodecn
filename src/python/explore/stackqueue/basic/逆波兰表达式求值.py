#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   逆波兰表达式求值.py
@Time    :   2020/09/18 23:11:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import math

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t == '+':
                nums.append(nums.pop() + nums.pop())
            elif t == '-':
                b, a = nums.pop(), nums.pop()
                nums.append(a - b)
            elif t == '*':
                b, a = nums.pop(), nums.pop()
                nums.append(a * b)
            elif t == '/':
                b, a = nums.pop(), nums.pop()
                c = a / b
                nums.append(math.ceil(c) if c < 0 else math.floor(c))
            else:
                nums.append(int(t))
        return nums[0]


if __name__ == '__main__':
    solu = Solution()
    print(solu.evalRPN(["2", "1", "+", "3", "*"]))
    print(solu.evalRPN(["4", "13", "5", "/", "+"]))
    print(
        solu.evalRPN([
            "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
        ]))
