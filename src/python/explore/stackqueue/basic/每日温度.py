#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   每日温度.py
@Time    :   2020/09/18 22:48:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def dailyTemperatures(self, ts: List[int]) -> List[int]:
        ans, stack = [0] * len(ts), []
        for i, t in enumerate(ts):
            while stack and t > ts[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
