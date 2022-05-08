#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6056.字符串中最大的3位相同数字.py
@Time    :   2022/05/08 10:30:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def largestGoodInteger(self, num: str) -> str:
        for digit in range(9, -1, -1):
            option = str(digit) * 3
            if num.find(option) != -1:
                return option
        return ""
