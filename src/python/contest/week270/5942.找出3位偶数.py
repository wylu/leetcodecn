#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5942.找出3位偶数.py
@Time    :   2021/12/05 10:30:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        for i, num1 in enumerate(digits):
            if num1 == 0:
                continue

            for j, num2 in enumerate(digits):
                if j == i:
                    continue

                for k, num3 in enumerate(digits):
                    if k == i or k == j:
                        continue

                    num = num1 * 100 + num2 * 10 + num3
                    if num % 2 == 0:
                        ans.add(num)

        ans = list(ans)
        ans.sort()
        return ans
