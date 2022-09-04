#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6169.最长优雅子数组.py
@Time    :   2022/09/04 10:52:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans, cnt = 1, [0] * 32

        def check() -> bool:
            return all(c <= 1 for c in cnt)

        i, j, n = 0, 0, len(nums)
        while j < n:
            num = nums[j]
            for k in range(32):
                if (1 << k) & num:
                    cnt[k] += 1

            while i < j and not check():
                num = nums[i]
                for k in range(32):
                    if (1 << k) & num:
                        cnt[k] -= 1
                i += 1

            j += 1
            ans = max(ans, j - i)

        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [1, 3, 8, 48, 10]
    print(solu.longestNiceSubarray(nums))

    nums = [3, 1, 5, 11, 13]
    print(solu.longestNiceSubarray(nums))
