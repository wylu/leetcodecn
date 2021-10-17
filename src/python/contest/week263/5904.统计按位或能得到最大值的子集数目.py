#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5904.统计按位或能得到最大值的子集数目.py
@Time    :   2021/10/17 10:41:42
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        max_val, n = 0, len(nums)

        def dfs(i: int, cur: int) -> None:
            nonlocal max_val
            if i == n:
                counter[cur] += 1
                max_val = max(max_val, cur)
                return

            dfs(i + 1, cur)
            dfs(i + 1, cur | nums[i])

        dfs(0, 0)
        return counter[max_val]


if __name__ == '__main__':
    solu = Solution()
    print(solu.countMaxOrSubsets(nums=[3, 1]))
    print(solu.countMaxOrSubsets(nums=[2, 2, 2]))
    print(solu.countMaxOrSubsets(nums=[3, 2, 1, 5]))
