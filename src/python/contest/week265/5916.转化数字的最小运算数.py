#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5916.转化数字的最小运算数.py
@Time    :   2021/10/31 11:03:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        seen = {start}
        que = deque([start])

        cnt = 0
        while que:
            cnt += 1
            for _ in range(len(que)):
                x = que.popleft()

                for num in nums:
                    y1 = x + num
                    y2 = x - num
                    y3 = x ^ num
                    if y1 == goal or y2 == goal or y3 == goal:
                        return cnt

                    if 0 <= y1 <= 1000 and y1 not in seen:
                        que.append(y1)
                        seen.add(y1)
                    if 0 <= y2 <= 1000 and y2 not in seen:
                        que.append(y2)
                        seen.add(y2)
                    if 0 <= y3 <= 1000 and y3 not in seen:
                        que.append(y3)
                        seen.add(y3)

        return -1


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimumOperations(nums=[1, 3], start=6, goal=4))
    print(solu.minimumOperations(nums=[2, 4, 12], start=2, goal=12))
    print(solu.minimumOperations(nums=[3, 5, 7], start=0, goal=-4))
    print(solu.minimumOperations(nums=[2, 8, 16], start=0, goal=1))
    print(solu.minimumOperations(nums=[1], start=0, goal=3))
