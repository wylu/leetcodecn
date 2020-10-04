#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5517.找到处理最多请求的服务器.py
@Time    :   2020/10/03 23:12:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List
from sortedcontainers import SortedSet


class Solution:
    def busiestServers(self, k: int, arrival: List[int],
                       load: List[int]) -> List[int]:
        cnts = [0] * k
        idle = SortedSet([i for i in range(k)])
        busy = []
        heapq.heapify(busy)

        n, most = len(arrival), 0
        for i in range(n):
            while busy and busy[0][0] <= arrival[i]:
                _, sr = heapq.heappop(busy)
                idle.add(sr)

            if not idle:
                continue

            idx = idle.bisect_left(i % k)
            if idx == len(idle):
                idx = 0
            sr = idle[idx]
            cnts[sr] += 1
            most = max(most, cnts[sr])
            heapq.heappush(busy, (arrival[i] + load[i], sr))
            idle.discard(sr)

        ans = []
        for i, cnt in enumerate(cnts):
            if cnt == most:
                ans.append(i)

        return ans


if __name__ == "__main__":
    solu = Solution()
    print(solu.busiestServers(3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3]))
    arrival = [1, 2, 3, 4, 8, 9, 10]
    load = [5, 2, 10, 3, 1, 2, 2]
    print(solu.busiestServers(3, arrival, load))
