#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   钥匙和房间.py
@Time    :   2020/09/22 23:48:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = [False] * n

        def dfs(lable: int) -> None:
            visit[lable] = True
            for key in rooms[lable]:
                if not visit[key]:
                    dfs(key)

        dfs(0)
        return all(visit)


if __name__ == '__main__':
    solu = Solution()
    print(solu.canVisitAllRooms([[1], [2], [3], []]))
    print(solu.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
