#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   字符串解码.py
@Time    :   2020/09/19 21:51:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def decodeString(self, s: str) -> str:
        num, cnts, vals = 0, [], [[]]
        for ch in s:
            if '0' <= ch <= '9':
                num = num * 10 + ord(ch) - ord('0')
            elif ch == '[':
                vals.append([])
                cnts.append(num)
                num = 0
            elif ch == ']':
                tmp = ''.join(vals.pop()) * cnts.pop()
                vals[-1].append(tmp)
            else:
                vals[-1].append(ch)

        return ''.join(vals[-1])


if __name__ == '__main__':
    solu = Solution()
    print(solu.decodeString("3[a]2[bc]"))
    print(solu.decodeString("3[a2[c]]"))
    print(solu.decodeString("2[abc]3[cd]ef"))
    print(solu.decodeString("abc3[cd]xyz"))
