#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6004.得到0的操作数.py
@Time    :   2022/02/13 10:30:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0

        if num1 >= num2:
            return 1 + self.countOperations(num1 - num2, num2)

        return 1 + self.countOperations(num1, num2 - num1)
