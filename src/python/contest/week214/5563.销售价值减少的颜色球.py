#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5563.销售价值减少的颜色球.py
@Time    :   2020/11/08 11:02:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort()
        n = len(inventory)
        ans, i = 0, n - 2

        def calValue(start: int, end: int) -> int:
            return (start + end) * (end - start + 1) // 2

        while i >= -1 and orders > 0:
            while i >= 0 and inventory[i] == inventory[i + 1]:
                i -= 1

            base = 0 if i < 0 else inventory[i]
            cnt = (inventory[i + 1] - base) * (n - 1 - i)
            if cnt <= orders:
                ans += (n - 1 - i) * calValue(base + 1, inventory[i + 1])
                orders -= cnt
            else:
                line = (n - 1 - i)
                if line <= orders:
                    cnt = orders // line
                    ans += line * calValue(inventory[i + 1] - cnt + 1,
                                           inventory[i + 1])
                    orders -= cnt * line
                    inventory[i + 1] -= cnt

                ans += orders * inventory[i + 1]
                orders = 0

            i -= 1

        return ans % (10**9 + 7)


if __name__ == "__main__":
    solu = Solution()
    print(solu.maxProfit([2, 5], 4))
    print(solu.maxProfit([3, 5], 6))
    print(solu.maxProfit([2, 8, 4, 10, 6], 20))
    print(solu.maxProfit([1000000000], 1000000000))
