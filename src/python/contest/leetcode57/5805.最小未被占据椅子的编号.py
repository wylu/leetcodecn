#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5805.最小未被占据椅子的编号.py
@Time    :   2021/07/24 22:34:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i, time_ in enumerate(times):
            time_.append(i)

        times.sort()
        seats = list(range(len(times)))
        heapq.heapify(seats)
        pq = []
        for a, l, i in times:
            while pq and pq[0][0] <= a:
                heapq.heappush(seats, pq[0][1])
                heapq.heappop(pq)

            if i == targetFriend:
                return heapq.heappop(seats)

            heapq.heappush(pq, (l, heapq.heappop(seats)))

        return -1


if __name__ == '__main__':
    solu = Solution()
    print(solu.smallestChair(times=[[1, 4], [2, 3], [4, 6]], targetFriend=1))
    print(solu.smallestChair(times=[[3, 10], [1, 5], [2, 6]], targetFriend=0))

    times = [[33889, 98676], [80071, 89737], [44118, 52565], [52992, 84310],
             [78492, 88209], [21695, 67063], [84622, 95452], [98048, 98856],
             [98411, 99433], [55333, 56548], [65375, 88566], [55011, 62821],
             [48548, 48656], [87396, 94825], [55273, 81868], [75629, 91467]]
    targetFriend = 6
    print(solu.smallestChair(times, targetFriend))
