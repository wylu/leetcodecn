#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6151.统计特殊整数.py
@Time    :   2022/08/14 11:10:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from functools import cache


class Solution:

    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        # 返回从 i 开始填数字，i 前面填的数字的集合是 mask，能构造出的特殊整数的数目
        # is_limit 表示前面填的数字是否都是 n 对应位上的，如果为 true，那么当前位至多为
        #     int(s[i])，否则至多为 9
        # is_num 表示前面是否填了数字（是否跳过），如果为 true，那么当前位可以从 0 开始，
        #     如果为 false，那么我们可以跳过，或者从 1 开始填数字
        @cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)

            res = 0
            if not is_num:
                # 选择跳过，不填数字
                res += f(i + 1, mask, False, False)

            up = int(s[i]) if is_limit else 9
            for d in range(1 - int(is_num), up + 1):
                if (mask >> d) & 1 == 0:
                    res += f(i + 1, mask | (1 << d), is_limit and d == up,
                             True)

            return res

        return f(0, 0, True, False)


if __name__ == '__main__':
    solu = Solution()
    print(solu.countSpecialNumbers(n=20))
    print(solu.countSpecialNumbers(n=5))
    print(solu.countSpecialNumbers(n=135))
