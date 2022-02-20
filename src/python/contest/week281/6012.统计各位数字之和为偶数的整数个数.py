#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6012.统计各位数字之和为偶数的整数个数.py
@Time    :   2022/02/20 10:30:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def countEven(self, num: int) -> int:
        ans = 0
        for a in range(1, num + 1):
            if sum(map(int, str(a))) % 2 == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.countEven(4))
    print(solu.countEven(30))
