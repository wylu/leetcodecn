#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   杨辉三角.py
@Time    :   2020/08/07 22:25:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        ans, i = [[1]], 1
        while i < numRows:
            row = [1]
            for j in range(1, i):
                row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            row.append(1)

            ans.append(row)
            i += 1

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.generate(5))
