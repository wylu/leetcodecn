#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6019.替换数组中的非互质数.py
@Time    :   2022/03/06 11:17:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
import math
from typing import List


class Solution:

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        while True:
            stk = []
            flag = False
            for num in nums:
                while stk:
                    res = math.gcd(stk[-1], num)
                    if res == 1:
                        break

                    flag = True
                    num = (num * stk[-1]) // res
                    stk.pop()

                stk.append(num)

            nums = stk
            if not flag:
                break

        return nums


if __name__ == '__main__':
    solu = Solution()
    nums = [6, 4, 3, 2, 7, 6, 2]
    print(solu.replaceNonCoprimes(nums))

    nums = [2, 2, 1, 1, 3, 3, 3]
    print(solu.replaceNonCoprimes(nums))
