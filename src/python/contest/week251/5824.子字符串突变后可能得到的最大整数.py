#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5824.子字符串突变后可能得到的最大整数.py
@Time    :   2021/07/25 10:35:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)

        flag = False
        for i in range(len(num)):
            digit = int(num[i])
            if change[digit] > digit:
                num[i] = str(change[digit])
                flag = True
            elif change[digit] == digit:
                continue
            elif flag:
                break

        return ''.join(num)


if __name__ == '__main__':
    solu = Solution()
    num = "021"
    change = [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]
    print(solu.maximumNumber(num, change))  # "934"

    num = "214010"
    change = [6, 7, 9, 7, 4, 0, 3, 4, 4, 7]
    print(solu.maximumNumber(num, change))  # "974676"

    num = "334111"
    change = [0, 9, 2, 3, 3, 2, 5, 5, 5, 5]
    print(solu.maximumNumber(num, change))  # "334999"
