#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   FizzBuzz.py
@Time    :   2020/08/02 22:31:58
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


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
