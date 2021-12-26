#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5965.相同元素的间隔之和.py
@Time    :   2021/12/26 11:20:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i, num in enumerate(arr):
            pos[num].append(i)

        num2sums = defaultdict(deque)
        for num, positions in pos.items():
            n = len(positions)
            cur = sum(idx - positions[0] for idx in positions)
            num2sums[num].append(cur)
            for i in range(1, n):
                gap = positions[i] - positions[i - 1]
                cur += i * gap - (n - i) * gap
                num2sums[num].append(cur)

        ans = []
        for num in arr:
            ans.append(num2sums[num].popleft())

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.getDistances(arr=[2, 1, 3, 1, 2, 3, 3]))
    print(solu.getDistances(arr=[10, 5, 10, 10]))
