#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6150.根据模式串构造最小数字.py
@Time    :   2022/08/14 10:44:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:

    def smallestNumber(self, pattern: str) -> str:
        ans, n = [], len(pattern)
        seen = [False] * 10

        def dfs(i: int) -> bool:
            if i == n:
                return True

            if pattern[i] == 'I':
                obj = range(ans[-1] + 1, 10)
            else:
                obj = range(1, ans[-1])

            for num in obj:
                if not seen[num]:
                    ans.append(num)
                    seen[num] = True
                    if dfs(i + 1):
                        return True
                    seen[num] = False
                    ans.pop()

            return False

        for num in range(1, 10):
            ans.append(num)
            seen[num] = True
            if dfs(0):
                return ''.join(map(str, ans))
            seen[num] = False
            ans.pop()

        return ''


if __name__ == '__main__':
    solu = Solution()
    print(solu.smallestNumber(pattern="IIIDIDDD"))
    print(solu.smallestNumber(pattern="DDD"))
