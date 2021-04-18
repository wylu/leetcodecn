#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5736.单线程CPU.py
@Time    :   2021/04/18 10:34:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        que = []
        for i, task in enumerate(tasks):
            que.append((task[0], task[1], i))
        que.sort(reverse=True)

        ans = []

        cur_time, cost, tno = que.pop()
        pq = [(cost, tno)]
        while pq:
            cost, tno = heapq.heappop(pq)
            cur_time += cost

            ans.append(tno)

            if not pq and que and que[-1][0] > cur_time:
                cur_time = que[-1][0]

            while que and que[-1][0] <= cur_time:
                _, cost, tno = que.pop()
                heapq.heappush(pq, (cost, tno))

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.getOrder(tasks=[[1, 2], [1, 2], [6, 1]]))
    print(solu.getOrder(tasks=[[1, 2], [1, 2], [3, 1], [6, 1]]))

    print(solu.getOrder(tasks=[[1, 1], [1, 1], [1, 1]]))
    print(solu.getOrder(tasks=[[1, 5], [2, 5], [3, 5]]))

    print(solu.getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1]]))
    print(solu.getOrder(tasks=[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]))

    # [14,5,12,3,0,13,10,11,9,6,4,15,8,1,17,2,7,16]
    print(
        solu.getOrder(
            tasks=[[46, 9], [46, 42], [30, 46], [30, 13], [30, 24], [30, 5],
                   [30, 21], [29, 46], [29, 41], [29, 18], [29, 16], [29, 17],
                   [29, 5], [22, 15], [22, 13], [22, 25], [22, 49], [22, 44]]))

    # [15,14,13,1,6,3,5,12,8,11,9,4,10,7,0,2]
    print(
        solu.getOrder(
            tasks=[[35, 36], [11, 7], [15, 47], [34, 2], [47, 19], [16, 14],
                   [19, 8], [7, 34], [38, 15], [16, 18], [27, 22], [7, 15],
                   [43, 2], [10, 5], [5, 4], [3, 11]]))
