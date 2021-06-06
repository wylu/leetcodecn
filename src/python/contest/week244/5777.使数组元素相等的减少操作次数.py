#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5777.使数组元素相等的减少操作次数.py
@Time    :   2021/06/06 10:38:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        ans, n = 0, len(nums)

        i = 0
        while i < n - 1:
            if nums[i] == nums[-1]:
                break

            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1

            i += 1
            ans += i

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.reductionOperations(nums=[5, 1, 3]))
    print(solu.reductionOperations(nums=[1, 1, 1]))
    print(solu.reductionOperations(nums=[1, 1, 2, 2, 3]))
    print(solu.reductionOperations(nums=[1]))
