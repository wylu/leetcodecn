#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6160.和有限的最长子序列.py
@Time    :   2022/08/28 10:33:18
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for query in queries:
            cur, j = 0, -1
            for i, num in enumerate(nums):
                if cur + num > query:
                    break
                cur += num
                j = i
            ans.append(j + 1)
        return ans


if __name__ == '__main__':
    solu = Solution()
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    print(solu.answerQueries(nums, queries))

    nums = [2, 3, 4, 5]
    queries = [1]
    print(solu.answerQueries(nums, queries))
