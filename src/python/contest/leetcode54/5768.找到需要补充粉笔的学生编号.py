#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5768.找到需要补充粉笔的学生编号.py
@Time    :   2021/06/12 22:34:24
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import bisect
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + chalk[i]

        _, r = divmod(k, ps[n])
        return bisect.bisect_right(ps, r) % (n + 1) - 1


if __name__ == '__main__':
    solu = Solution()
    print(solu.chalkReplacer([5, 1, 5], 22))
    print(solu.chalkReplacer([3, 4, 1, 2], 25))
    print(solu.chalkReplacer([3, 4, 1, 2], 0))
    print(solu.chalkReplacer([3, 4, 1, 2], 3))
    print(solu.chalkReplacer([3, 4, 1, 2], 8))
