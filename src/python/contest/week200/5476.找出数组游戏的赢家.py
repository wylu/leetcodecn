#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5476.找出数组游戏的赢家.py
@Time    :   2020/08/02 10:44:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import deque
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)

        que = deque(arr)
        cur, cnt = que.popleft(), 0
        while que:
            num = que.popleft()
            if cur > num:
                cnt += 1
                que.append(num)
            else:
                cnt = 1
                que.append(cur)
                cur = num

            if cnt == k:
                return cur

        return -1


if __name__ == '__main__':
    solu = Solution()
    print(solu.getWinner([2, 1, 3, 5, 4, 6, 7], 2))
    print(solu.getWinner([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000))
