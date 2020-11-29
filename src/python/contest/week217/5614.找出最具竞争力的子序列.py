#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5614.找出最具竞争力的子序列.py
@Time    :   2020/11/29 10:32:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack, n = [], len(nums)
        for i in range(n):
            while (stack and nums[i] < stack[-1]
                   and len(stack) + (n - i - 1) >= k):
                stack.pop()
            stack.append(nums[i])
        return stack[:k]


if __name__ == "__main__":
    solu = Solution()
    print(solu.mostCompetitive([3, 5, 2, 6], 2))
    print(solu.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4))
