#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5629.重新格式化电话号码.py
@Time    :   2020/12/20 10:30:23
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '')
        number = number.replace(' ', '')
        ans, n = [], len(number)

        def sep(s: str) -> None:
            for i in range(0, len(s), 3):
                ans.append(s[i:i + 3])

        if n % 3 == 0:
            sep(number)
        elif n % 3 == 1:
            sep(number[:-4])
            ans.append(number[-4:-2])
            ans.append(number[-2:])
        else:
            sep(number[:-2])
            ans.append(number[-2:])

        return '-'.join(ans)


if __name__ == "__main__":
    solu = Solution()
    print(solu.reformatNumber("1-23-45 6"))
    print(solu.reformatNumber("123 4-567"))
