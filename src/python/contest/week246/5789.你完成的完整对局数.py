#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   5789.你完成的完整对局数.py
@Time    :   2021/06/20 10:33:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        ans = 0
        sh, sm = map(int, startTime.split(':'))
        eh, em = map(int, finishTime.split(':'))
        d = (0, 15, 30, 45, 60)

        def count(sm, em):
            i, j = 0, len(d) - 1
            while d[i] < sm:
                i += 1
            while d[j] > em:
                j -= 1
            return j - i

        if sh == eh:
            ans += count(sm, em)
            if sm > em:
                ans += 24 * 4
        elif sh < eh:
            ans += (eh - (sh + 1)) * 4
            ans += count(sm, 60) + count(0, em)
        else:
            ans += (24 - (sh + 1)) * 4
            ans += eh * 4
            ans += count(sm, 60) + count(0, em)

        return ans


if __name__ == '__main__':
    solu = Solution()
    print(solu.numberOfRounds(startTime="12:01", finishTime="12:44"))
    print(solu.numberOfRounds(startTime="20:00", finishTime="06:00"))
    print(solu.numberOfRounds(startTime="00:00", finishTime="23:59"))

    print(solu.numberOfRounds(startTime="00:01", finishTime="00:00"))
    print(solu.numberOfRounds(startTime="00:01", finishTime="00:30"))
    print(solu.numberOfRounds(startTime="06:30", finishTime="00:15"))
