#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   合并区间.py
@Time    :   2020/09/26 22:42:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for interval in intervals:
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(solu.merge([[1, 4], [4, 5]]))
    print(solu.merge([[1, 2], [3, 5], [4, 6]]))
    print(solu.merge([[1, 4], [2, 3]]))
    print(solu.merge([[1, 3], [0, 2], [2, 3], [4, 6], [4, 5], [5, 5]]))
