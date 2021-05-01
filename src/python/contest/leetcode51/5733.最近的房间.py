#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5733.最近的房间.py
@Time    :   2021/05/01 22:58:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List
from sortedcontainers import SortedSet


class Solution:
    def closestRoom(self, rooms: List[List[int]],
                    queries: List[List[int]]) -> List[int]:
        n = len(rooms)
        rooms.sort(key=lambda x: x[1])
        ids = SortedSet(room[0] for room in rooms)
        for i, query in enumerate(queries):
            query.append(i)
        queries.sort(key=lambda x: x[1])

        def searchSize(size: int) -> int:
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if rooms[mid][1] < size:
                    left = mid + 1
                else:
                    right = mid
            return left

        ans = [-1] * len(queries)
        pre = 0
        for preferred, minSize, idx in queries:
            cur = searchSize(minSize)
            if cur == n:
                continue

            while pre < cur:
                ids.discard(rooms[pre][0])
                pre += 1

            lt = ids.bisect_left(preferred)
            if lt == len(ids):
                if lt > 0:
                    ans[idx] = ids[lt - 1]
            else:
                ans[idx] = ids[lt]
                tmp = ids[lt] - preferred
                if lt > 0 and preferred - ids[lt - 1] <= tmp:
                    ans[idx] = ids[lt - 1]

        return ans


if __name__ == '__main__':
    solu = Solution()
    rooms = [[2, 2], [1, 2], [3, 2]]
    queries = [[3, 1], [3, 3], [5, 2]]
    print(solu.closestRoom(rooms, queries))

    rooms = [[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]]
    queries = [[2, 3], [2, 4], [2, 5]]
    print(solu.closestRoom(rooms, queries))
