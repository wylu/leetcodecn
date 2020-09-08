#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   42.连续子数组的最大和.py
@Time    :   2020/09/08 23:34:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, pre = -101, -101
        for num in nums:
            pre = max(pre + num, num)
            ans = max(ans, pre)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solu.maxSubArray([-1]))
