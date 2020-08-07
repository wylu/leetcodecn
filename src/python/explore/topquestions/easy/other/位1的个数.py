#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   位1的个数.py
@Time    :   2020/08/07 12:40:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        # x&(x-1) 将x的二进制表示中的最右边的1变为0
        while n > 0:
            n &= (n - 1)
            ans += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.hammingWeight(3))
    print(solu.hammingWeight(-1))
