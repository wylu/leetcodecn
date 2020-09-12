#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   2.早餐组合.py
@Time    :   2020/09/12 15:03:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int],
                        x: int) -> int:
        def binary_search(t: int) -> int:
            s, e = 0, len(drinks) - 1
            while s < e:
                m = (s + e + 1) // 2
                if drinks[m] <= t:
                    s = m
                else:
                    e = m - 1
            return s

        drinks.sort()
        ans = 0
        for s in staple:
            if x - s < drinks[0]:
                continue
            ans += binary_search(x - s) + 1

        return ans % 1000000007


if __name__ == '__main__':
    solu = Solution()
    print(solu.breakfastNumber([10, 20, 5], [5, 5, 2], 15))
    print(solu.breakfastNumber([2, 1, 1], [8, 9, 5, 1], 9))
