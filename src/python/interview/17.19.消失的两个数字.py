#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   17.19.消失的两个数字.py
@Time    :   2022/09/26 21:32:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def missingTwo(self, nums: List[int]) -> List[int]:
        seen = set()
        n = len(nums)
        for i in range(n):
            while nums[i] != i + 1 and nums[i] <= n:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] > n:
                seen.add(nums[i])
                nums[i] = n + 1

        ans = []
        for i, num in enumerate(nums):
            if num == n + 1:
                ans.append(i + 1)

        if len(ans) == 2:
            return ans

        if len(ans) == 0:
            return [n + 2, n + 1]

        ans.append(n + 2 if n + 1 in seen else n + 1)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.missingTwo([1]))
    print(solu.missingTwo([2, 3]))
