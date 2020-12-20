#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5630.删除子数组的最大得分.py
@Time    :   2020/12/20 10:51:33
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        ans, tot = 0, 0
        seen = set()

        while left < n:
            while right < n and nums[right] not in seen:
                seen.add(nums[right])
                tot += nums[right]
                right += 1

            ans = max(ans, tot)
            seen.remove(nums[left])
            tot -= nums[left]
            left += 1

        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.maximumUniqueSubarray([4, 2, 4, 5, 6]))
    print(solu.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]))
