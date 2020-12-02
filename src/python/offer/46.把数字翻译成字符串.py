#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   46.把数字翻译成字符串.py
@Time    :   2020/12/02 22:14:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
总翻译结果数 = 除去最后1位的部分的翻译结果数 * 1
             + 除去最后2位的部分的翻译结果数 * 1

定义状态：dp[i] 表示 nums[0...i] 能翻译成字符串的种类数
状态转移方程：dp[i] = dp[i-1] + dp[i-2]
初始状态：dp[0] = 1

空间优化：当前状态只与前两个状态相关，因此可以使用滚动变量进行优化
"""


class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        d0, d1, n = 1, 1, len(num)
        for i in range(1, n):
            tmp = d1
            if 9 < int(num[i - 1:i + 1]) < 26:
                d1 += d0
            d0 = tmp
        return d1


if __name__ == "__main__":
    solu = Solution()
    print(solu.translateNum(12258))
    print(solu.translateNum(123))
