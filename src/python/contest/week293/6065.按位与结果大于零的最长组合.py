#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6065.按位与结果大于零的最长组合.py
@Time    :   2022/05/15 10:49:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(25):
            cnt, state = 0, 1 << i
            for num in candidates:
                if num & state:
                    cnt += 1
            ans = max(ans, cnt)
        return ans


if __name__ == '__main__':
    solu = Solution()
    candidates = [16, 17, 71, 62, 12, 24, 14]
    print(solu.largestCombination(candidates))

    candidates = [8, 8]
    print(solu.largestCombination(candidates))
