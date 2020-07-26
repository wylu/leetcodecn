#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   加一.py
@Time    :   2020/07/26 10:10:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry += digits[i]
            digits[i] = carry % 10
            carry //= 10

        if carry > 0:
            digits.insert(0, carry)

        return digits
