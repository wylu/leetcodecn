#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5774.使用服务器处理任务.py
@Time    :   2021/05/30 10:48:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        busy, idle = [], [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(idle)

        i, n = 0, len(tasks)
        ans = [-1] * n
        current = 0

        while i < n:
            if i > 0 and idle:
                current += 1
            elif busy:
                current = busy[0][0]

            while busy and busy[0][0] <= current:
                heapq.heappush(idle, heapq.heappop(busy)[1])

            while idle and i < n and i <= current:
                srv = heapq.heappop(idle)
                heapq.heappush(busy, (current + tasks[i], srv))
                ans[i] = srv[1]
                i += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    servers = [3, 3, 2]
    tasks = [1, 2, 3, 2, 1, 2]
    print(solu.assignTasks(servers, tasks))

    servers = [5, 1, 4, 3, 2]
    tasks = [2, 1, 2, 4, 5, 2, 1]
    print(solu.assignTasks(servers, tasks))
