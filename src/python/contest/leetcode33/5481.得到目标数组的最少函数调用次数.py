#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5481.得到目标数组的最少函数调用次数.py
@Time    :   2020/08/22 22:43:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans, m = 0, 0
        for num in nums:
            n = 0
            while num:
                if num & 1:
                    num -= 1
                    ans += 1
                else:
                    num //= 2
                    n += 1
            m = max(m, n)
        return ans + m


if __name__ == '__main__':
    solu = Solution()
    print(solu.minOperations([1, 5]))
    print(solu.minOperations([2, 2]))
    print(solu.minOperations([2, 4, 5]))
    print(solu.minOperations([2, 4, 8, 16]))
    print(solu.minOperations([3, 2, 2, 4]))
    print(solu.minOperations([1000000000]))
