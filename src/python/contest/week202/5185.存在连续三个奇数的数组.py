#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5185.存在连续三个奇数的数组.py
@Time    :   2020/08/16 10:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if not arr or len(arr) < 3:
            return False

        i = 0
        while i <= len(arr) - 3:
            if arr[i] % 2 == 0:
                i += 1
                continue
            if arr[i + 1] % 2 == 0:
                i += 2
                continue
            if arr[i + 2] % 2 == 0:
                i += 3
            else:
                return True

        return False


if __name__ == '__main__':
    solu = Solution()
    print(solu.threeConsecutiveOdds([1, 1, 1]))
