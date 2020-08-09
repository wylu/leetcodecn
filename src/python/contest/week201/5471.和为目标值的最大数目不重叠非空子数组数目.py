#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5471.和为目标值的最大数目不重叠非空子数组数目.py
@Time    :   2020/08/09 11:10:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0}
        cur, ans = 0, 0
        for num in nums:
            cur += num
            if cur - target in seen:
                ans += 1
                seen = {0}
                cur = 0
            else:
                seen.add(cur)
        return ans


# class Solution:
#     def maxNonOverlapping(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         s = {0: 0}
#         areas = []
#         cur = 0
#         for i in range(n):
#             cur += nums[i]

#             need = cur - target
#             if need in s:
#                 areas.append((s[need], i))

#             s[cur] = i + 1

#         ans, tail = 0, -1
#         for area in areas:
#             if area[0] > tail:
#                 ans += 1
#                 tail = area[1]

#         return ans

if __name__ == '__main__':
    solu = Solution()
    print(solu.maxNonOverlapping([1, 1, 1, 1, 1], 2))
    print(solu.maxNonOverlapping([-1, 3, 5, 1, 4, 2, -9], 6))
    print(solu.maxNonOverlapping([-2, 6, 6, 3, 5, 4, 1, 2, 8], 10))
    print(solu.maxNonOverlapping([0, 0, 0], 0))
    print(solu.maxNonOverlapping([-5, 5, -4, 5, 4], 5))
