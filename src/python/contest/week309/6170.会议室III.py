#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6170.会议室III.py
@Time    :   2022/09/04 11:09:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        idle, busy = list(range(n)), []
        heapq.heapify(idle)

        cnt = [0] * n
        for start, end in meetings:
            while busy and busy[0][0] <= start:
                cur, room = heapq.heappop(busy)
                heapq.heappush(idle, room)

            if idle:
                cur = start
            else:
                cur, room = heapq.heappop(busy)
                heapq.heappush(idle, room)

            room = heapq.heappop(idle)
            cnt[room] += 1
            duration = end - start
            heapq.heappush(busy, (cur + duration, room))

        ans = 0
        for i in range(1, n):
            if cnt[i] > cnt[ans]:
                ans = i

        return ans


if __name__ == '__main__':
    solu = Solution()
    n = 2
    meetings = [[0, 10], [1, 5], [2, 7], [3, 4]]
    print(solu.mostBooked(n, meetings))

    n = 3
    meetings = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
    print(solu.mostBooked(n, meetings))

    n = 2
    meetings = [[0, 10], [1, 2], [12, 14], [13, 15]]
    print(solu.mostBooked(n, meetings))
