#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5732.减小和重新排列数组后的最大元素.py
@Time    :   2021/05/01 22:44:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self,
                                                      arr: List[int]) -> int:
        arr.sort()
        cur = 1
        i, n = 1, len(arr)
        while i < n:
            if arr[i] == cur or arr[i] == cur + 1:
                cur = arr[i]
            else:
                cur += 1
            i += 1
        return cur


if __name__ == '__main__':
    solu = Solution()
    print(solu.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]))
    print(solu.maximumElementAfterDecrementingAndRearranging([100, 1, 1000]))
    print(solu.maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]))
