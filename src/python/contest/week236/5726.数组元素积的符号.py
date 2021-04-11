#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5726.数组元素积的符号.py
@Time    :   2021/04/11 10:30:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                ans *= -1
        return ans
