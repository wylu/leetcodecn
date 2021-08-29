#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5856.完成任务的最少工作时间段.py
@Time    :   2021/08/29 10:37:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from itertools import chain
from itertools import combinations
from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort()

        def powerset(nums):
            return chain.from_iterable(
                combinations(nums, n) for n in range(len(nums) + 1))

        ans = 0
        while tasks:
            ans += 1
            remain = sessionTime
            subsets = powerset(tasks)
            tot2set = {}
            for ss in subsets:
                tot = sum(ss)
                if tot not in tot2set:
                    tot2set[tot] = ss

            opt = -1
            for tot in tot2set.keys():
                if tot <= remain:
                    opt = max(opt, tot)

            if opt == -1:
                continue

            for num in tot2set[opt]:
                tasks.remove(num)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minSessions(tasks=[1, 2, 3], sessionTime=3))
    print(solu.minSessions(tasks=[3, 1, 3, 1, 1], sessionTime=8))
    print(solu.minSessions(tasks=[1, 2, 3, 4, 5], sessionTime=15))

    tasks = [2, 3, 3, 4, 4, 4, 5, 6, 7, 10]
    sessionTime = 12
    print(solu.minSessions(tasks, sessionTime))  # 4

    tasks = [1, 1, 2, 2, 2, 2, 3, 3, 6, 6, 6, 6]
    sessionTime = 10
    print(solu.minSessions(tasks, sessionTime))  # 4
