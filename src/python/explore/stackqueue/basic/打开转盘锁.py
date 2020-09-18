#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   打开转盘锁.py
@Time    :   2020/09/18 13:39:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def bfs(cur: str) -> int:
            dist = 0
            q = deque()
            q.append(cur)
            while q:
                dist += 1
                size = len(q)
                for _ in range(size):
                    cur = list(q.popleft())
                    for i in range(4):
                        for j in (-1, 1):
                            tmp = cur[i]
                            cur[i] = str((int(tmp) + j + 10) % 10)
                            opt = ''.join(cur)
                            if opt == target:
                                return dist
                            if opt not in visit and opt not in deadends:
                                visit.add(opt)
                                q.append(opt)
                            cur[i] = tmp

            return -1

        start = '0000'
        visit = {start}
        deadends = set(deadends)

        if start in deadends:
            return -1
        if start == target:
            return 0
        return bfs(start)


if __name__ == '__main__':
    solu = Solution()
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(solu.openLock(deadends, target))

    deadends = ["8888"]
    target = "0009"
    print(solu.openLock(deadends, target))

    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    print(solu.openLock(deadends, target))

    deadends = ["0000"]
    target = "8888"
    print(solu.openLock(deadends, target))
