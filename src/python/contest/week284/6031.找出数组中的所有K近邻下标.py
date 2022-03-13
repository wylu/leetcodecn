#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6031.找出数组中的所有K近邻下标.py
@Time    :   2022/03/13 10:30:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def findKDistantIndices(self, nums: List[int], key: int,
                            k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            for j in range(max(i - k, 0), min(i + k + 1, n)):
                if nums[j] == key:
                    ans.append(i)
                    break

        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [3, 4, 9, 1, 3, 9, 5]
    key = 9
    k = 1
    print(solu.findKDistantIndices(nums, key, k))
