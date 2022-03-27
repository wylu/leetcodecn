#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5236.美化数组的最少删除数.py
@Time    :   2022/03/27 10:32:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:

    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        stk = []
        for num in nums:
            if stk and (len(stk) - 1) % 2 == 0 and stk[-1] == num:
                ans += 1
                continue
            stk.append(num)

        if len(stk) % 2:
            ans += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minDeletion(nums=[1, 1, 2, 2, 3, 3]))
