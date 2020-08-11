#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   08.06.汉诺塔问题.py
@Time    :   2020/08/11 23:42:21
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :   https://leetcode-cn.com/problems/hanota-lcci/
"""
from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        return self.move(len(A), A, B, C)

    def move(self, n: int, A: List[int], B: List[int], C: List[int]) -> None:
        if n == 1:
            C.append(A.pop())
        else:
            self.move(n - 1, A, C, B)
            C.append(A.pop())
            self.move(n - 1, B, A, C)
