#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5851.找出不同的二进制字符串.py
@Time    :   2021/08/22 10:32:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)
        n = len(nums)
        for num in range(1 << n):
            res = bin(num)[2:]
            if n - len(res):
                res = '0' * (n - len(res)) + res

            if res not in seen:
                return res

        return ''
