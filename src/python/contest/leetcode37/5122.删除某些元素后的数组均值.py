#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5122.删除某些元素后的数组均值.py
@Time    :   2020/10/17 22:30:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        m = n // 20
        return sum(arr[m:-m]) / (n - 2 * m)


if __name__ == "__main__":
    solu = Solution()
    arr = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]
    print(solu.trimMean(arr))
