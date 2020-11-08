#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5561.获取生成数组中的最大值.py
@Time    :   2020/11/08 10:30:27
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 0:
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(1, n // 2 + 1):
            nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        return max(nums)


if __name__ == "__main__":
    solu = Solution()
    print(solu.getMaximumGenerated(7))
    print(solu.getMaximumGenerated(2))
    print(solu.getMaximumGenerated(3))
    print(solu.getMaximumGenerated(0))
    print(solu.getMaximumGenerated(1))
