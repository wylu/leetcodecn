#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5752.子数组最小乘积的最大值.py
@Time    :   2021/05/09 11:10:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]

        lts, rts = [0] * n, [0] * n
        stk = [0]
        for i in range(1, n):
            while stk and nums[i] <= nums[stk[-1]]:
                stk.pop()
            if stk:
                lts[i] = stk[-1] + 1
            else:
                lts[i] = 0
            stk.append(i)

        rts[n - 1] = n - 1
        stk = [n - 1]
        for i in range(n - 2, -1, -1):
            while stk and nums[i] <= nums[stk[-1]]:
                stk.pop()
            if stk:
                rts[i] = stk[-1] - 1
            else:
                rts[i] = n - 1
            stk.append(i)

        # print(lts)
        # print(rts)

        ans = 0
        for i in range(n):
            ans = max(ans, nums[i] * (ps[rts[i] + 1] - ps[lts[i]]))
        return ans % (10**9 + 7)


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxSumMinProduct(nums=[1, 2, 3, 2]))
    print(solu.maxSumMinProduct(nums=[2, 3, 3, 1, 2]))
    print(solu.maxSumMinProduct(nums=[3, 1, 5, 6, 4, 2]))
