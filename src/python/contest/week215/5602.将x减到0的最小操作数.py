#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5602.将x减到0的最小操作数.py
@Time    :   2020/11/15 11:22:44
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n, tot = len(nums), 0
        pos = {0: -1}
        for i in range(n):
            tot += nums[i]
            if tot not in pos:
                pos[tot] = i

        target = tot - x
        ans, tot = -1, 0
        for i in range(n):
            tot += nums[i]
            if tot - target in pos:
                ans = max(ans, i - pos[tot - target])

        return -1 if ans == -1 else n - ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.minOperations([1, 1, 4, 2, 3], 5))
    print(solu.minOperations([5, 6, 7, 8, 9], 4))
    print(solu.minOperations([3, 2, 20, 1, 1, 3], 10))
