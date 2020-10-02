#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   长度最小的子数组.py
@Time    :   2020/10/02 17:12:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        i, j = 0, 0
        n, tot = len(nums), 0
        ans = n + 1
        while j < n:
            tot += nums[j]
            while tot >= s:
                ans = min(ans, j - i + 1)
                tot -= nums[i]
                i += 1
            j += 1

        return 0 if ans == n + 1 else ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
