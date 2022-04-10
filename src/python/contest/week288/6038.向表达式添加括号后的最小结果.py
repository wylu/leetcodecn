#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6038.向表达式添加括号后的最小结果.py
@Time    :   2022/04/10 10:36:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split('+')
        n1, n2 = len(num1), len(num2)
        ans, val = '', 0x7FFFFFFF
        for i in range(n1):
            cur_before = 1 if i == 0 else int(num1[:i])
            before = '' if i == 0 else num1[:i]
            a = int(num1[i:])

            for j in range(n2):
                b = int(num2[:j + 1])
                after = '' if j == n2 - 1 else num2[j + 1:]
                cur_after = 1 if j == n2 - 1 else int(num2[j + 1:])

                cur = cur_before * (a + b) * cur_after
                if cur < val:
                    ans = f'{before}({a}+{b}){after}'
                    val = cur

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.minimizeResult(expression="247+38"))
    print(solu.minimizeResult(expression="12+34"))
    print(solu.minimizeResult(expression="999+999"))
