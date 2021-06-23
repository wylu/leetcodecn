#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   16.16.部分排序.py
@Time    :   2021/06/23 14:46:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        size = len(array)
        max_left, min_right = float('-inf'), float('inf')
        L, R = -1, -1
        for i in range(size):
            # 右边界
            if max_left > array[i]:
                R = i
            else:
                max_left = max(max_left, array[i])

            # 左边界
            j = size - i - 1
            if min_right < array[j]:
                L = j
            else:
                min_right = min(min_right, array[j])
        return [L, R]
