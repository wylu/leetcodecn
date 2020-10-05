#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   分割数组的最大值.py
@Time    :   2020/10/06 00:38:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def ok(tot: int) -> bool:
            cur, cnt = 0, 1
            for num in nums:
                if cur + num > tot:
                    cur = 0
                    cnt += 1
                cur += num
            return cnt > m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if ok(mid):
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    solu = Solution()
    print(solu.splitArray([7, 2, 5, 10, 8], 2))
