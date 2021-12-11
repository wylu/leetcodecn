#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5935.适合打劫银行的日子.py
@Time    :   2021/12/11 22:34:15
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        lefts = [0] * n
        rights = [0] * n

        stk = [security[0]]
        for i in range(1, n):
            lefts[i] = len(stk)
            if stk and security[i] > stk[-1]:
                stk = []
            stk.append(security[i])

        stk = [security[-1]]
        for i in range(n - 2, -1, -1):
            rights[i] = len(stk)
            if stk and security[i] > stk[-1]:
                stk = []
            stk.append(security[i])

        ans = []
        for i in range(n):
            if lefts[i] >= time and rights[i] >= time:
                if time == 0:
                    ans.append(i)

                elif (0 < i < n - 1
                      and security[i - 1] >= security[i] <= security[i + 1]):
                    ans.append(i)

        return ans


if __name__ == '__main__':
    solu = Solution()
    security = [5, 3, 3, 3, 5, 6, 2]
    time = 2
    print(solu.goodDaysToRobBank(security, time))

    security = [1, 2, 3, 4]
    time = 1
    print(solu.goodDaysToRobBank(security, time))
