#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5928.解码斜向换位密码.py
@Time    :   2021/11/14 11:24:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        matrix = [[' '] * cols for _ in range(rows)]
        for i, ch in enumerate(encodedText):
            r, c = divmod(i, cols)
            matrix[r][c] = ch

        print(matrix)

        ans = []
        for i in range(cols):
            for j in range(rows):
                if i + j >= cols:
                    break
                ans.append(matrix[j][i + j])

        return ''.join(ans).rstrip()


if __name__ == '__main__':
    solu = Solution()
    print(solu.decodeCiphertext(encodedText="ch   ie   pr", rows=3))
