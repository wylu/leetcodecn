#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5823.字符串转化后的各位数字之和.py
@Time    :   2021/07/25 10:30:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = []
        for ch in s:
            nums.append(str(ord(ch) - ord('a') + 1))

        tot = ''.join(nums)
        while k:
            tot = str(sum(map(int, list(tot))))
            k -= 1

        return int(tot)
