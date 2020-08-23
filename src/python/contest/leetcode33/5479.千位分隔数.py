#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5479.千位分隔数.py
@Time    :   2020/08/22 22:30:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        i = len(s)
        ans = []
        while i - 3 >= 0:
            ans.append(s[i - 3:i])
            i -= 3

        if i > 0:
            ans.append(s[0:i])

        ans.reverse()
        return '.'.join(ans)


if __name__ == '__main__':
    solu = Solution()
    print(solu.thousandSeparator(1234))
    print(solu.thousandSeparator(123456789))
    print(solu.thousandSeparator(12345678))
    print(solu.thousandSeparator(0))
    print(solu.thousandSeparator(123))
