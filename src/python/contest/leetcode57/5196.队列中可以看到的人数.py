#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5196.队列中可以看到的人数.py
@Time    :   2021/07/24 23:17:43
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import bisect
from collections import deque
from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n

        que = deque([heights[n - 1]])
        for i in range(n - 2, -1, -1):
            j = bisect.bisect_left(que, heights[i])
            ans[i] = j + 1 if j < len(que) else j
            while que and heights[i] >= que[0]:
                que.popleft()
            que.appendleft(heights[i])

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.canSeePersonsCount(heights=[10, 6, 8, 5, 11, 9]))
    print(solu.canSeePersonsCount(heights=[5, 1, 2, 3, 10]))
    print(solu.canSeePersonsCount(heights=[5, 1, 2, 3]))
