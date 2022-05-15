#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6064.不含特殊楼层的最大连续楼层数.py
@Time    :   2022/05/15 10:37:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special = [num for num in special if bottom <= num <= top]
        special.sort()
        if bottom != special[0]:
            special.insert(0, bottom - 1)
        if top != special[-1]:
            special.append(top + 1)

        ans = 0
        # print(special)
        for i in range(1, len(special)):
            # print((special[i - 1] + 1), (special[i] - 1))
            ans = max(ans, (special[i] - 1) - (special[i - 1] + 1) + 1)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxConsecutive(bottom=2, top=9, special=[4, 6]))
    print(solu.maxConsecutive(bottom=6, top=8, special=[7, 6, 8]))
